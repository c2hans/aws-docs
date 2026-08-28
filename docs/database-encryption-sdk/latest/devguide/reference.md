---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/reference.html
---

# Reference
<a name="reference"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

The following topics provide technical details for the AWS Database Encryption SDK.

## Material description format
<a name="material-description-format"></a>

The [material description](concepts.md#material-description) serves as the header for an encrypted record. When you encrypt and sign fields with the AWS Database Encryption SDK, the encryptor records the material description as it assembles the cryptographic materials and stores the material description in a new field (`aws_dbe_head`) that the encryptor adds to your record. The material description is a portable formatted data structure that contains the encrypted data key and information about how the record was encrypted and signed. The following table describes the values that form the material description. The bytes are appended in the order shown.

| Value | Length in bytes |
| --- | --- |
| [Version](#format-version) | 1 |
| [Signatures Enabled](#format-signatures) | 1 |
| [Record ID](#format-recordID) | 32 |
| [Encrypt Legend](#format-encrypt-legend) | Variable |
| [Encryption Context Length](#format-encrypt-context-length) | 2 |
| [Encryption Context](#format-encrypt-context) | Variable |
| [Encrypted Data Key Count](#format-data-key-count) | 1 |
| [Encrypted Data Keys](#format-data-keys) | Variable |
| [Record Commitment](#format-commitment) | 1 |

**Version**
The version of this `aws_dbe_head` field's format.

**Signatures Enabled**
Encodes whether ECDSA digital signatures are enabled for this record.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/reference.html)

**Record ID**
A randomly generated 256-bit value that identifies the record. The Record ID:
+ Uniquely identifies the encrypted record.
+ Binds the material description to the encrypted record.

**Encrypt Legend**
A serialized description of which authenticated fields were encrypted. The Encrypt Legend is used to determine what fields the decryption method should attempt to decrypt.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/reference.html)
The Encrypt Legend is serialized as follows:

1. Lexicographically by the byte sequence that represents their canonical path.

1. For each field, in order, append one of the byte values specified above to indicate whether that field should be encrypted.

**Encryption Context Length**
The length of the encryption context. It is a 2-byte value interpreted as a 16-bit unsigned integer. The maximum length is 65,535 bytes.

**Encryption Context**
A set of name-value pairs that contain arbitrary, non-secret additional authenticated data.
When [ECDSA digital signatures](concepts.md#digital-sigs) are enabled, the encryption context contains the key-value pair `{"aws-crypto-footer-ecdsa-key": Qtxt}`. `Qtxt` represents the elliptic curve point `Q` compressed according to [SEC 1 version 2.0](https://www.secg.org/sec1-v2.pdf) and then base64-encoded.

**Encrypted Data Key Count**
The number of encrypted data keys. It is a 1-byte value interpreted as a 8-bit unsigned integer that specifies the number of encrypted data keys. The maximum number of encrypted data keys in each record is 255.

**Encrypted Data Keys**
A sequence of encrypted data keys. The length of the sequence is determined by the number of encrypted data keys and the length of each. The sequence contains at least one encrypted data key.
The following table describes the fields that form each encrypted data key. The bytes are appended in the order shown.
**Encrypted Data Key Structure**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/reference.html)
**Key Provider ID Length**
The length of the key provider identifier. It is a 2-byte value interpreted as a 16-bit unsigned integer that specifies the number of bytes that contain the key provider ID.
**Key Provider ID**
The key provider identifier. It is used to indicate the provider of the encrypted data key and intended to be extensible.
**Key Provider Information Length**
The length of the key provider information. It is a 2-byte value interpreted as a 16-bit unsigned integer that specifies the number of bytes that contain the key provider information.
**Key Provider Information**
The key provider information. It is determined by the key provider.
When you are using an AWS KMS keyring, this value contains the Amazon Resource Name (ARN) of the AWS KMS key.
**Encrypted Data Key Length**
The length of the encrypted data key. It is a 2-byte value interpreted as a 16-bit unsigned integer that specifies the number of bytes that contain the encrypted data key.
**Encrypted Data Key**
The encrypted data key. It is the data key encrypted by the key provider.

**Record Commitment**
A distinct 256-bit Hash-Based Message Authentication Code (HMAC) hash calculated over all preceding material description bytes using the commit key.

## AWS KMS Hierarchical keyring technical details
<a name="hierarchical-keyring-details"></a>

The [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md) uses a unqiue data key to encrypt each field and encrypts each data key with a unique wrapping key derived from an active branch key. It uses a [key derivation](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-108r1.pdf) in counter mode with a pseudorandom function with HMAC SHA-256 to derive the 32 byte wrapping key with the following inputs.
+ A 16 byte random salt
+ The active branch key
+ The [UTF-8 encoded](https://en.wikipedia.org/wiki/UTF-8) value for the key provider identifier "aws-kms-hierarchy"

The Hierarchical keyring uses the derived wrapping key to encrypt a copy of the plaintext data key using AES-GCM-256 with a 16 byte authentication tag and the following inputs.
+ The derived wrapping key is used as the AES-GCM cipher key
+ The data key is used as the AES-GCM message
+ A 12 byte random initialization vector (IV) is used as the AES-GCM IV
+ Additional authenticated data (AAD) containing the following serialized values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/reference.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
