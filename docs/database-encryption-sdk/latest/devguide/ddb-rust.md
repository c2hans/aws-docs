---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-rust.html
---

# Rust
<a name="ddb-rust"></a>

This topic explains how to install and use version 1.*x* of the Rust client-side encryption library for DynamoDB. For details about programming with the AWS Database Encryption SDK for DynamoDB, see the [Rust examples](https://github.com/aws/aws-database-encryption-sdk-dynamodb/blob/main/releases/rust/db_esdk/examples/) in the aws-database-encryption-sdk-dynamodb repository on GitHub.

All programming language implementations of the AWS Database Encryption SDK for DynamoDB are interoperable.

**Topics**
+ [Prerequisites](#ddb-rust-prerequisites)
+ [Installation](#ddb-rust-install)
+ [Using the Rust client](ddb-rust-using.md)

## Prerequisites
<a name="ddb-rust-prerequisites"></a>

Before you install the Rust client-side encryption library for DynamoDB, be sure you have the following prerequisites.

**Install Rust and Cargo**
Install the current stable release of [Rust](https://www.rust-lang.org/) using [rustup](https://rustup.rs/).
For more information on downloading and installing rustup, see the [installation procedures](https://doc.rust-lang.org/cargo/getting-started/installation.html) in The Cargo Book.

## Installation
<a name="ddb-rust-install"></a>

The Rust client-side encryption library for DynamoDB is available as the [aws-db-esdk](https://crates.io/crates/aws-db-esdk) crate on Crates.io. For details about installing and building the library, see the [ README.md](https://github.com/aws/aws-database-encryption-sdk-dynamodb/) file in the aws-database-encryption-sdk-dynamodb GitHub repository.

**Manually**
To install the Rust client-side encryption library for DynamoDB, clone or download the [aws-database-encryption-sdk-dynamodb](https://github.com/aws/aws-database-encryption-sdk-dynamodb/) GitHub repository.

**To install the latest version**
Run the following Cargo command in your project directory:

```
cargo add aws-db-esdk
```
Or add the following line to your Cargo.toml:

```
aws-db-esdk = "{{<version>}}"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
