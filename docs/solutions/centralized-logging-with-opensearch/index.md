---
source_url: https://docs.aws.amazon.com//solutions/centralized-logging-with-opensearch//index.html
---

---
title: 'Centralized Logging with OpenSearch'
canonical_url: https://docs.aws.amazon.com/solutions/centralized-logging-with-opensearch/
source: aws-documentation
generated_on: 2026-09-22
---

# Centralized Logging with OpenSearch

Build a centralized log analytics platform with Amazon OpenSearch Service on AWS in 20 minutes

- **Version**: 2.4.15
- **Released**: 8/2026
- **Author**: AWS
- **Est. deployment time**: 15 mins
- **Estimated cost**: [See details](/solutions/latest/centralized-logging-with-opensearch/cost.html)

## Overview

**Important: This AWS Solution will retire in December 2026. Deployments (via CloudFormation or GitHub) will remain operational, but customers will assume responsibility for maintenance and API-related updates post retirement.** **We encourage customers to explore using [Amazon CloudWatch's new unified data management and analytics capabilities](https://aws.amazon.com/blogs/aws/amazon-cloudwatch-introduces-unified-data-management-and-analytics-for-operations-security-and-compliance/). Learn more about [AWS CloudWatch unified data and telemetry](https://aws.amazon.com/cloudwatch/features/unified-data-and-telemetry/) and give it a try in the [AWS CloudWatch console](https://console.aws.amazon.com/cloudwatch/).** **You can find other AWS Solutions in the [AWS Solutions Library](https://aws.amazon.com/solutions/).** Centralized Logging with OpenSearch helps organizations collect, ingest, and visualize log data from various sources using Amazon OpenSearch Service. This AWS Solution provides a web-based console, which you can use to create log ingestion pipelines with a few clicks. Log ingestion pipelines include log collection agent deployment, log enrichment without writing codes, buffer layer creation, and OpenSearch index configuration. After logs are stored in OpenSearch Service, the solution automatically generates ready-to-use dashboards for analyzing AWS service logs and application logs in different formats (for example, Nginx, JSON, and Spring Boot). In combination with other AWS services, this solution provides you with a turnkey environment to begin logging and monitoring your AWS applications.

## Benefits

### Ease of use

Use a web console from your AWS account to ingest both application and AWS service logs, then analyze the logs with visualization dashboards.

### Improved operational efficiency

Serverless technologies with built-in high availability and a pay-for-use billing model reduces the need for infrastructure management, allowing you to focus more on building log analytics for your business.

### Open source and customization

The solution is open sourced and free for commercial use. You pay only for the AWS usage. You can take the source code as a reference to make your own implementation that fits your needs.

## How it works

You can automatically deploy this architecture using the implementation guide and the AWS CloudFormation templates for AWS Regions or AWS China Regions.

[View implementation guide](/solutions/latest/centralized-logging-with-opensearch/solution-overview.html)

![Architecture diagram](/images/solutions/centralized-logging-with-opensearch/images/centralized-logging-with-opensearch-1.png)

1. **Step 1**: Amazon CloudFront distributes the frontend web UI assets hosted in an Amazon S3 bucket.
1. **Step 2**: Amazon Cognito user pool or OpenID Connector (OIDC) can be used for authentication.
1. **Step 3**: AWS AppSync provides the backend GraphQL APIs.
1. **Step 4**: Amazon DynamoDB stores the solution-related information as the backend database.
1. **Step 5**: AWS Lambda interacts with other AWS Services to process the core logic of managing log pipeline, log agents, and obtains information updated in DynamoDB tables.
1. **Step 6**: AWS Step Functions orchestrates the on-demand AWS CloudFormation deployment of a set of predefined stacks for log pipeline management. The log pipeline stacks deploy separate AWS resources and are used to collect and process logs and ingest them into Amazon OpenSearch Service for further analysis and visualization.
1. **Step 7**: Service Log Pipeline or Application Log Pipeline is provisioned on demand via Centralized Logging with the OpenSearch console.
1. **Step 8**: AWS Systems Manager and Amazon EventBridge manage log agents for collecting logs from application servers, such as installing log agents (Fluent Bit) for application servers and monitoring the health status of the agents.
1. **Step 9**: Amazon EC2 or Amazon EKS installs Fluent Bit agents and uploads log data to the application log pipeline.
1. **Step 10**: Application log pipelines read, parse, process application logs, and ingest them into Amazon OpenSearch Service domains or Light Engine.
1. **Step 11**: Service log pipelines read, parse, process AWS service logs and ingest them into Amazon OpenSearch Service domains or Light Engine.
## Deploy with confidence

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.Open guide

[Open guide](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Open the CloudFormation template in the AWS Console to begin setting up the infrastructure you need. You'll be prompted to access your AWS account if you haven't yet logged in.Launch in the AWS Console:Launch in a new VPC in AWS RegionsLaunch in an existing VPC in AWS RegionsLaunch in a new VPC in AWS China RegionsLaunch in an existing VPC in China Regions

[Launch in a new VPC in AWS Regions](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fcentralized-logging-with-opensearch%2Flatest%2FCentralizedLogging.template&redirectId=SolutionWeb)
[Launch in an existing VPC in AWS Regions](https://console.aws.amazon.com/cloudformation/home#/stacks/new?templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fcentralized-logging-with-opensearch%2Flatest%2FCentralizedLoggingFromExistingVPC.template&redirectId=SolutionWeb)
[Launch in a new VPC in AWS China Regions](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https:%2F%2Fs3.cn-north-1.amazonaws.com.cn%2Fsolutions-reference-cn%2Fcentralized-logging-with-opensearch%2Flatest%2FCentralizedLoggingWithOIDC.template&redirectId=SolutionWeb)
[Launch in an existing VPC in China Regions](https://console.amazonaws.cn/cloudformation/home#/stacks/new?templateURL=https:%2F%2Fs3.cn-north-1.amazonaws.com.cn%2Fsolutions-reference-cn%2Fcentralized-logging-with-opensearch%2Flatest%2FCentralizedLoggingFromExistingVPCWithOIDC.template&redirectId=SolutionWeb)

## Deployment Options

- **Source Code**: The source code for this AWS Solution is available in GitHub.

[Go to Github](https://github.com/aws-solutions/centralized-logging-with-opensearch)

- **Implementation Guide**: Follow the implementation guide for step-by-step instructions to deploy this AWS Solution.

[Download guide](https://docs.aws.amazon.com/pdfs/solutions/latest/centralized-logging-with-opensearch/centralized-logging-with-opensearch.pdf)

## Related content

- **Solution Web Console**: This image shows a preview of the web console for Centralized Logging with OpenSearch.

[Go to image](https://d1.awsstatic.com/centralized-logging-with-opensearch-aws-console.5ce6332704c5dc0d658a0fe8a612197ec3bbeefc.png)

- **Blog Amazon CloudWatch Cross-Account Observability**: This blog describes an Amazon CloudWatch capability to search, analyze, and correlate cross-account telemetry data stored in CloudWatch such as metrics, logs, and traces.

[Go to blog](https://aws.amazon.com/blogs/aws/new-amazon-cloudwatch-cross-account-observability/)

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/centralized-logging-with-opensearch/contact-aws-support.html)

## RSS Feed

- [Subscribe now to get updates on the latest release.](https://solutions-reference.s3.us-east-1.amazonaws.com/centralized-logging-with-opensearch/latest/rss.xml)
