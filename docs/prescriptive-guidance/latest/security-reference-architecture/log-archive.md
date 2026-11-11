---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html
---

# Security OU – Log Archive account
<a name="log-archive"></a>

The following diagram illustrates the AWS security services that are configured in the Log Archive account.

![Security services in the Log Archive account.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/images/guide-img/91d313fc-d5f1-45a8-a5a6-2f4fc7abc93a/images/664aad4f-2aa6-458a-b8a4-57992a45c041.png)

The Log Archive account is dedicated to ingesting and archiving all security-related logs and backups. With centralized logs in place, you can monitor, audit, and alert on Amazon S3 object access, unauthorized activity by identities, IAM policy changes, and other critical activities performed on sensitive resources. The security objectives are as follows: Log storage in the Log Archive account MUST be immutable. Access to logs MUST be limited to controlled, automated, and monitored mechanisms. Log storage SHOULD be replicated and archived for durability (for example, by using the appropriate replication and archival processes). The Log Archive account MUST apply layered preventive and detective controls to protect log integrity and availability. In addition to preventive controls, such as assigning least privilege roles to be used for access and encrypting logs with a controlled KMS key, use detective controls such as AWS Config to monitor (and alert and remediate) this collection of permissions for unexpected changes.

**Design consideration:**
+ Operational log data used by your infrastructure, operations, and workload teams often overlaps with the log data used by security, audit, and compliance teams. You SHOULD consolidate operational log data into the Log Archive account. Based on your specific security and governance requirements, you might need to filter operational log data saved to this account. You MUST define and enforce which principals can access operational log data in the Log Archive account.

## Types of logs
<a name="log-types"></a>

