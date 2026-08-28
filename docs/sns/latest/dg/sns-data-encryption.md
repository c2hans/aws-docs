---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-data-encryption.html
---

# Amazon SNS data encryption
<a name="sns-data-encryption"></a>

Data protection refers to protecting data while in-transit (as it travels to and from Amazon SNS) and at rest (while it is stored on disks in Amazon SNS data centers). You can protect data in transit using Secure Sockets Layer (SSL) or client-side encryption. By default, Amazon SNS stores messages and files using disk encryption. You can protect data at rest by requesting Amazon SNS to encrypt your messages before saving them to the encrypted file system in its data centers. Amazon SNS recommends using SSE for optimized data encryption.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
