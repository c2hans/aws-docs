---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/keystores.html
---

# Key stores in the AWS Database Encryption SDK
<a name="keystores"></a>

In the AWS Database Encryption SDK, a *key store* is a Amazon DynamoDB table that persists hierarchical data used by the [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md). The key store helps reduce the number of calls that you need to make to AWS KMS to perform cryptographic operations with the Hierarchical keyring.

The key store persists and manages the *branch keys* that the Hierarchical keyring uses to perform envelope encryption and protect data encryption keys. The key store stores the active branch key and all previous versions of the branch key. The *active* branch key is the most recent branch key version. The Hierarchical keyring uses a unique data encryption key for each encrypt request and encrypts each data encryption key with a unique wrapping key derived from the active branch key. The Hierarchical keyring is dependent on the hierarchy established between active branch keys and their derived wrapping keys.

## Key store terminology and concepts
<a name="keystore-concepts"></a>

**Key store**
The DynamoDB table that persists hierarchical data, such as branch keys and beacon keys.

**Root key**
A symmetric encryption KMS key that generates and protects the branch keys and beacon keys in your key store.

**Branch key**
A data key that is reused to derive unique wrapping key for envelope encryption. You can create multiple branch keys in one key store, but each branch key can only have one active branch key version at a time. The *active* branch key is the most recent branch key version.
Branch keys are derived from AWS KMS keys using the [kms:GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html) operation.

**Wrapping key**
A unique data key that is used to encrypt the data encryption key used in encrypt operations.
Wrapping keys are derived from branch keys. For more information on the key derivation process, see [AWS KMS Hierarchical keyring technical details](reference.md#hierarchical-keyring-details).

**Data encryption key**
A data key that is used in encrypt operations. The Hierarchical keyring uses a unique data encryption key for each encrypt request.

**Beacon key**
A data key that is used to generate beacons for searchable encryption. For more information, see [Searchable encryption](searchable-encryption.md).
