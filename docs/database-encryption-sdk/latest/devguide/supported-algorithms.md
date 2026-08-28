---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/supported-algorithms.html
---

# Supported algorithm suites in the AWS Database Encryption SDK
<a name="supported-algorithms"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

An *algorithm suite* is a collection of cryptographic algorithms and related values. Cryptographic systems use the algorithm implementation to generate the ciphertext.

The AWS Database Encryption SDK uses an algorithm suite to encrypt and sign the fields in your database. All supported algorithm suites use the Advanced Encryption Standard (AES) algorithm with Galois/Counter Mode (GCM), known as AES-GCM, to encrypt raw data. The AWS Database Encryption SDK supports 256-bit encryption keys. The length of the authentication tag is always 16 bytes.

**AWS Database Encryption SDK Algorithm Suites**

| Algorithm | Encryption algorithm | Data key length (in bits) | Key derivation algorithm | Symmetric signature algorithm | Asymmetric signature algorithm | Key commitment |
| --- | --- | --- | --- | --- | --- | --- |
| Default | AES-GCM | 256 | HKDF with SHA-512 | HMAC-SHA-384 | ECDSA with P-384 and SHA-384 | HKDF with SHA-512 |
| AES-GCM without ECDSA digital signatures | AES-GCM | 256 | HKDF with SHA-512 | HMAC-SHA-384 | None | HKDF with SHA-512 |

**Encryption algorithm**
The name and mode of the encryption algorithm used. Algorithm suites in the AWS Database Encryption SDK use the Advanced Encryption Standard (AES) algorithm with Galois/Counter Mode (GCM).

