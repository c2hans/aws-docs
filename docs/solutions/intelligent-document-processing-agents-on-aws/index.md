---
source_url: https://docs.aws.amazon.com/solutions/intelligent-document-processing-agents-on-aws/index.html
---

---
title: 'Guidance for Intelligent Document Processing Agents on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/intelligent-document-processing-agents-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Intelligent Document Processing Agents on AWS

## Overview

This Guidance demonstrates how your financial institution can transform its loan application processes through secure, AI-powered automation. By using Amazon Bedrock, you can create intelligent workflows that streamline document processing, reduce manual intervention, and enhance both operational efficiency and the customer experience. These advanced AI capabilities enable you to automatically extract, verify, and process loan documentation while maintaining security and compliance. By demonstrating the seamless integration of customer-facing interfaces with powerful backend processing, this Guidance enables you to accelerate loan processing times, reduce errors, and provide a more transparent experience for both applicants and brokers.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/intelligent-document-processing-agents-on-aws.pdf)

![Architecture diagram](/images/solutions/intelligent-document-processing-agents-on-aws/images/intelligent-document-processing-agents-on-aws-1.png)

1. **Step 1**: The user initiates their journey by accessing the web UI through their web browser.
1. **Step 2**: Amazon CloudFront handles the content delivery, ensuring optimal performance across different geographical locations.
1. **Step 3**: The user authenticates through Amazon Cognito to the web app while AWS WAF protects against malicious activities.
1. **Step 4**: The user can interact using a static web app hosted on Amazon Simple Storage Service (Amazon S3), where they can upload required documentation to Amazon S3.
1. **Step 5**: Amazon Bedrock Data Automation, invoked by Amazon EventBridge, begins processing and analyzing the submitted documents for relevant information extraction.
1. **Step 6**: AWS AppSync manages the user's interactions with AWS Lambda resolver and Amazon DynamoDB.
1. **Step 7**: Amazon Bedrock multiagent collaboration orchestrates the agentic workflow. The supervisor agent oversees the entire process, monitoring both applicant assistant agent and broker assistant agent, routing requests correctly through each stage.
1. **Step 8**: The supervisor agent routes the user's requests to the applicant assistant agent to verify documents and manage the data collection.
1. **Step 9**: The applicant assistant uses action groups with tools to calculate the debt-to-income ratio and generate the application summary, then saves the application result to Amazon S3.
1. **Step 10**: The broker assistant agent processes the application based on the collected information and predefined criteria, then generates a preapproval letter for the loan application.
1. **Step 11**: Amazon CloudWatch provides comprehensive monitoring and logging across the entire system, as well as tracking of all components.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-intelligent-document-processing-agents-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CloudWatch monitors the document processing pipeline and agent interactions and provides detailed insights into the loan application journey, like document processing times and approval rates. DynamoDB tracks application states. AWS Cloud Development Kit (AWS CDK) manages infrastructure deployment with defined testing environments, maintaining consistent infrastructure deployments across environments. Finally, EventBridge reliably orchestrates the workflow between document processing stages, invoking functions and agents as needed. Together, these services provide real-time visibility, enabling you to quickly detect and respond to bottlenecks or agent failures and helping you maintain consistent service quality. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Cognito manages user authentication for loan applicants, while AWS WAF protects the application from web-based attacks. CloudFront provides encrypted content delivery, and AWS Identity and Access Management (IAM) enforces fine-grained, least-privilege access controls for document processing workflows, including services and agents. AWS AppSync implements API authentication so only authorized users can access loan application data from the front-end application and interact with the document processing pipeline. Finally, Amazon S3 bucket policies and server-side encryption secure sensitive loan documents at rest. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

EventBridge orchestrates document processing workflows by managing state transitions between document upload, verification, and approval stages. CloudFront ensures consistent delivery of application content across multiple Availability Zones even during regional issues. DynamoDB provides durable storage and maintains consistent application state tracking. Amazon S3 versioning and Lambda functions offer built-in retry mechanisms to make sure loan documents are processed reliably even during service disruptions. Finally, Amazon Bedrock Agents use action groups to provide consistent document analysis and decision-making capabilities throughout the loan processing and approval pipeline. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

With global edge locations, CloudFront delivers UI content with low latency. AWS AppSync provides efficient real-time data synchronization that enables instant updates of loan application status. EventBridge orchestrates document processing workflows with minimal overhead, and its combination with Lambda facilitates parallel processing of documents. Amazon Bedrock uses optimized AI models that process multiple documents simultaneously through dedicated agents for applicant and broker workflows. Finally, DynamoDB provides single-digit millisecond access to application data, and its automatic scaling handles varying application loads efficiently. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda provides pay-per-use compute for document processing, removing idle server costs. CloudFront caches UI content to reduce repeated data transfer costs. DynamoDB automatic scales to match capacity with demand, so you pay only for actual database operations during loan processing. Amazon Bedrock Agents use action groups to optimize AI model invocations and minimize their costs. Finally, Amazon S3 lifecycle policies manage document storage across processing stages, automatically transitioning older loan documents to lower-cost storage tiers. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda provides serverless compute, automatically scaling based on demand and eliminating idle resource use, and efficient Amazon Bedrock AI models further minimize computational overhead. The event-driven architecture of EventBridge means that processing occurs only when needed, avoiding continuous polling. The combination of serverless computing, event-driven processing, and optimized AI operations reduces energy use in compute. Additionally, CloudFront caching reduces data transfer distances and redundant data processing. Finally, DynamoDB automatic scaling and Amazon S3 Intelligent-Tiering minimize storage infrastructure needs, reducing the carbon footprint of maintaining loan documents throughout their lifecycle. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
