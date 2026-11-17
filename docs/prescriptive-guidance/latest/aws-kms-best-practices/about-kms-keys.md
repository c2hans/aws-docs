---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-kms-best-practices/about-kms-keys.html
---

# About AWS KMS keys
<a name="about-kms-keys"></a>

AWS Key Management Service (AWS KMS) allows you to create cryptographic keys that can be used on data that you pass to the service. The primary resource type is the KMS key, of which there are [three types](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html):
+ **Advanced Encryption Standard (AES) symmetric keys** – These are 256-bit keys that you use with the Galois Counter Mode (GCM) of AES. These keys provide authenticated encryption and decryption of data that is up to 4096 bytes (4 KB) in size. This is the most common type of key. You can use it to protect other data keys, such as those used in your applications or by AWS services that encrypt data on your behalf.
+ **RSA or elliptic curve asymmetric keys** ­– These keys are available in various sizes and support many algorithms. Depending on the algorithm, they can be used for encryption and decryption and for sign and verify operations.
+ **Symmetric keys for performing hash-based message authentication code (HMAC) operations** – These keys are available in 224-bit, 256-bit, 384-bit, and 512-bit sizes and are used for generate and verify MAC operations.

KMS keys cannot be exported from the service in plaintext. The service's hardware security modules (HSMs) generate them, and you can use them only within those HSMs. This is a foundational security property of AWS KMS that helps protect against key compromise. In China (Beijing) and China (Ningxia) Regions, [OSCCA](https://www.oscca.gov.cn/) certifies these HSMs. In all other Regions, the HSMs used in AWS KMS are validated under the [FIPS 140-3 Cryptographic Module Validation Program](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/3739) at Security Level 3. For more information about design and controls in AWS KMS that help protect your keys, see [AWS Key Management Service Cryptographic Details](https://docs.aws.amazon.com/kms/latest/cryptographic-details/intro.html).

You can submit data to AWS KMS by using various cryptographic APIs to perform encrypt, decrypt, sign, or verify operations with KMS keys. You can also choose to have a KMS key act as a *key-encryption key*, which protects a key type called a *data key*. You can export a data key from AWS KMS for use within your local application or an AWS service that protects data on your behalf. The use of data keys is common in key management systems and is often referred to as [envelope encryption](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping). *Envelope encryption* lets you use a data key on the remote system that handles your sensitive data, instead of sending your sensitive data to AWS KMS for encryption directly under a KMS key.

For more information, see [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) and [AWS KMS cryptography essentials](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html) in the AWS KMS documentation.