**Data key length**
The length of the [data key](concepts.md#data-key) in bits. The AWS Database Encryption SDK supports 256-bit data keys. The data key is used as input to an HMAC-based extract-and-expand key derivation function (HKDF). The output of the HKDF is used as the data encryption key in the encryption algorithm.

**Key derivation algorithm**
The HMAC-based extract-and-expand key derivation function (HKDF) used to derive the data encryption key. The AWS Database Encryption SDK uses the HKDF defined in [RFC 5869](https://tools.ietf.org/html/rfc5869).
+ The hash function used is SHA-512
+ For the extract step:
  + No salt is used. Per the RFC, the salt is set to a string of zeros.
  + The input keying material is the data key from the [keyring](concepts.md#keyring-concept).
+ For the expand step:
  + The input pseudorandom key is the output from the extract step.
  + The key label is the UTF-8-encoded bytes of the `DERIVEKEY` string in big endian byte order.
  + The input info is a concatenation of the algorithm ID and the key label (in that order).
  + The length of the output keying material is the **Data key length**. This output is used as the data encryption key in the encryption algorithm.

**Symmetric signature algorithm**
The Hash-Based Message Authentication Code (HMAC) algorithm used to generate a symmetric signature. All supported algorithm suites include HMAC verification.
The AWS Database Encryption SDK serializes the material description and all fields marked `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`. Then, it uses HMAC with a cryptographic hash function algorithm (SHA-384) to sign the canonicalization.
The symmetric HMAC signature is stored in a new field (`aws_dbe_foot`) that the AWS Database Encryption SDK adds to the record.

**Asymmetric signature algorithm**
The signature algorithm used to generate an asymmetric digital signature.
The AWS Database Encryption SDK serializes the material description and all fields marked `ENCRYPT_AND_SIGN`, `SIGN_ONLY`, or `SIGN_AND_INCLUDE_IN_ENCRYPTION_CONTEXT`. Then, it uses the Elliptic Curve Digital Signature Algorithm (ECDSA) with the following specifics to sign the canonicalization:
+ The elliptic curve used is the P-384, as defined in [Digital Signature Standard (DSS) (FIPS PUB 186-4)](http://doi.org/10.6028/NIST.FIPS.186-4).
+ The hash function used is SHA-384.
The asymmetric ECDSA signature is stored with the symmetric HMAC signature in the `aws_dbe_foot` field.
ECDSA digital signatures are included by default, but not required.

**Key commitment**
The HMAC-based extract-and-expand key derivation function (HKDF) used to derive the commit key.
+ The hash function used is SHA-512
+ For the extract step:
  + No salt is used. Per the RFC, the salt is set to a string of zeros.
  + The input keying material is the data key from the [keyring](concepts.md#keyring-concept).
+ For the expand step:
  + The input pseudorandom key is the output from the extract step.
  + The input info is the UTF-8-encoded bytes of the `COMMITKEY` string in big endian byte order.
  + The length of the output keying material is 256 bits. This output is used as the commit key.
The commit key calculates the [record commitment](reference.md#format-commitment), a distinct 256-bit Hash-Based Message Authentication Code (HMAC) hash, over the [material description](reference.md#material-description-format). For a technical explanation of adding key commitment to an algorithm suite, see [Key Committing AEADs](https://eprint.iacr.org/2020/1153) in Cryptology ePrint Archive.

## Default algorithm suite
<a name="recommended-algorithms"></a>

By default, the AWS Database Encryption SDK uses an algorithm suite with AES-GCM, an HMAC-based extract-and-expand key derivation function (HKDF), HMAC verification, ECDSA digital signatures, key commitment, and a 256-bit encryption key.

The default algorithm suite includes HMAC verification (symmetric signatures) and [ECDSA digital signatures](concepts.md#digital-sigs) (asymmetric signatures). These signatures are stored in a new field (`aws_dbe_foot`) that the AWS Database Encryption SDK adds to the record. ECDSA digital signatures are particularly useful when the authorization policy allows one set of users to encrypt data and a different set of users to decrypt data.

The default algorithm suite also derives a [key commitment](concepts.md#key-commitment) – an HMAC hash that ties the data key to the record. The key commitment value is an HMAC calculated from the material description and commit key. The key commitment value is then stored in the material description. Key commitment ensures that each ciphertext decrypts to only one plaintext. They do this by validating the data key used as input to the encryption algorithm. When encrypting, the algorithm suite derives a key commitment HMAC. Before decrypting, they validate that the data key produces the same key commitment HMAC. If it does not, the decrypt call fails.

## AES-GCM without ECDSA digital signatures
<a name="other-algorithms"></a>

Although the default algorithm suite is likely suitable for most applications, you can choose an alternate algorithm suite. For example, some trust models would be satisfied by an algorithm suite without ECDSA digital signatures. Use this suite only when the users who encrypt data and the users who decrypt data are equally trusted.

All AWS Database Encryption SDK algorithm suites include HMAC verification (symmetric signatures). The only difference, is that the AES-GCM algorithm suite without ECDSA digital signature lacks the asymmetric signature that provides an additional layer of authenticity and non-repudiation.

For example, if you have multiple wrapping keys in your keyring, `wrappingKeyA`, `wrappingKeyB`, and `wrappingKeyC`, and you decrypt a record using `wrappingKeyA`, the HMAC symmetric signature verifies that the record was encrypted by a user with access to `wrappingKeyA`. If you used the default algorithm suite, the HMACs provide the same verification of `wrappingKeyA`, and additionally use the ECDSA digital signature to ensure the record was encrypted by a user with encrypt permissions for `wrappingKeyA`.

To select the AES-GCM algorithm suite without digital signatures, include the following snippet in your encryption configuration.

------
#### [ Java ]

The following snippet specifies the AES-GCM algorithm suite without ECDSA digital signatures. For more information, see [Encryption configuration in the AWS Database Encryption SDK for DynamoDB](ddb-java-using.md#ddb-config-encrypt).

```
.algorithmSuiteId(
    DBEAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_SYMSIG_HMAC_SHA384)
```

------
#### [ C\# / .NET ]

The following snippet specifies the AES-GCM algorithm suite without ECDSA digital signatures. For more information, see [Encryption configuration in the AWS Database Encryption SDK for DynamoDB](ddb-net-using.md#ddb-net-config-encrypt).

```
AlgorithmSuiteId = DBEAlgorithmSuiteId.ALG_AES_256_GCM_HKDF_SHA512_COMMIT_KEY_SYMSIG_HMAC_SHA384
```

------
#### [ Rust ]

The following snippet specifies the AES-GCM algorithm suite without ECDSA digital signatures. For more information, see [Encryption configuration in the AWS Database Encryption SDK for DynamoDB](ddb-rust-using.md#ddb-rust-config-encrypt).

```
.algorithm_suite_id(
    DbeAlgorithmSuiteId::AlgAes256GcmHkdfSha512CommitKeyEcdsaP384SymsigHmacSha384,
)
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
