---
source_url: https://docs.aws.amazon.com/solutions/fraud-detection-with-intelligent-document-processing-on-aws/index.html
---

---
title: 'Guidance for Fraud Detection with Intelligent Document Processing on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/fraud-detection-with-intelligent-document-processing-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Fraud Detection with Intelligent Document Processing on AWS

## Overview

This Guidance demonstrates how to build a comprehensive intelligent document processing (IDP) workflow that combines AWS AI services for enhanced fraud detection and data extraction. By leveraging key services like Amazon Bedrock and Amazon SageMaker AI, organizations can transform their document handling processes, achieving faster, more accurate, and secure business operations. This Guidance reduces development time by up to 80 percent while incorporating intelligent data extraction, computer vision for tampering detection, and automated reasoning checks to verify AI-generated insights.

## Benefits

### Reduce document processing time

Transform manual document review with AI-powered processing that combines data extraction, tampering detection, and automated verification. Process diverse document types simultaneously through standardized workflows that deliver faster, more accurate results.

### Detect sophisticated document fraud

Identify document tampering through computer vision models that analyze submitted images for manipulation. Combine visual analysis with automated reasoning checks to verify AI-generated insights, creating multiple layers of fraud detection capabilities.

### Streamline claims analysis workflows

Create standardized document processing blueprints that extract critical information from various document formats. Enable analysts to focus on decision-making rather than manual data extraction, with AI-generated summary reports and automated notifications.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/fraud-detection-with-intelligent-document-processing-on-aws.pdf)

![Architecture diagram](/images/solutions/fraud-detection-with-intelligent-document-processing-on-aws/images/fraud-detection-with-intelligent-document-processing-on-aws-1.png)

1. **Step 1**: The claims analyst uploads sample documents through the web client to the Amazon Simple Storage Service (Amazon S3) bucket for blueprint creation.
1. **Step 2**: Amazon Bedrock Data Automation uses JSON templates and Python scripts to create standardized blueprints for processing future claims file submissions.
1. **Step 3**: Amazon Bedrock Data Automation refines and stores custom blueprints.
1. **Step 4**: Claims analysts upload claim document packets that include supporting materials, such as claim forms, property damage pictures, identification documents, and audio files.
1. **Step 5**: An AWS Step Functions (Claims Processing) workflow processes the submitted documents using the Amazon Bedrock Data Automation blueprints that were published in Step 2 to extract data.
1. **Step 6**: The automated process stores extracted insights from text documents, audio files, and image metadata in Amazon DynamoDB.
1. **Step 7**: A computer vision model hosted on Amazon SageMaker AI endpoints processes the submitted images to detect tampering and stores the results in DynamoDB. This model uses error level analysis (ELA), highlighting areas where compression levels don't match to reveal tampering.
1. **Step 8**: Amazon Nova Pro/Lite foundation model analyzes the data stored in DynamoDB to generate summary reports, which users can view in the web client.
1. **Step 9**: Amazon Bedrock processes the insights to generate customized reports for claims analysts or trigger automated notifications through Amazon Simple Notification Service (Amazon SNS) using email notifications.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-fraud-detection-with-intelligent-document-processing-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
