---
source_url: https://docs.aws.amazon.com/solutions/hotel-check-in-experience-on-aws/index.html
---

---
title: 'Guidance for Hotel Check-In Experience on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/hotel-check-in-experience-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Hotel Check-In Experience on AWS

## Overview

This Guidance shows how Hospitality companies can leverage artificial intelligence and event-driven services to automatically trigger check-in and registration activities, providing a more seamless experience for for travelers/guests.

## How it works

Provide a frictionless check-in experience for guests whether they use mobile, web, or kiosk. Create personalized interactions by checking in guests anywhere in the lobby while upselling upgrades and amenities during the process.

[Download the architecture diagram](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/guidance-for-hotel-check-in-experience-ra.pdf)

![Architecture diagram](/images/solutions/hotel-check-in-experience-on-aws/images/hotel-check-in-experience-on-aws-1.png)

1. **Step 1**: Ingest real-time customer activity either from central and on-premises systems as application events with Amazon EventBridge or directly from software as a service (SaaS) applications with Amazon AppFlow.
1. **Step 2**: Process customer activity and detect the guest location and journey stage (for example, checking in) with AWS Step Functions.
1. **Step 3**: Infer the next best action by invoking AWS Lambda and Amazon SageMaker trained machine learning (ML) model.
1. **Step 4**: Amazon DynamoDB tables store customer check-in info, location, and recommended next best action, then triggers guest notifications with Amazon DynamoDB Streams.
1. **Step 5**: Use Amazon Pinpoint to notify guests about check in, room readiness, and other events over channels like email, SMS, push, or in-app messaging.
1. **Step 6**: The hotel's mobile or web app or on-property guest service apps send requests through an Amazon API Gateway endpoint.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The reference architecture can be scripted using Amazon CloudFormation, added to your own development pipeline, and deployed in your cloud environment. Use Amazon CloudWatch to increase your observability with application and service-level metrics, personalized dashboards, and logs. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

With Amazon Cognito user pools, you can use identity pools to provide built-in user management and secure access to APIs. The Lambda back end only has access to the services they need with least privileged roles. The guest data in DynamoDB and Amazon Simple Storage Service (Amazon S3) is encrypted at rest. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

EventBridge and Amazon AppFlow are fully managed services that provide consistent throughput at scale. All the serverless components are highly available and automatically scale based on usage. We recommend DynamoDB cross-region deployment for higher availability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Serverless architectures help you provision the exact resources that the workload needs. Monitor for expected performance by using CloudWatch alarms and Lambda metrics. For unexpected traffic, configure DynamoDB on-demand; use provisioned mode for consistent traffic. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Serverless architectures provide a pay-per-value pricing model and scale based on demand. A good practice is to use AWS Budgets to create budgets for cost and usage governance. Create and use Cloud Intelligence Dashboards for comprehensive cost management and financial optimization. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By choosing serverless services, you are using only the resources that you need and therefore reducing impacts. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
