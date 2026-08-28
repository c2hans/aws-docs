---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/s3-default-encryption-kms.html
---

# s3-default-encryption-kms
<a name="s3-default-encryption-kms"></a>

Checks if the S3 buckets are encrypted with AWS Key Management Service (AWS KMS). The rule is NON\_COMPLIANT if the S3 bucket is not encrypted with an AWS KMS key.

**Identifier:** S3\_DEFAULT\_ENCRYPTION\_KMS

**Resource Types:** AWS::S3::Bucket, AWS::KMS::Key

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

kmsKeyArns (Optional)Type: CSV
Comma separated list of AWS KMS key ARNs allowed for encrypting Amazon S3 Buckets.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1417c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
