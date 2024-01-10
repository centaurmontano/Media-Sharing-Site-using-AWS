# Media Sharing Site using AWS

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="AWS Logo" width="100" height="100"/> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original.svg" alt="Amazon EC2 Logo" width="100" height="100"/> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original.svg" alt="Amazon S3 Logo" width="100" height="100"/> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original.svg" alt="Amazon DynamoDB Logo" width="100" height="100"/>

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

**Overview:**
Amazon EC2 (Elastic Compute Cloud) is a scalable cloud computing service that allows you to host applications on virtual servers, known as instances.

**Steps:**
1. **Log in to AWS Console:**
   - Access your [AWS Management Console](https://aws.amazon.com/).

2. **Navigate to EC2:**
   - Go to the EC2 service.

3. **Launch an Instance:**
   - Click "Launch Instance" to create a virtual server.

4. **Choose an AMI:**
   - Select an Amazon Machine Image (AMI) suitable for your application.

5. **Configure Instance:**
   - Set instance details, choose instance type, configure networking, and add storage.

6. **Configure Security Group:**
   - Set up security groups to allow incoming traffic on ports like 80 (HTTP) or 443 (HTTPS).

7. **Review and Launch:**
   - Review your configuration and launch the instance.

8. **Create or Select a Key Pair:**
   - Create a key pair for secure connection to the instance.

9. **Access the Instance:**
   - Obtain the public IP or DNS of your instance and connect using SSH or [EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html).
  
   https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html

   ### Amazon S3 Bucket:

**Overview:**
Amazon S3 (Simple Storage Service) is a scalable object storage service for storing and retrieving any amount of data.

**Steps:**
1. **Log in to AWS Console:**
   - Access your [AWS Management Console](https://aws.amazon.com/).

2. **Navigate to S3:**
   - Go to the S3 service.

3. **Create a Bucket:**
   - Click "Create Bucket" to create a storage container.

4. **Configure Bucket:**
   - Enter a unique bucket name and choose the region for the bucket.
   - Configure additional settings like versioning, logging, etc.

5. **Review and Create:**
   - Review your configuration and create the bucket.

### DynamoDB:

**Overview:**
Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance.

**Steps:**
1. **Log in to AWS Console:**
   - Access your [AWS Management Console](https://aws.amazon.com/).

2. **Navigate to DynamoDB:**
   - Go to the DynamoDB service.

3. **Create a Table:**
   - Click "Create Table" to define a table.

4. **Configure Table:**
   - Enter a table name, primary key, and configure provisioned capacity if needed.

5. **Review and Create:**
   - Review your configuration and create the table.

