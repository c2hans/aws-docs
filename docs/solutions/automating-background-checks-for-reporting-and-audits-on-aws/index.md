---
source_url: https://docs.aws.amazon.com/solutions/automating-background-checks-for-reporting-and-audits-on-aws/index.html
---

---
title: 'Guidance for Automating Background Checks for Reporting & Audits on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/automating-background-checks-for-reporting-and-audits-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Automating Background Checks for Reporting & Audits on AWS

## Overview

This Guidance shows how you can automate background check reporting and auditing using AWS artificial intelligence and analytics services and immutable ledger technology. Background checks are essential for every business to assess hiring risks and comply with industry standards, like Service Organization Control Type 2 (SOC2). However, manual auditing processes can be redundant, error-prone, inefficient at scale, time-consuming, and often have no precise mechanism to track the history of when data is updated. By using this Guidance, you can set up a solution that automates tasks, increases quality and efficiency, and tracks history and data lineage, helping you meet compliance requirements while building a strong brand reputation. Please note: [Disclaimer]

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automating-background-checks-for-reporting-and-audits-on-aws.pdf)

![Architecture diagram](/images/solutions/automating-background-checks-for-reporting-and-audits-on-aws/images/automating-background-checks-for-reporting-and-audits-on-aws-1.png)

1. **Step 1**: Risk and compliance teams receive background check reports from direct sources or third-parties, which are then uploaded into Amazon Simple Storage Service (Amazon S3). These reports are stored in Amazon S3 using frontend applications or are automatically moved from the Network File System (NFS) or Server Message Block (SMB) storage using AWS DataSync or AWS Storage Gateway.
1. **Step 2**: The reports are processed in batches using a preconfigured Amazon EventBridge scheduler, which initiates a three-stage AWS Step Functions workflow based on a defined schedule in an asynchronous fashion.
1. **Step 3**: The report extraction stage uses an AWS Lambda function as an invocation type to read files from Amazon S3. Amazon Textract extracts data from the report files and stores it on Amazon Simple Queue Service (Amazon SQS). Amazon SQS supports dead-letter queues (DLQs), which other queues can target for messages that are not processed successfully.
1. **Step 4**: In the storage stage, a Lambda function (as an invocation type) reads the messages from Amazon SQS and stores the message payload on Amazon Quantum Ledger Database (Amazon QLDB). Amazon QLDB maintains the entire history of data changes on individual data records in an immutable fashion for full traceability. Any messages that are not processed successfully are moved to the DLQ.
1. **Step 5**: In the notification stage, a Lambda function validates messages on the DLQ and sends email notifications using Amazon Simple Notification Service (Amazon SNS).
1. **Step 6**: Depending on the required frequency for reporting, the EventBridge scheduler invokes the daily, weekly, or monthly data extraction from Amazon QLDB using a Lambda function in an Amazon Ion format. It then stores the data on Amazon S3 as a raw export and invokes an AWS Glue workflow.
1. **Step 7**: An AWS Glue workflow transforms the Amazon Ion extract from Amazon QLDB into partitioned Apache Parquet files. An AWS Glue crawler reads and catalogs the Parquet-formatted version, making it available to Amazon Athena.
1. **Step 8**: Athena views that are created on partitioned Parquet data provide data enrichment for the Amazon QuickSight dashboard.
1. **Step 9**: The QuickSight dashboard uses Athena views to create business intelligence dashboards on top of background check reports.
1. **Step 10**: Amazon CloudWatch is used for workflow monitoring, logging, and event tracking.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Lambda helps reduce operational overhead because there is no need to provision, scale, or manage servers. Additionally, versioning support lets you publish multiple versions of a function and roll back to previous versions if needed. Step Functions provides resilience, and its state machines are automatically distributed across Availability Zones (AZs) for high availability. It also reduces operational overhead by managing state, checkpoints, and restarts for you, and you can easily change Step Functions workflows without writing code. EventBridge manages all the underlying infrastructure needed to deliver events at scale, so you don’t need to build custom event solutions. CloudWatch provides integrated monitoring for events and workflows, providing visibility into service performance and issues. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) policies govern the permissions and policies for specific AWS services and associated API actions, applying least-privilege controls to allow only the least required permissions for effective operation of any particular service. AWS Key Management Service (AWS KMS) lets you encrypt the data at rest, and the use of the recommended TLS 1.3 keeps data encrypted in transit during the request flow. The Amazon QLDB Federal Information Processing Standard (FIPS) endpoint uses a TLS library that complies with FIPS 140-2. This endpoint helps security-sensitive ledger applications meet strict encryption, compliance, and regulatory requirements required by businesses that interact with state governments. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance stores source data Amazon S3, an object storage service that offers 99.999999999% (11 nines) data durability. Amazon QLDB is fully managed, serverless, highly available, and helps you store extracted data and all data changes. Its ledger is deployed across multiple AZs, with multiple copies for each AZ, and ledger write is acknowledged only after being written to durable storage in multiple AZs to provide strong durability of your data. DataSync provides reliable data transfer capabilities between on-premises and cloud storage, keeping data in sync across locations and automatically resuming data transfer jobs from points of failure. Lambda automatically scales to handle thousands of concurrent implementations without any capacity planning, and it retries implementations at least three times before events might be rejected, improving reliability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Textract accelerates workflows that rely on information from documents and supports both synchronous and asynchronous operations. It lets you quickly extract structured data, such as fields, values and tables, from documents at scale using machine learning models. Amazon SQS and Amazon SNS support push-based and pull-based communication, respectively, to optimize for different use cases. The push model of Amazon SNS lets you send time-critical notifications, and Amazon SQS lets you decouple sending and receiving components through an asynchronous messaging model. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance provides an event-driven architecture that uses serverless services and managed services, helping you optimize costs without under-provisioning or over-provisioning. AWS serverless services let you pay only for what you use, and there are no minimum fees or mandatory service usage. Additionally, Storage Gateway offers free data transfer-in costs from gateway applications. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS serverless services provision the minimum number of resources needed and follow an event-driven architecture to accomplish tasks, helping you minimize your overall resource consumption and maximize your resource utilization, leading to improved sustainability. Additionally, Amazon Textract only runs when handling API requests, and DataSync lets you move your data to sustainable and cost-efficient cloud storage, reducing the overall footprint of your data storage. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
