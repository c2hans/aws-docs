---
source_url: https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-kms-permissions.html
---

# Permissions for AWS KMS–encrypted Amazon SNS topics
<a name="sns-kms-permissions"></a>

 The Amazon SNS topic you specify might be encrypted by AWS Key Management Service. To allow DevOps Guru to work with encrypted topics, you must first create a AWS KMS key and then add the following statement to the policy of the KMS key. For more information, see [Encrypting messages published to Amazon SNS with AWS KMS](https://aws.amazon.com/blogs/compute/encrypting-messages-published-to-amazon-sns-with-aws-kms/), [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *AWS KMS User Guide*, and [Data encryption](https://docs.aws.amazon.com/sns/latest/dg/sns-data-encryption.html) in the *Amazon Simple Notification Service Developer Guide*.

**Note**
DevOps Guru currently supports encrypted topics for use within a single account. Using an encrypted topic across multiple accounts is not supported at this time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
