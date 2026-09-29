---
source_url: https://docs.aws.amazon.com/solutions/real-time-text-search-using-amazon-opensearch-service/index.html
---

---
title: 'Guidance for Real-Time Text Search Using Amazon OpenSearch Service'
canonical_url: https://docs.aws.amazon.com/solutions/real-time-text-search-using-amazon-opensearch-service/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Real-Time Text Search Using Amazon OpenSearch Service

## Overview

This Guidance enables you to integrate Amazon DynamoDB with Amazon OpenSearch Service to enable real-time search. Most applications should use Amazon DynamoDB zero-ETL integration with Amazon OpenSearch Service. For applications with requirements that do not align with zero-ETL integration, this Guidance demonstrates how to perform an initial load of data from DynamoDB into OpenSearch Service through parallel functions and how to replicate new data into OpenSearch Service. By keeping data in both places, you can target queries to the database best suited to your requirements: DynamoDB powers any fixed access patterns that require performance and scalability, and OpenSearch Service powers access patterns that require flexibility in searching and filtering.

## How it works

This architecture diagram shows how to load and stream data from an Amazon DynamoDB table to Amazon OpenSearch Service to support real-time, open-ended searching and filtering.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/real-time-text-search-using-amazon-opensearch-service.pdf?target=_blank)

![Architecture diagram](/images/solutions/real-time-text-search-using-amazon-opensearch-service/images/real-time-text-search-using-amazon-opensearch-service-1.png)

1. **Step 1**: To process existing data, an AWS Lambda function is invoked to describe the Amazon DynamoDB table and split it into a number of segments based on the returned item count. The function writes one message to an Amazon Simple Queue Service (Amazon SQS) queue for each segment number.
1. **Step 2**: Amazon SQS acts as an event source for Lambda. Lambda will invoke functions from messages in the queue and process segments of the DynamoDB table in parallel.
1. **Step 3**: The Lambda function uses a parallel scan to read the segment of the DynamoDB table listed in the source event from Amazon SQS.
1. **Step 4**: The function then writes the data retrieved from DynamoDB into Amazon OpenSearch Service in batches through the bulk-create operation.
1. **Step 5**: Insert or update items in DynamoDB to invoke capture by DynamoDB streams.
1. **Step 6**: DynamoDB streams send item-level modifications captured from DynamoDB to the Lambda streaming update function.
1. **Step 7**: The Lambda function writes that data in batches to OpenSearch Service through the bulk index operation. Track ingested documents with the SearchableDocuments metric in Amazon CloudWatch.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Deploy this Guidance Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-solutions-library-samples/guidance-for-real-time-text-search-using-amazon-dynamodb)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS Cloud Development Kit (AWS CDK) defines the infrastructure for the solution as code, helping you achieve consistent deployment. Lambda divides work into smaller units of work, each responsible for a different application function. These single-task functions reduce human error and support small incremental changes that are easier to reverse if they fail. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Where applicable, this Guidance launches services in private Amazon Virtual Private Cloud (Amazon VPC) networks rather than public. Private networking through Amazon VPC supports security at all layers by letting you control how data is accessed. Additionally, the use of single-purpose, least-privilege AWS Identity and Access Management (IAM) policies helps you prevent permission changes from having broader, unanticipated consequences and reduces the risk of users mishandling sensitive data. AWS Secrets Manager generates and securely stores admin secrets, preventing users from storing credentials in code or environment variables where they are at risk of exposure. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon SQS provides an automatic retry mechanism if a portion of the import fails, helping you quickly recover from failures. As the system of record, DynamoDB uses point-in-time recovery for continuous backup, enabling recovery to any second within the last 35 days. OpenSearch Service helps you prevent drift between the two databases by using the “create” operation for initial data loading, preventing older data from overwriting newer data. OpenSearch Service is set to use a single-node cluster, but you can change this to a multi–Availability Zone cluster to maintain availability in production. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda enables you to parallelize workloads: reads from DynamoDB go through segmented parallel scans split across multiple Lambda function invocations. This parallelization enables significantly higher throughput than a single thread could manage. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda reads DynamoDB items together in a batch rather than as individual GetItem requests. As a result, this Guidance consumes fewer read capacity units. By lowering the amount of work spent on tasks like initializing connections, the use of batches reduces compute time and the number of Lambda invocations, lowering your compute costs. Additionally, OpenSearch Service batch operations are efficient, helping you reduce the overall cost of compute resources. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda only invokes functions when data needs to be moved into OpenSearch Service and does not run while idle. This helps you maximize your utilization of compute resources. Additionally, as a serverless, managed service, DynamoDB helps reduce inefficiencies and decrease the total power consumed by your workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Amazon DynamoDB zero-ETL integration with Amazon OpenSearch Service is now available**: This blog post demonstrates how to get started with Amazon DynamoDB zero-ETL integration with Amazon OpenSearch Service.

[Read the blog](https://aws.amazon.com/blogs/aws/amazon-dynamodb-zero-etl-integration-with-amazon-opensearch-service-is-now-generally-available/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
