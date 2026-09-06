---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/aws-services-used.html
---

# AWS Services Used
<a name="aws-services-used"></a>

## Core Services
<a name="core-services"></a>

 **Amazon S3** – Primary storage for spatial asset files with versioning, encryption, and lifecycle policies. Includes asset storage buckets, CloudFront origin buckets, and logging buckets.

 **Amazon DynamoDB** – NoSQL database for application state with 11 tables managing libraries, projects, assets, files, connectors, members, resource associations, locks, and processing state. Point-in-time recovery enabled with 35-day retention.

 **Amazon OpenSearch Serverless** – Search engine for full-text and geospatial queries with VPC endpoint integration and security policies.

 **AWS Lambda** – Serverless compute for API handlers, event processing, and workflow orchestration. Includes deployment UUID generation, CloudFront key generation, asset management, and event processing functions.

 **Amazon API Gateway** – REST API management with Cognito and IAM authorization, throttling, usage plans, and monitoring.

## Content Delivery and Security
<a name="content-delivery-and-security"></a>

 **Amazon CloudFront** – Global content delivery network for web portal and asset previews with HTTPS enforcement, custom domain support, and edge optimization.

 **Amazon Cognito** – User authentication and authorization with user pools, identity pools, MFA enforcement, and API Gateway integration.

 **AWS KMS** – Encryption key management for S3, DynamoDB, Lambda environment variables, and CloudWatch logs with automatic yearly rotation.

 **AWS IAM** – Identity and access management with service roles, resource policies, and least privilege access control.

 **AWS Secrets Manager** – Secure storage for service credentials with 30-day rotation policy.

 **Amazon Verified Permissions** – Cedar-based authorization service for fine-grained access control with policy store management, batch authorization requests, and schema validation.

## Processing and Integration
<a name="processing-and-integration"></a>

 **AWS Deadline Cloud** – Managed service for rendering, transcoding, and batch processing with render farm configuration and job management.

 **Amazon EventBridge** – Event bus for workflow orchestration, asset processing events, and system notifications.

 **Amazon SQS** – Message queuing for asset processing and notification delivery with FIFO queues, encryption, dead letter queues, and retry policies.

 **Amazon SNS** – Notification service for system alerts, error notifications, and status updates with topic encryption and delivery tracking.

## Monitoring and Operations
<a name="monitoring-and-operations"></a>

 **Amazon CloudWatch** – Metrics collection, log aggregation, and alarms for Lambda invocations, API Gateway requests, and custom application metrics.

 **AWS CloudTrail** – Multi-region API activity logging for security and compliance with S3 storage and management event tracking.

 **AWS X-Ray** – Distributed tracing for Lambda and API Gateway with service maps, trace analysis, and performance monitoring.

 **AWS Glue Data Catalog** – Metadata repository for analytics tables with database and table definitions for audit events and telemetry data.

 **Amazon Athena** – SQL query service for analyzing CloudTrail logs, access logs, and usage patterns with AWS Glue Data Catalog integration.

## Networking and Security
<a name="networking-and-security"></a>

 **Amazon VPC** – Private network for API Gateway, Lambda, and Deadline Cloud with VPC endpoints for S3, DynamoDB, and OpenSearch Serverless.

 **Amazon VPC Endpoints** – Private network access to AWS services for Lambda, S3, DynamoDB, and OpenSearch Serverless.

 **Amazon Security Groups** – Network access control for VPC resources with inbound and outbound rules.

 **Amazon Route 53** – DNS service for API Gateway custom domain and CloudFront custom domain.

 **Amazon Certificate Manager** – SSL/TLS certificate management for CloudFront custom domain and API Gateway custom domain.

 **Next:** [Core Concepts](core-concepts.md)
