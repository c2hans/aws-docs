---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/keystore-least-privilege.html
---

# Implementing least privileged permissions
<a name="keystore-least-privilege"></a>

When using a key store and AWS KMS Hierarchical keyrings, we recommend that you follow the principle of least privilege by defining the following roles:

**Key store administrator**
Key store administrators are responsible for creating and managing the key store and the branch keys that it that persists and protects. Key store administrators should be the only users with write permissions to the Amazon DynamoDB table that serves as your key store. They should be the only users with access to privileged, administrator operations, such as [`CreateKey`](create-branch-keys.md) and [`VersionKey`](rotate-branch-key.md). You can only perform these operations when you [statically configure your key store actions](keystore-actions.md#static-keystore).
`CreateKey` is a privileged operation that can add a new KMS key ARN to your key store allowlist. This KMS key can create new active branch keys. We recommend limiting access to this operation because once a KMS key is added to the branch key store, it cannot be deleted.

**Key store user**
In most use cases, the key store user only interacts with key store via the Hierarchical keyring as they encrypt, decrypt, sign, and verify data. As a result, they only need read permissions to the Amazon DynamoDB table that serves as your key store. Key store users should only need access to the usage operations that make cryptographic operations possible, such as `GetActiveBranchKey`, `GetBranchKeyVersion`, and `GetBeaconKey`. They don't need permissions to create or manage the branch keys that they use.
You can perform usage operations when your key store actions are [statically configured](keystore-actions.md#static-keystore), or when they're configured for [discovery](keystore-actions.md#discovery-keystore). You cannot perform administrator operations (`CreateKey` and `VersionKey`) when your key store actions is configured for discovery.
If your branch key store administrator allowlisted multiple KMS keys in your branch key store, we recommend that your key store users configure their key store actions for discovery so that their Hierarchical keyring can use multiple KMS keys.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
