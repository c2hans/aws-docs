---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/solution-overview.html
---

# Build your own centralized log analytics platform with Amazon OpenSearch Service in 20 minutes
<a name="solution-overview"></a>

**Important**
This AWS Solution will retire in December 2026. We encourage customers to explore using [Amazon CloudWatch's new unified data management and analytics capabilities](https://aws.amazon.com/blogs/aws/amazon-cloudwatch-introduces-unified-data-management-and-analytics-for-operations-security-and-compliance/). Learn more about [AWS CloudWatch unified data and telemetry](https://aws.amazon.com/cloudwatch/features/unified-data-and-telemetry/) and give it a try in the [AWS CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

The Centralized Logging with OpenSearch solution provides comprehensive log management and analysis functions to help you simplify the build of log analytics pipelines. Built on top of Amazon OpenSearch Service, the solution helps you to streamline log ingestion, log processing, and log visualization. You can use the solution in multiple use cases, such as to abide by security and compliance regulations, achieve refined business operations, and enhance IT troubleshooting and maintenance.

**Important**
Centralized Logging with OpenSearch supports Amazon OpenSearch Service with OpenSearch 1.3 or later.

Use this navigation table to quickly find responses to these questions:

| If you want to …​ | Read…​ |
| --- | --- |
| Know the cost for running this solution |  [Cost](cost.md)  |
| Understand the security considerations for this solution |  [Security](security.md)  |
| Know which AWS Regions are supported for this solution |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
| Get started with the solution quickly to import an Amazon OpenSearch Service domain, build a log analytics pipeline, and access the built-in dashboard |  [Getting started](getting-started.md)  |
| Learn the operations related to Amazon OpenSearch Service domains |  [Domain management](domain-management.md)  |
| Walk through the processes of building log analytics pipelines |  [AWS Services logs](aws-service-logs.md) and [Application logs](application-logs.md)  |
| Encountering issues when using the solution |  [Troubleshooting](troubleshooting.md)  |
| Go through a hands-on workshop designed for this solution |  [Workshop](https://catalog.workshops.aws/centralized-logging-with-opensearch/)  |

This implementation guide describes architectural considerations and configuration steps for deploying the Centralized Logging with OpenSearch solution in the AWS Cloud. It includes links to CloudFormation templates that launch and configure the AWS services required to deploy this solution using AWS best practices for security and availability.

The guide is intended for IT architects, developers, DevOps, and data engineers with practical experience architecting on the AWS Cloud.

## Features and benefits
<a name="features-and-benefits"></a>

The solution has the following features:

 **All-in-one log ingestion**

Provides a single web console to ingest both application logs and AWS service logs into log analytics engines. For supported AWS service logs, see [AWS service logs](aws-service-logs.md). For supported application logs, refer to [Application logs](application-logs.md).

 **Codeless log processor**

Supports log processor plugins developed by AWS. You can enrich the raw log data through a few steps on the web console.

 **Out-of-the-box dashboard template**

Offers a collection of reference designs of visualization templates, for both commonly used software such as NGINX and Apache HTTP Server, and AWS services such as Amazon S3 and AWS CloudTrail.

## Use cases
<a name="use-cases"></a>

The solution can be applied to the following use cases:

 **Security and compliance regulations**

Comply with regulatory requirements such as GDPR, PCI DSS, MLPS, and HIPAA. Easily store equipment, network, and application logs in a centralized place for log auditing and threat detection.

 **Business operations and data analysis**

Identify trends and patterns in minutes, and build interactive and intuitive visualization. Derive business insights from logs and inform business decisions with data.

 **Application and infrastructure troubleshooting**

Monitor both application and cloud infrastructure logs with ease, understand and resolve the root cause of issues quickly. Improve the observability of your workloads and achieve better business stability.

## Concepts
<a name="concepts"></a>

This section describes key concepts and defines terminology specific to this solution:

 **Log Analytics Engine**

A log analytics engine is a sophisticated tool designed to process, analyze, and visualize vast amounts of log data from diverse systems, applications, and devices. Our solution primarily uses the **Amazon OpenSearch Service** as the default log analytics engine, complemented by a **Light Engine** specifically optimized for structured, infrequent logs.

 **OpenSearch Engine**

The OpenSearch Engine in this solution refers to the [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/), a distributed, community-driven, Apache 2.0-licensed, 100% open source search and analytics suite used for a broad set of use cases like real-time application monitoring, log analytics, and website search.

 **Light Engine**

The Light Engine is a serverless log analytics engine that uses AWS services like Athena, Glue, Lambda, and Step Functions. Designed to analyze structured and infrequent logs, it offers up to a 90% cost reduction compared to the OpenSearch Engine.

 **Log Analytics Pipeline**

A Log Analytics Pipeline, or Log Pipeline, represents the entire data flow from the source to the log analytics engines. It typically encompasses the stages of shipping, buffering, processing, filtering, enriching, and storing logs. Centralized Logging with OpenSearch supports two types of Log Analytics Pipelines: the Service Log Pipeline, tailored for ingesting logs generated by AWS Services, and the Application Log Pipeline, designed for ingesting logs from custom applications.

 **Log Source**

A Log Config defines the metadata of your logs, specifying the log type, format, sample logs, filters, and the schema needed to map raw log data into the structured format used by the log analytics engine. A Log Source refers to the location where logs are generated or stored. Centralized Logging with OpenSearch supports ingesting logs from diverse sources, encompassing both application logs and logs from AWS services. For supported AWS service logs, refer to [AWS Service Logs](aws-service-logs.md). For supported application logs, refer to [Application Logs](application-logs.md).

 **Log Agent**

A log agent is a program that reads logs from one location and sends them to another location (for example, OpenSearch). Currently, Centralized Logging with OpenSearch only supports the [Fluent Bit 1.9](https://docs.fluentbit.io/manual/) log agent, which is installed automatically. The Fluent Bit agent has a dependency of [OpenSSL 1.1](https://www.openssl.org/source/). To learn how to install OpenSSL on Linux instances, refer to [OpenSSL installation](additional-resources.md#openssl-1.1-installation). To find the platforms supported by Fluent Bit, see [Supported Platforms](https://docs.fluentbit.io/manual/installation/supported-platforms).

 **Log Config**

A Log Config defines the metadata of your logs, specifying the log type, format, sample logs, filters, and the schema needed to map raw log data into the structured format used by the log analytics engine.

 **Log Buffer**

Log Buffer is a buffer layer between the Log Agent and OpenSearch clusters. The agent uploads logs into the buffer layer before being processed and delivered into the log analytics engine. A buffer layer is a way to protect the log analytics engine from being overwhelmed. For AWS service logs, a log buffer is automatically configured if needed. For Application logs, this solution provides the following types of buffer layers.
+  **Amazon S3**. Use this option if you can bear minutes-level latency for log ingestion. The log agent periodically uploads logs to an Amazon S3 bucket. The frequency of data delivery to Amazon S3 is determined by Buffer size (default value is 50 MiB) and Buffer interval (default value is 60 seconds) values that you configured when creating the application log analytics pipelines. The condition satisfied first starts data delivery to Amazon S3.
+  **Amazon Kinesis Data Streams**. Use this option if you need real-time log ingestion. The log agent uploads logs to Amazon Kinesis Data Stream in seconds. The frequency of data delivery to Kinesis Data Streams is determined by Buffer size (10 MiB) and Buffer interval (5 seconds). The condition satisfied first triggers data delivery to Kinesis Data Streams.

Log Buffer is optional when creating an application log analytics pipeline. For all types of application logs, you can use this solution to ingest logs without any buffer layers. However, we only recommend this option when you have small log volume, and you are confident that the logs will not exceed the thresholds at the OpenSearch side.

 **Instance Group**

An Instance Group represents a group of EC2 instances, which enables the solution to associate a Log Config with multiple EC2 instances quickly. Centralized Logging with OpenSearch uses [Systems Manager Agent (SSM Agent)](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) to install/configure Fluent Bit agent, and sends log data to [Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/). Instance Group is one of the supported Log Sources in this solution.

 **Main Account**

An AWS account where the Centralized Logging with OpenSearch console is deployed. The Log Analytics Engines must also reside in the same account.

 **Member Account**

Another AWS account from which you want to ingest AWS Service logs or application logs. Logs are sent from Member Accounts to Main Accounts, where they are analyzed using resources in the Main Account.

 **Access Proxy**

An Access Proxy serves as an intermediary for accessing Amazon OpenSearch Service domains from the internet securely. By default, an Amazon OpenSearch Service domain within a VPC is not accessible from the internet. The Centralized Logging with OpenSearch solution implements a Nginx-based proxy stack architecture to enable internet access to OpenSearch Dashboards. This allows users to interact conveniently with the dashboards from anywhere with internet connectivity.
