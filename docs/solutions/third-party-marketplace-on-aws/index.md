---
source_url: https://docs.aws.amazon.com/solutions/third-party-marketplace-on-aws/index.html
---

---
title: 'Guidance for Third-Party Marketplace on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/third-party-marketplace-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Third-Party Marketplace on AWS

## Overview

This Guidance demonstrates how retailers can onboard new suppliers and process orders of these suppliers’ products to help them provide customers with more product choices without higher inventory cost. It is designed for retailers who want to offer a wide range of products to their customers, but can’t always take on the cost of holding the inventory. For many retailers, creating an online marketplace for third-party sellers addresses this problem and creates an additional revenue stream through listing fees. With this Guidance, retailers can implement the marketplace software that allows them to quickly recruit and onboard new sellers and list their products alongside their own, offering their customers more choice. When these new products are ordered, the order is routed to the seller for fulfillment and the retailer collects their fee.

## How it works

This architecture diagram demonstrates how retailers can onboard new suppliers and process orders of these suppliers’ products, enabling the retailer to provide their customer with more product choices without higher inventory cost.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/third-party-marketplace-on-aws.pdf)

![Architecture diagram](/images/solutions/third-party-marketplace-on-aws/images/third-party-marketplace-on-aws-1.png)

1. **Step 1**: A new supplier uses Amazon API Gateway for onboarding the third-party marketplace by providing brand information.
1. **Step 2**: AWS Lambda function stores the supplier's information in Amazon DynamoDB.
1. **Step 3**: Any changes to the DynamoDB tables generates a DynamoDB Stream, which Amazon EventBridge Pipes use to invoke AWS Step Functions.
1. **Step 4**: Step Functions verifies the modified supplier information through various custom validation steps, including calling several Lambda functions.
1. **Step 5**: When an inconsistent data point is detected, the problematic record can either go through automated correction steps or be put in an Amazon Simple Queue Service (Amazon SQS) queue for manual review. Administrators from the retailer are able to modify the DynamoDB record with their corrections.
1. **Step 6**: After successful onboarding, the suppliers are able to update their products following a similar process for product registration.
1. **Step 7**: A shopper who is interested in a third-party supplier's product is able to place the order through the API Gateway.
1. **Step 8**: The order management system (OMS) accepts the order through an integration layer, and processes it through an API layer.
1. **Step 9**: The allocation engine is able to call the third-party supplier's provided Order Acceptance API to successfully process the placed order.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-third-party-marketplace-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The services deployed in this Guidance can help you better understand your workloads and their expected behaviors by each emitting their own set of metrics into Amazon CloudWatch, where you can monitor errors. CloudWatch provides a centralized dashboard with logs and metrics, and can also be configured with alerts for operational anomalies. Additionally, consider tagging your CloudWatch resources for better organization, identification, and cost accounting. A tag is a custom label that you or AWS assigns to an AWS resource and can help in identifying how to respond to alarms and events. Additionally, you can leverage AWS Cost Anomaly Detection to detect unusual activity on your account, so you can understand and monitor the state of the resources consumed by this Guidance. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

By default, the data in this Guidance is encrypted at rest using the DynamoDB-owned key from AWS Key Management Service (AWS KMS). You can use the default AWS-owned encryption key, use an AWS managed key (the key that is created on your behalf), or a customer managed key (the key that you create). Lambda, by default, encrypts the environmental variables used at rest using the AWS managed KMS key. You can optionally configure Lambda to use a customer managed key instead of the default AWS managed key. Additionally, CloudWatch encrypts the logs by default at rest using server-side encryption. You can also use customer managed AWS KMS keys to get more control over encryption of the logs. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

There are several architectural components in this Guidance that support loose coupling, so you can implement a reliable application-level architecture. For example, the DynamoDB streams invoke a data validation process whenever new entries are made to DynamoDB tables. Also, Step Functions that host the data validation workflow have built-in retry capabilities. Additionally, error handling is multifaceted, from automated data recovery to manual verification that is performed on entries on Amazon SQS. Amazon SQS helps decouple the dependency between identifying an error that needs manual intervention, and implementing a workflow that allows administrators to perform data corrections. Amazon SQS also has the capability to use dead-letter queues to capture messages that fail even after multiple retries. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services selected for this Guidance, including Lambda, DynamoDB, and API Gateway, were selected because they are serverless services. Serverless services feature automatic scaling. If there is an influx of changes occurring in the content, the Guidance will scale accordingly, and make changes in near real-time. To optimize the process of the Lambda function, you can use the Lambda Power Tuning tool which automates the manual process of running tests on functions with different memory allocations, and then measuring the time taken to complete. The DynamoDB operations can be optimized by using Amazon DynamoDB Accelerator (DAX) that improves the performance of the application and also reduces the read capacity units used by DynamoDB. Finally, API Gateway allows for API caching to enhance responsiveness. This will reduce the number of calls made to the endpoint and improve the latency of the requests to the API. You can also enable payload compression for your API to improve responsiveness. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance relies on serverless AWS services—DynamoDB, Lambda, Step Functions, Amazon SQS, and API Gateway—that are fully managed and auto-scale according to workload demand. As a result, you only pay for what you use and save cost at times of low load. DynamoDB resources and costs can be reduced by choosing the most appropriate read capacity units (RCU) and write capacity units (WCU). By analyzing the data access patterns, you should refrain from over provisioning RCU and WCU. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS managed services help to scale up and down according to business requirements and traffic, and are inherently more sustainable than on-premises solutions. Additionally, leveraged serverless components automate the process of infrastructure management and make it more sustainable. Based on the query patterns for the Guidance, we have created a data model that works with a single DynamoDB table. When you use this Guidance, you should identify and remove unused DynamoDB resources based on your needs and avoid over provisioning RCU and WCU. You can also reduce resources by clearing old data using Time to Live (TTL) and compressing data. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
