---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/create-keystore.html
---

# Create a key store
<a name="create-keystore"></a>

Before you can [create branch keys](create-branch-keys.md) or use an [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md), you must create your key store, a Amazon DynamoDB table that manages and protects your branch keys.

**Important**
Do not delete the DynamoDB table that persists your branch keys. If you delete this table, you will be unable to decrypt any data encrypted using the Hierarchical keyring.

Follow the [Create a table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-1.html) procedures in the *Amazon DynamoDB Developer Guide*, using the following required string values for the partition key and sort key.

|   | Partition key | Sort key |
| --- | --- | --- |
| Base table | branch-key-id | type |

**Logical key store name**
When naming the DynamoDB table that serves as your key store, it's important to carefully consider the *logical key store name* that you'll specify when [configuring your key store actions](keystore-actions.md#config-keystore-actions). The logical key store name acts as an identifier for your key store and cannot be changed after it is initially defined by the first user. You must always specify the same logical key store name in your [key store actions](keystore-actions.md).

There must be a one-to-one mapping between the DynamoDB table name and the logical key store name. The logical key store name is cryptographically bound to all data stored in the table to simplify DynamoDB restore operations. While the logical key store name can be different from your DynamoDB table name, we strongly recommend specifying your DynamoDB table name as the logical key store name. In the event that your table name changes after [restoring your DynamoDB table from a backup](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Restore.Tutorial.html), the logical key store name can be mapped to the new DynamoDB table name to ensure that the Hierarchical keyring can still access your key store.

Do not include confidential or sensitive information in your logical key store name. The logical key store name is displayed in plaintext in AWS KMS CloudTrail events as the `tablename`.

**Next steps**

1. [Configure key store actions](keystore-actions.md)

1. [Create an active branch key](create-branch-keys.md)

1. [Create an AWS KMS Hierarchical keyring](use-hierarchical-keyring.md)
