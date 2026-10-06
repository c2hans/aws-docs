---
source_url: https://docs.aws.amazon.com/solutions/near-real-time-personalized-recommendations-on-aws/index.html
---

---
title: 'Guidance for Near Real-Time Personalized Recommendations on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/near-real-time-personalized-recommendations-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Near Real-Time Personalized Recommendations on AWS

## Overview

This Guidance helps businesses build a real-time recommendation pipeline using Amazon Personalize. The pipeline creates personalized recommendations based on a user’s profile and behavior to improve the customer experience. Developers can use this Guidance to show personalized recommendations, including recommended products, promotions, and items for upsell or cross-sell. This Guidance provides an Advanced Composite Recipe that retrieves information stored in Amazon DynamoDB about items similar to the item a user is viewing. It combines this information with a User Personalized Ranking Recipe to generate item recommendations for cross-selling.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/near-real-time-personalized-recommendations-on-aws.pdf)

![Architecture diagram](/images/solutions/near-real-time-personalized-recommendations-on-aws/images/near-real-time-personalized-recommendations-on-aws-1.png)

1. **Step 1**: Amazon Athena queries and exports historical user interaction data from Google Analytics to Amazon Simple Storage Service (Amazon S3) using Google BigQuery. This data is used to train the Amazon Personalize user recommendation model.
1. **Step 2**: The user interacts with a website or a mobile app that uses Google Tag Manager (GTM) tags to track user interactions.
1. **Step 3**: A GTM tag submits the user interaction event to Amazon API Gateway. The user event record is sent to Amazon Kinesis. AWS Lambda reads the records from the Kinesis stream and submits it to Amazon Personalize.
1. **Step 4**: A GTM tag gets recommendations for the user. Amazon Personalize recommends items using the Recommended For You Recipe.
1. **Step 5**: Advanced Composite Recipe: The user adds items to their cart. A GTM tag requests recommended items for cross-sell. Lambda gets "similar item" recommendations from Amazon DynamoDB and re-ranks with a User Personalized Ranking Recipe in Amazon Personalize, including promotional items.
1. **Step 6**: An Amazon EventBridge time-based event triggers Lambda, which starts an Amazon Personalize batch inference to get similar items. Inference results are stored in Amazon S3, and Lambda writes them to DynamoDB for use in the Advanced Composite Recipe.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-samples/amazon-personalize-online-recommendations-with-google-tag-manager)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

You can monitor Amazon CloudWatch metrics like GetRecommendationsLatency, DatasetImportJobError, and PutEventsRequests in Amazon Personalize. You can configure CloudWatch alarms with Amazon Simple Notification Service (Amazon SNS) notifications. Additionally, you can monitor Amazon Personalize using the Amazon Personalize monitor. You can configure CloudWatch alarms based on metrics with Lambda, API Gateway, DynamoDB, and other services in this architecture. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Data stored in Amazon Personalize is encrypted at rest with Amazon Personalize-managed AWS Key Management Service (AWS KMS) keys. Amazon Personalize uses transport layer security (TLS) with AWS certificates to encrypt any data sent to other AWS services. Any communication with other AWS services happens over HTTPS, and Amazon Personalize endpoints support only secure connections over HTTPS. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The managed services in this architecture, including Amazon Personalize, use the AWS global infrastructure for data resiliency. When creating an Amazon Personalize resource in an AWS Region, Amazon Personalize manages the resilience and data redundancy of the resource across multiple Availability Zones. Additionally, DynamoDB uses AWS Auto Scaling to dynamically adjust provisioned throughput capacity in response to actual traffic patterns. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Services in this architecture scale according to traffic patterns. For example, API Gateway automatically scales to handle the amount of traffic received through the API. Throttling ensures that API traffic is controlled to help your backend services maintain performance and availability. Additionally, Lambda scales up as invocations increase exponentially. Lambda initializes a new instance for any request that can't be routed to an available instance. When the burst concurrency limit is reached, the function starts to scale linearly. Amazon Personalize automatically scales to meet demand of near real-time recommendations. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This architecture uses application level services, including Amazon Personalize, Lambda, and DynamoDB, which use the pay as you go model, meaning you only pay for the exact resources you use. Additionally, Amazon Personalize includes training costs based on training hours in addition to campaigns costs based on transactions per second (TPS)-hour for near real-time recommendations and the number of recommendations for batch processing. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This architecture uses managed services (such as Amazon Personalize, DynamoDB, and Lambda) which optimize utilization of the architecture’s underlying resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
