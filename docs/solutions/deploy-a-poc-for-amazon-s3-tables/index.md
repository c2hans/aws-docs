---
source_url: https://docs.aws.amazon.com/solutions/deploy-a-poc-for-amazon-s3-tables/index.html
---

---
title: 'Guidance for Deploy a PoC for Amazon S3 Tables'
canonical_url: https://docs.aws.amazon.com/solutions/deploy-a-poc-for-amazon-s3-tables/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Deploy a PoC for Amazon S3 Tables

## Overview

This Guidance helps organizations validate a fully managed Apache Iceberg table workflow on Amazon S3 Tables before committing to a full-scale data lakehouse. It deploys a proof of concept that covers table creation, multi-engine querying, and streaming ingestion, connecting Amazon Athena, AWS Glue Data Catalog, and Amazon Data Firehose so teams can exercise real-world ingestion, querying, and table administration patterns. S3 Tables automatically handle compaction, snapshot management, and garbage collection without manual intervention. All traffic routes privately through VPC endpoints to services such as Amazon S3, AWS Glue, and Amazon Athena, keeping the environment isolated while you evaluate a modern, low-maintenance data lakehouse.

## Benefits

### Validate before you commit

Deploy a working proof of concept that exercises table creation, multi-engine querying, and streaming ingestion from end to end. You confirm real-world data lakehouse patterns work for your specific workloads before investing time and resources in a full-scale production deployment.

### Reduce table maintenance overhead

Table storage automatically handles compaction, snapshot expiry, orphan file removal, and intelligent tiering without manual intervention. Your teams spend less time on housekeeping and more on analytics, while maintenance metrics stay visible for ongoing operational awareness.

### Keep data access private

Route all traffic through private VPC endpoints and reach instances through session-based access, removing the need for public internet exposure. Fine-grained governance and access controls protect table data, so you evaluate the workflow inside a secure, isolated environment.

## How it works

This architecture diagram illustrates how to build and operate a PoC for Amazon S3 Tables on AWS. It shows the key components and their interactions. [Download the architecture diagram](downloads/deploy-a-poc-for-amazon-s3-tables.pdf)

![Architecture diagram for Deploy a PoC for Amazon S3 Tables](/images/solutions/deploy-a-poc-for-amazon-s3-tables/images/deploy-a-poc-for-amazon-s3-tables.png)

1. **Step 1**: The user logs into the AWS Management Console and deploys the proof-of-concept (PoC) template provided in this Guidance, using AWS CloudFormation to create a new stack that deploys an Amazon Virtual Private Cloud (Amazon VPC).
1. **Step 2**: Amazon Elastic Compute Cloud (Amazon EC2): Private subnet instance accessed through SSM Session Manager. No internet gateway or NAT Gateway - all traffic routes through VPC endpoints.
1. **Step 3**: VPC Endpoints: S3 (Gateway), S3 Tables, SSM, SSM Messages, EC2 Messages, Glue, and Athena endpoints provide private connectivity to AWS services.
1. **Step 4**: Amazon S3 Tables: Table Bucket stores data in Apache Iceberg V2/V3 format. Namespace poc data contains sensor_readings and maintenance_test tables. Automatic maintenance handles compaction, snapshot expiry, orphan file removal, and intelligent-tiering, with Amazon CloudWatch providing S3 Tables maintenance metrics.
1. **Step 5**: AWS Glue Data Catalog: Catalog integration from S3 Tables registers metadata for query engines.
1. **Step 6**: Amazon Athena: Workgroup queries S3 Tables through the Glue Data Catalog. Results stored in a dedicated S3 bucket for Athena Results & Spark Staging.
1. **Step 7**: Amazon SageMaker Lakehouse & AWS Lake Formation: Governance layer (optional) for fine-grained access control on S3 Tables data. AWS IAM roles and policies grant SSM access and Athena, Glue, and Lake Formation permissions.
1. **Step 8**: Amazon EMR Serverless & Amazon Data Firehose: Optional paths: EMR Serverless (Scenario 4b) for Spark-based processing; Data Firehose (Scenario 5) for streaming ingestion into S3 Tables.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-deploying-a-poc-for-amazon-s3-tables)

[Read usage guidelines](/solutions/guidance-disclaimers/)
