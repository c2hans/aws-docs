---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-elasticache-integration/introduction.html
---

# Integrating Amazon DynamoDB and Amazon ElastiCache by using read-through caching
<a name="introduction"></a>

*Jason Hunter, Amazon Web Services*

This guide presents the key design points to consider when you add an Amazon ElastiCache caching layer in front of an Amazon DynamoDB database. It explains how to implement a client-side shim that adds read-through caching to DynamoDB calls without requiring significant code modification in the application. A reference implementation is provided in Python to demonstrate the internal details.

ElastiCache is a popular and robust caching service that provides an advanced set of features, including:
+ Valkey and Redis OSS compatibility
+ 99.99 percent service-level agreement (SLA)
+ Availability in all AWS Regions
+ Support for the latest Amazon Elastic Compute Cloud (Amazon EC2) node types
+ In-place changing of the node type
+ Automatic failover
+ Automatic scaling
+ Data tiering
+ Global replication
+ Backup support
+ Reserved nodes
+ Compliance with System and Organization Controls (SOC) 1, 2, 3, and other standards
+ Cache invalidation
+ Serverless option

DynamoDB also offers DynamoDB Accelerator (DAX) as a DynamoDB-specific memory cache option. This guide is for readers who prefer to use ElastiCache instead.

## Sample repository
<a name="repo"></a>

For a Python-based reference implementation of the designs discussed in this guide, see the GitHub [DynamoDB ElastiCache Integration repository](https://github.com/aws-samples/amazon-elasticache-samples/tree/main/dynamodb-elasticache-integration). The sample code is provided for demonstration purposes only, on an as-is basis and without any support. Use at your own risk.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
