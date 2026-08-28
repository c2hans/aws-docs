---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-log-group-encrypted.html
---

# cloudwatch-log-group-encrypted
<a name="cloudwatch-log-group-encrypted"></a>

Checks if Amazon CloudWatch Log Groups are encrypted with any AWS KMS key or a specified AWS KMS key Id. The rule is NON\_COMPLIANT if a CloudWatch Log Group is not encrypted with a KMS key or is encrypted with a KMS key not supplied in the rule parameter.

**Identifier:** CLOUDWATCH\_LOG\_GROUP\_ENCRYPTED

**Resource Types:** AWS::Logs::LogGroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

KmsKeyId (Optional)Type: String
Amazon Resource Name (ARN) of the ID for the KMS key that is used to encrypt the log group.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d357c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
