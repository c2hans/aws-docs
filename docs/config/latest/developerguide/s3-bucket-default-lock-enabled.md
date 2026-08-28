---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-default-lock-enabled.html
---

# s3-bucket-default-lock-enabled
<a name="s3-bucket-default-lock-enabled"></a>

Checks if the S3 bucket has lock enabled, by default. The rule is NON\_COMPLIANT if the lock is not enabled.

**Identifier:** S3\_BUCKET\_DEFAULT\_LOCK\_ENABLED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

mode (Optional)Type: String
mode: (optional): A mode parameter with valid values of GOVERNANCE or COMPLIANCE.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1391c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
