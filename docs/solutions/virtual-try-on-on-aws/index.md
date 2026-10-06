---
source_url: https://docs.aws.amazon.com/solutions/virtual-try-on-on-aws/index.html
---

---
title: 'Guidance for Virtual Try-On on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/virtual-try-on-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Virtual Try-On on AWS

## Overview

This Guidance demonstrates how retailers can overcome online shopping limitations by implementing a virtual try-on solution on AWS that allows customers to digitally experience products before purchase. The solution uses Amazon S3 to store customer photos and product images, while AWS Lambda processes requests and updates metadata in DynamoDB tables. Amazon Bedrock powers the Nova Canvas model that generates realistic try-on images, with AWS Step Functions orchestrating the entire workflow for a seamless customer experience. You can increase sales and customer satisfaction while reducing return rates by enabling shoppers to visualize products on themselves before making a purchase decision.

## Benefits

### Accelerate retail innovation

Deploy virtual try-on experiences that allow customers to visualize products before purchase. Leverage Amazon Bedrock's Nova Canvas model combined with serverless architecture to deliver compelling shopping experiences without managing complex infrastructure.

### Enhance customer engagement

Create interactive, real-time product visualization that reduces purchase hesitation and increases conversion rates. The WebSocket connections through API Gateway provide immediate feedback to customers, keeping them engaged throughout the try-on experience.

### Scale with demand effortlessly

Handle fluctuating traffic patterns common in retail with a fully serverless architecture. AWS Lambda, Step Functions, and SQS work together to process try-on requests efficiently while DynamoDB tracks job status, ensuring reliable performance during peak shopping periods.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/virtual-try-on-on-aws.pdf)

![Architecture diagram](/images/solutions/virtual-try-on-on-aws/images/virtual-try-on-on-aws-1.png)

1. **Step 1**: Amazon S3 stores the uploaded customer model photos and product images.
1. **Step 2**: Each upload generates a message sent to an Amazon SQS queue. Lambda creates the corresponding metadata, S3 path, and stores it in the Amazon DynamoDB product table for later retrieval.
1. **Step 3**: Amazon API Gateway manages the WebSocket connections for real-time status updates between the client and the VTO.
1. **Step 4**: AWS Lambda processes initial requests by retrieving product information from the Amazon DynamoDB product table and creating job entries in DynamoDB.
1. **Step 5**: Amazon DynamoDB: The products table (vtoproducts) stores catalog items available for the VTO, notably the Amazon S3 picture location.
1. **Step 6**: The Virtual Try-On Jobs DynamoDB Table (vtojobs) tracks the state of each try-on request.
1. **Step 7**: Amazon DynamoDB Streams asynchronously triggers AWS Step Functions workflows on job creation for processing try-on requests.
1. **Step 8**: AWS Step Functions orchestrates the VTO generation. It triggers a Lambda function that calls the Amazon Nova Canvas model through Amazon Bedrock. The DynamoDB job table is updated with the VTO status.
1. **Step 9**: Amazon S3 stores the generated try-on images with job ID metadata.
1. **Step 10**: Amazon SQS handles Amazon S3 event notifications for completed try-on images.
1. **Step 11**: AWS Lambda Function sends the Amazon S3 URL of the result back to the user via WebSocket.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-virtual-try-ons-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
