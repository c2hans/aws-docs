---
source_url: https://docs.aws.amazon.com/solutions/post-call-analytics-on-aws/index.html
---

---
title: 'Guidance for Post Call Analytics on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/post-call-analytics-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Post Call Analytics on AWS

## Overview

This Guidance demonstrates a scalable, cost-effective approach to post-call analytics that uses AWS pre-trained artificial intelligence (AI) services. It helps you gather actionable insights by using AI to transcribe and analyze customer conversations. Through advanced natural language processing, this Guidance extracts intent, context, and sentiment cues from these transcripts, allowing you to spot emerging trends and pinpoint areas for improvement. You also gain greater visibility into agent performance, surfacing coaching opportunities to enhance customer experiences.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/post-call-analytics-on-aws.pdf)

![Architecture diagram](/images/solutions/post-call-analytics-on-aws/images/post-call-analytics-on-aws-1.png)

1. **Step 1**: Call audio is delivered from the telephone system to an Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 2**: This event initiates the creation of an AWS Step Functions workflow, which orchestrates the entire analytics process.
1. **Step 3**: AWS pre-trained artificial intelligence (AI) services are called by the workflow at the appropriate times for speech-to-text and text analytics functions. • Amazon Transcribe is called to convert audio call recordings into text transcripts, forming the basis for further analysis. • Amazon Comprehend is called to perform sentiment analysis, entity recognition, and key phrase extraction on the transcribed text. • Amazon Bedrock is called to apply advanced natural language processing tasks for deeper insights into the transcribed text.
1. **Step 4**: Transcript text and AI insights data are delivered to an Amazon S3 bucket to facilitate further analysis.
1. **Step 5**: Supervisors or agents can log in to the Guidance's user interface to review transcripts and insights for specific calls.
1. **Step 6**: Business analysts can log in to Amazon QuickSight to build dashboards based upon the AI insights data, including sentiment trends, agent performance, hot topic trends, and entity insights.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Data, such as speaker sentiment analysis and how well a customer’s internal compliance rules are met, is used to identify how effective contact center agents are at handling customer calls. The same data identifies the topics and entities discussed in the call. All of this data can be visualised in QuickSight to help business analysts identify trends from a customer’s perspective and potential training needs for agents. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

All data is encrypted both in motion and at rest, and can use customer-controlled AWS Key Management Service (AWS KMS) keys for this encryption. The solution is entirely serverless, but the AWS Lambda components can optionally run within a customer’s VPC, accessing external services such as Amazon Transcribe and Amazon S3 only through a customer’s approved endpoints. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The solution is entirely serverless, and each of those services (Amazon Transcribe, Amazon S3) operate using multiple Availability Zones in a resilient fashion. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The solution scales usage of its serverless components as it needs to, both up and down, in order to handle the concurrent processing of potentially thousands of calls or those times when there are no pending calls to process. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The solution only uses serverless components when there is an active call audio file to process, minimizing the incurred costs as much as possible. If required, the original audio files can be archived to lower cost long-term storage on a customer-specified schedule in order to minimize storage costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By using managed services and dynamic scaling, we minimize the environmental impact of the backend services. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Amazon Transcribe Post Call Analytics**: This sample code demonstrates how to provide an end-to-end solution that can process call recordings from your existing contact center.

[Learn more](https://github.com/aws-samples/amazon-transcribe-post-call-analytics)

- **Post call analytics for your contact center with Amazon language AI services**: This post demonstrates how to use Amazon Machine Learning (ML) services to transcribe and extract insights from your contact center audio recordings at scale.

[Learn more](https://aws.amazon.com/blogs/machine-learning/post-call-analytics-for-your-contact-center-with-amazon-language-ai-services/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
