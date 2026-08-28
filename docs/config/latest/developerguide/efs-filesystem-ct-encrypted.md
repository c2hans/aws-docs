---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/efs-filesystem-ct-encrypted.html
---

# efs-filesystem-ct-encrypted
<a name="efs-filesystem-ct-encrypted"></a>

Checks if Amazon Elastic File System (Amazon EFS) encrypts data with AWS Key Management Service (AWS KMS). The rule is NON\_COMPLIANT if a file system is not encrypted. Optionally, you can check if a file system is not encrypted with specified KMS keys.

**Identifier:** EFS\_FILESYSTEM\_CT\_ENCRYPTED

**Resource Types:** AWS::EFS::FileSystem

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Israel (Tel Aviv), Canada West (Calgary) Region

**Parameters:**

kmsKeyArns (Optional)Type: String
(Optional) Comma-separated list of Amazon Resource Names (ARNs) for AWS KMS keys. If provided, the rule checks if the specified KMS keys do not encrypt an Amazon EFS file system.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d699c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
