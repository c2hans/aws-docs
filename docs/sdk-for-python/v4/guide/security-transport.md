---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/security-transport.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Working with TLS in the AWS SDK for Python v4
<a name="security-transport"></a>

The AWS SDK for Python v4 relies on the TLS implementation of its HTTP transport to secure connections to AWS services. AWS service endpoints require TLS 1.2 or later. We recommend TLS 1.3.

TLS 1.3 is required to enable post-quantum cryptography, which might require additional actions or configuration. For more information, see [Enabling hybrid post-quantum TLS](https://docs.aws.amazon.com/sdkref/latest/guide/pqtls-details.html) in the *AWS SDKs and Tools Reference Guide*.

## How TLS versions are selected
<a name="security-transport-defaults"></a>

The SDK doesn't select a specific TLS protocol version. The TLS behavior depends on the HTTP transport that the client's configuration uses:
+ By default, synchronous clients use `Urllib3HTTPClient`. This transport creates a urllib3 connection pool without supplying an SSL context. The urllib3 library then creates a verified SSL context with Python's `ssl` module and sets its minimum version to TLS 1.2. The enabled versions and cipher suites depend on the Python runtime's TLS library and its configuration.
+ By default, asynchronous clients use `AIOHTTPClient`. This transport creates an `aiohttp` client session without supplying an SSL context. By default, `aiohttp` creates a verified SSL context with Python's `ssl` module. The enabled versions and cipher suites depend on the Python runtime's TLS library and its configuration.
+ Asynchronous clients configured with `AWSCRTHTTPClient`, which is required for HTTP/2 bidirectional streaming, use an AWS Common Runtime (CRT) TLS context with default options. The SDK doesn't override its TLS version settings. The enabled versions depend on AWS CRT and its platform TLS implementation.

When the transport opens a connection, it negotiates a TLS version that both the client environment and the AWS service endpoint support. All three built-in transports verify server certificates by default. If you provide a custom transport, check its documentation for its TLS behavior.

## Check TLS version information
<a name="security-transport-check"></a>

`Urllib3HTTPClient` and `AIOHTTPClient` both use Python's `ssl` module. For clients that use either transport, use the `ssl` module to inspect the TLS library and the version limits of the default SSL context:

```
import ssl

context = ssl.create_default_context()

print(f"TLS library: {ssl.OPENSSL_VERSION}")
print(f"Minimum TLS version: {context.minimum_version.name}")
print(f"Maximum TLS version: {context.maximum_version.name}")
```

The output depends on the Python runtime and platform. It shows the settings of the default Python SSL context, not the TLS version negotiated for a particular request.

This check doesn't apply to clients that use `AWSCRTHTTPClient` because that transport uses AWS CRT instead of Python's `ssl` module. The built-in CRT transport doesn't provide a public API for reporting the TLS version negotiated for a connection. If you need to confirm the negotiated version, use TLS diagnostic tooling appropriate for your environment.

## Enforce a minimum TLS version
<a name="security-transport-configuration"></a>

The SDK doesn't override the minimum TLS version of any built-in transport. The built-in transports don't have a configuration setting for a minimum version. For `Urllib3HTTPClient`, the urllib3 library sets a minimum of TLS 1.2. AWS service endpoints reject connections that use a version earlier than TLS 1.2.

If your application must explicitly enforce a minimum version on the client, provide a compatible custom HTTP transport through the generated client's `transport` configuration. Use a transport that matches the client mode. To enforce the required minimum version, configure the transport or its TLS implementation as the transport's documentation describes. For more information, see [HTTP configuration](http-configuration.md).

## AWS API endpoints and TLS 1.2
<a name="tls-more-info"></a>

For more information about the TLS 1.2 minimum for AWS API endpoints, see [TLS 1.2 to become the minimum TLS protocol level for all AWS API endpoints](https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/).
