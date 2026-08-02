---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/appendix-crates.html
---

# Crates used by the AWS SDK for Rust
<a name="appendix-crates"></a>

This topic contains advanced information about the crates used by the AWS SDK for Rust. This includes the Smithy components it uses, crates you might need to use under certain build circumstances, and other information.

## Smithy crates
<a name="smithy-crates"></a>

The AWS SDK for Rust is based on [Smithy](https://smithy.io/), like most of the AWS SDKs. Smithy is a language used to describe the data types and functions offered by the SDK. These models are then used to help build the SDK itself.

When looking at versions of the SDK for Rust crates and those of its Smithy dependencies, it might be helpful to know that these crates all use [standard semantic version numbering](https://semver.org/).

For additional detailed information about Smithy crates for Rust, see [Smithy Rust Design](https://smithy-lang.github.io/smithy-rs/design/).

### Crates used with the SDK for Rust
<a name="crates-to-know"></a>

There are a number of Smithy crates published by AWS. Some of these are relevant to SDK for Rust users, while others are implementation details:

`aws-smithy-async`
Include this crate if you're not using Tokio for asynchronous functionality.

`aws-smithy-runtime`
Includes building blocks required by all AWS SDKs.

`aws-smithy-runtime-api`
Underlying interfaces used by the SDK.

`aws-smithy-types`
Types re-exported from other AWS SDKs. Use this if you use multiple SDKs.

`aws-smithy-types-convert`
Utility functions for moving in and out of `aws-smithy-types`.

### Other crates
<a name="other-crates"></a>

The following crates exist, but you should not need to know anything about them:

Server-related crates that SDK for Rust users don't need:
+ `aws-smithy-http-server`
+ `aws-smithy-http-server-python`

Crates that contain under-the-hood code that SDK users don't need to use:
+ `aws-smithy-checksum-callbacks`
+ `aws-smithy-eventstream`
+ `aws-smithy-http`
+ `aws-smithy-protocol-test`
+ `aws-smithy-query`
+ `aws-smithy-json`
+ `aws-smithy-xml`

Crates that are unsupported and will go away in the future:
+ `aws-smithy-client`
+ `aws-smithy-http-auth`
+ `aws-smithy-http-tower`
