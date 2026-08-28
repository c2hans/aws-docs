---
source_url: https://docs.aws.amazon.com/efs/latest/ug/encryption.html
---

# Data encryption in Amazon EFS
<a name="encryption"></a>

Amazon EFS provides comprehensive encryption capabilities to protect your data both at rest and in transit.
+ **Encryption at rest** – Encrypts data stored on your file system.
+ **Encryption in transit** – Encrypts data as it travels between your clients and the file system.

If your organization is subject to corporate or regulatory policies that require encryption of data and metadata, we recommend creating a file system that is encrypted at rest and mounting your file system using encryption of data in transit.

**Topics**
+ [Encrypting data at rest](encryption-at-rest.md)
+ [Encrypting data in transit](encryption-in-transit.md)
+ [Using AWS KMS keys for Amazon EFS](EFSKMS.md)
+ [Troubleshooting encryption](troubleshooting-efs-encryption.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic File System (EFS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query efs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
