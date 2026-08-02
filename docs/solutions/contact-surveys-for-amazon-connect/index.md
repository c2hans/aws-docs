---
source_url: https://docs.aws.amazon.com/solutions/contact-surveys-for-amazon-connect/index.html
---

# Guidance for Contact Surveys for Amazon Connect Customer Customer

Analyze customer satisfaction scores with a serverless post-contact survey solution

## Overview

This Guidance helps you create, manage, and analyze post-contact surveys with Connect Customer. With surveys being an important diagnostic tool to adjust the experiences and services delivered to your customers, this Guidance is designed to help you better understand your customer's motivations and intentions following their experience with your business. You can integrate this Guidance with your existing Connect Customer instances, and get started with post-contact surveys in minutes. Once deployed, you can access a secure web application to define surveys, edit existing surveys, and visualize aggregated results for each survey. You benefit from a modern interface that integrates your contact center and surveys, all in one place.

## How it works

This architecture diagram shows how to analyze customer satisfaction scores using a modern web application built on AWS. You can integrate this Guidance with your Connect Customer instance to configure, manage, and visualize the results of post-contact surveys stemming from your contact center.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/contact-surveys-for-amazon-connect.pdf?target=_blank)

![Architecture diagram](/images/solutions/contact-surveys-for-amazon-connect/images/contact-surveys-for-amazon-connect-1.png)

1. **Step 1**: The web application (built with React) is hosted in an Amazon Simple Storage Service (Amazon S3) bucket, and is served through Amazon CloudFront.
1. **Step 2**: Users (contact center administrators, managers) authenticate using Amazon Cognito. A token is generated. It will secure the REST calls to Amazon API Gateway.
1. **Step 3**: As the users interact with the web application, API calls are made to API Gateway, reflecting the operations in the application (such as creating, editing, or visualizing the result of a survey).
1. **Step 4**: API Gateway invokes an AWS Lambda function to read and write data in Amazon DynamoDB.
1. **Step 5**: The configuration data (surveys' definition) and the user data (surveys' results) are stored in DynamoDB. This data is read and written through a set of Lambda functions.
1. **Step 6**: Using a pre-configured flow module in Amazon Connect Customer, users define which survey will be offered to customers. Using a Lambda function, the configuration of the required survey is retrieved and offered to the caller.
## Related content

- **Contact surveys for Connect Customer**: This sample code gives an end-to-end solution that will enable users to create and manage surveys, use these surveys with their Connect Customer contact center, and visualize their results.

[Learn more](https://github.com/aws-samples/amazon-connect-contact-surveys)

[Read usage guidelines](/solutions/guidance-disclaimers/)