The primary logs shown in the AWS SRA include AWS CloudTrail (organization trail), Amazon VPC flow logs, access logs from Amazon CloudFront and AWS WAF, and DNS logs from Amazon Route 53. These logs provide an audit of actions taken (or attempted) by a user, role, AWS service, or network entity (identified, for example, by an IP address). You can also capture and archive other log types (for example, application logs or database logs). For more information about log sources and logging best practices, see the [security documentation for each service](https://docs.aws.amazon.com/security/).

## Amazon S3 as central log store
<a name="log-s3"></a>

Many AWS services log information in Amazon S3—either by default or exclusively. AWS CloudTrail, Amazon VPC Flow Logs, Elastic Load Balancing, Amazon GuardDuty, AWS Config, and AWS WAF are some examples of services that log information in Amazon S3. This means that S3 object integrity supports log integrity; S3 object access controls support log confidentiality; and S3 Object Lock, S3 object versions, and S3 Lifecycle rules support log availability. By logging information in a dedicated and centralized S3 bucket that resides in a dedicated account, you can manage these logs in just a few buckets and enforce strict security controls, access, and separation of duties.

In the AWS SRA, the primary logs stored in Amazon S3 come from CloudTrail, so this section describes how to protect those objects. This guidance also applies to any other S3 objects created either by your own applications or by other AWS services. Any S3 data that requires high integrity, strong access control, or automated retention SHOULD use the same Object Lock, versioning, and lifecycle patterns as the log buckets.

All new objects (including CloudTrail logs) that are uploaded to S3 buckets are [encrypted by default](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-encryption-faq.html) by using Amazon server-side encryption with Amazon S3-managed encryption keys (SSE-S3). This helps protect the data at rest, but access is managed exclusively by IAM policies. All security log S3 buckets SHOULD use SSE-KMS with customer managed keys. This adds a second level of access control. To read log files, a user must have both Amazon S3 read permissions for the S3 object and an IAM policy or role applied that allows them permissions to decrypt, along with permission granted by an associated key policy.

Two options help you protect or verify the integrity of CloudTrail log objects that are stored in Amazon S3. CloudTrail provides [log file integrity validation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html) to determine whether a log file was modified or deleted after CloudTrail delivered it. The other option is [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html).

Permissions for logging services (for example, CloudTrail) and the Log Archive account MUST follow least privilege. For example, users with permissions granted by the AWS managed IAM policy `AWSCloudTrail_FullAccess` can disable or reconfigure the most sensitive and important auditing functions in their AWS accounts. The AWSCloudTrail\_FullAccess managed policy MUST be attached only to the minimal set of approved principals.

You SHOULD use AWS Config and IAM Access Analyzer to detect, alert on, and remediate unexpected changes to log-protection controls.

For a deeper discussion of security best practices for S3 buckets, see the [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html), [online tech talks](https://www.youtube.com/watch?v=7M3s_ix9ljE), and the blog post [Top 10 security best practices for securing data in Amazon S3](https://aws.amazon.com/blogs/security/top-10-security-best-practices-for-securing-data-in-amazon-s3/).

**Implementation example:**
+ The [AWS SRA code library](https://github.com/aws-samples/aws-security-reference-architecture-examples) provides a sample implementation of [Amazon S3 block account public access](https://github.com/aws-samples/aws-security-reference-architecture-examples/blob/main/aws_sra_examples/solutions/s3/s3_block_account_public_access). This module blocks Amazon S3 public access for all existing and future accounts in the AWS organization.

## Amazon Security Lake
<a name="log-security-lake"></a>

[For organizations with existing Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) deployments or specific requirements for subscriber-based data access patterns, Security Lake remains a supported option.

The AWS SRA recommends that you SHOULD use the Log Archive account as the delegated administrator account for Security Lake. When you do this, Security Lake collects supported logs in dedicated S3 buckets in the same account as other SRA-recommended security logs.

To protect the availability of the logs and the log management process, AWS Key Management Service (AWS KMS) key―use detective controls such as AWS Config to monitor, alert, and remediate this collection of permissions for unexpected changes.

The Security Lake administrator can enable log collection across your AWS organization. These logs are stored in regional S3 buckets in the Log Archive account. Additionally, to centralize logs and facilitate easier storage and analysis, the Security Lake administrator can choose one or more rollup Regions where logs from all the regional S3 buckets are consolidated and stored. Logs from supported AWS services are automatically converted into OCSF and saved in Apache Parquet format in Security Lake S3 buckets. With OCSF support, Security Lake efficiently normalizes and consolidates security data from AWS and other enterprise security sources to create a unified and reliable repository of security-related information.

Security Lake can collect logs that are associated with AWS CloudTrail management events and CloudTrail data events for Amazon S3 and AWS Lambda. To collect CloudTrail management events in Security Lake, you MUST have at least one multi-Region organization trail with logging enabled that captures read and write management events. Logging must be enabled for the trail. A multi-Region trail delivers log files from multiple Regions to a single S3 bucket for a single AWS account. Before enabling multi-Region trails across countries, you MUST verify that data export and residency requirements permit it.

AWS Security Hub CSPM is a supported native data source in Security Lake, and you SHOULD add Security Hub CSPM findings to Security Lake. Security Hub CSPM generates findings from many different AWS services and third-party integrations. These findings help you get an overview of your compliance posture and whether you're following security recommendations for AWS and AWS Partner solutions.

To gain visibility and actionable insights from logs and events, you can query the data by using tools such as Amazon Athena, Amazon OpenSearch Service, AWS Quick, and third-party solutions. Users MUST NOT access Security Lake data directly in the Log Archive account. Users SHOULD access Security Lake data through query or data-access subscribers in the Security Tooling account. Or they can use other AWS accounts or on-premises locations that provide analytics tools such as OpenSearch Service, Quick, or third-party tools such as security information and event management (SIEM) tools. To provide access to the data, the Security Lake administrator SHOULD grant data access only by configuring subscribers (query access) for the consuming account. For more information, see [Amazon Security Lake](security-tooling.md#tool-security-lake) in the *Security OU ‒ Security Tooling* account section of this guide.

Security Lake provides an AWS managed policy to help you manage administrator access to the service. As a best practice, Security Lake configuration SHOULD be changed only through deployment pipelines. Deny console and CLI configuration changes using IAM policies or SCPs. Additionally, permissions to manage Security Lake MUST be least privilege and SHOULD be enforced with both IAM policies and SCPs.. You SHOULD alert on any direct (non-Security Lake) access to Security Lake S3 buckets.

## Centralized log collection
<a name="log-centralized-log-collection"></a>

The AWS SRA recommends two options for centralized log collection and analytics across your AWS organization. You SHOULD use Amazon CloudWatch Unified Data Store in Security Tooling account in the Security OU as the primary centralized log injection and analytics solution. Organizations MAY use Security Lake as an alternative with existing investments or specific subscriber-based access requirements. For long term WORM (Write-Once-Read-Many) immutable log archival you MUST use the Log Archive account is the tightly access controlled account.
