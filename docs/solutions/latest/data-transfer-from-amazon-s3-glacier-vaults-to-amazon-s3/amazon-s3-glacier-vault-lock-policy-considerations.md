---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/amazon-s3-glacier-vault-lock-policy-considerations.html
---

# Amazon Glacier Vault Lock policy considerations
<a name="amazon-s3-glacier-vault-lock-policy-considerations"></a>

 This Guidance doesn't delete the original archives or the source Amazon Glacier vault. You must manually delete the archives and vault. For more information, refer to [Deleting an Archive in Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive.html) in the *Amazon Glacier Developer Guide*.

 If your source Amazon Glacier vault has a [Vault Lock policy](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-policy.html) that prevents deletion, you must delete this policy before deleting the original archives. However, if your Vault Lock policy is in the `Locked` state, you can't delete it. See [Amazon Glacier Vault Lock](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html) and [Abort Vault Lock (DELETE lock-policy)](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-AbortVaultLock.html) in the Amazon Glacier Developer Guide for more information.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
