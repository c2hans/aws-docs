---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/go.html
---

# AWS Encryption SDK for Go
<a name="go"></a>

This topic explains how to install and use the AWS Encryption SDK for Go. For details about programming with the AWS Encryption SDK for Go, see [go](https://github.com/aws/aws-encryption-sdk/tree/mainline/releases/go/encryption-sdk/) directory of the aws-encryption-sdk repository on GitHub.

The AWS Encryption SDK for Go differs from some of the other programming language implementations of the AWS Encryption SDK in the following ways:
+ No support for [data key caching](data-key-caching.md). However, the AWS Encryption SDK for Go supports the [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md), an alternative cryptographic materials caching solution.
+ No support for streaming data

The AWS Encryption SDK for Go includes all of the security features introduced in versions 2.0.*x* and later of other language implementations of the AWS Encryption SDK. However, if you are using the AWS Encryption SDK for Go to decrypt data that was encrypted by a pre-2.0.*x* version another language implementation of the AWS Encryption SDK, you might need to adjust your [commitment policy](concepts.md#commitment-policy). For details, see [How to set your commitment policy](migrate-commitment-policy.md#migrate-commitment-step1).

The AWS Encryption SDK for Go is a product of the AWS Encryption SDK in [Dafny](https://github.com/dafny-lang/dafny/blob/master/README.md), a formal verification language in which you write specifications, the code to implement them, and the proofs to test them. The result is a library that implements the features of the AWS Encryption SDK in a framework that assures functional correctness.

**Learn More**
+ For examples showing how to configure options in the AWS Encryption SDK, such as specifying an alternate algorithm suite, limiting encrypted data keys, and using AWS KMS multi-Region keys, see [Configuring the AWS Encryption SDK](configure.md).
+ For examples showing how to configure and use the AWS Encryption SDK for Go, see the [Go examples](https://github.com/aws/aws-encryption-sdk/tree/mainline/releases/go/encryption-sdk/examples) in the aws-encryption-sdk repository on GitHub.

**Topics**
+ [Prerequisites](#prerequisites-go)
+ [Installation](#go-installation)
+ [Examples](go-examples.md)

## Prerequisites
<a name="prerequisites-go"></a>

Before you install the AWS Encryption SDK for Go, be sure you have the following prerequisites.

**A supported version of Go**
Go 1.23 or later is required by AWS Encryption SDK for Go.
For more information on downloading and installing Go, see [Go installation](https://go.dev/doc/install).

## Installation
<a name="go-installation"></a>

Install the latest version of the AWS Encryption SDK for Go. For details on installing and building the AWS Encryption SDK for Go, see the [README.md](https://github.com/aws/aws-encryption-sdk/tree/mainline/releases/go/encryption-sdk/README.md) in the go directory of the aws-encryption-sdk repository on GitHub.

**To install the latest version**
+ Install the AWS Encryption SDK for Go

  ```
  go get github.com/aws/aws-encryption-sdk/releases/go/encryption-sdk@latest
  ```
+ Install the [Cryptographic Material Providers Library](https://github.com/aws/aws-cryptographic-material-providers-library) (MPL)

  ```
  go get github.com/aws/aws-cryptographic-material-providers-library/releases/go/mpl
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
