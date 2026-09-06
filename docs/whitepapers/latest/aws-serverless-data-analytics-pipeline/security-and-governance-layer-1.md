---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-serverless-data-analytics-pipeline/security-and-governance-layer-1.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security and governance layer
<a name="security-and-governance-layer-1"></a>

 Components across all layers of the presented architecture protect data, identities, and processing resources by natively using the following capabilities provided by the security and governance layer.

## Authentication and authorization
<a name="authentication-and-authorization"></a>

 AWS Identity and Access Management (IAM) provides user-, group-, and role-level identity to users and the ability to configure fine-grained access control for resources managed by AWS services in all layers of our architecture. IAM supports multi-factor authentication and single sign-on through integrations with corporate directories and open identity providers such as Google, Facebook, and Amazon.

 [Lake Formation provides a simple and centralized authorization model](https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html) for tables hosted in the data lake. After implemented in Lake Formation, authorization policies for databases and tables are enforced by [other AWS services](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html#service-integrations) such as Athena, Amazon EMR, QuickSight, and Amazon Redshift Spectrum. In Lake Formation, you can grant or revoke database-, table-, or column-level access for IAM users, groups, or roles defined in the same account hosting the Lake Formation catalog or [another AWS account](https://docs.aws.amazon.com/lake-formation/latest/dg/crosss-account-how-works.html). The simple grant/revoke-based authorization model of Lake Formation considerably simplifies the previous IAM-based authorization model that relied on separately securing S3 data objects and metadata objects in the AWS AWS Glue Data Catalog.

## Encryption
<a name="encryption"></a>

 AWS KMS provides the capability to create and manage symmetric and asymmetric customer managed encryption keys. AWS services in all layers of our architecture natively integrate with AWS KMS to encrypt data in the data lake. It supports both creating new keys and importing existing customer keys. Access to the encryption keys is controlled using IAM and is monitored through detailed audit trails in CloudTrail.

## Network protection
<a name="network-protection"></a>

 Our architecture uses [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) to provision a logically isolated section of the AWS Cloud (called VPC) that is isolated from the internet and other AWS customers. Amazon VPC provides the ability to choose your own IP address range, create subnets, and configure route tables and network gateways. AWS services from other layers in our architecture launch resources in this private VPC to protect all traffic to and from these resources.

## Monitoring and logging
<a name="monitoring-and-logging"></a>

 AWS services in all layers of our architecture store detailed logs and monitoring metrics in [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/). CloudWatch provides the ability to analyze logs, visualize monitored metrics, define monitoring thresholds, and send alerts when thresholds are crossed.

 All AWS services in our architecture also store extensive audit trails of user and service actions in CloudTrail. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console (login required), AWS SDKs, command line tools, and other AWS services. This event history simplifies security analysis, resource change tracking, and troubleshooting. In addition, you can use CloudTrail to detect unusual activity in your AWS accounts. These capabilities help simplify operational analysis and troubleshooting.
