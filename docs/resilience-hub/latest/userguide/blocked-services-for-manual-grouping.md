---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/blocked-services-for-manual-grouping.html
---

# Blocked services for manual grouping
<a name="blocked-services-for-manual-grouping"></a>

AWS Resilience Hub blocks you from manually grouping resources of certain AWS services to prevent configuration errors that could affect the resilience assessment and recommendations for your application. These services are automatically grouped based on their dependencies and configurations. When you define an application inclusive of these resources on AWS Resilience Hub, it analyzes their relationships, dependencies, and resilience requirements to create optimal groupings that ensure accurate assessment results.

List of AWS services blocked for manual grouping:
+ Amazon API Gateway
+ Amazon DocumentDB
+ Amazon DynamoDB
+ Amazon Elastic Block Store
+ Amazon Elastic File System
+ Amazon Relational Database Service
+ Amazon S3
+ Amazon Simple Queue Service
+ FSx for Windows File Server
+ NAT Gateway

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
