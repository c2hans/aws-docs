---
source_url: https://docs.aws.amazon.com/solutions/live-call-analytics-with-agent-assist-on-aws/index.html
---

---
title: 'Guidance for Live Call Analytics with Agent Assist on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/live-call-analytics-with-agent-assist-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Live Call Analytics with Agent Assist on AWS

Deploy dashboards and boost key performance indicator (KPI) visibility for call center agents

## Overview

This Guidance uses Artificial Intelligence (AI) to analyze speech and conversations in near real-time to improve agent key performance indicators (KPIs) and the customer experience. Data can be visualized through dashboards on Amazon QuickSight, increasing the visibility into agent effectiveness and improving the customer experience. Machine learning is used to capture intent and context from conversations and offer intelligent search features.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/guidance-for-live-call-analytics-with-agent-assist-on-aws-ra.pdf)

![Architecture diagram](/images/solutions/live-call-analytics-with-agent-assist-on-aws/images/live-call-analytics-with-agent-assist-on-aws-1.png)

1. **Step 1**: Amazon Chime Voice Connector streams call audio to Amazon Kinesis Video Streams. Call signaling events are sent to Amazon Event Bridge.
1. **Step 2**: The event initiates call transcription processing. Audio is streamed to Amazon Transcribe for real-time transcription. Recordings are stored in Amazon Simple Storage Service (S3).
1. **Step 3**: Transcription results are written in real time to Amazon Kinesis Data Streams. The transcript processor function reads the transcription stream and enriches the transcription and call metadata.
1. **Step 4**: The transcript processor function reads the transcription stream and enriches the transcription and call metadata.
1. **Step 5**: Amazon Comprehend applies sentiment analysis and enriches the metadata.
1. **Step 6**: The transcription and metadata integrates with agent assistance services powered by Amazon Lex V2 (NLU/NLP) and Amazon Kendra (ML search).
1. **Step 7**: The agent user interface is served through Amazon CloudFront and uses an AWS AppSync API to provide real-time agent assistance during a call.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-samples/amazon-transcribe-live-call-analytics)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Data, such as sentiment analysis of speakers and how well contact center agents meet a customer’s internal compliance rules, is used to identify how effective contact center agents are at handling customer calls. The same data also identifies the topics and entities discussed in the call. All of this data can be visualized in Amazon QuickSight to help business analysts identify trends from a customer’s perspective and potential training needs for agents. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

All data is encrypted both in motion and at rest, and can use customer-controlled AWS Key Management Service (AWS KMS) keys for this encryption. Although the solution is entirely serverless, the AWS Lambda components can optionally run within a customer’s VPC, accessing external services such as Amazon Transcribe and Amazon S3 only through a customer’s approved endpoints. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The solution is entirely serverless, and each of those services (for example, Amazon Transcribe, Amazon S3) operate using multiple Availability Zones in a resilient fashion. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The solution scales its usage of its serverless components as it needs to, both up and down, in order to handle the concurrent processing of potentially thousands of calls or those times when there are no pending calls to process. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

As in the Performance Efficiency pillar, the solution will only use serverless components when there is an active call audio file to process, minimizing the incurred costs as much as possible. If required, the original audio files can be archived to lower-cost long-term storage on a customer-specified schedule in order to minimize storage costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By extensively using managed services and dynamic scaling, we minimize the environmental impact of the backend services. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Live call analytics and agent assist for your contact center with Amazon language AI services**: Your contact center connects your business to your community, enabling customers to order products, callers to request support, clients to make appointments, and much more. When calls go well, callers retain a positive image of your brand, and are likely to return and recommend you to others.  This post demonstrates how to use Amazon Machine Learning (ML) services to transcribe and extract insights from your contact center calls at scale.

[Learn more](https://aws.amazon.com/blogs/machine-learning/live-call-analytics-and-agent-assist-for-your-contact-center-with-amazon-language-ai-services/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
