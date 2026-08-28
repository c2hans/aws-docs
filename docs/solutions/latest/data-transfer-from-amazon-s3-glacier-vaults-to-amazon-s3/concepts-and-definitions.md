---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/concepts-and-definitions.html
---

# Concepts and definitions
<a name="concepts-and-definitions"></a>

 This section describes key concepts and defines terminology specific to this Guidance:

 **archive**

 Any data stored in an Amazon Glacier vault, such as a photo, video, or document. An archive is similar to an Amazon S3 object: it's the base unit of storage in the Amazon Glacier service. For more information, see [Archive](https://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-data-model.html#data-model-archive) in the *Amazon Glacier Developer Guide*.

 **chunk**

 Term used to describe a *part* in a multipart upload or download for the Amazon Glacier service. This Guidance uses multipart upload to transfer the archives. For more information, see [Uploading Large Archives in Parts (Multipart Upload)](https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html) and [Retrieving Amazon Glacier Archives Using AWS Management Console](https://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive-two-steps.html) in the *Amazon Glacier Developer Guide*.

 **inventory**

 A point in time snapshot or listing of the archives stored within an Amazon Glacier vault. For more information, see [Downloading a Vault Inventory in Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-inventory.html) in the *Amazon Glacier Developer Guide*.

 **tag**

 A key-value pair used to categorize storage in the Amazon S3 service. For more information, see [Categorizing your storage using tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html) in the *Amazon S3 User Guide*.

 **vault**

 A container in the Amazon Glacier service for storing archives. An Amazon Glacier vault is similar to an S3 bucket. For more information, see [Vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-data-model.html#data-model-vault) in the *Amazon Glacier Developer Guide*.

 **workflow\_run**

 An identifier used to represent the transfer of an Amazon Glacier vault to an S3 bucket. The Guidance randomly generates the `workflow_run` value on the first run (or you can choose the value). The Guidance uses this value when resuming a transfer.

**Note**
 For a general reference of AWS terms, see the [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
