# Media Sharing Site using AWS

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

### Setting Up AWS Credentials
To set up AWS credentials on your local machine using AWS CLI, follow these steps:
1. Install AWS CLI by following the instructions in the [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
2. Open a terminal and run the following command:
   ```bash
   aws configure
