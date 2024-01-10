# Media Sharing Site using AWS

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="Amazon Logo" width="100" height="100"/> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg" alt="Flask Logo" width="100" height="100"/> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python Logo" width="100" height="100"/> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original.svg" alt="Amazon DynamoDB Logo" width="100" height="100"/>


A comprehensive full-stack media sharing site leveraging Flask and AWS services (Amazon EC2, Amazon S3, Amazon DynamoDB), enabling users to browse, upload, and delete images seamlessly.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [AWS Services](#aws-services)
- [How to Use](#how-to-use)
  - [Setting Up AWS Credentials](#setting-up-aws-credentials)
- [Contribution](#contribution)
- [License](#license)

## Overview
This project is a Media Sharing Site built on [Amazon Web Services (AWS)](https://aws.amazon.com/). It leverages [Amazon EC2](https://aws.amazon.com/ec2/) for hosting the web application, [Amazon S3 Bucket](https://aws.amazon.com/s3/) for storing media files, and [DynamoDB](https://aws.amazon.com/dynamodb/) as the database for data management.

## Features
- **Image Management:** Browse, upload, and delete images within the website.
- **User-friendly Interface:** Intuitive interface for seamless image browsing and storage.

## Tech Stack
- **Front End:** Developed using [Flask](https://palletsprojects.com/p/flask/) framework.
- **Languages:** HTML and Python (apppy) in [MS Visual Studio Code](https://code.visualstudio.com/).

## AWS Services
- **Amazon EC2:** Hosts the web application.
- **Amazon S3 Bucket:** Stores and manages media files.
- **DynamoDB:** Database for efficient data storage.

## How to Use
1. Clone the repository.
2. Set up your AWS credentials.
   - Follow the steps below to configure AWS CLI on your local machine:
     - Install AWS CLI: [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
     - Open a terminal and run:
       ```bash
       aws configure
       ```
     - Enter your AWS Access Key ID, Secret Access Key, default region, and default output format as prompted.
3. Configure the Flask app.
4. Run the application locally or deploy it on [Amazon EC2](https://aws.amazon.com/ec2/).

### Amazon EC2:

**Connect using EC2 Instance Connect:**
[EC2 Instance Connect Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html)

### Amazon S3 Bucket:

**Overview:**
Amazon S3 (Simple Storage Service) is a scalable object storage service for storing and retrieving any amount of data.

[S3 Bucket Creation Overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)

### DynamoDB:

**Overview:**
Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance.

[DynamoDB Getting Started](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-1.html)


## Conclusion

Thank you for exploring our Media Sharing Site using AWS! This project can serve as a foundation for various applications, including:

1. **Social Media Platforms:** Enhance user experience by allowing seamless image sharing and browsing within social networking sites.

2. **Portfolio Websites:** Showcase your work by integrating this media sharing functionality into your portfolio, providing an engaging way to display images.

3. **Collaborative Projects:** Facilitate collaboration by integrating image sharing capabilities, ideal for projects where visual content is crucial.

4. **Educational Platforms:** Create interactive learning environments by incorporating image sharing for educational materials and collaborative projects.

Feel free to adapt and extend this project to meet the specific needs of your application or explore other creative use cases!



