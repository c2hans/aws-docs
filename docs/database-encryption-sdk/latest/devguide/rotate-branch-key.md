---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/rotate-branch-key.html
---

# Rotate your active branch key
<a name="rotate-branch-key"></a>

There can only be one active version for each branch key at a time. Typically, each active branch key version is used to satisfy multiple requests. But you control the extent to which active branch keys are reused and determine how often the active branch key is rotated.

Branch keys are not used to encrypt plaintext data keys. They are used to derive the unique wrapping keys that encrypt plaintext data keys. The [wrapping key derivation process](reference.md#hierarchical-keyring-details) produces a unique 32 byte wrapping key with 28 bytes of randomness. This means that a branch key can derive more than 79 octillion, or 296, unique wrapping keys before cryptographic wear-out occurs. Despite this very low exhaustion risk, you might be required to rotate your active branch keys due to business or contract rules or government regulations.

The active version of the branch key remains active until you rotate it. Previous versions of the active branch key will not be used to perform encrypt operations and cannot be used to derive new wrapping keys, but they can still be queried and provide wrapping keys to decrypt the data keys that they encrypted while active.

**Warning**
Deleting branch keys in test environments is irreversible. You cannot recover deleted branch keys. When you delete and recreate branch keys with the same ID in test environments, the following issues can occur:
Materials from previous test runs might remain in the cache
Some test hosts or threads might encrypt data using deleted branch keys
Data encrypted with deleted branches can't be decrypted
To prevent encryption failures in integration tests:
Reset the hierarchical keyring reference before creating new branch keys OR
Use unique branch key IDs for each test

**Required permissions**
To rotate branch keys, you need [kms:GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html) and [kms:ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html) permissions on the KMS key specified in your key store actions.

**Rotate an active branch key**
Use the `VersionKey` operation to rotate your active branch key. When you rotate the active branch key, a new branch key is created to replace the previous version. The `branch-key-id` does not change when you rotate the active branch key. You must specify the `branch-key-id` that identifies the current active branch key when you call `VersionKey`.

------
#### [ Java ]

```
keystore.VersionKey(
    VersionKeyInput.builder()
        .branchKeyIdentifier("{{branch-key-id}}")
        .build()
);
```

------
#### [ C\# / .NET ]

```
 keystore.VersionKey(new VersionKeyInput{BranchKeyIdentifier = branchKeyId});
```

------
#### [ Rust ]

```
keystore.version_key()
        .branch_key_identifier(branch_key_id)
        .send()
        .await?;
```

------
