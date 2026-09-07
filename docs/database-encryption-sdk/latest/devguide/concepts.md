---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/concepts.html
---

# AWS Database Encryption SDK concepts
<a name="concepts"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

This topic explains the concepts and terminology used in the AWS Database Encryption SDK.

To learn how the components of the AWS Database Encryption SDK interact, see [How the AWS Database Encryption SDK works](how-it-works.md).

To learn more about the AWS Database Encryption SDK, see the following topics.
+ Learn how the AWS Database Encryption SDK uses [envelope encryption](#envelope-encryption) to protect your data.
+ Learn about the elements of envelope encryption: the [data keys](#data-key) that protect your records and the [wrapping keys](#wrapping-key) that protect your data keys.
+ Learn about the [keyrings](#keyring-concept) that determine which wrapping keys you use.
+ Learn about the [encryption context](#encryption-context) that adds integrity to your encryption process.
+ Learn about the [material description](#material-description) that the encryption methods add to your record.
+ Learn about the [cryptographic actions](#crypt-actions) that tell the AWS Database Encryption SDK what fields to encrypt and sign.

**Topics**
+ [Envelope encryption](#envelope-encryption)
+ [Data key](#data-key)
+ [Wrapping key](#wrapping-key)
+ [Keyrings](#keyring-concept)
+ [Cryptographic actions](#crypt-actions)
+ [Material description](#material-description)
+ [Encryption context](#encryption-context)
+ [Cryptographic materials manager](#crypt-materials-manager)
+ [Symmetric and asymmetric encryption](#symmetric-key-encryption)
+ [Key commitment](#key-commitment)
+ [Digital signatures](#digital-sigs)

## Envelope encryption
<a name="envelope-encryption"></a>

The security of your encrypted data depends in part on protecting the data key that can decrypt it. One accepted best practice for protecting the data key is to encrypt it. To do this, you need another encryption key, known as a *key-encryption key* or [wrapping key](#wrapping-key). The practice of using a wrapping key to encrypt data keys is known as *envelope encryption*.

**Protecting data keys**
The AWS Database Encryption SDK encrypts each field with a unique data key. Then it encrypts each data key under the wrapping key you specify. It stores the encrypted data keys in the [material description](#material-description).
To specify your wrapping key, you use a [keyring](#keyring-concept).

![Envelope encryption with the AWS Database Encryption SDK](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/images/dbesdk-envelope.png)

**Encrypting the same data under multiple wrapping keys**
You can encrypt the data key with multiple wrapping keys. You might want to provide different wrapping keys for different users, or wrapping keys of different types, or in different locations. Each of the wrapping keys encrypts the same data key. The AWS Database Encryption SDK stores all of the encrypted data keys alongside the encrypted fields in the [material description](#material-description).
To decrypt the data, you need to provide at least one wrapping key that can decrypt the encrypted data keys.

**Combining the strengths of multiple algorithms**
To encrypt your data, by default, the AWS Database Encryption SDK uses an [algorithm suite](supported-algorithms.md) with AES-GCM symmetric encryption, an HMAC-based key derivation function (HKDF), and [ECDSA signing](#digital-sigs). To encrypt the data key, you can specify a [symmetric or asymmetric encryption algorithm](#symmetric-key-encryption) appropriate to your wrapping key.
In general, symmetric key encryption algorithms are faster and produce smaller ciphertexts than asymmetric or *public key encryption*. But public key algorithms provide inherent separation of roles. To combine the strengths of each, you can encrypt the data key with public key encryption.
We recommend using one of the AWS KMS keyrings whenever possible. When you use the [AWS KMS keyring](use-kms-keyring.md), you can choose to combine the strengths of multiple algorithms by specifying an asymmetric RSA AWS KMS key as your wrapping key. You can also use a symmetric encryption KMS key.

## Data key
<a name="data-key"></a>

A *data key* is an encryption key that the AWS Database Encryption SDK uses to encrypt the fields in a record that are marked `ENCRYPT_AND_SIGN` in the [cryptographic actions](#crypt-actions). Each data key is a byte array that conforms to the requirements for cryptographic keys. The AWS Database Encryption SDK uses a unique data key to encrypt each attribute.

You don't need to specify, generate, implement, extend, protect, or use data keys. The AWS Database Encryption SDK does that work for you when you call the encrypt and decrypt operations.

To protect your data keys, the AWS Database Encryption SDK encrypts them under one or more *key-encryption keys* known as [wrapping keys](#wrapping-key). After the AWS Database Encryption SDK uses your plaintext data keys to encrypt your data, it removes them from memory as soon as possible. Then stores the encrypted data key in the [material description](#material-description). For details, see [How the AWS Database Encryption SDK works](how-it-works.md).

**Tip**
In the AWS Database Encryption SDK, we distinguish *data keys* from *data encryption keys*. As a best practice, all of the supported [algorithm suites](supported-algorithms.md) use a [key derivation function](https://en.wikipedia.org/wiki/Key_derivation_function). The key derivation function takes a data key as input and returns the data encryption keys that are actually used to encrypt your records. For this reason, we often say that data is encrypted "under" a data key rather than "by" the data key.

Each encrypted data key includes metadata, including the identifier of the wrapping key that encrypted it. This metadata makes it possible for the AWS Database Encryption SDK to identify valid wrapping keys when decrypting.

## Wrapping key
<a name="wrapping-key"></a>

A *wrapping key* is a key-encryption key that the AWS Database Encryption SDK uses to encrypt the [data key](#data-key) that encrypts your records. Each data key can be encrypted under one or more wrapping keys. You determine which wrapping keys are used to protect your data when you configure a [keyring](#keyring-concept).

![Encrypt one data key with multiple wrapping keys](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/images/dbesdk-wrapping-key.png)

The AWS Database Encryption SDK supports several commonly used wrapping keys, such as [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) (AWS KMS) symmetric encryption KMS keys (including [multi-Region AWS KMS keys](use-kms-keyring.md#config-mrks)) and asymmetric [RSA KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/asymmetric-key-specs.html#key-spec-rsa), raw AES-GCM (Advanced Encryption Standard/Galois Counter Mode) keys, and raw RSA keys. We recommend using KMS keys whenever possible. To decide which wrapping key you should use, see [Selecting wrapping keys](configure.md#config-keys).

When you use envelope encryption, you need to protect your wrapping keys from unauthorized access. You can do this in any of the following ways:
+ Use a service designed for this purpose, such as [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/).
+ Use a [hardware security module (HSM)](https://en.wikipedia.org/wiki/Hardware_security_module) such as those offered by [AWS CloudHSM](https://aws.amazon.com/cloudhsm/).
+ Use other key management tools and services.

If you don't have a key management system, we recommend AWS KMS. The AWS Database Encryption SDK integrates with AWS KMS to help you protect and use your wrapping keys.

## Keyrings
<a name="keyring-concept"></a>

To specify the wrapping keys you use for encryption and decryption, you use a keyring. You can use the keyrings that the AWS Database Encryption SDK provides or design your own implementations.

A *keyring* generates, encrypts, and decrypts data keys. It also generates the MAC keys used to calculate the Hash-Based Message Authentication Codes (HMACs) in the signature. When you define a keyring, you can specify the [wrapping keys](#wrapping-key) that encrypt your data keys. Most keyrings specify at least one wrapping key or a service that provides and protects wrapping keys. When encrypting, the AWS Database Encryption SDK uses all of the wrapping keys specified in the keyring to encrypt the data key. For help with choosing and using the keyrings that the AWS Database Encryption SDK defines, see [Using keyrings](keyrings.md).

## Cryptographic actions
<a name="crypt-actions"></a>

*Cryptographic actions* tell the encryptor which actions to perform on each field in a record.

The cryptographic action values can be one of the following:
+ **Encrypt and sign** – Encrypt the field. Include the encrypted field in the signature.
+ **Sign only** – Include the field in the signature.
+ **Sign and include in encryption context** – Include the field in the signature and [encryption context](#encryption-context).

  By default, the partition and sort keys are the only attribute included in the encryption context. You might consider defining additional fields as `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` so that the branch key ID supplier for your [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md) can identify which branch key is required for decryption from the encryption context. For more information, see [branch key ID supplier](use-hierarchical-keyring.md#branch-key-id-supplier).
**Note**
To use the `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` cryptographic action, you must use version 3.3 or later of the AWS Database Encryption SDK. Deploy the new version to all readers before [updating your data model](ddb-update-data-model.md) to include `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`.
+ **Do nothing** – Do not encrypt or include the field in the signature.

For any field that can store sensitive data, use **Encrypt and sign**. For primary key values (for example, a partition key and sort key in a DynamoDB table), use **Sign only** or **Sign and include in encryption context**. If you specify any **Sign and include in encryption context** attributes, then the partition and sort attributes must also be **Sign and include in encryption context**. You do not need to specify cryptographic actions for the [material description](#material-description). The AWS Database Encryption SDK automatically signs the field that the material description is stored in.

Choose your cryptographic actions carefully. When in doubt, use **Encrypt and sign**. After you have used the AWS Database Encryption SDK to protect your records, you cannot change an existing `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` field to `DO_NOTHING`, or change the cryptographic action assigned to an existing `DO_NOTHING` field. However, you can still [make other changes to your data model](ddb-update-data-model.md). For example, you can add or remove encrypted fields, in a single deployment.

## Material description
<a name="material-description"></a>

The material description serves as the header for an encrypted record. When you encrypt and sign fields with the AWS Database Encryption SDK, the encryptor records the material description as it assembles the cryptographic materials and stores the material description in a new field (`aws_dbe_head`) that the encryptor adds to your record.

The material description is a portable [formatted data structure](reference.md#material-description-format) that contains encrypted copies of the data keys and other information, such as encryption algorithms, [encryption context](#encryption-context), and encryption and signing instructions. The encryptor records the material description as it assembles the cryptographic materials for encryption and signing. Later, when it needs to assemble cryptographic materials to verify and decrypt a field, it uses the material description as its guide.

Storing the encrypted data keys alongside the encrypted field streamlines the decryption operation and frees you from having to store and manage encrypted data keys independently of the data that they encrypt.

For technical information about the material description, see [Material description format](reference.md#material-description-format).

## Encryption context
<a name="encryption-context"></a>

To improve the security of your cryptographic operations, the AWS Database Encryption SDK includes an encryption context in all requests to encrypt and sign a record.

An *encryption context* is a set of name-value pairs that contain arbitrary, non-secret additional authenticated data. The AWS Database Encryption SDK includes the logical name for your database and primary key values (for example, a partition key and sort key in a DynamoDB table) in the encryption context. When you encrypt and sign a field, the encryption context is cryptographically bound to the encrypted record so that the same encryption context is required to decrypt the field.

If you use an AWS KMS keyring, the AWS Database Encryption SDK also uses the encryption context to provide additional authenticated data (AAD) in the calls the keyring makes to AWS KMS.

Whenever you use the [default algorithm suite](supported-algorithms.md#recommended-algorithms), the [cryptographic materials manager](#crypt-materials-manager) (CMM) adds a name-value pair to the encryption context that consists of a reserved name, `aws-crypto-public-key`, and a value that represents the public verification key. The public verification key is stored in the [material description](#material-description).

## Cryptographic materials manager
<a name="crypt-materials-manager"></a>

The cryptographic materials manager (CMM) assembles the cryptographic materials that are used to encrypt, decrypt, and sign your data. Whenever you use the [default algorithm suite](supported-algorithms.md#recommended-algorithms), the *cryptographic materials* include plaintext and encrypted data keys, symmetric signing keys, and an asymmetric signing key. You never interact with the CMM directly. The encryption and decryption methods handle it for you.

Because the CMM acts as a liaison between the AWS Database Encryption SDK and a keyring, it is an ideal point for customization and extension, such as support for policy enforcement. You can explicitly specify a CMM, but it's not required. When you specify a keyring, the AWS Database Encryption SDK creates a default CMM for you. The default CMM gets the encryption or decryption materials from the keyring that you specify. This might involve a call to a cryptographic service, such as [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/) (AWS KMS).

## Symmetric and asymmetric encryption
<a name="symmetric-key-encryption"></a>

*Symmetric encryption* uses the same key to encrypt and decrypt data.

*Asymmetric encryption* uses a mathematically related data key pair. One key in the pair encrypts the data; only the other key in the pair can decrypt the data.

The AWS Database Encryption SDK uses [envelope encryption](#envelope-encryption). It encrypts your data with a symmetric data key. It encrypts the symmetric data key with one or more symmetric or asymmetric wrapping keys. It adds a [material description](#material-description) to the record that includes at least one encrypted copy of the data key.

**Encrypting your data (symmetric encryption)**
To encrypt your data, the AWS Database Encryption SDK uses a symmetric [data key](#data-key) and an [algorithm suite](supported-algorithms.md) that includes a symmetric encryption algorithm. To decrypt the data, the AWS Database Encryption SDK uses the same data key and the same algorithm suite.

**Encrypting your data key (symmetric or asymmetric encryption)**
The [keyring](#keyring-concept) that you supply to an encrypt and decrypt operation determines how the symmetric data key is encrypted and decrypted. You can choose a keyring that uses symmetric encryption, such as an AWS KMS keyring with a symmetric encryption KMS key, or one that uses asymmetric encryption, such as an AWS KMS keyring with an asymmetric RSA KMS key.

## Key commitment
<a name="key-commitment"></a>

The AWS Database Encryption SDK supports *key commitment* (sometimes known as *robustness*), a security property that ensures that each ciphertext can be decrypted only to a single plaintext. To do this, key commitment ensures that only the data key that encrypted your record will be used to decrypt it. The AWS Database Encryption SDK includes key commitment for all encryption and decryption operations.

Most modern symmetric ciphers (including AES) encrypt plaintext under a single secret key, like the [unique data key](#data-key) that the AWS Database Encryption SDK uses to encrypt each plaintext field marked `ENCRYPT_AND_SIGN` in a record. Decrypting this record with the same data key returns a plaintext that is identical to the original. Decrypting with a different key will usually fail. Although difficult, it's technically possible to decrypt a ciphertext under two different keys. In rare cases, it is feasible to find a key that can partially decrypt ciphertext into a different, but still intelligible, plaintext.

The AWS Database Encryption SDK always encrypts each attribute under one unique data key. It might encrypt that data key under multiple wrapping keys, but the wrapping keys always encrypt the same data key. Nonetheless, a sophisticated, manually crafted encrypted record might actually contain different data keys, each encrypted by a different wrapping key. For example, if one user decrypts the encrypted record it returns 0x0 (false) while another user decrypting the same encrypted record gets 0x1 (true).

To prevent this scenario, the AWS Database Encryption SDK includes key commitment when encrypting and decrypting. The encrypt method cryptographically binds the unique data key that produced the ciphertext to the *key commitment*, a Hash-Based Message Authentication Code (HMAC) calculated over the material description using a derivation of the data key. Then it stores the key commitment in the [material description](#material-description). When it decrypts a record with key commitment, the AWS Database Encryption SDK verifies that the data key is the only key for that encrypted record. If data key verification fails, the decrypt operation fails.

## Digital signatures
<a name="digital-sigs"></a>

The AWS Database Encryption SDK encrypts your data using an authenticated encryption algorithm, AES-GCM, and the decryption process verifies the integrity and authenticity of an encrypted message without using a digital signature. But because AES-GCM uses symmetric keys, anyone who can decrypt the data key used to decrypt the ciphertext could also manually create a new encrypted ciphertext, causing a potential security concern. For instance, if you use an AWS KMS key as a wrapping key, a user with `kms:Decrypt` permissions could create encrypted ciphertexts without calling `kms:Encrypt`.

To avoid this issue, the [default algorithm suite](supported-algorithms.md#recommended-algorithms) adds an Elliptic Curve Digital Signature Algorithm (ECDSA) signature to encrypted records. The default algorithm suite encrypts the fields in your record marked `ENCRYPT_AND_SIGN` using an authenticated encryption algorithm, AES-GCM. Then, it calculates both Hash-Based Message Authentication Codes (HMACs) and asymmetric ECDSA signatures over the fields in your record marked `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, and `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`. The decryption process uses the signatures to verify that an authorized user encrypted the record.

When the default algorithm suite is used, the AWS Database Encryption SDK generates a temporary private key and public key pair for each encrypted record. The AWS Database Encryption SDK stores the public key in the [material description](#material-description) and discards the private key. This ensures that no one can create another signature that verifies with the public key. The algorithm binds the public key to the encrypted data key as additional authenticated data in the material description, preventing users who can only decrypt fields from altering the public key or affecting signature verification.

The AWS Database Encryption SDK always includes HMAC verification. ECDSA digital signatures are enabled by default, but not required. If the users encrypting data and the users decrypting data are equally trusted, you might consider using an algorithm suite that does not include digital signatures to improve your performance. For more information on selecting alternative algorithm suites, see [Choosing an algorithm suite](ddb-java-using.md#config-algorithm).

**Note**
If a keyring doesn't delineate between encryptors and decryptors, digital signatures provide no cryptographic value.

[AWS KMS keyrings](use-kms-keyring.md), including the asymmetric RSA AWS KMS keyring, can delineate between encryptors and decryptors based on AWS KMS key policies and IAM policies.

Due to their cryptographic nature, the following keyrings cannot delineate between encryptors and decryptors:
+ AWS KMS Hierarchical keyring
+ AWS KMS ECDH keyring
+ Raw AES keyring
+ Raw RSA keyring
+ Raw ECDH keyring
