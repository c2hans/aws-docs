---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/best-practices.html
---

# Best practices for using AWS SDK for Rust
<a name="best-practices"></a>

The following are best practices for using the AWS SDK for Rust.

## Reuse SDK clients when possible
<a name="bp-reuseClient"></a>

Depending on how an SDK client is constructed, creating a new client may result in each client maintaining its own HTTP connection pools, identity caches, and so on. We recommend sharing a client or at least sharing `SdkConfig` to avoid the overhead of expensive resource creation. All SDK clients implement `Clone` as a single atomic reference count update.

## Configure API timeouts
<a name="bp-apiTimeouts"></a>

 The SDK provides default values for some timeout options, such as connection timeout and socket timeouts, but not for API call timeouts or individual API call attempts. It is a good practice to set timeouts for both the individual attempt and the entire request. This will ensure your application fails fast in an optimal way when there are transient issues that could cause request attempts to take longer to complete or fatal network issues.

For more information on configuring operation timeouts, see [Configuring timeouts in the AWS SDK for Rust](timeouts.md).
