---
source_url: https://docs.aws.amazon.com/kms/latest/cryptographic-details/kms-keys.html
---

# Working with AWS KMS keys
<a name="kms-keys"></a>

An AWS KMS key refers to a logical key that might refer to one or more hardware security module (HSM) backing keys (HBKs). This topic explains how to create a KMS key, import key material, and how to enable, disable, rotate, and delete KMS keys.

**Note**
AWS KMS is replacing the term *customer master key (CMK)* with *AWS KMS key* and *KMS key*. The concept has not changed. To prevent breaking changes, AWS KMS is keeping some variations of this term.

This chapter discusses the lifecycle of a KMS key from creation to deletion, as shown in the following image.

![KMS key lifecycle.](http://docs.aws.amazon.com/kms/latest/cryptographic-details/images/keystate.png)

**Topics**
+ [Calling CreateKey](create-key.md)
+ [Importing key material](importing-key-material.md)
+ [Enabling and disabling keys](enable-and-disable-key.md)
+ [Deleting keys](key-deletion.md)
+ [Rotating key material](rotate-customer-master-key.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
