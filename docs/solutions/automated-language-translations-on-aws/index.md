---
source_url: https://docs.aws.amazon.com/solutions/automated-language-translations-on-aws/index.html
---

---
title: 'Guidance for Automated Language Translations on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/automated-language-translations-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Automated Language Translations on AWS

## Overview

This Guidance helps sellers perform content localization and accurate translations so they can adapt their content for a global audience. Amazon Translate allows ecommerce and marketplace retailers to translate millions of product titles, descriptions, and interactions between customers and sellers. In a global economy with customers around the world, localization can improve customer interactions and increase transactions. By automating content translation at scale, this Guidance minimizes the manual work involved with maintaining localized content.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automated-language-translations-on-aws.pdf)

![Architecture diagram](/images/solutions/automated-language-translations-on-aws/images/automated-language-translations-on-aws-1.png)

1. **Step 1**: This architecture relies on external data sources and covers two common systems: Production Information Management (PIM) and Content Management Systems (CMS). The architecture assumes a webhook integration, where the destination API is built using Amazon API Gateway. The ProductChanged AWS Lambda function dissects the incoming payload and transforms it into a consistent message format.
1. **Step 2**: Amazon EventBridge is the central event bus that decouples domains and systems. EventBridge will pass events between systems. For example, the ProductChanged event will be pushed into EventBridge. The translation workflow built with AWS Step Functions can be a target with a specific filter.
1. **Step 3**: Using Step Functions, the translation workflow will kick off the process of automated translation with Amazon Translate, a neural machine translation service. Forward and backward translations provide a mechanism to compare and generate an accuracy score for the translation. Based on this score, the translation event can then be sent for further human review.
1. **Step 4**: The translation management user interface (UI) is a web application for translators to conduct administrative activities. It allows translators to override translations that are deemed low quality or to confirm quality of content so it can be published automatically. Amazon Cognito provides authentication to the application. Amazon CloudFront provides a content distribution network to give your global translator workforce quick and secure access to the interface. AWS Amplify provides the tooling to help build and ship changes to this application. API Gateway allows an endpoint to interact with dynamic data. Lambda helps with powering the user interface and kicks off the continuation of the Step Functions workflow.
1. **Step 5**: Translators that help verify and improve content quality come from a globally distributed workforce. A scalable reporting suite using Amazon QuickSight provides insights to translators around the world. The suite also helps the review team confirm that the content pipeline is in good condition and the backlog is manageable. The reporting suite provides an opportunity to collect customer feedback on the translation quality of the content in addition to product information for further quality review.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS managed services emit their own set of metrics into Amazon CloudWatch, where you can monitor services for errors and set up CloudWatch alarm notifications. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This solution uses Amazon Cognito to authenticate translators prior to providing them with access to the translation management application. For data ingress from the PIM and CMS, this architecture will provide flexible authentication options including API keys, AWS Identity and Access Management (IAM) if the source system supports it, and customer authentication against a different identity provider using Lambda authorizers. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance is based on an event-driven, distributed architecture. It uses a Step Functions workflow that provides built-in retry capabilities. Additionally, it uses EventBridge to support built-in retry capability for up to 24 hours with exponential back-off, a pattern where the wait time is increased exponentially after every retry attempt, and jitter, which adds some amount of randomness to the backoff to spread the retries around in time. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Serverless technologies feature automatic scaling. If there is an influx of changes in the translation content, the architecture will scale accordingly and make changes in near real time. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This architecture follows a serverless-first approach. Where possible, serverless services scale based on the number of content changes, which means costs will scale based on service usage. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS managed services scale up and down according to business requirements and traffic, making them more sustainable than on-premises architectures that do not offer on-demand scalability. Additionally, serverless components of this architecture automate the process of infrastructure management. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
