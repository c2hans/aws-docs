---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices-and-features-for-aws-services/aws-cryptography-services.html
---

# AWS approach to cryptography
<a name="aws-cryptography-services"></a>

*Cryptographic algorithms *are mathematical constructions designed to provide security services like confidentiality (encryption), authenticity (message authentication codes and digital signatures), and non-repudiation (digital signatures). If you are new to cryptography, encryption, and related terminology, read [About data encryption](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/about-data-encryption.html) before you proceed with this guide.

## AWS cryptographic foundations
<a name="foundations"></a>

Cryptography is an essential part of security for AWS. AWS services support encryption for data in transit, at rest, or in memory. To learn more about the AWS commitment to innovating and investing in additional controls for sovereignty and encryption features, see the blog post [AWS Digital Sovereignty Pledge: Control without compromise](https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/).

AWS follows the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) to help you protect your data. AWS services use trusted cryptographic algorithms that meet industry standards and foster interoperability. Public standards bodies and academic research vet these algorithms. Governments, industry, and academia widely accept the associated standards.

AWS defaults to high-assurance cryptographic implementations and prefers efficient, hardware-optimized solutions. The AWS cryptographic core library, AWS-LC, is available as open source ([AWS-LC repository on GitHub](https://github.com/aws/aws-lc)) for transparency and industry-wide reuse. AWS formally verifies the recommended cryptographic algorithms in AWS-LC for correctness. The library is also validated under the National Institute of Standards and Technology (NIST) Federal Information Processing Standard (FIPS) 140 program.

## Cryptographic algorithms
<a name="about-algorithms"></a>

We define three types of cryptographic algorithms:
+

## Recommended cryptographic algorithms in AWS
<a name="algorithms"></a>

The following tables summarize the cryptographic algorithms, modes, and key sizes that AWS considers suitable for deployment across its services to help protect your data. This guidance will evolve as cryptographic standards evolve.

Algorithms available within services vary. See the documentation for each service for details. If you need a software library implementation for an approved algorithm, check whether the latest version of the [AWS-LC library](https://github.com/aws/aws-lc) includes it.

Algorithms are approved for use in AWS under one of two categories:
+ Preferred algorithms meet the AWS security and performance standards.
+ You can use acceptable algorithms for compatibility in some applications, but they are not preferred.

### Asymmetric cryptography
<a name="asymmetric-cryptography.6403f4f8-a7aa-55aa-a19e-02da1d417f7c"></a>

The following table lists asymmetric algorithms considered suitable for use within AWS for encryption, key agreement, and digital signatures.

|  |  |  |
| --- |--- |--- |
| Type | Algorithm | Status |
| Encryption | RSA-OAEP (≥2048-bit modulus) | Acceptable |
| Encryption | HPKE (P-256 or P-384, HKDF and AES-GCM) | Acceptable |
| Key agreement | ML-KEM-768 or ML-KEM-1024 | Preferred (quantum-resistant) |
| Key agreement | ML-KEM-768 | Acceptable (quantum-resistant) |
| Key agreement | ECDH(E) with P-256, P-384, P-521, or XEd25519 | Acceptable |
| Key agreement | ECDH(E) with brainpoolP256r1, brainpoolP384r1, or brainpoolP512r1 | Acceptable |
| Signatures | ML-DSA-65 or ML-DSA-87 | Preferred (quantum-resistant) |
| Signatures | ML-DSA-44 or ML-DSA-65 | Acceptable (quantum-resistant) |
| Signatures | SLH-DSA (all parameters) | Acceptable (quantum-resistant) |
| Signatures | ECDSA with P-384 | Acceptable |
| Signatures | ECDSA with P-256, P-521, or Ed25519 | Acceptable |
| Signatures | RSA (≥2048-bit modulus) | Acceptable |

### Symmetric cryptography
<a name="symmetric-cryptography.f8984a79-e182-58eb-9b07-922bb8e7225a"></a>

The following table lists symmetric algorithms considered suitable for use within AWS for encryption, authenticated encryption, and key wrapping.

|  |  |  |
| --- |--- |--- |
| Type | Algorithm | Status |
| Authenticated encryption | AES-GCM-256 | Preferred |
| Authenticated encryption | AES-GCM-128 | Acceptable |
| Authenticated encryption | ChaCha20/Poly1305 | Acceptable |
| Encryption modes | AES-XTS-256 (only for block storage) | Preferred |
| Encryption modes | AES-CBC / CTR (unauthenticated modes) | Acceptable |
| Key wrapping | AES-GCM-256 | Preferred |
| Key wrapping | AES-KW or AES-KWP with 256-bit keys | Acceptable |

### Other cryptographic functions
<a name="other-cryptographic-functions.61ed554e-2d62-5b46-857c-be9dc9e29c26"></a>

The following table lists algorithms considered suitable for use within AWS for hashing, key derivation, and message authentication.

|  |  |  |
| --- |--- |--- |
| Type | Algorithm | Status |
| Hashing | SHA-384 | Preferred |
| Hashing | SHA-256 | Acceptable |
| Hashing | SHA-3 | Acceptable |
| Key derivation | HKDF\_Expand or HKDF with SHA-256 | Preferred |
| Key derivation | Counter Mode KDF with HMAC-SHA-256 | Acceptable |
| Message authentication code | HMAC-SHA-384 | Preferred |
| Message authentication code | HMAC-SHA-256 | Acceptable |
| Message authentication code | KMAC | Acceptable |
| Password hashing | scrypt with SHA-384 | Preferred |
| Password hashing | PBKDF2 | Acceptable |

## Cryptography used in AWS services
<a name="used-services"></a>

### Cryptography Used in AWS Services
<a name="cryptography-used-in-aws-services.ef3ecb12-7213-5214-b649-6d7ce45455a2"></a>

AWS services use open-source implementations of vetted algorithms to help you protect your data. The algorithms and configurations vary by service. Some AWS tools and services use a specific algorithm. For others, you can choose between supported algorithms and key lengths, or you can use the recommended defaults.

AWS cryptographic services support a wide range of cryptographic security standards, which can help you meet governmental or industry regulations. For a full list of the compliance programs that cover AWS services, see [AWS compliance programs](https://aws.amazon.com/compliance/programs/). To learn more about how to build your data protection strategy in AWS, see the data protection guide.
