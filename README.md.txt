# Secure Serverless API on AWS

## Overview
This project demonstrates an end-to-end, secure serverless web application backend built on Amazon Web Services (AWS). It features a fully functional API that processes client requests, executes serverless compute logic, and stores data in a NoSQL database, all protected behind a global content delivery network and web application firewall.

## Architecture Flow
**Client → Amazon CloudFront → AWS WAF → Amazon API Gateway → AWS Lambda → Amazon DynamoDB**

## Technologies & Services Used
* **Amazon CloudFront:** Acts as the global entry point to distribute traffic securely at the edge.
* **AWS WAF (Web Application Firewall):** Attached to CloudFront to inspect incoming HTTP requests and block common web exploits before they reach the API.
* **Amazon API Gateway (HTTP API):** Securely routes the validated web traffic to the backend compute resources.
* **AWS Lambda (Python 3):** Serverless compute function that processes the request, generates a unique UUID, and uses the `boto3` SDK to interact with the database.
* **Amazon DynamoDB:** NoSQL database used to quickly store and retrieve the generated records.
* **AWS IAM:** Strict, least-privilege execution roles allowing Lambda to write to DynamoDB securely.

## Project Evidence
Please review the uploaded files in this repository for evidence of the working architecture:
1. `lambda_function.py`: The Python script deployed to AWS Lambda.
2. **API Live Test:** Screenshot confirming the API is reachable over the internet and returning the correct success JSON payload.
3. **Database Records:** Screenshot of the DynamoDB console showing the dynamically generated UUID records.
4. **WAF Active Metrics:** Screenshot of the CloudFront security dashboard proving the AWS WAF is actively intercepting, inspecting, and logging HTTP requests.