---
source_url: https://docs.aws.amazon.com/solutions/automated-restore-and-copy-for-amazon-s3-glacier-objects/index.html
---

---
title: 'Guidance for Automated Restore and Copy for Amazon S3 Glacier Objects'
canonical_url: https://docs.aws.amazon.com/solutions/automated-restore-and-copy-for-amazon-s3-glacier-objects/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Automated Restore and Copy for Amazon S3 Glacier Objects

## Overview

This Guidance enables you to leverage Amazon S3 Batch Operations with enhanced flexibility in manifest generation. You can either use an automated manifest generator that filters objects based on criteria like prefix, suffix, and last modified date, or manually upload a CSV manifest for precise control. The Guidance presents two architectural approaches: the first demonstrates how to request restoration of archived objects using S3 Batch Operations and perform copying through Batch Operations Invoke Lambda, while the second showcases an event-driven method for copying archived objects after being restored by S3 Batch Operations. These approaches provide efficient, scalable solutions for managing large-scale Amazon S3 operations, particularly when dealing with archived content.

## How it works

### Automated Archive Restore with S3 Batch Operations Copy

The first architecture is an overview that shows you how to request restoration of archived objects with Amazon S3 Batch Operations and copy using Batch Operations Invoke Lambda.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automated-restore-and-copy-for-amazon-s3-glacier-objects.pdf)Step 1Allow the AWS CloudFormation stack to automate manifest generation or upload a manifest of archived objects to the Amazon Simple Storage Service (Amazon S3) bucket.Step 2The Stack or CSV upload invokes the Custom Resource or Restore Worker AWS Lambda function.Step 3The Restore Worker Lambda function submits a Restore Operation job to Amazon S3 Batch Operations.Step 4Amazon S3 Batch Operations initiates object restore in the S3 bucket containing the archived objects.Step 5The Amazon S3 Batch Operations completion report invokes the Job Tracker Worker Lambda function.Step 6The Job Tracker Worker Lambda function creates an entry in the Amazon DynamoDB table with the restore details.Step 7Amazon EventBridge invokes the Job Scheduler Worker Lambda function on a schedule.Step 8The Job Scheduler Worker Lambda function queries the state table to determine the status of each restore job and when it is eligible for a copy job.Step 9The Job Scheduler Worker Lambda function invokes the Copy Worker Lambda function to submit Amazon S3 Batch Operations and invoke the Lambda function job.Step 10Amazon S3 Batch Operations invokes a Lambda function that performs the actual copy operation to the destination S3 bucket.Step 11The Amazon S3 Batch Operations report invokes the Job Tracker Worker Lambda function to send an Amazon Simple Notification Service (Amazon SNS) message to the user stating that the Amazon S3 Batch Operations Copy Job is completed.### Automated Archive Restore with Event Driven Copy

The second architecture shows restoration of archived objects with Amazon S3 Batch Operations and event driven copy.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automated-restore-and-copy-for-amazon-s3-glacier-objects.pdf)Step 1Allow the CloudFormation stack to automate manifest generation or upload a manifest of archived objects to the S3 bucket.Step 2The Stack or CSV upload invokes the Custom Resource or Restore Worker Lambda function.Step 3The Restore Worker Lambda function submits a Restore Operation job to Amazon S3 Batch Operations.Step 4Amazon S3 Batch Operations initiates object restore in the S3 bucket containing the archived objects.Step 5The Amazon S3 Batch Operations completion report invokes the Job Tracker Worker Lambda function.Step 6The Job Tracker Worker Lambda function creates an entry in the DynamoDB table with the restore details.Step 7EventBridge sends ObjectRestoreComplete Amazon S3 events to the Amazon Simple Queue Service (Amazon SQS) queue.Step 8The queue triggers a Copy Lambda function that performs object copy between the archive S3 bucket and the destination S3 buckets.Step 9The Copy Lambda function inserts a copy status record for each invocation in the Events DynamoDB table. The records include objects successfully copied or objects that fail to copy due to Amazon S3 Client errors, such as access denied.Step 10Restore event records with failed function invocations, such as Lambda timeout or throttling, are sent to the dead-letter queue. The PutFailedRecord Lambda function inserts the records in the Events DynamoDB table.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-automated-restore-and-copy-for-amazon-s3-glacier-objects)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance can be re-deployed using the AWS CloudFormation template. The solution includes an SNS notification function that provides job status and failures. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Data stored in DynamoDB and Amazon S3 are protected by default through AWS encryption. By default, S3 buckets have access control lists (ACLs) disabled and public block access enabled. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Step Functions has retry and exponential back-off enabled to retry the Lambda functions it invokes. Step Functions states in the Guidance implement a retry and back-off mechanisms. Amazon S3 Batch Operations also retries Lambda service-related errors. Additionally, AWS Software Development Kits (SDKs) used in the Lambda functions have default retry and back-off configuration. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon S3 Batch Operations is designed to manage large-scale operations. Lambda functions automatically scale to handle the number of concurrent invocations. You can enable provisioned capacity for DynamoDB which will reserve sufficient system resources to meet your requirements. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

S3 Glacier provides multiple options for archive retrieval, including bulk retrieval, the lowest cost option that allows you to retrieve petabytes of data within 5-12 hours. S3 Glacier Flexible Retrieval provides free bulk retrieval for archived items that you’d want to retrieve infrequently, such as 1-2 times a year. Additionally, Amazon S3 Batch Operations allows you to manage billions of objects at scale without the need to provision costly and complex compute. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon S3 Lifecycle rule is applied to the guidance S3 bucket to have objects expire after 180 days. The solution DynamoDB items are set to expire 60 days after restore and copy job completion. Automating expiration helps you avoid unnecessarily using storage resources for items that you no longer need. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
