---
source_url: https://docs.aws.amazon.com/solutions/live-chat-content-moderation-with-generative-ai-on-aws/index.html
---

---
title: 'Guidance for Live Chat Content Moderation with Generative AI on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/live-chat-content-moderation-with-generative-ai-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Live Chat Content Moderation with Generative AI on AWS

## Overview

This Guidance demonstrates how organizations can implement generative artificial intelligence (AI) services for automated message screening in live chat environments. The architecture integrates with existing chat platforms through a secure, scalable cloud infrastructure. It also uses AWS machine learning services to offer near real-time content analysis and customizable filtering rules. Organizations can significantly reduce manual reviews, maintain consistent moderation standards, and create safer communication environments by automatically detecting and filtering inappropriate content across multiple languages. This approach helps businesses efficiently manage content moderation at scale while improving user experience and safety.

## How it works

This architecture diagram illustrates a real-time chat moderation system designed for live streaming platforms. It uses AWS services and generative artificial intelligence (AI) to automatically filter and moderate chat messages, creating a safer and more engaging environment for users.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/live-chat-content-moderation-with-generative-ai-on-aws.pdf?target=_blank)

![Architecture diagram](/images/solutions/live-chat-content-moderation-with-generative-ai-on-aws/images/live-chat-content-moderation-with-generative-ai-on-aws-1.png)

1. **Step 1**: User interaction and message submission: Users access a web application based on React that is served by Amazon CloudFront and Amazon Simple Storage Service (Amazon S3). Additional security from AWS WAF is used to block requests from potential threats. When a user sends a message, the application sends a POST request to Amazon API Gateway. API Gateway then routes the message to an Amazon Simple Queue Service (Amazon SQS) First-In-First-Out (FIFO) queue for processing.
1. **Step 2**: Message processing and AI moderation: An AWS Lambda function, triggered by Amazon SQS, applies Amazon Bedrock Guardrails for initial content filtering. The message is analyzed by the Anthropic Claude Haiku model. The model evaluates the content based on the moderation guidelines and responds with either "y" for approved or "n" for rejected messages.
1. **Step 3**: Message handling and storage: Based on the model's decision, the Lambda function routes the message accordingly. Approved messages are stored in the Amazon DynamoDB Approved Messages table, while rejected messages go to the Unapproved Messages table. Other messages are stored in a Hallucinations table.
1. **Step 4**: Real-time updates and notifications: For approved messages, AWS AppSync broadcasts the content to all subscribed clients through WebSocket connections. For rejected messages, AppSync notifies only the original sender. This system maintains user privacy while enforcing moderation policies.
1. **Step 5**: Monitoring and observability: Amazon CloudWatch and AWS X-Ray log metrics and trace requests, providing insights into message flow. This data is aggregated into a CloudWatch dashboard, offering visibility into the chat moderation system's operations.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-live-chat-content-moderation-with-generative-ai-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Live Chat Content Moderation with Generative AI transforms online conversation management. It deploys through an AWS Cloud Development Kit (AWS CDK), minimizing configuration errors with fast, consistent, and repeatable deployments. Operations teams gain visibility through CloudWatch dashboards and logs, tracking moderation accuracy and chat performance in real-time. And through automated Lambda functions, the system processes and moderates’ messages using generative AI, protecting users while maintaining natural conversation flow. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Lambda functions and API Gateway endpoints operate with specific AWS Identity and Access Management (IAM) roles that grant only the permissions needed for each component's function. For example, the message processing Lambda function has permissions limited to reading from and writing to its designated DynamoDB tables. Data remains encrypted both at rest through a default AWS Key Management Service ( AWS KMS) encryption, and in transit using HTTPS. This encryption covers the full message lifecycle, from initial user input through moderation processing and storage. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The fault tolerance design for this architecture centers on Amazon SQS queues. These queues help ensure message processing reliability, while dedicated dead-letter queues capture and preserve any failed processing attempts. If message processing fails, the system automatically retries based on configurable policies before moving messages to the dead-letter queue for investigation. This design also relies entirely on serverless technologies, including Lambda functions, API Gateway endpoints, and DynamoDB tables. More specifically, Lambda functions automatically retry on failure, API Gateway maintains high availability across multiple Availability Zones, and DynamoDB provides automatic replication. These services also scale automatically based on incoming traffic, adjusting capacity in response to demand without manual intervention, handling variations from normal chat volumes to unexpected traffic spikes. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

CloudFront caches static assets at edge locations, reducing latency for end users by serving content from the nearest geographical point. This architecture also decouples message ingestion from processing using Amazon SQS, allowing this design to maintain consistent performance during high-load periods by buffering incoming messages and processing them asynchronously. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Through the serverless and managed services, costs are directly aligned with usage. Lambda charges based on execution time and memory consumption, while API Gateway and DynamoDB costs scale with actual request volume and storage needs. AppSync and Amazon Bedrock follow similar consumption-based pricing models. Performance and cost trade-offs can be adjusted through Lambda configuration settings, allowing for the fine-tuning of memory allocation and timeout values based on observed execution patterns and requirements. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This architecture can be deployed in AWS Regions that operate with higher percentages of renewable energy, contributing to reduced carbon footprint. In addition, resource efficiency is achieved through dynamic scaling, where compute and storage capacity adjust automatically to match actual demand, eliminating the waste associated with over-provisioned infrastructure. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
