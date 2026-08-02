---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/keyrings.html
---

# Keyrings
<a name="keyrings"></a>

****

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

The AWS Database Encryption SDK uses *keyrings* to perform [envelope encryption](concepts.md#envelope-encryption). Keyrings generate, encrypt, and decrypt data keys. Keyrings determine the source of the unique data keys that protect each encrypted record, and the [wrapping keys](concepts.md#wrapping-key) that encrypt that data key. You specify a keyring when encrypting and the same or a different keyring when decrypting.

You can use each keyring individually or combine keyrings into a [multi-keyring](use-multi-keyring.md). Although most keyrings can generate, encrypt, and decrypt data keys, you might create a keyring that performs only one particular operation, such as a keyring that only generates data keys, and use that keyring in combination with others.

We recommend that you use a keyring that protects your wrapping keys and performs cryptographic operations within a secure boundary, such as the AWS KMS keyring, which uses AWS KMS keys that never leave [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/) (AWS KMS) unencrypted. You can also write a keyring that uses wrapping keys that are stored in your hardware security modules (HSMs) or protected by other master key services.

Your keyring determines the wrapping keys that protect your data keys, and ultimately, your data. Use the most secure wrapping keys that are practical for your task. Whenever possible use wrapping keys that are protected by a hardware security module (HSM) or a key management infrastructure, such as KMS keys in [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/) (AWS KMS) or encryption keys in [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/).

The AWS Database Encryption SDK provides several keyrings and keyring configurations, and you can create your own custom keyrings. You can also create a [multi-keyring](use-multi-keyring.md) that includes one or more keyrings of the same or a different type.

**Topics**
+ [How keyrings work](#using-keyrings)
+ [AWS KMS keyrings](use-kms-keyring.md)
+ [AWS KMS Hierarchical keyrings](use-hierarchical-keyring.md)
+ [AWS KMS ECDH keyrings](use-kms-ecdh-keyring.md)
+ [Raw AES keyrings](use-raw-aes-keyring.md)
+ [Raw RSA keyrings](use-raw-rsa-keyring.md)
+ [Raw ECDH keyrings](use-raw-ecdh-keyring.md)
+ [Multi-keyrings](use-multi-keyring.md)

## How keyrings work
<a name="using-keyrings"></a>

****

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

When you encrypt and sign a field in your database, the AWS Database Encryption SDK asks the keyring for encryption materials. The keyring returns a plaintext data key, a copy of the data key that's encrypted by each of the wrapping keys in the keyring, and a MAC key that is associated with the data key. The AWS Database Encryption SDK uses the plaintext key to encrypt the data, and then removes the plaintext data key from memory as soon as possible. Then, the AWS Database Encryption SDK adds a [material description](concepts.md#material-description) that includes the encrypted data keys and other information, such as encryption and signing instructions. The AWS Database Encryption SDK uses the MAC key to calculate Hash-Based Message Authentication Codes (HMACs) over the canonicalization of the material description and all fields marked `ENCRYPT_AND_SIGN` or `SIGN_ONLY`.

When you decrypt data, you can use the same keyring that you used to encrypt the data, or a different one. To decrypt the data, a decryption keyring must have access to at least one wrapping key in the encryption keyring.

The AWS Database Encryption SDK passes the encrypted data keys from the material description to the keyring, and asks the keyring to decrypt any one of them. The keyring uses its wrapping keys to decrypt one of the encrypted data keys and returns a plaintext data key. The AWS Database Encryption SDK uses the plaintext data key to decrypt the data. If none of the wrapping keys in the keyring can decrypt any of the encrypted data keys, the decrypt operation fails.

You can use a single keyring or also combine keyrings of the same type or a different type into a [multi-keyring](use-multi-keyring.md). When you encrypt data, the multi-keyring returns a copy of the data key encrypted by all of the wrapping keys in all of the keyrings that comprise the multi-keyring and a MAC key that is associated with the data key. You can decrypt the data using a keyring with any one of the wrapping keys in the multi-keyring.
