---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/about-versions.html
---

# Versions of the AWS Encryption SDK
<a name="about-versions"></a>

The AWS Encryption SDK language implementations use [semantic versioning](https://semver.org/) to make it easier for you to identify the magnitude of changes in each release. A change in the major version number, such as 1.*x*.*x* to 2.*x*.*x*, indicates a breaking change that is likely to require code changes and a planned deployment. Breaking changes in a new version might not impact every use case, review the release notes to see if you're impacted. A change in a minor version, such as *x*.1.*x* to *x*.2.*x*, is always backward compatible, but might include deprecated elements.

Whenever possible, use the latest version of the AWS Encryption SDK in your chosen programming language. The [maintenance and support policy](introduction.md#support) for each version differs between programming language implementations. For details about the supported versions in your preferred programming language, see the `SUPPORT_POLICY.rst` file in its [GitHub repository](introduction.md#esdk-repos).

When upgrades include new features that require special configuration to avoid encryption or decryption error, we provide an intermediate version and detailed instructions for using it. For example, versions 1.7.*x* and 1.8.*x* are designed to be transitional versions that help you upgrade from versions earlier than 1.7.*x* to versions 2.0.*x* and later. For details, see [Migrating your AWS Encryption SDK](migration.md).

**Note**
The *x* in a version number represents any patch of the major and minor version. For example, version 1.7.*x* represents all versions that begin with 1.7, including 1.7.1 and 1.7.9.
New security features were originally released in AWS Encryption CLI versions 1.7.*x* and 2.0.*x*. However, AWS Encryption CLI version 1.8.*x* replaces version 1.7.*x* and AWS Encryption CLI 2.1.*x* replaces 2.0.*x*. For details, see the relevant [security advisory](https://github.com/aws/aws-encryption-sdk-cli/security/advisories/GHSA-2xwp-m7mq-7q3r) in the [aws-encryption-sdk-cli](https://github.com/aws/aws-encryption-sdk-cli/) repository on GitHub.

The following tables provide an overview of the major differences between supported versions of the AWS Encryption SDK for each programming language.

## C
<a name="esdk-c-versions"></a>

For a detailed description of all changes, see the [CHANGELOG.md](https://github.com/aws/aws-encryption-sdk-c/blob/master/CHANGELOG.md) in the [aws-encryption-sdk-c](https://github.com/aws/aws-encryption-sdk-c/) repository on GitHub.

|
|
| **Major version** | **Details** | **SDK major version life-cycle phase** |
| --- |--- |--- |
| 1.x | 1.0 | Initial release. | [End-of-Support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) |
| 1.7 | Updates to the AWS Encryption SDK that help users of earlier versions upgrade to versions 2.0.x and later. For more information, see [version 1.7.*x*](#version-1.7). |
| 2.x | 2.0 | Updates to the AWS Encryption SDK. For more information, see [version 2.0.*x*](#version-2). | [General Availability](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) (GA) |
| 2.2 | Improvements to the message decryption process. |
| 2.3 | Adds support for AWS KMS multi-Region keys. |

## C\# / .NET
<a name="esdk-dot-net-versions"></a>

For a detailed description of all changes, see the [CHANGELOG.md](https://github.com/aws/aws-encryption-sdk/tree/mainline/AwsEncryptionSDK/runtimes/net/CHANGELOG.md) in the [https://github.com/aws/aws-encryption-sdk/tree/mainline/AwsEncryptionSDK/runtimes/net/](https://github.com/aws/aws-encryption-sdk/tree/mainline/AwsEncryptionSDK/runtimes/net/) repository on GitHub.

|
|
| **Major version** | **Details** | **SDK major version life-cycle phase** |
| --- |--- |--- |
| 3.x | 3.1.0 | Initial release. | [End-of-Support](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) <br />[Version 3.x of the AWS Encryption SDK for .NET](https://www.nuget.org/packages/AWS.EncryptionSDK) has entered End of Support; please, [upgrade to 4.x.](https://www.nuget.org/packages/AWS.Cryptography.EncryptionSDK) |
| 4.x | 4.0 | Adds support for the AWS KMS Hierarchical keyring, the required encryption context CMM, and asymmetric RSA AWS KMS keyrings. | [General Availability](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) (GA) |
| 5.x | 5.0 | Updates to version 2.x of the Material Providers Library (MPL). Drops support for the AWS SDK for .NET v3 and requires the AWS SDK for .NET v4. | [General Availability](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) (GA) |

## Command line interface (CLI)
<a name="esdk-cli-versions"></a>

For a detailed description of all changes, see [Versions of the AWS Encryption CLI](crypto-cli-versions.md) and the [CHANGELOG.rst](https://github.com/aws/aws-encryption-sdk-cli/blob/master/CHANGELOG.rst) in the [aws-encryption-sdk-cli](https://github.com/aws/aws-encryption-sdk-cli/) repository on GitHub.

|
|
| **Major version** | **Details** | **SDK major version life-cycle phase** |
| --- |--- |--- |
| 1.x | 1.0 | Initial release. | [End-of-Support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) |
| 1.7 | Updates to the AWS Encryption SDK that help users of earlier versions upgrade to versions 2.0.x and later. For more information, see [version 1.7.*x*](#version-1.7). |
| 2.x | 2.0 | Updates to the AWS Encryption SDK. For more information, see [version 2.0.*x*](#version-2). | [End-of-Support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) |
| 2.1 | Removes the `--discovery` parameter and replaces it with the `discovery` attribute of the `--wrapping-keys` parameter.<br />Version 2.1.0 of the AWS Encryption CLI is equivalent to version 2.0 in other programming languages. |
| 2.2 | Improvements to the message decryption process. |
| 3.x | 3.0 | Adds support for AWS KMS multi-Region keys. | [End-of-Support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) |
| 4.x | 4.0 | The AWS Encryption CLI no longer supports Python 2 or Python 3.4. As of major version 4.x of the AWS Encryption CLI, only Python 3.5 or later is supported. | [General Availability](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) (GA) |
| 4.1 | The AWS Encryption CLI no longer supports Python 3.5. As of version 4.1.x of the AWS Encryption CLI, only Python 3.6 or later is supported. |
| 4.2 | The AWS Encryption CLI no longer supports Python 3.6. As of version 4.2.x of the AWS Encryption CLI, only Python 3.7 or later is supported. |

## Java
<a name="esdk-java-versions"></a>

For a detailed description of all changes, see the [CHANGELOG.rst](https://github.com/aws/aws-encryption-sdk-java/blob/master/CHANGELOG.md) in the [aws-encryption-sdk-java](https://github.com/aws/aws-encryption-sdk-java/) repository on GitHub.

|
|
| **Major version** | **Details** | **SDK major version life-cycle phase** |
| --- |--- |--- |
| 1.x | 1.0 | Initial release. | [End-of-Support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) |
| 1.3 | Adds support for cryptographic materials manager and data key caching. Moved to deterministic IV generation. |
| 1.6.1 | Deprecates `AwsCrypto.encryptString()` and `AwsCrypto.decryptString()` and replaces them with `AwsCrypto.encryptData()` and `AwsCrypto.decryptData()`. |
| 1.7 | Updates to the AWS Encryption SDK that help users of earlier versions upgrade to versions 2.0.x and later. For more information, see [version 1.7.*x*](#version-1.7). |
| 2.x | 2.0 | Updates to the AWS Encryption SDK. For more information, see [version 2.0.*x*](#version-2). | [General Availability](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) (GA)<br />Version 2.x of the AWS Encryption SDK for Java will enter maintenance mode in 2024. |
| 2.2 | Improvements to the message decryption process. |
| 2.3 | Adds support for AWS KMS multi-Region keys. |
| 2.4 | Adds support for AWS SDK for Java 2.x. |
| 3.x | 3.0 | Integrates the AWS Encryption SDK for Java with the [Material Providers Library](https://github.com/aws/aws-cryptographic-material-providers-library) (MPL).<br />Adds support for symmetric and asymmetric RSA AWS KMS keyrings, AWS KMS ECDH keyrings, AWS KMS Hierarchical keyrings, Raw AES keyrings, Raw RSA keyrings, Raw ECDH keyrings, Multi-keyrings, and the required encryption context CMM. | [General Availability](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) (GA) |

## Go
<a name="esdk-go-versions"></a>

For a detailed description of all changes, see the [CHANGELOG.md](https://github.com/aws/aws-encryption-sdk/tree/mainline/releases/go/encryption-sdk/CHANGELOG.md) in the Go directory of the [aws-encryption-sdk](https://github.com/aws/aws-encryption-sdk/tree/mainline) repository on GitHub.

|
|
| **Major version** | **Details** | **SDK major version life-cycle phase** |
| --- |--- |--- |
| 0.1.x | 0.1.0 | Initial release. | [General Availability](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) (GA) |

## JavaScript
<a name="esdk-javascript-versions"></a>

For a detailed description of all changes, see the [CHANGELOG.md](https://github.com/aws/aws-encryption-sdk-javascript/blob/master/CHANGELOG.md) in the [aws-encryption-sdk-javascript](https://github.com/aws/aws-encryption-sdk-javascript/tree/master/modules) repository on GitHub.

|
|
| **Major version** | **Details** | **SDK major version life-cycle phase** |
| --- |--- |--- |
| 1.x | 1.0 | Initial release. | [End-of-Support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) |
| 1.7 | Updates to the AWS Encryption SDK that help users of earlier versions upgrade to versions 2.0.x and later. For more information, see [version 1.7.*x*](#version-1.7). |
| 2.x | 2.0 | Updates to the AWS Encryption SDK. For more information, see [version 2.0.*x*](#version-2). | [End-of-Support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) |
| 2.2 | Improvements to the message decryption process. |
| 2.3 | Adds support for AWS KMS multi-Region keys. |
| 3.x | 3.0 | Removes CI coverage for Node 10. Upgrades dependencies to no longer support Node 8 and Node 10. | [Maintenance](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle)<br />Support for version 3.x of the AWS Encryption SDK for JavaScript will end on January 17, 2024. |
| 4.x | 4.0 | Requires version 3 of the AWS Encryption SDK for JavaScript's kms-client to use the AWS KMS keyring. | [General Availability](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) (GA) |

## Python
<a name="esdk-python-versions"></a>

For a detailed description of all changes, see the [CHANGELOG.rst](https://github.com/aws/aws-encryption-sdk-python/blob/master/CHANGELOG.rst) in the [aws-encryption-sdk-python](https://github.com/aws/aws-encryption-sdk-python/) repository on GitHub.

|
|
| **Major version** | **Details** | **SDK major version life-cycle phase** |
| --- |--- |--- |
| 1.x | 1.0 | Initial release. | [End-of-Support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) |
| 1.3 | Adds support for cryptographic materials manager and data key caching. Moved to deterministic IV generation. |
| 1.7 | Updates to the AWS Encryption SDK that help users of earlier versions upgrade to versions 2.0.x and later. For more information, see [version 1.7.*x*](#version-1.7). |
| 2.x | 2.0 | Updates to the AWS Encryption SDK. For more information, see [version 2.0.*x*](#version-2). | [End-of-Support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) |
| 2.2 | Improvements to the message decryption process. |
| 2.3 | Adds support for AWS KMS multi-Region keys. |
| 3.x | 3.0 | The AWS Encryption SDK for Python no longer supports Python 2 or Python 3.4. As of major version 3.x of the AWS Encryption SDK for Python, only Python 3.5 or later is supported. | [General Availability](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) (GA) |
| 4.x | 4.0 | Integrates the AWS Encryption SDK for Python with the [Material Providers Library](https://github.com/aws/aws-cryptographic-material-providers-library) (MPL). | [General Availability](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) (GA) |

## Rust
<a name="esdk-rust-versions"></a>

For a detailed description of all changes, see the [CHANGELOG.md](https://github.com/aws/aws-encryption-sdk-dafny/tree/mainline/AwsEncryptionSDK/runtimes/rust/CHANGELOG.md) in the Rust directory of the [aws-encryption-sdk](https://github.com/aws/aws-encryption-sdk/tree/mainline) repository on GitHub.

|
|
| **Major version** | **Details** | **SDK major version life-cycle phase** |
| --- |--- |--- |
| 1.x | 1.0 | Initial release. | [General Availability](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) (GA) |

## Version details
<a name="version-details"></a>

The following list describes the major differences between supported versions of the AWS Encryption SDK.

**Topics**
+ [Versions earlier than 1.7.*x*](#versions-earlier)
+ [Version 1.7.*x*](#version-1.7)
+ [Version 2.0.*x*](#version-2)
+ [Version 2.2.*x*](#version2.2.x)
+ [Version 2.3.*x*](#version2.3)

### Versions earlier than 1.7.*x*
<a name="versions-earlier"></a>

**Note**
All 1.*x*.*x* versions of the AWS Encryption SDK are in the [end-of-support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle). Upgrade to the latest available version of the AWS Encryption SDK for your programming language as soon as is practical. To upgrade from an AWS Encryption SDK version earlier than 1.7.*x*, you must first upgrade to 1.7.*x*. For details, see [Migrating your AWS Encryption SDK](migration.md).

Versions of the AWS Encryption SDK earlier than 1.7.*x* provide important security features, including encryption with the Advanced Encryption Standard algorithm in Galois/Counter Mode (AES-GCM), an HMAC-based extract-and-expand key derivation function (HKDF), signing, and a 256-bit encryption key. However, these versions don't support [best practices](best-practices.md) that we recommend, including [key commitment](concepts.md#key-commitment).

### Version 1.7.*x*
<a name="version-1.7"></a>

**Note**
All 1.*x*.*x* versions of the AWS Encryption SDK are in the [end-of-support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle).

Version 1.7.*x* is designed to help users of earlier versions of the AWS Encryption SDK to upgrade to versions 2.0.*x* and later. If you are new to the AWS Encryption SDK, you can skip this version and begin with the latest available version in your programming language.

Version 1.7.*x* is fully backward compatible; it does not introduce any breaking changes or change the behavior of the AWS Encryption SDK. It's also forwards compatible; it allows you to update your code so it's compatible with version 2.0.*x*. It includes new features, but doesn't fully enable them. And it requires configuration values that prevent you from immediately adopting all new features until you are ready.

Version 1.7.*x* includes the following changes:

**AWS KMS master key provider updates (required)**  <a name="changes-to-mkps"></a>
Version 1.7.*x* introduces new constructors to the AWS Encryption SDK for Java and AWS Encryption SDK for Python that explicitly create AWS KMS master key providers in either *strict* or *discovery* mode. This version adds similar changes to the AWS Encryption SDK command-line interface (CLI). For details, see [Updating AWS KMS master key providers](migrate-mkps-v2.md).
+ In *strict mode*, AWS KMS master key providers require a list of wrapping keys, and they encrypt and decrypt with only the wrapping keys you specify. This is an AWS Encryption SDK best practice that assures that you are using the wrapping keys you intend to use.
+ In *discovery mode*, AWS KMS master key providers do not take any wrapping keys. You cannot use them for encrypting. When decrypting, they can use any wrapping key to decrypt an encrypted data key. However, you can limit the wrapping keys used for decryption to those in particular AWS accounts. Account filtering is optional, but it's a [best practice](best-practices.md) that we recommend.
The constructors that create earlier versions of AWS KMS master key providers are deprecated in version 1.7.*x* and removed in version 2.0.*x*. These constructors instantiate master key providers that encrypt using the wrapping keys you specify. However, they decrypt encrypted data keys using the wrapping key that encrypted them, without regard to the specified wrapping keys. Users might unintentionally decrypt messages with wrapping keys they don't intend to use, including AWS KMS keys in other AWS accounts and Regions.
There are no changes to constructors for AWS KMS master keys. When encrypting and decrypting, AWS KMS master keys use only the AWS KMS key that you specify.

**AWS KMS keyring updates (optional)**
Version 1.7.*x* adds a new filter to the AWS Encryption SDK for C and AWS Encryption SDK for JavaScript implementations that limits [AWS KMS discovery keyrings](use-kms-keyring.md#kms-keyring-discovery) to particular AWS accounts. This new account filter is optional, but it's a [best practice](best-practices.md) that we recommend. For details, see [Updating AWS KMS keyrings](migrate-keyrings-v2.md).
There are no changes to constructors for AWS KMS keyrings. Standard AWS KMS keyrings behave like master key providers in strict mode. AWS KMS discovery keyrings are created explicitly in discovery mode.

**Passing a key ID to AWS KMS Decrypt**
Beginning in version 1.7.*x*, when decrypting encrypted data keys, the AWS Encryption SDK always specifies an AWS KMS key in its calls to the AWS KMS [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) operation. The AWS Encryption SDK gets the key ID value for the AWS KMS key from the metadata in each encrypted data key. This feature doesn't require any code changes.
Specifying the key ID of the AWS KMS key is not required to decrypt ciphertext that was encrypted under a symmetric encryption KMS key, but it is an [AWS KMS best practice](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html#KMS-Decrypt-request-KeyId). Like specifying wrapping keys in your key provider, this practice assures that AWS KMS only decrypts using the wrapping key you intend to use.

**Decrypt ciphertext with key commitment**
Version 1.7.*x* can decrypt ciphertext that was encrypted with or without [key commitment](concepts.md#key-commitment). However, it cannot encrypt ciphertext with key commitment. This property allows you to fully deploy applications that can decrypt ciphertext encrypted with key commitment before they ever encounter any such ciphertext. Because this version decrypts messages that are encrypted without key commitment, you don't need to re-encrypt any ciphertext.
To implement this behavior, version 1.7.*x* includes a new [commitment policy](concepts.md#commitment-policy) configuration setting that determines whether the AWS Encryption SDK can encrypt or decrypt with key commitment. In version 1.7.*x*, the only valid value for the commitment policy, `ForbidEncryptAllowDecrypt`, is used in all encrypt and decrypt operations. This value prevents the AWS Encryption SDK from encrypting with either of the new algorithm suites that include key commitment. It allows the AWS Encryption SDK to decrypt ciphertext with and without key commitment.
Although there is only one valid commitment policy value in version 1.7.*x*, we require that you can set this value explicitly when you use the new APIs introduced in this release. Setting the value explicitly prevents your commitment policy from changing automatically to `require-encrypt-require-decrypt` when you upgrade to version 2.1.*x*. Instead, you can [migrate your commitment policy](migrate-commitment-policy.md) in stages.

**Algorithm suites with key commitment**
Version 1.7.*x* includes two new [algorithm suites](supported-algorithms.md) that support key commitment. One includes signing; the other does not. Like earlier supported algorithm suites, both of these new algorithm suites include encryption with AES-GCM, a 256-bit encryption key, and an HMAC-based extract-and-expand key derivation function (HKDF).
However, the default algorithm suite used for encryption does not change. These algorithm suites are added to version 1.7.*x* to prepare your application to use them in versions 2.0.*x* and later.

**CMM implementation changes**
Version 1.7.*x* introduces changes to the Default cryptographic materials manager (CMM) interface to support key commitment. This change affects you only if you have written a custom CMM. For details, see the API documentation or GitHub repository for your [programming language](programming-languages.md).

### Version 2.0.*x*
<a name="version-2"></a>

Version 2.0.*x* supports new security features offered in the AWS Encryption SDK, including specified wrapping keys and key commitment. To support these features, version 2.0.*x* includes breaking changes for earlier versions of the AWS Encryption SDK. You can prepare for these changes by deploying version 1.7.*x*. Version 2.0.*x* includes all of the new features introduced in version 1.7.*x* with the following additions and changes.

**Note**
Version 2.*x*.*x* of the AWS Encryption SDK for Python, AWS Encryption SDK for JavaScript, and the AWS Encryption CLI are in the [end-of-support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle).
For information about [support and maintenance](introduction.md#support) of this AWS Encryption SDK version in your preferred programming language, see the `SUPPORT_POLICY.rst` file in its [GitHub repository](introduction.md#esdk-repos).

**AWS KMS master key providers**
The original AWS KMS master key provider constructors that were deprecated in version 1.7.*x* are removed in version 2.0.*x*. You must explicitly construct AWS KMS master key providers in [strict mode or discovery mode](migrate-mkps-v2.md).

**Encrypt and decrypt ciphertext with key commitment**
Version 2.0.*x* can encrypt and decrypt ciphertext with or without [key commitment](concepts.md#key-commitment). Its behavior is determined by the commitment policy setting. By default, it always encrypts with key commitment and only decrypts ciphertext encrypted with key commitment. Unless you change the commitment policy, the AWS Encryption SDK will not decrypt ciphertexts encrypted by any earlier version of the AWS Encryption SDK, including version 1.7.*x*.
By default, version 2.0.*x* will not decrypt any ciphertext that was encrypted without key commitment. If your application might encounter a ciphertext that was encrypted without key commitment, set a commitment policy value with `AllowDecrypt`.
In version 2.0.*x*, the commitment policy setting has three valid values:
+ `ForbidEncryptAllowDecrypt` — The AWS Encryption SDK cannot encrypt with key commitment. It can decrypt ciphertexts encrypted with or without key commitment.
+ `RequireEncryptAllowDecrypt` — The AWS Encryption SDK must encrypt with key commitment. It can decrypt ciphertexts encrypted with or without key commitment.
+ `RequireEncryptRequireDecrypt` (default) — The AWS Encryption SDK must encrypt with key commitment. It only decrypts ciphertexts with key commitment.
If you are migrating from an earlier version of the AWS Encryption SDK to version 2.0.*x*, set the commitment policy to a value that assures that you can decrypt all existing ciphertexts that your application might encounter. You are likely to adjust this setting over time.

### Version 2.2.*x*
<a name="version2.2.x"></a>

Adds support for digital signatures and limiting encrypted data keys.

**Note**
Version 2.*x*.*x* of the AWS Encryption SDK for Python, AWS Encryption SDK for JavaScript, and the AWS Encryption CLI are in the [end-of-support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle).
For information about [support and maintenance](introduction.md#support) of this AWS Encryption SDK version in your preferred programming language, see the `SUPPORT_POLICY.rst` file in its [GitHub repository](introduction.md#esdk-repos).

**Digital signatures**
To improve handling of [digital signatures](concepts.md#digital-sigs) when decrypting, the AWS Encryption SDK includes the following features:
+ *Non-streaming mode* — returns plaintext only after processing all input, including verifying the digital signature if present. This feature prevents you from using plaintext before verifying the digital signature. Use this feature whenever you decrypt data encrypted with digital signatures (the default algorithm suite). For example, because the AWS Encryption CLI always processes data in streaming mode, use the `- -buffer` parameter when decrypting ciphertext with digital signatures.
+ *Unsigned-only decryption mode* — this feature only decrypts unsigned ciphertext. If decryption encounters a digital signature in the ciphertext, the operation fails. Use this feature to avoid unintentionally processing plaintext from signed messages before verifying the signature.

**Limiting encrypted data keys**
You can [limit the number of encrypted data keys](configure.md#config-limit-keys) in an encrypted message. This feature can help you detect a misconfigured master key provider or keyring when encrypting, or identify a malicious ciphertext when decrypting.
You should limit encrypted data keys when you decrypt messages from an untrusted source. It prevents unnecessary, expensive, and potentially exhaustive calls to your key infrastructure.

### Version 2.3.*x*
<a name="version2.3"></a>

Adds support for AWS KMS multi-Region keys. For details, see [Using multi-Region AWS KMS keys](configure.md#config-mrks).

**Note**
The AWS Encryption CLI supports multi-Region keys beginning in version 3.0.*x*.
Version 2.*x*.*x* of the AWS Encryption SDK for Python, AWS Encryption SDK for JavaScript, and the AWS Encryption CLI are in the [end-of-support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle).
For information about [support and maintenance](introduction.md#support) of this AWS Encryption SDK version in your preferred programming language, see the `SUPPORT_POLICY.rst` file in its [GitHub repository](introduction.md#esdk-repos).
