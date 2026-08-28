---
source_url: https://docs.aws.amazon.com/kms/latest/cryptographic-details/customer-data-operations.html
---

# Customer data operations
<a name="customer-data-operations"></a>

After you have established a KMS key, it can be used to perform cryptographic operations. Whenever data is encrypted under a KMS key, the resulting object is a customer ciphertext. The ciphertext contains two sections: an unencrypted header (or cleartext) portion, protected by the authenticated encryption scheme as the additional authenticated data, and an encrypted portion. The cleartext portion includes the HBK identifier (HBKID). These two immutable fields of the ciphertext value help ensure that AWS KMS can decrypt the object in the future.

**Topics**
+ [Generating data keys](generating-data-keys.md)
+ [Encrypt](encrypt-operation.md)
+ [Decrypt](decrypt-operation.md)
+ [Reencrypting an encrypted object](reencrypting-an-encrypted-object.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
