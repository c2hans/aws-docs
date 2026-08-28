---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-versioning-enabled.html
---

# s3-bucket-versioning-enabled
<a name="s3-bucket-versioning-enabled"></a>

Checks if versioning is enabled for your S3 buckets. Optionally, the rule checks if MFA delete is enabled for your S3 buckets.

**Identifier:** S3\_BUCKET\_VERSIONING\_ENABLED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

isMfaDeleteEnabled (Optional)Type: String
MFA delete is enabled for your S3 buckets.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1415c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
