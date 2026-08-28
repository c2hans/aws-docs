---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-kms-best-practices/data-protection.html
---

# Data protection best practices for AWS KMS
<a name="data-protection"></a>

This section helps you to make choices about AWS Key Management Service (AWS KMS) key usage for data protection, such as which keys to use for each data type. It also provides specific examples of using AWS KMS with different AWS services. These recommendations and examples help you understand how many keys you might need and which principals require permissions to use those keys.

The section also discusses key rotation. *Key rotation* is the practice of either replacing an existing KMS key with a new key or replacing the cryptographic material associated with an existing KMS key with new material. This guide provides examples and instructions for how to rotate KMS keys for commonly used AWS services. The recommendations and examples are designed to help you make informed choices about your key rotation strategy.

Finally, this section makes recommendations for how to use the AWS Encryption SDK, a tool for implementing client-side encryption in your applications. This section includes design choices that you can make based on the feature set and capabilities of the AWS Encryption SDK.

**This section discusses the following encryption topics:**
+ [Encryption with AWS KMS](data-protection-encryption.md)
+ [Key rotation and scope of impact](data-protection-key-rotation.md)
+ [Recommendations for using the AWS Encryption SDK](data-protection-sdk.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
