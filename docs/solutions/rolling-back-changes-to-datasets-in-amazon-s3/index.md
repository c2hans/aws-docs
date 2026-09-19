---
source_url: https://docs.aws.amazon.com/solutions/rolling-back-changes-to-datasets-in-amazon-s3/index.html
---

---
title: 'Guidance for Rolling Back Changes to Datasets in Amazon S3'
canonical_url: https://docs.aws.amazon.com/solutions/rolling-back-changes-to-datasets-in-amazon-s3/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Rolling Back Changes to Datasets in Amazon S3

## Overview

This Guidance demonstrates how to recover Amazon S3 datasets at scale by reverting to a specified point-in-time using S3 Versioning. The process begins by deploying an AWS CloudFormation template that creates Athena queries to identify necessary object actions. Lambda functions then orchestrate these queries and create S3 Batch Operations using CSV manifests, efficiently restoring the bucket to its previous state. You can restore millions of objects quickly, with the ability to revert 1 million changes in a 10-billion-object bucket in under an hour, or handle smaller restorations in just 15 minutes.

## Benefits

### Accelerate data recovery

Deploy a serverless solution that can restore your S3 bucket to a previous state in minutes or hours, depending on scale. This tool can revert thousands of changes in smaller buckets in under 15 minutes, helping you quickly recover from accidental deletions or corruptions.

### Minimize operational overhead

Leverage fully managed AWS services like Lambda, Athena, and S3 Batch Operations to handle complex rollback operations without managing infrastructure. The solution automatically identifies necessary actions through Athena queries and orchestrates the restoration process, allowing your team to focus on core business activities.

### Scale with confidence

Handle massive data recovery operations efficiently across billions of objects in your S3 buckets. The architecture can detect and revert 1 million changes in a bucket containing 10 billion objects in under an hour, providing enterprise-grade recovery capabilities for your most critical storage environments.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/rolling-back-changes-to-datasets-in-amazon-s3.pdf)

![Architecture diagram](/images/solutions/rolling-back-changes-to-datasets-in-amazon-s3/images/rolling-back-changes-to-datasets-in-amazon-s3-1.png)

1. **Step 1**: Deploy Amazon Simple Storage Service (Amazon S3) Rollback AWS CloudFormation template, specifying bucket to restore, and the desired point in time to restore to.
1. **Step 2**: AWS Lambda functions check compatibility and pre-requisites for the tool.
1. **Step 3**: AWS CloudFormation creates Amazon Athena queries.
1. **Step 4**: AWS Lambda function orchestrates execution of the Amazon Athena queries that identify what actions need to be taken on objects.
1. **Step 5**: Amazon Athena delivers results of queries as CSV manifests to temporary Amazon S3 bucket.
1. **Step 6**: AWS Lambda function creates Amazon S3 Batch Operations using newly created CSV manifests.
1. **Step 7**: Amazon S3 Batch Operations runs jobs to return bucket to state at a specified point in time, which might invoke AWS Lambda functions. Amazon S3 Rollback can detect and revert 1 million changes, in a bucket containing 10 billion objects, in under 1 hour, or 100 million changes in under 15 hours. It can also revert a few thousand changes in a smaller bucket (up to millions of objects) in under 15 minutes end-to-end, including near real-time inventory creation.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-rolling-back-changes-to-datasets-in-amazon-s3)

[Read usage guidelines](/solutions/guidance-disclaimers/)
