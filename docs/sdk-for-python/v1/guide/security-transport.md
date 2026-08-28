---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/security-transport.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Working with TLS in the AWS SDK for Python
<a name="security-transport"></a>

The AWS SDK for Python relies on the TLS implementation of its HTTP transport to secure connections to AWS services. AWS service endpoints require TLS 1.2 or later, and TLS 1.3 is recommended.

TLS 1.3 is required to enable post-quantum cryptography, which might require additional actions or configuration. To learn more, see [Enabling hybrid post-quantum TLS](https://docs.aws.amazon.com/sdkref/latest/guide/pqtls-details.html).

## How TLS versions are selected
<a name="security-transport-defaults"></a>

The SDK does not select a specific TLS protocol version. The TLS behavior depends on the HTTP transport that the client's configuration uses:
+ By default, clients use `AIOHTTPClient`. This transport creates an `aiohttp` client session without supplying an SSL context. By default, `aiohttp` uses a verified SSL context created by Python's `ssl` module. The enabled versions and cipher suites depend on the TLS library used by the Python runtime and its configuration.
+ Clients configured with `AWSCRTHTTPClient`, which is required for HTTP/2 bidirectional streaming, use an AWS Common Runtime (CRT) TLS context with default options, and the SDK does not override its TLS-version settings. The enabled versions depend on AWS CRT and its platform TLS implementation.

When a connection is established, the transport negotiates a TLS version supported by both the client environment and the AWS service endpoint. Both built-in transports verify server certificates by default. If you provide a custom transport, consult its documentation for its TLS behavior.

## Check TLS version information
<a name="security-transport-check"></a>

For clients that use `AIOHTTPClient`, use the Python `ssl` module to inspect the TLS library and the version limits of the default SSL context:

```
import ssl

context = ssl.create_default_context()

print(f"TLS library: {ssl.OPENSSL_VERSION}")
print(f"Minimum TLS version: {context.minimum_version.name}")
print(f"Maximum TLS version: {context.maximum_version.name}")
```

The output depends on the Python runtime and platform. It shows the settings of the default Python SSL context, not the TLS version negotiated for a particular request.

This check does not apply to clients that use `AWSCRTHTTPClient` because that transport uses AWS CRT instead of Python's `ssl` module. The built-in CRT transport does not provide a public API for reporting the TLS version negotiated for a connection. If you need to confirm the negotiated version, use TLS diagnostic tooling appropriate for your environment.

## Enforce a minimum TLS version
<a name="security-transport-configuration"></a>

The SDK does not override the minimum TLS version of either built-in transport, and their public configuration does not provide a minimum-version setting. AWS service endpoints reject connections that use a version earlier than TLS 1.2.

If your application must explicitly enforce a minimum version on the client, provide a compatible custom HTTP transport through the generated client's `transport` configuration. Configure the transport or its TLS implementation to enforce the required minimum version, and follow the transport's documentation.

## AWS API endpoints and TLS 1.2
<a name="tls-more-info"></a>

For more information about the TLS 1.2 minimum for AWS API endpoints, see [TLS 1.2 to become the minimum TLS protocol level for all AWS API endpoints](https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
