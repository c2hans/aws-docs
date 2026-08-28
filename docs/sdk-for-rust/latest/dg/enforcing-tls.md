---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/enforcing-tls.html
---

# Enforce a minimum TLS version in the AWS SDK for Rust
<a name="enforcing-tls"></a>

The AWS SDK for Rust uses TLS to increase security when communicating with AWS services. The SDK enforces a minimum TLS version of 1.2 by default. By default, the SDK also negotiates the highest version of TLS available to both the client application and the service. For example, the SDK might be able to negotiate TLS 1.3.

A particular TLS version can be enforced in the application by providing manual configuration of the TCP connector that the SDK uses. To illustrate this, the following example shows you how to enforce TLS 1.3.

**Note**
Some AWS services do not yet support TLS 1.3, so enforcing this version might affect SDK interoperability. We recommend testing this configuration with each service before production deployment.

```
pub async fn connect_via_tls_13() -> Result<(), Error> {
    println!("Attempting to connect to KMS using TLS 1.3: ");

    // Let webpki load the Mozilla root certificates.
    let mut root_store = RootCertStore::empty();
    root_store.add_server_trust_anchors(webpki_roots::TLS_SERVER_ROOTS.0.iter().map(|ta| {
        rustls::OwnedTrustAnchor::from_subject_spki_name_constraints(
            ta.subject,
            ta.spki,
            ta.name_constraints,
        )
    }));

    // The .with_protocol_versions call is where we set TLS1.3. You can add rustls::version::TLS12 or replace them both with rustls::ALL_VERSIONS
    let config = rustls::ClientConfig::builder()
        .with_safe_default_cipher_suites()
        .with_safe_default_kx_groups()
        .with_protocol_versions(&[&rustls::version::TLS13])
        .expect("It looks like your system doesn't support TLS1.3")
        .with_root_certificates(root_store)
        .with_no_client_auth();

    // Finish setup of the rustls connector.
    let rustls_connector = hyper_rustls::HttpsConnectorBuilder::new()
        .with_tls_config(config)
        .https_only()
        .enable_http1()
        .enable_http2()
        .build();

    // See https://github.com/awslabs/smithy-rs/discussions/3022 for the HyperClientBuilder
    let http_client = HyperClientBuilder::new().build(rustls_connector);

    let shared_conf = aws_config::defaults(BehaviorVersion::latest())
        .http_client(http_client)
        .load()
        .await;

    let kms_client = aws_sdk_kms::Client::new(&shared_conf);
    let response = kms_client.list_keys().send().await?;

    println!("{:?}", response);

    Ok(())
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Rust. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-rust` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
