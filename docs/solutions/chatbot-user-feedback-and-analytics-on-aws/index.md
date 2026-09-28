---
source_url: https://docs.aws.amazon.com/solutions/chatbot-user-feedback-and-analytics-on-aws/index.html
---

---
title: 'Guidance for Chatbot User Feedback and Analytics on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/chatbot-user-feedback-and-analytics-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Chatbot User Feedback and Analytics on AWS

## Overview

This Guidance demonstrates a prescriptive approach to gathering and storing human feedback on generative artificial intelligence (AI) applications, allowing businesses to estimate the value of their AI investments by collecting user satisfaction data. It implements a feedback collection mechanism for custom-built chatbots on AWS and Amazon Q Business chatbots. Decision-makers can easily access and visualize key performance indicators (KPIs) derived from user ratings and comments on chat responses, which provide valuable insights into the performance and effectiveness of their generative AI applications.

## How it works

### For Amazon Q Business Chatbot

This architecture diagram shows how to enhance observability of user interactions with an Amazon Q Business chatbot. For the custom generative AI chatbot built on AWS, open the other tab.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/chatbot-user-feedback-and-analytics-on-aws.pdf#page=1)Step 1The custom chatbot user shares feedback on their last interaction with an Amazon Q Business chatbot application.Step 2The feedback events are captured in AWS CloudTrail.Step 3An Amazon EventBridge rule invokes an AWS Lambda function to process Amazon Q Business originated events.Step 4Lambda pushes the feedback received from Amazon Q Business through the feedback API endpoint.Step 5By default, AWS Identity and Access Management (IAM) protects access to the API, making it available only to IAM authenticated principals.Step 6The Lambda function processes feedback events by cleansing and mapping the data to the feedback data model. It also handles storing the feedback data in Amazon Simple Storage Service (Amazon S3).Step 7Feedback metadata and quality metrics are then stored in Amazon S3.Step 8The feedback metrics metadata are cataloged and maintained within an AWS Glue Data Catalog table.Step 9Both the metrics data and metadata are stored encrypted using AWS Key Management Service (AWS KMS).Step 10Amazon Athena runs SQL queries against the feedback table.Step 11Amazon QuickSight builds visuals and dashboards, providing insight into the feedback metrics.### For Custom Chatbot

This architecture diagram shows how to enhance observability of user interactions with a custom generative AI chatbot built on AWS. For the Amazon Q Business chatbot, open the other tab.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/chatbot-user-feedback-and-analytics-on-aws.pdf#page=2)Step 1The custom chatbot user shares feedback on their last interaction with a generative AI chatbot application based on models hosted on Amazon Bedrock or Amazon SageMaker.Step 2The feedback API generic endpoint deployed in Amazon API Gateway posts the feedback.Step 3By default, IAM protects access to the API, making it available only to IAM authenticated principals.Step 4The Lambda function processes feedback events by cleansing and mapping the data to the feedback data model. It also handles storing the feedback data in Amazon S3.Step 5Feedback metadata and quality metrics are then stored in Amazon S3.Step 6The feedback metrics metadata are cataloged and maintained within a Data Catalog table.Step 7Both the metrics data and metadata are stored encrypted using AWS KMS.Step 8Athena runs SQL queries against the feedback table.Step 9QuickSight builds visuals and dashboards, providing insight into the feedback metrics.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-chatbot-user-feedback-and-analytics-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Lambda functions process and handle incoming requests and events, enabling operational excellence through serverless computing. EventBridge seamlessly routes feedback data emitted by Amazon Q, while API Gateway serves as the secure entry point, minimizing operational overhead. AWS handles provisioning, scaling, and maintenance, allowing you to focus on application logic. This reduces operational burden and ensures efficient, reliable operations. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Sensitive user feedback data is securely stored in Amazon S3, with encryption managed by AWS KMS. Access control is implemented through API Gateway's custom authorizers, providing a secure entry point. This comprehensive approach to data protection, access control, and secure communication safeguards customer information and application integrity. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses AWS Cloud Development Kit (AWS CDK), which enables infrastructure as code deployment and promotes consistent, repeatable deployments that reduce the risk of human error. Serverless Lambda functions handle data processing and business logic with serverless components that automatically scale and recover from failures transparently, ensuring a reliable posture. The services in this Guidance contribute to reliability by providing fault tolerance, scalability, and automated recovery. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

EventBridge ingests events from Amazon Simple Queue Service (Amazon SQS), while API Gateway ingests feedback events from custom AI chatbots. EventBridge can process and deliver high volumes of events with low latency, and API Gateway is a scalable, high-performance API management service. These services can handle varying workloads and traffic without compromising performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3 provides cost-effective data storage and charges only for the amount of data stored. Lambda avoids idle compute costs by automatically scaling and charging only for execution duration. Athena enables ad-hoc SQL querying of data stored in Amazon S3 without provisioning dedicated infrastructure, so that you pay only for queries executed. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Serverless services like Lambda and API Gateway enhance sustainability by automatically scaling up and down based on demand. When there are no events to process, these components remain idle, optimizing resource usage and minimizing wasted resources. This approach reduces the environmental impact of the Guidance to its effective usage, aligning with sustainable practices. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
