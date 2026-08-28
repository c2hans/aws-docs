---
source_url: https://docs.aws.amazon.com/kms/latest/developerguide/determining-access.html
---

# Determining access to AWS KMS keys
<a name="determining-access"></a>

To determine the full extent of who or what currently has access to an AWS KMS key, you must examine the key policy of the KMS key, all [grants](grants.md) that apply to the KMS key, and potentially all AWS Identity and Access Management (IAM) policies. You might do this to determine the scope of potential usage of a KMS key, or to help you meet compliance or auditing requirements. The following topics can help you generate a complete list of the AWS principals (identities) that currently have access to a KMS key.

**Topics**
+ [Examining the key policy](determining-access-key-policy.md)
+ [Examining IAM policies](determining-access-iam-policies.md)
+ [Examining grants](determining-access-grants.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
