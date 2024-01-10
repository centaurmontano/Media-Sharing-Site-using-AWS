from flask import Flask, render_template, request, redirect, flash, url_for, Response
import boto3
from io import BytesIO
from PIL import Image
import logging

# Flask app configuration
app = Flask(__name__, template_folder=r'C:\Users\charl\Desktop\AWS Media Sharing\templates')
app.secret_key = 'v^}Yi-L)(52gBY3dCZv8iY^tfYIl1mEe'

# Enable debug mode
app.debug = True

# AWS S3 and DynamoDB setup
s3 = boto3.client('s3')  # S3 client
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')  # DynamoDB resource, change region if needed.
table = dynamodb.Table('media')  # DynamoDB table name

# Logging configuration
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Flask routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Handle file upload
            name = request.form['name']
            description = request.form['description']
            location = request.form['location']
            file = request.files['file']
            
            # Upload file to S3
            s3.upload_fileobj(file, 'cmwebsolutions', file.filename)  # Replace 'cmwebsolutions' with your S3 bucket name

            # Add metadata to DynamoDB table 
            key = file.filename
            table.put_item(
                Item={
                    'ImageKey': key,
                    'name': name,
                    'description': description,
                    'location': location
                }
            )

            flash('File uploaded successfully')
            return redirect('/')
        except Exception as e:
            logger.error(f"Error uploading file: {str(e)}")
            flash('Error uploading file')
            return redirect('/')
    else:
        try:
            # Retrieve objects from S3
            objects = s3.list_objects(Bucket='cmwebsolutions')['Contents']  # Replace 'cmwebsolutions' with your S3 bucket name
            files = []
            for obj in objects:
                if obj['Key'].endswith(('.jpg', '.png')):
                    url = url_for('thumbnail', key=obj['Key'])
                    
                    # Retrieve metadata from DynamoDB
                    try:
                        response = table.get_item(
                            Key={
                                'ImageKey': obj['Key']
                            }
                        )
                        name = response['Item']['name']
                        description = response['Item']['description']
                        location = response['Item']['location']
                        files.append({'key': obj['Key'], 'url': url, 'name': name, 'description': description, 'location': location})
                    except KeyError:
                        logger.warning(f"No metadata found for key {obj['Key']}")
                    except Exception as e:
                        logger.error(f"Error retrieving metadata for key {obj['Key']}: {str(e)}")
        except Exception as e:
            logger.error(f"Error retrieving files: {str(e)}")
            files = []
        return render_template('index.html', files=files)

@app.route('/delete', methods=['POST'])
def delete_file():
    try:
        # Handle file deletion
        key = request.form['key']
        s3.delete_object(Bucket='cmwebsolutions', Key=key)  # Replace 'cmwebsolutions' with your S3 bucket name
        
        # Delete metadata from DynamoDB
        table.delete_item(
            Key={
                'ImageKey': key
            }
        )
        flash('File deleted successfully')
    except Exception as e:
        logger.error(f"Error deleting file: {str(e)}")
        flash('Error deleting file')
    return redirect('/')

from flask import abort

@app.route('/thumbnail/<key>')
def thumbnail(key):
    try:
        # Generate and serve thumbnail
        response = s3.get_object(Bucket='cmwebsolutions', Key=key)
        image = Image.open(BytesIO(response['Body'].read()))
        image.thumbnail((200, 200))
        image = image.convert('RGB')
        
        with BytesIO() as output:
            image.save(output, format='JPEG')
            contents = output.getvalue()
        
        return Response(contents, mimetype='image/jpeg')
    
    except s3.exceptions.NoSuchKey:
        logger.error(f"Object not found in S3: {key}")
        abort(404)
    
    except Exception as e:
        logger.error(f"Error generating thumbnail for key {key}: {str(e)}")
        abort(500)


# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0')
