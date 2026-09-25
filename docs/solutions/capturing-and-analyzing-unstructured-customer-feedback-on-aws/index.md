---
source_url: https://docs.aws.amazon.com/solutions/capturing-and-analyzing-unstructured-customer-feedback-on-aws/index.html
---

---
title: 'Guidance for Capturing and Analyzing Unstructured Customer Feedback on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/capturing-and-analyzing-unstructured-customer-feedback-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Capturing and Analyzing Unstructured Customer Feedback on AWS

## Overview

This Guidance helps you collect and democratize customer feedback provided in unstructured data formats such as forms, reviews, emails, and chatbots. It uses natural language processing (NLP) services such as Amazon Comprehend to extract text and perform entity parsing and sentiment analysis. This Guidance also notifies internal teams of feedback using event-based services, including AWS Lambda, Amazon Simple Notification Service (Amazon SNS), and Amazon Simple Queue Service (Amazon SQS).

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/capturing-and-analyzing-unstructured-customer-feedback-on-aws.pdf)

![Architecture diagram](/images/solutions/capturing-and-analyzing-unstructured-customer-feedback-on-aws/images/capturing-and-analyzing-unstructured-customer-feedback-on-aws-1.png)

1. **Step 1**: Source applications collect feedback from emails, feedback forms, customer support call recordings, and chatbot transcripts in databases or file systems.
1. **Step 2**: Amazon Transcribe creates transcripts of customer call recordings. AWS Transfer Family transfers files to AWS and AWS Database Migration Service (AWS DMS) and connects and replicates data from different databases to AWS. Amazon Simple Storage Service (Amazon S3) provides an intermediate landing zone for raw data at any velocity, volume, or variety.
1. **Step 3**: A new feedback event pushes text files to Amazon S3. The event-based architecture invokes the respective AWS Lambda function to start feedback inference.
1. **Step 4**: Lambda translates the data to English in near real-time using the neural machine on Amazon Translate.
1. **Step 5**: Lambda extracts and processes the text using Amazon Comprehend, which processes the extracted text and performs clustered data and feedback, CSAT report, feedback summary, sentiment analysis, and product performance. For better accuracy, we leverage a custom classifier within Amazon Comprehend.
1. **Step 6**: Lambda uses a large language model (LLM) on Amazon SageMaker to identify the right department to be notified and routing rule for urgent feedback. Amazon Simple Notification Service (Amazon SNS) sends these notifications. Lambda pushes the final data to store in an open search index.
1. **Step 7**: Amazon Open Search Service performs custom querying data for near real-time search, big data analytics, and custom dashboards.
1. **Step 8**: SageMaker LLM summarizes non-urgent feedback, such as a feature suggestion, which is then stored in Open Search Service using a different index.
1. **Step 9**: Amazon QuickSight provides a comprehensive view of all customer feedback with a summary to drill down capabilities and analyze feedback.
1. **Step 10**: AWS security services secure and monitor this Guidance.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The event-driven architecture allows near real-time feedback communication to respective teams. Once customer feedback is received, Amazon S3 invokes a Lambda function that derives inference from feedback. Critical feedback is communicated to users in near real-time using Amazon SNS. Amazon S3 provides reliable, scalable storage and kicks off subsequent processing. Open Search Service captures near real-time updates to the records and feedback in indexes. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Enabling encryption by default for the S3 bucket and Open Search Service keeps data protected from unauthorized access in case of a security breach or accidental exposure. This helps maintain the confidentiality and integrity of the stored data. IAM configures granular permissions based on roles, including permissions for accessing resources on other resources, such as S3 buckets and Open Search Service indexes. Configuring the SNS topics to only accept encrypted communication helps ensure secure transmission, reducing the risk of eavesdropping or tampering during communication. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon S3 provides high reliability and fault tolerance while also being cost effective. You can apply custom business logic to determine when to redirect requests to other AWS Regions. QuickSight and Amazon SNS are serverless services that store data, visualize insights, and notify events at scale. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda is a serverless compute service that automatically scales depending on demand. The distributed nature of Open Search Service enables it to process large volumes of data in parallel, quickly finding the best matches for your queries. Serverless services help ensure that services can accommodate to demand. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda is an event-driven mechanism used to process the event of new customer feedback and start feedback events and the inference process. This removes the need for a server to be running continuously. By using Lambda functions, you can use compute capacity only when required. Amazon SNS users pay per SNS notification request, and Amazon SNS Free Tier offers the first 100,000 notifications over HTTP for free. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon S3, Lambda, and Amazon SNS are all serverless services that work on demand and can accommodate for the compute capacity required. This maximizes the performance and usage of resources. Additionally, the efficient use of serverless resources reduces the overall energy required to operate the workload. SageMaker batch inference jobs are executed using the right instance size for optimal utilization of the resources while being cost-efficient. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
