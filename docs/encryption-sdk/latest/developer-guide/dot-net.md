---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/dot-net.html
---

# AWS Encryption SDK for .NET
<a name="dot-net"></a>

The AWS Encryption SDK for .NET is a client-side encryption library for developers who are writing applications in C\# and other .NET programming languages. It is supported on Windows, macOS, and Linux.

**Note**
Version 4.0.0 of the AWS Encryption SDK for .NET deviates from the AWS Encryption SDK Message Specification. As a result, messages encrypted by version 4.0.0 can only be decrypted by version 4.0.0 or later of the AWS Encryption SDK for .NET. They cannot be decrypted by any other programming language implementation.
Version 4.0.1 of the AWS Encryption SDK for .NET writes messages according to the AWS Encryption SDK Message Specification, and is interoperable with other programming language implementations. By default, version 4.0.1 can read messages encrypted by version 4.0.0. However, if you do not want to decrypt messages encrypted by version 4.0.0, you can specify the [`NetV4_0_0_RetryPolicy`](https://github.com/aws/aws-encryption-sdk/tree/mainline/AwsEncryptionSDK/runtimes/net/Examples/NetV4_0_0Example.cs) property to prevent the client from reading these messages. For more information, see the [v4.0.1 release notes](https://github.com/aws/aws-encryption-sdk/releases/tag/v4.0.1) in the aws-encryption-sdk repository on GitHub.

The AWS Encryption SDK for .NET differs from some of the other programming language implementations of the AWS Encryption SDK in the following ways:
+ No support for [data key caching](data-key-caching.md)
**Note**
Version 4.*x* of the AWS Encryption SDK for .NET supports the [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md), an alternative cryptographic materials caching solution.
+ No support for streaming data
+ [No logging or stack traces](#dot-net-debugging) from the AWS Encryption SDK for .NET
+ [Requires the AWS SDK for .NET](#dot-net-install)

The AWS Encryption SDK for .NET includes all of the security features introduced in versions 2.0.*x* and later of other language implementations of the AWS Encryption SDK. However, if you are using the AWS Encryption SDK for .NET to decrypt data that was encrypted by a pre-2.0.*x* version another language implementation of the AWS Encryption SDK, you might need to adjust your [commitment policy](concepts.md#commitment-policy). For details, see [How to set your commitment policy](migrate-commitment-policy.md#migrate-commitment-step1).

The AWS Encryption SDK for .NET is a product of the AWS Encryption SDK in [Dafny](https://github.com/dafny-lang/dafny/blob/master/README.md), a formal verification language in which you write specifications, the code to implement them, and the proofs to test them. The result is a library that implements the features of the AWS Encryption SDK in a framework that assures functional correctness.

**Learn More**
+ For examples showing how to configure options in the AWS Encryption SDK, such as specifying an alternate algorithm suite, limiting encrypted data keys, and using AWS KMS multi-Region keys, see [Configuring the AWS Encryption SDK](configure.md).
+ For details about programming with the AWS Encryption SDK for .NET, see the [`aws-encryption-sdk-net`](https://github.com/aws/aws-encryption-sdk/tree/mainline/AwsEncryptionSDK/runtimes/net/) directory of the aws-encryption-sdk repository on GitHub.

**Topics**
+ [Install and build](#dot-net-install)
+ [Debugging](#dot-net-debugging)
+ [Examples](dot-net-examples.md)

## Installing the AWS Encryption SDK for .NET
<a name="dot-net-install"></a>

The AWS Encryption SDK for .NET is available as the [`AWS.Cryptography.EncryptionSDK`](https://www.nuget.org/packages/AWS.Cryptography.EncryptionSDK) package in NuGet. For details about installing and building the AWS Encryption SDK for .NET, see the [README.md](https://github.com/aws/aws-encryption-sdk/tree/mainline/AwsEncryptionSDK/runtimes/net/#readme) file in the `aws-encryption-sdk-net` repository.

**Version 3.x**
Version 3.*x* of the AWS Encryption SDK for .NET supports .NET Framework 4.5.2 – 4.8 only on Windows. It supports .NET Core 3.0\+ and .NET 5.0 and later on all supported operating systems.

**Version 4.x**
Version 4.*x* of the AWS Encryption SDK for .NET supports .NET 6.0 and .NET Framework net48 and later. Version 4.*x* requires the AWS SDK for .NET v3.

**Version 5.x**
Version 5.*x* of the AWS Encryption SDK for .NET supports .NET 6.0 and .NET Framework net48 and later. Version 5.*x* requires version 2.*x* of the Material Providers Library (MPL) and the AWS SDK for .NET v4.

The AWS Encryption SDK for .NET requires the SDK for .NET even if you aren't using AWS Key Management Service (AWS KMS) keys. It's installed with the NuGet package. However, unless you are using AWS KMS keys, AWS Encryption SDK for .NET does not require an AWS account, AWS credentials, or interaction with any AWS service. For help setting up an AWS account if you need it, see [Using the AWS Encryption SDK with AWS KMS](getting-started.md).

## Debugging the AWS Encryption SDK for .NET
<a name="dot-net-debugging"></a>

The AWS Encryption SDK for .NET does not generate any logs. Exceptions in the AWS Encryption SDK for .NET generate an exception message, but no stack traces.

To help you debug, be sure to enable logging in the SDK for .NET. The logs and error messages from the SDK for .NET can help you distinguish errors arising in the SDK for .NET from those in the AWS Encryption SDK for .NET. For help with SDK for .NET logging, see [AWSLogging](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-config-other.html#config-setting-awslogging) in the *AWS SDK for .NET Developer Guide*. (To see the topic, expand the **Open to view .NET Framework content** section.)
