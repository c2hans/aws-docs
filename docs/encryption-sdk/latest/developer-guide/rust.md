---
source_url: https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/rust.html
---

# AWS Encryption SDK for Rust
<a name="rust"></a>

This topic explains how to install and use the AWS Encryption SDK for Rust. For details about programming with the AWS Encryption SDK for Rust, see the [Rust](https://github.com/aws/aws-encryption-sdk-dafny/tree/mainline/AwsEncryptionSDK/runtimes/rust/) directory of the aws-encryption-sdk repository on GitHub.

The AWS Encryption SDK for Rust differs from some of the other programming language implementations of the AWS Encryption SDK in the following ways:
+ No support for [data key caching](data-key-caching.md). However, the AWS Encryption SDK for Rust supports the [AWS KMS Hierarchical keyring](use-hierarchical-keyring.md), an alternative cryptographic materials caching solution.
+ No support for streaming data

The AWS Encryption SDK for Rust includes all of the security features introduced in versions 2.0.*x* and later of other language implementations of the AWS Encryption SDK. However, if you are using the AWS Encryption SDK for Rust to decrypt data that was encrypted by a pre-2.0.*x* version another language implementation of the AWS Encryption SDK, you might need to adjust your [commitment policy](concepts.md#commitment-policy). For details, see [How to set your commitment policy](migrate-commitment-policy.md#migrate-commitment-step1).

The AWS Encryption SDK for Rust is a product of the AWS Encryption SDK in [Dafny](https://github.com/dafny-lang/dafny/blob/master/README.md), a formal verification language in which you write specifications, the code to implement them, and the proofs to test them. The result is a library that implements the features of the AWS Encryption SDK in a framework that assures functional correctness.

**Learn More**
+ For examples showing how to configure options in the AWS Encryption SDK, such as specifying an alternate algorithm suite, limiting encrypted data keys, and using AWS KMS multi-Region keys, see [Configuring the AWS Encryption SDK](configure.md).
+ For examples showing how to configure and use the AWS Encryption SDK for Rust, see the [Rust examples](https://github.com/aws/aws-encryption-sdk-dafny/tree/mainline/AwsEncryptionSDK/runtimes/rust/examples) in the aws-encryption-sdk repository on GitHub.

**Topics**
+ [Prerequisites](#prerequisites-rust)
+ [Installation](#rust-installation)
+ [Examples](rust-examples.md)

## Prerequisites
<a name="prerequisites-rust"></a>

Before you install the AWS Encryption SDK for Rust, be sure you have the following prerequisites.

**Install Rust and Cargo**
Install the current stable release of [Rust](https://www.rust-lang.org/) using [rustup](https://rustup.rs/).
For more information on downloading and installing rustup, see the [installation procedures](https://doc.rust-lang.org/cargo/getting-started/installation.html) in The Cargo Book.

## Installation
<a name="rust-installation"></a>

The AWS Encryption SDK for Rust is available as the [`aws-esdk`](https://crates.io/crates/aws-esdk) crate on Crates.io. For details on installing and building the AWS Encryption SDK for Rust, see the [README.md](https://github.com/aws/aws-encryption-sdk/tree/mainline) in the aws-encryption-sdk repository on GitHub.

You can install the AWS Encryption SDK for Rust in the following ways.

**Manually**
To install the AWS Encryption SDK for Rust, clone or download the [aws-encryption-sdk](https://github.com/aws/aws-encryption-sdk/tree/mainline) GitHub repository.

**Using Crates.io**
Run the following Cargo command in your project directory:

```
cargo add aws-esdk
```
Or add the following line to your Cargo.toml:

```
aws-esdk = "{{<version>}}"
```
