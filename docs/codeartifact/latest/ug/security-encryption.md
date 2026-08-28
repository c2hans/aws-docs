---
source_url: https://docs.aws.amazon.com/codeartifact/latest/ug/security-encryption.html
---

# Data encryption
<a name="security-encryption"></a>

 Encryption is an important part of CodeArtifact security. Some encryption, such as for data in transit, is provided by default and does not require you to do anything. Other encryption, such as for data at rest, you can configure when you create your project or build.
+  **Encryption of data at rest** - All assets stored in CodeArtifact are encrypted by using AWS KMS keys (KMS keys). This includes all assets in all packages in all repositories. One KMS key is used for each domain to encrypt all its assets. By default, an AWS managed KMS key is used, so you do not need to create a KMS key. If you want, you can use a customer-managed KMS key that you create and configure. For more information, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) and [AWS Key Management Service concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) in the *AWS Key Management Service User Guide*. You can specify a customer-managed KMS key when you create a domain. For more information, see [Working with domains in CodeArtifact](domains.md).
+  **Encryption of data in transit** - CodeArtifact uses TLS encryption to protect all communication between customers and CodeArtifact and between CodeArtifact and its downstream dependencies.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
