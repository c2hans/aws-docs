---
source_url: https://docs.aws.amazon.com/solutions/analyzing-customer-conversations-on-aws/index.html
---

---
title: 'Guidance for Analyzing Customer Conversations on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/analyzing-customer-conversations-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Analyzing Customer Conversations on AWS

## Overview

This Guidance demonstrates how to use voice analytics to uncover insights from customer phone conversations and improve customer satisfaction. Customer service phone calls are automatically transcribed using speech-to-text technology and then analyzed using generative AI natural language processing to identify trends, complaints, product issues, and frequently asked questions. The insights gained from these analyses are summarized in reports for management, helping you better understand customer pain points and opportunities to enhance the customer experience.

## How it works

This architecture diagram shows how to build an automated workflow for analyzing contact center customer conversations (such as voice calls and chat) using foundation models hosted on Amazon Bedrock.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/analyzing-customer-conversations-on-aws.pdf)

![Architecture diagram](/images/solutions/analyzing-customer-conversations-on-aws/images/analyzing-customer-conversations-on-aws-1.png)

1. **Step 1a**: A user uploads contact center chat transcripts as text files to an Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 1b**: The contact center call recordings are stored on another S3 storage bucket, which is configured to call an AWS Lambda function when an object is created.
1. **Step 2**: The Lambda function uses Amazon Transcribe to convert the audio call into a text file and stores the resultant text files in the output S3 location.
1. **Step 3**: The S3 buckets storing text transcripts (from Step 1a) and output of Amazon Transcribe (from Step 1b) are configured to call Lambda when a new object is available. This Lambda function uses an Amazon Bedrock-hosted Anthropic Claude 3.5 Sonnet model to generate summary and sentiment of the contact center conversations in the input file. This function also uses a prompt template that can be customized as needed to control input context passed to the foundation models.
1. **Step 4**: Lambda parses the JSON output from Amazon Bedrock and persists the key details such as conversation summary, customer and agent sentiments, confidence scores, and action items derived from the conversations in Amazon DynamoDB.
1. **Step 5**: Amazon EventBridge scheduler calls another Lambda function at a pre-set time.
1. **Step 6**: The Lambda function reads the data from DynamoDB to generate a CSV file with the analysis results of the contact center conversations in the past 24 hours that have sentiment scores below a pre-defined threshold. This CSV file is then stored on Amazon S3.
1. **Step 7**: Amazon S3 then initiates an event to call Amazon Simple Notification Service (Amazon SNS), which sends an email to the subscribed users. These business users can review the analysis results and take necessary actions to improve the customer experiences.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-analyzing-customer-conversations-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The built-in logging capabilities, operational metrics of Lambda, Amazon S3, and DynamoDB, coupled with Amazon CloudWatch, provide visibility into the application's performance. The event-driven architecture, facilitated by Amazon S3 events, streamlines deployment and maintenance processes. It also enables efficient resource allocation and scalability, while reducing operational overhead. This approach allows for proactive identification and resolution of issues. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Granular access control mechanisms, such as AWS Identity and Access Management (IAM) policies in Amazon S3, Lambda, and DynamoDB, secure the application. Scoping down IAM policies to the minimum required permissions limits unauthorized access to critical resources. Secure HTTPS connections between services like Lambda, Amazon Transcribe, and Amazon S3 protect data in transit, while encryption with AWS Key Management Service (AWS KMS) safeguards data at rest in DynamoDB. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Managed services such as Amazon Transcribe, Lambda, and Amazon SNS enhance the application’s reliability, as AWS handles infrastructure, scaling, and failover mechanisms for the services. The event-driven architecture decouples services, reducing single points of failure and allowing easier recovery or replacement of individual components. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Transcribe offers specialized capabilities for efficient audio and text data processing for faster analysis and quick responses. Lambda's automatic scaling minimizes resource provisioning concerns. Following best practices for Lambda memory size settings optimizes performance. For DynamoDB, Provisioned Capacity mode with autoscaling accommodates gradually changing or predictable traffic patterns, optimizing performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The pay-as-you-go pricing model of serverless services like Lambda and Amazon S3 optimizes costs by avoiding over-provisioning or underutilization. The DynamoDB Time to Live (TTL) feature automatically deletes aged-out data without consuming write throughput, and AWS Graviton2 Processors power cost-effective Lambda functions. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Serverless services such as Lambda and managed services such as Amazon S3, Amazon Transcribe, and DynamoDB enhance sustainability by optimizing resource utilization, eliminating idle waiting times, and avoiding unnecessary compute resource consumption. Automatic scaling provisions resources based on demand, minimizing idle resources and associated energy consumption. Amazon S3 storage classes, lifecycle policies, and the DynamoDB TTL feature further reduce storage costs. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
