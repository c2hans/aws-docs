---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/how-it-works.html
---

# How the AWS Database Encryption SDK works
<a name="how-it-works"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

The AWS Database Encryption SDK provides client-side encryption libraries that are designed specifically to protect the data that you store in databases. The libraries include secure implementations that you can extend or use unchanged. For more information about defining and using custom components, see the GitHub repository for your database implementation.

The workflows in this section explain how the AWS Database Encryption SDK encrypts and signs and decrypts and verifies the data in your database. These workflows describe the basic process using abstract elements and the default features. For details about how the AWS Database Encryption SDK works with your database implementation, see the *What is encrypted* topic for your database.

The AWS Database Encryption SDK uses [envelope encryption](concepts.md#envelope-encryption) to protect your data. Each record is encrypted under a unique [data key](concepts.md#data-key). The data key is used to derive a unique *data encryption key* for each field marked `ENCRYPT_AND_SIGN` in your cryptographic actions. Then, a copy of data key is encrypted by the wrapping keys you specify. To decrypt the encrypted record, the AWS Database Encryption SDK uses the wrapping keys you specify to decrypt at least one encrypted data key. Then it can decrypt the ciphertext and return a plaintext entry.

For more information about the terms used in the AWS Database Encryption SDK, see [AWS Database Encryption SDK concepts](concepts.md).

## Encrypt and sign
<a name="encrypt-and-sign"></a>

At its core, the AWS Database Encryption SDK is a record encryptor that encrypts, signs, verifies, and decrypts the records in your database. It takes in information about your records and instructions about which fields to encrypt and sign. It gets the encryption materials, and instructions on how to use them, from a [cryptographic materials manager](concepts.md#crypt-materials-manager) configured from the wrapping key you specify.

The following walkthrough describes how the AWS Database Encryption SDK encrypts and signs your data entries.

1. The cryptographic materials manager provides the AWS Database Encryption SDK with unique data encryption keys: one plaintext [data key](concepts.md#data-key), a copy of the data key encrypted by the specified [wrapping key](concepts.md#wrapping-key), and a MAC key.
**Note**
You can encrypt the data key under multiple wrapping keys. Each of the wrapping keys encrypt a separate copy of the data key. The AWS Database Encryption SDK stores all of the encrypted data keys in the [material description](concepts.md#material-description). The AWS Database Encryption SDK adds a new field (`aws_dbe_head`) to the record that stores the material description.
A MAC key is derived for each encrypted copy of the data key. The MAC keys are not stored in the material description. Instead, the decrypt method uses the wrapping keys to derive the MAC keys again.

1. The encryption method encrypts each field marked as `ENCRYPT_AND_SIGN` in the [cryptographic actions](concepts.md#crypt-actions) you specified.

1. The encryption method derives a `commitKey` from the data key and uses it to generate a [key commitment value](concepts.md#key-commitment), and then discards the data key.

1. The encryption method adds a [material description](concepts.md#material-description) to the record. The material description contains the encrypted data keys and the other information about the encrypted record. For a complete list of the information included in the material description, see [Material description format](reference.md#material-description-format).

1. The encryption method uses the MAC keys returned in **Step 1** to calculate Hash-Based Message Authentication Code (HMAC) values over the canonicalization of the material description, [encryption context](concepts.md#encryption-context), and each field marked `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` in the cryptographic actions. The HMAC values are stored in a new field (`aws_dbe_foot`) that the encryption method adds to the record.

1. The encryption method calculates an [ECDSA signature](concepts.md#digital-sigs) over the canonicalization of the material description, encryption context, and each field marked `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` and stores the ECDSA signatures in the `aws_dbe_foot` field.
**Note**
ECDSA signatures are enabled by default, but are not required.

1. The encryption method stores the encrypted and signed record in your database

## Decrypt and verify
<a name="decrypt-and-verify"></a>

1. The cryptographic materials manager (CMM) provides the decryption method with the decryption materials stored in the material description, including the plaintext [data key](concepts.md#data-key) and the associated MAC key.

   1. The CMM decrypts the encrypted data key with the [wrapping keys](concepts.md#wrapping-key) in the specified keyring and returns the plaintext data key.

1. The decryption method compares and verifies the key commitment value in the material description.

1. The decryption method verifies the signatures in the signature field.

   It identifies which fields are marked `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT` from the list of [allowed unauthenticated fields](ddb-java-using.md#allowed-unauth) that you defined. The decryption method uses the MAC key returned in **Step 1** to recalculate and compare HMAC values for the fields marked `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`. Then, it verifies the [ECDSA signatures](concepts.md#digital-sigs) using the public key stored in the [encryption context](concepts.md#encryption-context).

1. The decryption method uses the plaintext data key to decrypt each value marked `ENCRYPT_AND_SIGN`. The AWS Database Encryption SDK then discards the plaintext data key.

1. The decryption method returns the plaintext record.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
