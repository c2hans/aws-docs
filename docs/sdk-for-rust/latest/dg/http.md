---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/http.html
---

# Configuring HTTP-level settings within the AWS SDK for Rust
<a name="http"></a>

The AWS SDK for Rust provides built-in HTTP functionality that is used by the AWS service clients that you create in your code.

By default, the SDK for Rust uses an HTTPS client based on `hyper`, `rustls`, and `aws-lc-rs`. This client should work well for most use cases without additional configuration.
+ [`hyper`](https://docs.rs/hyper/latest/hyper/) is a lower-level HTTP library for Rust that can be used with the AWS SDK for Rust to make API service calls.
+ [`rustls`](https://github.com/rustls/rustls) is a modern TLS library written in Rust that has built-in options for cryptographic providers.
+ [`aws-lc`](https://github.com/aws/aws-lc) is a general-purpose cryptographic library containing algorithms needed for TLS and common applications.
+ [`aws-lc-rs`](https://github.com/aws/aws-lc-rs) is an idiomatic wrapper around the `aws-lc` library in Rust.

The `aws-smithy-http-client` crate provides some additional options and configuration if you want to choose a different TLS or cryptographic provider. For more advanced use cases you are encouraged to bring your own HTTP client implementation or file a feature request for consideration.

## Choosing an alternative TLS provider
<a name="tlsProviders"></a>

The `aws-smithy-http-client` crate provides a few alternative TLS providers.

The following providers are available:

**`rustls` with `aws-lc`**
A TLS provider based on [`rustls`](https://github.com/rustls/rustls) that uses [`aws-lc-rs`](https://github.com/aws/aws-lc-rs) for cryptography.
This is the default HTTP behavior for the SDK for Rust. If you want to use this option you don't need to take any additional action in your code.

**`s2n-tls`**
A TLS provider based on [`s2n-tls`](https://github.com/aws/s2n-tls).

**`rustls` with `aws-lc-fips`**
A TLS provider based on [`rustls`](https://github.com/rustls/rustls) that uses a FIPS-compliant version of [`aws-lc-rs`](https://github.com/aws/aws-lc-rs) for cryptography

**`rustls` with `ring`**
A TLS provider based on [`rustls`](https://github.com/rustls/rustls) that uses [`ring`](https://github.com/briansmith/ring) for cryptography.

### Prerequisites
<a name="prereqTls"></a>

Using `aws-lc-rs` or `s2n-tls` requires a C Compiler (Clang or GCC) to build. For some platforms, the build may also require CMake. Building with the "fips" feature on any platform requires CMake and Go. For more information, reference the [AWS Libcrypto for Rust (`aws-lc-rs`)](https://github.com/aws/aws-lc-rs/blob/main/aws-lc-rs/README.md) repository and build instructions.

### How to use an alternative TLS provider
<a name="s2nTls"></a>

The `aws-smithy-http-client` crate provides additional TLS options. For your AWS service clients to use a different TLS provider, override the `http_client` using the loader from the `aws_config` crate. The HTTP client is used for both AWS services and credentials providers.

The following example shows how to use the `s2n-tls` TLS provider. However, a similar approach works for other providers as well.

To compile the example code, run the following command to add dependencies to your project:

```
cargo add aws-smithy-http-client -F {{s2n-tls}}
```

Example code:

```
use aws_smithy_http_client::{tls, Builder};

#[tokio::main]
async fn main() {
    let http_client = Builder::new()
        .tls_provider(tls::Provider::{{S2nTls}})
        .build_https();

    let sdk_config = aws_config::defaults(
        aws_config::BehaviorVersion::latest()
    )
    .http_client(http_client)
    .load()
    .await;

    // create client(s) using sdk_config
    // e.g. aws_sdk_s3::Client::new(&sdk_config);
}
```

## Enabling FIPS support
<a name="fipsTls"></a>

The `aws-smithy-http-client` crate provides an option to enable a FIPS-compliant crypto implementation. For your AWS service clients to use the FIPS-compliant provider, override the `http_client` using the loader from the `aws_config` crate. The HTTP client is used for both AWS services and credentials providers.

**Note**
FIPS support requires additional dependencies in your build environment. See the [build](https://github.com/aws/aws-lc/blob/main/BUILDING.md) instructions for the `aws-lc` crate.

To compile the example code, run the following command to add dependencies to your project:

```
cargo add aws-smithy-http-client -F rustls-aws-lc-fips
```

The following example code enables FIPS support:

```
// file: main.rs
use aws_smithy_http_client::{
    tls::{self, rustls_provider::CryptoMode},
    Builder,
};

#[tokio::main]
async fn main() {
    let http_client = Builder::new()
        .tls_provider(tls::Provider::Rustls(CryptoMode::AwsLcFips))
        .build_https();

    let sdk_config = aws_config::defaults(
        aws_config::BehaviorVersion::latest()
    )
    .http_client(http_client)
    .load()
    .await;

    // create client(s) using sdk_config
    // e.g. aws_sdk_s3::Client::new(&sdk_config);
}
```

## Prioritizing post-quantum key exchange
<a name="quantumTls"></a>

The default TLS provider is based on `rustls` using `aws-lc-rs` which supports the `X25519MLKEM768` post-quantum key exchange algorithm. To make `X25519MLKEM768` the highest priority algorithm you need to add the `rustls` package to your crate and enable the `prefer-post-quantum` feature flag. Otherwise, it is available but not the highest priority. See the `rustls` [documentation](https://docs.rs/rustls/0.23.23/rustls/manual/_05_defaults/index.html#about-the-post-quantum-secure-key-exchange-x25519mlkem768) for more information.

**Note**
This will become the default in a future release.

## Overriding the DNS Resolver
<a name="overrideDns"></a>

 The default DNS resolver can be overridden by configuring the HTTP client manually.

To compile the example code, run the following commands to add dependencies to your project:

```
cargo add aws-smithy-http-client -F rustls-aws-lc
cargo add aws-smithy-runtime-api -F client
```

The following example code overrides the DNS resolver:

```
use aws_smithy_http_client::{
    tls::{self, rustls_provider::CryptoMode},
    Builder
};
use aws_smithy_runtime_api::client::dns::{DnsFuture, ResolveDns};
use std::net::{IpAddr, Ipv4Addr};

/// A DNS resolver that returns a static IP address (127.0.0.1)
#[derive(Debug, Clone)]
struct StaticResolver;

impl ResolveDns for StaticResolver {
    fn resolve_dns<'a>(&'a self, _name: &'a str) -> DnsFuture<'a> {
        DnsFuture::ready(Ok(vec![IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1))]))
    }
}

#[tokio::main]
async fn main() {
    let http_client = Builder::new()
        .tls_provider(tls::Provider::Rustls(CryptoMode::AwsLc))
        .build_with_resolver(StaticResolver);

    let sdk_config = aws_config::defaults(
        aws_config::BehaviorVersion::latest()
    )
    .http_client(http_client)
    .load()
    .await;

    // create client(s) using sdk_config
    // e.g. aws_sdk_s3::Client::new(&sdk_config);
}
```

**Note**
By default, Amazon Linux 2023 (AL2023) doesn’t cache DNS on the operating system level.

## Customizing root CA certificates
<a name="customizeCertificatesTls"></a>

By default, the TLS provider loads the system native root certificates for the given platform. To customize this behavior to load a custom CA bundle, you can configure a `TlsContext` with your own `TrustStore`.

To compile the example code, run the following commands to add dependencies to your project:

```
cargo add aws-smithy-http-client -F rustls-aws-lc
```

The following example uses `rustls` with `aws-lc` but will work for any supported TLS provider:

```
use aws_smithy_http_client::{
    tls::{self, rustls_provider::CryptoMode},
    Builder
};
use std::fs;

/// read the PEM encoded root CA (bundle) and return a custom TLS context
fn tls_context_from_pem(filename: &str) -> tls::TlsContext {
    let pem_contents = fs::read(filename).unwrap();

    // Create a new empty trust store (this will not load platform native certificates)
    let trust_store = tls::TrustStore::empty()
        .with_pem_certificate(pem_contents.as_slice());

    tls::TlsContext::builder()
        .with_trust_store(trust_store)
        .build()
        .expect("valid TLS config")
}

#[tokio::main]
async fn main() {
    let http_client = Builder::new()
        .tls_provider(tls::Provider::Rustls(CryptoMode::AwsLc))
        .tls_context(tls_context_from_pem("my-custom-ca.pem"))
        .build_https();

    let sdk_config = aws_config::defaults(
        aws_config::BehaviorVersion::latest()
    )
    .http_client(http_client)
    .load()
    .await;

    // create client(s) using sdk_config
    // e.g. aws_sdk_s3::Client::new(&sdk_config);
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Rust. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-rust` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
