---
source_url: https://docs.aws.amazon.com/solutions/processing-real-time-data-using-amazon-dynamodb/index.html
---

---
title: 'Guidance for Processing Real-Time Data Using Amazon DynamoDB'
canonical_url: https://docs.aws.amazon.com/solutions/processing-real-time-data-using-amazon-dynamodb/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Processing Real-Time Data Using Amazon DynamoDB

## Overview

This Guidance demonstrates how to use Amazon DynamoDB Streams to build near real-time data aggregations for DynamoDB tables. It outlines the configuration of DynamoDB Streams on a source table and provides sample code to implement an aggregation function. This function polls the stream, performs calculations or transformations on the data, and inserts the aggregated results into a target DynamoDB table. By integrating DynamoDB Streams with tables, you can gain visibility and near real-time insights into critical data, such as sales figures, enabling prompt inventory management and optimized operations.

## How it works

The architecture diagram illustrates near real-time data aggregations in Amazon DynamoDB utilizing DynamoDB Streams and AWS Lambda. It enables efficient computation of aggregated data summaries, enhancing performance and scalability for DynamoDB applications.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/processing-real-time-data-using-amazon-dynamodb.pdf)

![Architecture diagram](/images/solutions/processing-real-time-data-using-amazon-dynamodb/images/processing-real-time-data-using-amazon-dynamodb-1.png)

1. **Step 1**: Amazon API Gateway inserts a new item into the Amazon DynamoDB source table.
1. **Step 2**: DynamoDB automatically sends the new item to the associated Amazon DynamoDB Streams, which capture the item mutation.
1. **Step 3**: AWS Lambda polls the configured DynamoDB Streams four times per second and runs the Aggregation function.
1. **Step 4**: The Lambda function performs the required aggregation logic and inserts the data into the target DynamoDB table (which could also be the same table).
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Implementation Resources The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-processing-real-time-data-using-amazon-dynamo-db)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses DynamoDB Streams to automatically stream changes from your DynamoDB table to Lambda. This eliminates the need for you to build and maintain custom data streaming pipelines. Plus, with logging and monitoring in Amazon CloudWatch, you can quickly identify and troubleshoot any issues that may arise. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

By using DynamoDB and Lambda, you benefit from robust security features built into these AWS services. Specifically, DynamoDB offers encryption for data at rest, while Lambda provides a secure, isolated execution environment. Together, these services help ensure your sensitive data is protected from unauthorized access or tampering. Additionally, this Guidance follows the principle of least privilege, granting only the necessary permissions to the Lambda function to access and process the DynamoDB data, further strengthening the overall security posture. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

DynamoDB, DynamoDB Streams, and Lambda are all fully managed services provided by AWS. Lambda includes features such as automatic retries and error handling mechanisms to manage issues that arise while processing incoming data from the streams. All the services used throughout this Guidance can automatically scale under high loads, don't require downtime for patching, and are fault-tolerant by design with retry mechanisms built in. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses DynamoDB Streams to invoke Lambda functions. Utilizing these services allows you to access aggregated data efficiently without the need for costly table scans, which can be time-consuming and impact system latency. Invoking Lambda functions through DynamoDB Streams not only improves data retrieval efficiency but also addresses potential latency issues that arise from scanning large datasets, enhancing the overall performance of your system. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

With DynamoDB and Lambda, you pay only for the resources you use, eliminating the need to manage hardware. And since DynamoDB Streams is a built-in feature of DynamoDB, streaming data incurs no extra charge. This approach of streaming data from DynamoDB Streams, aggregating it through Lambda functions, and writing the aggregated data back to DynamoDB is more cost-effective compared to performing full table scans for aggregations. It's also more economical than streaming data to a separate database for such calculations. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance supports sustainable workloads through the serverless architecture of Lambda, which optimizes resource allocation and reduces the need to maintain physical hardware. The Lambda functions are only invoked when there is a change in the data in the base DynamoDB table, thus reducing the compute resource run times and the number of executions. This approach helps eliminate the need to maintain physical infrastructure, contributing to more sustainable workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Blog**: This blog post demonstrates how to perform aggregations on a DynamoDB table using Amazon DynamoDB Streams and AWS Lambda.

[Build aggregations for Amazon DynamoDB tables using Amazon DynamoDB Streams](https://aws.amazon.com/blogs/database/build-aggregations-for-amazon-dynamodb-tables-using-amazon-dynamodb-streams/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
