---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/document-history.html
---

# Document history for the AWS Encryption SDK Developer Guide
<a name="document-history"></a>

This topic describes significant updates to the *AWS Encryption SDK Developer Guide*.

**Topics**
+ [Recent updates](#recent-updates)
+ [Earlier updates](#earlier-updates)

## Recent updates
<a name="recent-updates"></a>

The following table describes significant changes to this documentation since November 2017. In addition to major changes listed here, we also update the documentation frequently to improve the descriptions and examples, and to address the feedback that you send to us. To be notified about significant changes, subscribe to the RSS feed.

| Change | Description | Date |
| --- |--- |--- |
| [AWS Encryption SDK for .NET version 5.x](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/dot-net.html) | Updates to version 2.0 of the Material Providers Library (MPL). Drops support for the AWS SDK for .NET v3 and adds support for the AWS SDK for .NET v4. | March 25, 2025 |
| [General availability](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-kms-ecdh-keyring.html) | Added documentation for the [AWS KMS ECDH keyring](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-kms-ecdh-keyring.html) and [Raw ECDH keyring](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-raw-ecdh-keyring.html). | June 17, 2024 |
| [AWS Encryption SDK for Java version 3.x](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/java.html) | Integrates the AWS Encryption SDK for Java with the material providers library. Adds support for keyrings and the required encryption context CMM. | December 6, 2023 |
| [AWS Encryption SDK for .NET version 4.x](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/dot-net.html) | Adds support for the AWS KMS Hierarchical keyring, the required encryption context CMM, and asymmetric RSA AWS KMS keyrings. | October 12, 2023 |
| [General availability](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/dot-net.html) | Introducing support for the AWS Encryption SDK for .NET. | May 17, 2022 |
| [Documentation change](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/concepts.html#master-key) | Replace the AWS Key Management Service term *customer master key (CMK)* with *AWS KMS key* and *KMS key*. | August 30, 2021 |
| [General availability](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/configure.html#config-mrks) | Added support for AWS Key Management Service.(AWS KMS) multi-Region keys. Multi-Region keys are AWS KMS keys in different AWS Regions that can be used interchangeably because they have the same key ID and key material. | June 8, 2021 |
| [General availability](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/concepts.html#digital-sigs) | Added and updated documentation about the improved message decryption process. | May 11, 2021 |
| [General availability](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/about-versions.html) | Added and updated documentation for the general availability release of AWS Encryption CLI version 1.8.*x* to replace AWS Encryption CLI version 1.7.*x*, and AWS Encryption CLI 2.1.*x* to replace AWS Encryption CLI 2.0.*x*. | October 27, 2020 |
| [General availability](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/about-versions.html) | Added and updated documentation for the general availability release of the AWS Encryption SDK versions 1.7.*x* and 2.0.*x*, including a [best practices guide](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/best-practices.html), a [migration guide](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/migration-guide.html), updated [concepts](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/concepts.html), updated [programming language topics](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/programming-languages.html), an updated [algorithm suites reference](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/algorithms-reference.html), an updated [message format reference](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/message-format.html), and a new [message format example](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/message-format-examples.html). | September 24, 2020 |
| [General availability](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/javascript.html) | Added and updated documentation for the general availability release of the [AWS Encryption SDK for JavaScript](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/javascript.html). | October 1, 2019 |
| [Preview release](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/javascript.html) | Added and updated documentation of the public beta release of the [AWS Encryption SDK for JavaScript](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/javascript.html). | June 21, 2019 |
| [General availability](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/c-language.html) | Added and updated documentation for the general availability release of the [AWS Encryption SDK for C](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/c-language.html). | May 16, 2019 |
| [Preview release](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/c-language.html) | Added documentation of the preview release of the [AWS Encryption SDK for C](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/c-language.html). | February 5, 2019 |
| [New release](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/crypto-cli.html) | Added documentation of the [command line interface](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/crypto-cli.html) for the AWS Encryption SDK. | November 20, 2017 |

## Earlier updates
<a name="earlier-updates"></a>

The following table describes significant changes to the *AWS Encryption SDK Developer Guide* before November 2017.

| Change | Description | Date |
| --- | --- | --- |
| New release | Added the [Data key caching](data-key-caching.md) chapter for the new feature.<br />Added the [AWS Encryption SDK initialization vector reference](IV-reference.md) topic that explains that the SDK changed from generating random IVs to constructing deterministic IVs.<br />Added the [Concepts in the AWS Encryption SDK](concepts.md) topic to explain concepts, including the new cryptographic materials manager. | July 31, 2017 |
| Update | Expanded the [Message format reference](message-format.md) documentation into a new [AWS Encryption SDK reference](reference.md) section.<br />Added a section about the AWS Encryption SDK [Supported algorithm suites](supported-algorithms.md). | March 21, 2017 |
| New release | The AWS Encryption SDK now supports the [Python](python.md) programming language, in addition to [Java](java.md). | March 21, 2017 |
| Initial release | Initial release of the AWS Encryption SDK and this documentation. | March 22, 2016 |
