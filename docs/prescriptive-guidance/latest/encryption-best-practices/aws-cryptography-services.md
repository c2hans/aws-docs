---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/aws-cryptography-services.html
---

# AWS approach to cryptography
<a name="aws-cryptography-services"></a>

*Cryptographic algorithms *are mathematical constructions designed to provide security services like confidentiality (encryption), authenticity (message authentication codes and digital signatures) and non-repudiation (digital signatures). If you are new to cryptography, encryption, and related terminology, we recommend that you read [About data encryption](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/about-data-encryption.html) before proceeding with this guide.

## AWS cryptographic foundations
<a name="foundations"></a>

Cryptography is an essential part of security for AWS. AWS services support encryption for data in transit, at rest, or in memory.  You can learn more about the AWS commitment to innovation and investing in additional controls for sovereignty and encryption features in our blog post announcing the [AWS digital sovereignty pledge](https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/).

AWS follows the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) to protect your data. AWS services use trusted cryptographic algorithms that meet industry standards and foster interoperability. These algorithms are vetted by public standards bodies and academic research. The associated standards are widely accepted by governments, industry, and academia.

AWS defaults to high-assurance cryptographic implementations and prefers hardware-optimized solutions that are efficient. Our cryptographic core library, [AWS-LC](https://github.com/aws/aws-lc), is available as open source for transparency and industry-wide reuse. The recommended cryptographic algorithms in AWS-LC are formally verified for correctness, and the library is validated under NIST's FIPS-140 program.

## Cryptographic algorithms
<a name="about-algorithms"></a>

We define three types of cryptographic algorithms:
+ *Asymmetric* *cryptography* uses a pair of keys: a public key for encryption (or verifying) and a private key for decryption (or signing). You can share the public key because it isn't used for decryption, but access to the private key should be highly restricted. AWS services support or plan to support post-quantum algorithms, such as ML-KEM and ML-DSA. AWS services also support traditional cryptographic algorithms, such as RSA and elliptic-curve cryptography (ECC).
+ *Symmetric* *cryptography* uses the same key to encrypt and decrypt, or authenticate and verify the data. AWS services generally integrate with AWS Key Management Service (AWS KMS) for encryption of data at rest, which uses a mode of AES-256.
+ *Other cryptographic functions* are used in conjunction with asymmetric and symmetric cryptography to build secure, practical protocols for confidentiality, integrity, authentication, and non-repudiation applications. Examples include hash functions and key derivation functions.

## Recommended cryptographic algorithms in AWS
<a name="algorithms"></a>

The following tables summarize the cryptographic algorithms, modes, and key sizes that AWS considers suitable for deployment across its services to protect your data. This guidance will evolve over time as cryptographic standards evolve.

Algorithms available within services can vary and are explained in the documentation for each service. If you need a software library implementation for an approved algorithm, please check to see if it is included in the latest version of the [AWS-LC library](https://github.com/aws/aws-lc).

Algorithms are approved for use in AWS under one of two categories:
+ *Preferred* algorithms meet the AWS security and performance standards.
+ *Acceptable* algorithms can be used for compatibility in some applications but are not preferred.

### Asymmetric cryptography
<a name="asymmetric-cryptography.bf5b1ec4-10bc-54db-9c8b-9a357ea882ca"></a>

The following table lists asymmetric algorithms considered suitable for use within AWS for encryption, key agreement, and digital signatures.

|
|
| **Type** | **Algorithm** | **Status** |
| --- |--- |--- |
| Encryption | RSA-OAEP (≥2048-bit modulus) | Acceptable |
| Encryption | HPKE (P-256 or P-384, HKDF and AES-GCM) | Acceptable |
| Key agreement | ML-KEM-768 or ML-KEM-1024 | Preferred (quantum-resistant) |
| Key agreement | ECDSA with P-256, P-384, P-521, or Ed25519 | Acceptable |
| Key agreement | ECDH(E) with brainpoolP256r1, brainpoolP384r1, or brainpoolP512r1 | Acceptable |
| Signatures | ML-DSA-65 or ML-DSA-87 | Preferred (quantum-resistant) |
| Signatures | SLH-DSA | Acceptable (quantum-resistant) |
| Signatures | ECDSA with P-384 | Acceptable |
| Signatures | ECDSA with P-256, P-521, or Ed25519 | Acceptable |
| Signatures | RSA (≥2048-bit modulus) | Acceptable |

### Symmetric cryptography
<a name="symmetric-cryptography.7cb55a3e-eecb-5f61-82b7-4faa705ac662"></a>

The following table lists symmetric algorithms considered suitable for use within AWS for encryption, authenticated encryption, and key wrapping.

|
|
| **Type** | **Algorithm** | **Status** |
| --- |--- |--- |
| Authenticated encryption | AES-GCM-256 | Preferred |
| Authenticated encryption | AES-GCM-128 | Acceptable |
| Authenticated encryption | ChaCha20/Poly1305 | Acceptable |
| Encryption modes | AES-XTS-256 (for block storage) | Preferred |
| Encryption modes | AES-CBC / CTR (unauthenticated modes) | Acceptable |
| Key wrapping | AES-GCM-256 | Preferred |
| Key wrapping | AES-KW or AES-KWP with 256-bit keys | Acceptable |

### Other cryptographic functions
<a name="other-cryptographic-functions.f1580287-815e-5157-9e15-9a2ca3d80bfa"></a>

The following table lists algorithms considered suitable for use within AWS for hashing, key derivation, and message authentication.

|
|
| **Type** | **Algorithm** | **Status** |
| --- |--- |--- |
| Hashing | SHA-384 | Preferred |
| Hashing | SHA-256 | Acceptable |
| Hashing | SHA3 | Acceptable |
| Key derivation | HKDF\_Expand or HKDF with SHA-256 | Preferred |
| Key derivation | Counter Mode KDF with HMAC-SHA-256 | Acceptable |
| Message authentication code | HMAC-SHA-384 | Preferred |
| Message authentication code | HMAC-SHA-256 | Acceptable |
| Message authentication code | KMAC | Acceptable |
| Password hashing | scrypt with SHA384 | Preferred |
| Password hashing | PBKDF2 | Acceptable |

## Cryptography used in AWS services
<a name="used-services"></a>

AWS services rely on secure, open-source implementations of vetted algorithms to protect your data. The specific choices and configurations of algorithms will vary by service. Some AWS tools and services use a specific algorithm. In others, you can choose between supported algorithms and key lengths, or you can use the recommended defaults.

AWS cryptographic services comply with a wide range of cryptographic security standards, so you can comply with governmental or industry regulations. For a full list of the data security standards that AWS services comply with, see [AWS compliance programs](https://aws.amazon.com/compliance/programs/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
