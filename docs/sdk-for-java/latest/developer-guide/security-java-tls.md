---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/security-java-tls.html
---

# Working with TLS in the SDK for Java
<a name="security-java-tls"></a>

The AWS SDK for Java uses the TLS capabilities of its underlying Java platform. In this topic, we show examples using the OpenJDK implementation used by [Amazon Corretto 17](https://docs.aws.amazon.com/corretto/latest/corretto-17-ug/index.html).

To work with AWS services, the underlying JDK must support a minimum version of TLS 1.2, but TLS 1.3 is recommended.

TLS 1.3 is the prerequisite to enable post-quantum cryptography, which may require additional actions or configurations. To learn more, see [ Enabling hybrid post-quantum TLS](https://docs.aws.amazon.com/sdkref/latest/guide/pqtls-details.html).

Users should consult the documentation of the the Java platform they are using with the SDK to find out which TLS versions are enabled by default as well as how to enable and disable specific TLS versions.

## How to check TLS version information
<a name="how-to-check-the-tls-version"></a>

Using OpenJDK, the following code shows the use of [SSLContext](https://devdocs.io/openjdk~17/java.base/javax/net/ssl/sslcontext#getSupportedSSLParameters()) to print which TLS/SSL versions are supported.

```
System.out.println(Arrays.toString(SSLContext.getDefault().getSupportedSSLParameters().getProtocols()));
```

For example, Amazon Corretto 17 (OpenJDK) produces the following output.

```
[TLSv1.3, TLSv1.2, TLSv1.1, TLSv1, SSLv3, SSLv2Hello]
```

To see the SSL handshake in action and what version of TLS is used, you can use the system property **javax.net.debug**.

For example, run a Java applications that uses TLS.

```
java app.jar -Djavax.net.debug=ssl:handshake
```

The application logs the SSL handshake similar to the following.

```
...
javax.net.ssl|DEBUG|10|main|2022-12-23 13:53:12.221 EST|ClientHello.java:641|Produced ClientHello handshake message (
"ClientHello": {
  "client version"      : "TLSv1.2",

...
javax.net.ssl|DEBUG|10|main|2022-12-23 13:53:12.295 EST|ServerHello.java:888|Consuming ServerHello handshake message (
"ServerHello": {
  "server version"      : "TLSv1.2",
...
```

**AWS CRT HTTP client TLS debugging**
If you use the AWS CRT HTTP client, the Java TLS debug properties shown in the preceding examples have no effect because the CRT uses its own TLS stack. To inspect network-level request details with the CRT HTTP client, enable wire logging. For more information, see [Enable wire logging](logging-slf4j.md#sdk-java-logging-verbose).

## Enforce a minimum TLS version
<a name="enforce-minimum-tls-version"></a>

The SDK for Java always prefers the latest TLS version supported by the platform and service. The approach to enforce a specific minimum TLS version differs depending on which HTTP client you use.

For the Apache, Netty, and URL Connection HTTP clients, which use the Java TLS stack, use the system property `jdk.tls.client.protocols`. For example, to enforce TLS 1.3 for SDK service clients, provide the following system property.

```
java -Djdk.tls.client.protocols=TLSv1.3 -jar app.jar
```

For more information about configuring TLS versions, see the documentation for your Java platform.

For the AWS CRT HTTP client, which uses its own TLS stack, the `jdk.tls.client.protocols` system property has no effect. Instead, use the `minTlsVersion` builder option to enforce a minimum TLS version.

The [TlsVersion](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/crt/TlsVersion.html) enum (`software.amazon.awssdk.http.crt.TlsVersion`) provides the following values:

**`TLS_1_3`**
Enforces TLS 1.3 as the minimum version.

**`SYSTEM_DEFAULT`**
Uses the platform's default TLS version negotiation behavior.

The following example creates a synchronous AWS CRT HTTP client that enforces TLS 1.3 as the minimum version.

```
import software.amazon.awssdk.http.crt.AwsCrtHttpClient;
import software.amazon.awssdk.http.crt.TlsVersion;

AwsCrtHttpClient httpClient = AwsCrtHttpClient.builder()
        .minTlsVersion(TlsVersion.TLS_1_3)
        .build();
```

The following example creates an asynchronous AWS CRT HTTP client that enforces TLS 1.3 as the minimum version.

```
import software.amazon.awssdk.http.crt.AwsCrtAsyncHttpClient;
import software.amazon.awssdk.http.crt.TlsVersion;

AwsCrtAsyncHttpClient asyncHttpClient = AwsCrtAsyncHttpClient.builder()
        .minTlsVersion(TlsVersion.TLS_1_3)
        .build();
```

You can then pass the configured HTTP client to an AWS service client.

```
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.http.crt.AwsCrtHttpClient;
import software.amazon.awssdk.http.crt.TlsVersion;

S3Client s3Client = S3Client.builder()
        .httpClientBuilder(AwsCrtHttpClient.builder()
                .minTlsVersion(TlsVersion.TLS_1_3))
        .build();
```

**macOS requirement for TLS 1.3**
Apple Secure Transport, the default macOS CRT TLS backend, does not support TLS 1.3. To use `TlsVersion.TLS_1_3` on macOS, you must set the environment variable `AWS_CRT_USE_NON_FIPS_TLS_13` to a non-empty value before starting the application. This switches the CRT to its s2n-tls backend.
Note the following considerations when you use this environment variable:
The s2n-tls backend is not FIPS-validated.
The s2n-tls backend does not integrate with the macOS Keychain.
If you do not set this environment variable on macOS, the first request fails with a CRT-side error.

**Mutual exclusion with post-quantum TLS settings**
You cannot combine `postQuantumTlsEnabled(false)` with `minTlsVersion(TlsVersion.TLS_1_3)`. These options are mutually exclusive in the CRT TLS context. If you specify both, the builder throws an `IllegalStateException`.

## AWS API endpoints upgrade to TLS 1.2
<a name="tls-more-info"></a>

See this [blog post](https://aws.amazon.com/blogs//security/tls-1-2-required-for-aws-endpoints/) for information about AWS API endpoints moving to TLS 1.2 for the minimum version.
