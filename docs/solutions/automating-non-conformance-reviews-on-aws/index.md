---
source_url: https://docs.aws.amazon.com/solutions/automating-non-conformance-reviews-on-aws/index.html
---

---
title: 'Guidance for Automating Non-Conformance Reviews on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/automating-non-conformance-reviews-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Automating Non-Conformance Reviews on AWS

## Overview

This Guidance shows how to automate non-conformance review (NCR) disposition recommendations using generative AI and image analysis to reduce manufacturing delays. It demonstrates a multimodal recommender system that integrates with existing quality ticketing systems to accelerate quality engineering decisions. The Guidance processes natural language descriptions and images of non-conformances, matching them with similar historical cases to suggest appropriate dispositions. By leveraging past NCR data to provide rapid, consistent recommendations, this Guidance helps quality engineers make faster decisions, reducing the time spent waiting for manual research and getting production back on track more quickly.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automating-non-conformance-reviews-on-aws.pdf)

![Architecture diagram](/images/solutions/automating-non-conformance-reviews-on-aws/images/automating-non-conformance-reviews-on-aws-1.png)

1. **Step 1**: Enter description of non-conformance into quality management interface, with images, part #, and other details. The App sends NCR information to AWS through Amazon API Gateway.
1. **Step 2**: Process NCR API requests automatically using AWS Lambda functions (sequenced by AWS Step Functions). Lambda invokes computer vision services for defect identification using Amazon Rekognition Custom Labels or third-party models.
1. **Step 3**: Record image and metadata to Amazon Simple Storage Service (Amazon S3) and Amazon DynamoDB.
1. **Step 4**: Query your large language model (LLM) for recommendation on disposition for the NCR using the Amazon Bedrock workflow for NCRs.
1. **Step 5**: Find the most relevant historical NCRs using Amazon Bedrock native integration to Amazon OpenSearch Service vector engine. The LLM uses this info as context to synthesize the best recommendation.
1. **Step 6**: Return recommendations to the user through an API Gateway response. Recommendations include most relevant past NCRs with associated images.
1. **Step 7**: Select final disposition in the UI, taking recommendations into account. This selection is sent to AWS through API Gateway.
1. **Step 8**: Automate entry of final NCR into a ticketing system using Amazon Bedrock Agents.
1. **Step 9**: Automate other workflows through Amazon Bedrock Agents using APIs to third-party systems over a secure AWS Virtual Private Network (AWS VPN). For example, if the NCR requires rework, queue up work orders in your manufacturing execution system (MES) or replacement part orders in your enterprise resource planning (ERP.)
1. **Step 10**: Continuously update your knowledge bases based on new NCR feedback, using Amazon EventBridge to trigger scheduled or on-demand re-indexing. Data mutations trigger EventBridge events, which coordinate idempotent re-indexing through Step Functions and Lambda, while images use versioning or timestamp-based naming.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-automating-non-conformance-reviews-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon S3, DynamoDB, and OpenSearch Service provide comprehensive monitoring features that offer early failure detection, while their versioning and recovery features enable rapid recovery of critical NCR and application state data. Amazon S3 delivers document versioning and automated lifecycle management, and DynamoDB offers snapshots, event monitoring, alerting, point-in-time (PiT) recovery, and automated replication. OpenSearch Service contributes snapshots, event monitoring, and automatic recovery. These capabilities support seamless operations management, minimize downtime from disruptive failures, and help ensure smooth version upgrades. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon Bedrock isolates training and inference data for LLMs within private accounts. Amazon S3, DynamoDB, and OpenSearch Service implement encryption of all data at rest, including search indices and log files, using service-managed keys by default. You can override this to use your own AWS Key Management Service (AWS KMS)-managed keys. This Guidance helps ensure that application data, NCR databases, problem descriptions, and recommended dispositions remain accessible only to authorized users. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon S3 provides 99.999999999%  (11 9's) of data durability through multi-Availability Zone (AZ) distribution, while DynamoDB and OpenSearch Service automatically manage replica deployment for changing capacity demands. Amazon Bedrock, Lambda, Step Functions, API Gateway, and Amazon Rekognition deliver fully-managed, auto-scaling capabilities to handle varying NCR processing workloads. Built-in version management features in Amazon Bedrock and Lambda provide controlled updates with automatic rollback capabilities. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

DynamoD B has a NoSQL architecture delivers single-digit millisecond access times, while Amazon Bedrock, Lambda, and Amazon Rekognition automatically adjust resource allocation to match customer workload demands. Rather than over-provisioning for peak production times, you can leverage these services to dynamically scale computing capacity. The Guidance eliminates the need to manage dedicated ML infrastructure for LLM processing or computer vision systems for defect classification. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3 provides low-cost storage with auto-tiering options for archiving infrequently-accessed data or automated deletion. DynamoDB delivers cost-effective database storage with auto-snapshots and time-to-live (TTL) features. Lambda and Step Functions implement pay-as-you-go serverless computing, while Amazon Bedrock uses a pay-per-token model that charges only for actual LLM usage. The common API framework allows easy experimentation with different models to optimize price-performance ratios, helping you match computing and storage costs to actual NCR demand without upfront investment. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon S3 has auto-tiering and auto-deletion capabilities move infrequently-used data to lower-impact storage tiers or remove it entirely. The DynamoDB TTL feature and automated storage snapshots enable efficient data lifecycle management. Lambda provides a serverless compute model that allocates resources strictly based on demand. Together, these services automatically reduce storage and compute resource usage during idle periods or when reference dispositions age out, minimizing your environmental footprint through efficient resource utilization. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
