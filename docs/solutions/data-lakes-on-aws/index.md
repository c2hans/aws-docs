---
source_url: https://docs.aws.amazon.com/solutions/data-lakes-on-aws/index.html
---

---
title: 'Guidance for Data Lakes on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/data-lakes-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Data Lakes on AWS

## Overview

This Guidance demonstrates an automatically configured data lake on AWS using an event-driven, serverless, and scalable architecture. It leverages AWS managed services to ingest, store, process, and analyze data, offering a secure, flexible, and cost-effective design with proper data governance. This approach provides greater agility, flexibility, and reliability compared to traditional data management systems. The entire solution is built as a codified application using infrastructure-as-code (IaC) and a continuous integration, continuous delivery (CI/CD) pipeline.

## Benefits

### Accelerate data-driven decisions

**AWS Serverless Data Lake Framework:** Deploy a serverless data lake framework that transforms raw data into actionable insights using AWS analytics services. Enable your business analysts to query processed data through Amazon Athena while maintaining comprehensive data governance through AWS Lake Formation. **Multi-Source Analytics Lakehouse with AI-Powered Insights:** Deploy a unified data lakehouse architecture that seamlessly ingests data from diverse sources including streaming inventory, relational databases, and enterprise systems like SAP. Reduce development time by leveraging zero-ETL capabilities and open table formats that eliminate complex data pipeline engineering.

### Streamline data processing workflows

**AWS Serverless Data Lake Framework:** Implement automated, event-driven data pipelines that efficiently transform and catalog your data across its lifecycle. AWS Step Functions orchestrates the workflow while AWS Glue handles ETL processes, converting data to optimized formats for improved query performance. **Multi-Source Analytics Lakehouse with AI-Powered Insights:** Enable business teams to generate actionable insights through natural language queries with Amazon Bedrock and visualize results with Amazon QuickSight. Query data through existing spark platform or leveraging the AWS services under one unified platform. Marketing and sales teams can independently access the data they need while IT maintains centralized governance through AWS Lake Formation.

### Enhance data accessibility securely

**AWS Serverless Data Lake Framework:** Create a unified data environment where teams can access and analyze data through their preferred tools while maintaining centralized governance. AWS Lake Formation provides fine-grained access controls while Amazon SageMaker and Amazon Bedrock enable advanced analytics and AI-powered insights from your data lake. **Multi-Source Analytics Lakehouse with AI-Powered Insights:** Implement a secure, well-governed data environment using Lakehouse for Amazon SageMaker with federated catalogs and AWS Lake Formation controls. This architecture allows you to maintain data security and compliance while enabling cross-account data sharing between producer and consumer accounts.

## How it works

### AWS Serverless Data Lake Framework

This architecture diagram shows how to build a data lake on AWS in addition to demonstrating how to process, store, and consume data using serverless AWS analytics services.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/data-lakes-on-aws.pdf)Step 1The data administrator uploads JSON files in the Amazon Simple Storage Service (Amazon S3) raw bucket. Object creation in Amazon S3 triggers an event in Amazon EventBridge.Step 2EventBridge has a rule that sends a message in Amazon Simple Queue Service (Amazon SQS), which invokes an AWS Lambda function.Step 3The Lambda function triggers the AWS Step Functions workflow, in which another Lambda function reads files from the S3 raw bucket and performs transformation. It also writes the new set of JSON files in the S3 stage bucket.Step 4A Lambda function updates the Amazon DynamoDB table with the Step Functions job status.Step 5Once the files are created in the S3 stage bucket, it triggers an event in EventBridge, which has a rule that sends a message in Amazon SQS with created file details.Step 6The Eventbridge scheduler runs at certain intervals and invokes a Lambda function that retrieves messages from Amazon SQS and starts another Step Functions workflow.Step 7AWS Glue extract, transform, load (ETL) reads the data from the AWS Glue database stage, then converts the files from JSON to Parquet format.Step 8AWS Glue ETL writes the Parquet files in the S3 analytics bucket. AWS Glue crawler crawls the Parquet files in the same bucket and then creates analytics tables in AWS Glue database analytics.Step 9All the staging and analytics catalogs are maintained in the AWS Glue Data Catalog.Step 10A Lambda function updates the DynamoDB table with the Step Functions job status.Step 11Business analysts use Amazon Athena to query the AWS Glue database analytics.### Multi-Source Analytics Lakehouse with AI-Powered Insights

This architecture diagram shows how to build a data lake on AWS in addition to demonstrating how to process, store, and consume data using Lakehouse for Amazon SageMaker and Amazon SageMaker Unified Studio.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/data-lakes-on-aws.pdf)Step 1Ingest store inventory data with Amazon Kinesis Data Streams, which feeds the data into Amazon Data Firehose.Step 2Upload store inventory streaming data into Amazon Simple Storage Service (Amazon S3) Tables.Step 3Catalog store inventory data into Lakehouse for Amazon SageMaker, managed with AWS Lake Formation, as a federated AWS Glue catalog.Step 4Ingest store, product, and promotions dimension data from Amazon Aurora (MySQL) to Amazon Redshift Serverless via Zero-ETL.Step 5Catalog dimension data into Lakehouse for Amazon SageMaker as a federated catalog.Step 6Ingest store sales data from SAP using AWS Glue via Zero-ETL. AWS Glue writes the store sales data into Amazon S3 in Apache Iceberg open table format.Step 7Catalog store sales data into Lakehouse for Amazon SageMaker as a federated catalog.Step 8Control access and governance through Amazon SageMaker Unified Studio from the central governance account. The producer account publishes the sales data. The consumer account subscribes and accesses the sales data.Step 9The marketing team generates insights from unified data using Amazon Athena. The data is pulled from Lakehouse for Amazon SageMaker. The sales team can also use Amazon QuickSight to visualize the data.Step 10The marketing team's data engineer with an existing Spark platform accesses sales data from Lakehouse for Amazon SageMaker by running Spark jobs on Amazon Elastic Compute Cloud (Amazon EC2) using an open Iceberg REST API.Step 11Sales team generates insights from unified data using Amazon Bedrock foundation models with Amazon Bedrock Knowledge Bases using Retrieval Augmented Generation (RAG) in the Producer account by using natural language queries.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/data-lakes-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
