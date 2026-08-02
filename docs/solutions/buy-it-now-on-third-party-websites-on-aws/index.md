---
source_url: https://docs.aws.amazon.com/solutions/buy-it-now-on-third-party-websites-on-aws/index.html
---

# Guidance for Buy-It-Now on Third Party Websites on AWS

## Overview

This Guidance helps consumer packaged goods (CPG) companies keep customers on their brand sites, even while purchasing products from a third-party online retailer. By keeping customers on the brand site, CPG companies can capture higher-quality, first-party data on the customer based on their purchase. CPG companies can still send the sales transactions to the retailer, while maintaining the customer experience on their brand site.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/buy-it-now-on-third-party-websites-on-aws.pdf)

![Architecture diagram](/images/solutions/buy-it-now-on-third-party-websites-on-aws/images/buy-it-now-on-third-party-websites-on-aws-1.png)

1. **Step 1**: Amazon API Gateway authenticates the client.
1. **Step 2**: The client browses the available products on the brand website using the Product Manager AWS Lambda function. Amazon DynamoDB stores the products.
1. **Step 3**: The client selects the items they want to purchase and adds them to a cart in DynamoDB using the Cart Manager Lambda function.
1. **Step 4**: The client views the cost of the items in the cart using the Third-party Product Manager Lambda from multiple stores. The third-party store endpoints retrieve the price of the items in the cart.
1. **Step 5**: AWS Step Functions Order Manager workflow places the order. The Initialize Order Lambda function locks the inventory in the third-party store using the selected store endpoint.
1. **Step 6**: The Verify Payment Lambda function uses the secrets stored in AWS Secrets Manager to verify the payment details using the third-party payment validation endpoint.
1. **Step 7**: The Add Customer Lambda function adds the client's details and any store loyalty details to the DynamoDB table.
1. **Step 8**: The Place Order Lambda function uses the selected store endpoint to place the order.
1. **Step 9**: The Capture Order Lambda function captures the order details from the previous step and stores it in the DynamoDB table.
1. **Step 10**: Amazon Simple Notification Service (Amazon SNS) updates the status of the order. If the client has subscribed to the SNS topic, they will receive an email with the order details.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-buy-it-now-on-third-party-website-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch provides centralized logging with metrics and alarms to raise alerts for operational anomalies. You should also consider using tags for better organization, identification, and cost accounting. Tags help in identifying how to respond to alarms and events on a granular level. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

DynamoDB encrypts data at rest by default using the DynamoDB-owned AWS Key Management Service (AWS KMS) key. You can use the default AWS-owned encryption key, an AWS-managed key, or a customer-managed key. By default, Lambda encrypts the environmental variables at rest using the AWS-managed KMS key. You can optionally configure Lambda to use a customer-managed key instead of the default AWS-managed key. By default, CloudWatch encrypts the logs at rest using server-side encryption. You can use customer-managed KMS keys for more control over log encryption. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses a Step Functions workflow that provides built-in retry capabilities. It also uses Amazon SNS, which supports built-in retry capabilities that can be configured for a reliable, loosely-coupled architecture. Amazon SNS also uses a dead-letter queue to capture events that fail, even after multiple retries. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

You can optimize DynamoDB read operations through Amazon DynamoDB Accelerator (DAX). Using DAX improves the performance of the application and reduces the read capacity units (RCUs) used by DynamoDB. Additionally, you can enable API-caching for API Gateway to enhance responsiveness. This will reduce the number of calls made to the endpoint and improve the latency of the requests to the API. You can also enable payload compression for your API to improve responsiveness. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By choosing the most appropriate RCUs and write capacity units (WCUs) for DynamoDB, you can reduce overall costs for this service. Analyze data access patterns to confirm that you are not overprovisioning RCUs and WCUs. You should also use efficient data modeling and querying to reduce the amount of consumed capacity. One of the major factors for determining cost of running Lambda functions is the high frequency of invocation. You can reduce this frequency by adding Amazon CloudFront caching in front of API Gateway. This approach is helpful for infrequently changing data, such as the list of products available on the site. While adding CloudFront increases CloudFront cost, it decreases API Gateway and Lambda costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Based on the query patterns for this Guidance, we have created a data model that works with a single DynamoDB table. When you use this Guidance, you should identify and remove unused DynamoDB resources based on your use case and avoid overprovisioning RCUs and WCUs. Use the Time to Live (TTL) feature to clear old data and compress data. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
