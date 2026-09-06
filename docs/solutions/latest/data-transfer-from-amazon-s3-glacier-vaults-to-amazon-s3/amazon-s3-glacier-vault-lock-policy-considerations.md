---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/amazon-s3-glacier-vault-lock-policy-considerations.html
---

# Amazon Glacier Vault Lock policy considerations
<a name="amazon-s3-glacier-vault-lock-policy-considerations"></a>

 This Guidance doesn't delete the original archives or the source Amazon Glacier vault. You must manually delete the archives and vault. For more information, refer to [Deleting an Archive in Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive.html) in the *Amazon Glacier Developer Guide*.

 If your source Amazon Glacier vault has a [Vault Lock policy](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-policy.html) that prevents deletion, you must delete this policy before deleting the original archives. However, if your Vault Lock policy is in the `Locked` state, you can't delete it. See [Amazon Glacier Vault Lock](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html) and [Abort Vault Lock (DELETE lock-policy)](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-AbortVaultLock.html) in the Amazon Glacier Developer Guide for more information.
