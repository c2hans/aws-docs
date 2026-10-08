---
source_url: https://docs.aws.amazon.com/solutions/content-moderation-on-aws/index.html
---

---
title: 'Guidance for Content Moderation on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/content-moderation-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Content Moderation on AWS

Moderate content with machine learning services to protect users

## Overview

This Guidance helps you implement a serverless architecture to efficiently moderate the increasing influx of user-contributed content and sensitive information. This content and information can come from a broad range of industries including gaming, social media, e-commerce, and regulated environments, such as healthcare and financial services.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/guidance-for-content-moderation-on-aws-ra.pdf)

![Architecture diagram](/images/solutions/content-moderation-on-aws/images/content-moderation-on-aws-1.png)

1. **Step 1**: Customers upload their content into the AWS Cloud.
1. **Step 2**: Content moves securely into an Amazon Simple Storage Service (Amazon S3) bucket or another data store.
1. **Step 3**: Workflows, publisher/subscription patterns, and custom code are used to moderate the content.
1. **Step 4**: The audio streams within video streams are processed using Amazon Transcribe and Amazon Rekognition, and content moderation categories are extracted using simple APIs.
1. **Step 5**: Amazon Transcribe is used to convert audio into text, alongside natural language processing (NLP) with Amazon Comprehend.
1. **Step 6**: Amazon Textract is used to extract content, with Amazon Comprehend natural language processing then used to moderate content.
1. **Step 7**: Employee input helps customize model vocabularies and image labels using Amazon SageMaker Ground Truth.
1. **Step 8**: Bring people into the loop for scenarios that aren't fully automatable using Amazon Augmented AI (Amazon A2I).
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

By choosing Lambda and Amazon S3 you can implement shared design standards. Providing you with the ability to share created assets across accounts, environments and teams. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance makes use of managed services to help you reduce the security maintenance tasks as part of the shared responsibility model. While out of scope for this Guidance, you can also validate the integrity of the software that runs in your Lambda functions. By choosing managed services you ensure AWS API calls are all done through HTTPS endpoints using TLS communication, thus protecting data in transit. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

By using Amazon API Gateway you ensure highly available network connectivity for this Guidance public endpoint as well as providing automatic protection against Distributed Denial of Service (DDoS) attacks through AWS Shield at no extra cost. By using a combination of Amazon EventBridge and Amazon Simple Queue Service (Amazon SQS) you are able to implement loosely couple dependencies, allowing us to isolate the behavior of a component from other components that depend on it, increasing resiliency and agility. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

By choosing managed serverless services, you can offload the need to manage scaling requirements. With Lambda, simply upload your code, and the service will manage everything required to run and scale that code. And Amazon API Gateway handles all the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance makes use of serverless or application-level services Lambda and Amazon SQS to remove the need to manage resources. By choosing both managed and serverless services you have the ability to set attributes that can ensure sufficient capacity. You must set and monitor these attributes so that your excess capacity is kept to a minimum and performance is maximized. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By choosing managed services, you remove the need to identify periods of low or no utilization in your resources. This Guidance optimizes software and architecture for asynchronous and scheduled jobs by using queue-driven architectures. Various user-contributed content do not require immediate action and as such they can be scheduled to avoid load spikes and resource contention from simultaneous execution. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Content moderation design patterns with AWS managed AI services**

[Learn more](https://aws.amazon.com/blogs/machine-learning/content-moderation-design-patterns-with-aws-managed-ai-services/)

- **Utilize AWS AI services to automate content moderation and compliance**

[Learn more](https://aws.amazon.com/blogs/machine-learning/utilize-aws-ai-services-to-automate-content-moderation-and-compliance/)

- **Protect your users, brand, and budget with AI-powered content moderation**

[Learn more](https://d1.awsstatic.com/psc-digital/2022/gc-400/ml-leading-use-case-ebook/204863_AWS_ML_Content_Moderation_eBook_Final.pdf)

[Read usage guidelines](/solutions/guidance-disclaimers/)
