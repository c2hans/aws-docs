---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-table-encrypted-kms.html
---

# dynamodb-table-encrypted-kms
<a name="dynamodb-table-encrypted-kms"></a>

Checks if Amazon DynamoDB table is encrypted with AWS Key Management Service (KMS). The rule is NON\_COMPLIANT if Amazon DynamoDB table is not encrypted with AWS KMS. The rule is also NON\_COMPLIANT if the encrypted AWS KMS key is not present in `kmsKeyArns` input parameter.

**Identifier:** DYNAMODB\_TABLE\_ENCRYPTED\_KMS

**Resource Types:** AWS::DynamoDB::Table

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

kmsKeyArns (Optional)Type: CSV
Comma separated list of AWS KMS key ARNs allowed for encrypting Amazon DynamoDB Tables

## AWS CloudFormation template
<a name="w2aac20c16c17b7d511c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
