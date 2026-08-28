---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/security-1.html
---

# Security
<a name="security-1"></a>

 When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## Server-side encryption
<a name="server-side-encryption"></a>

 AWS highly recommends that customers encrypt sensitive data in transit and at rest. This solution automatically encrypts media files and metadata at rest with [Amazon S3 server-side encryption (SSE)](http://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html).The solution's Amazon Simple Notification Service (Amazon SNS) topics and Amazon DynamoDB tables are also encrypted at rest using SSE.

## Amazon CloudFront
<a name="amazon-cloudfront"></a>

 This solution deploys a static website [hosted](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) in an Amazon S3 bucket. To help reduce latency and improve security, this solution includes an Amazon CloudFront distribution with an origin access identity, which is a special CloudFront user that helps restrict access to the solution's website bucket contents. For more information, refer to [Restricting access to Amazon S3 content by using an origin access identity](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html).

## Amazon OpenSearch Service
<a name="amazon-opensearch-service-1"></a>

 Documents indexed to the Amazon OpenSearch Service cluster are encrypted at rest. Node-to-node communication within the cluster is also encrypted.

## Search engine sizing
<a name="search-engine-sizing"></a>

 The CloudFormation template provides presets for the end user to configure different Amazon OpenSearch Service clusters: **Development and Testing**, **Suitable for Production Workload**, **Recommended for Production Workload**, and **Recommended for Large Production Workload**.
+  **Development and Testing** – This preset creates an Amazon OpenSearch Service cluster in a single Availability Zone with a single `m5.large.search` data node, 10GB storage, and without dedicated primary node.
+  **Suitable for Production Workflow** – This preset creates an Amazon OpenSearch Service cluster in two Availability Zones with two `m5.large.search` data nodes, 20GB storage, and three dedicated `t3.small.search` primary nodes.
+  **Recommended for Production Workload** – This preset creates an Amazon OpenSearch Service cluster in two Availability Zones with four `m5.large.search` data nodes, 20GB storage, and three dedicated `t3.small.search` primary nodes.
+  **Recommended for Large Production Workload** – This preset creates an Amazon OpenSearch Service cluster in three Availability Zones with six `m5.large.search` data nodes, 40GB storage, and three dedicated `t3.small.search` primary nodes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
