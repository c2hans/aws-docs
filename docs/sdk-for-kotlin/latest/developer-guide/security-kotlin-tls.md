---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/security-kotlin-tls.html
---

# AWS SDK for Kotlin support for Transport Layer Security (TLS)
<a name="security-kotlin-tls"></a>

The following information applies only to Java SSL implementation (the default SSL implementation in the AWS SDK for Kotlin targeting the JVM). If you’re using a different SSL implementation, see your specific SSL implementation to learn how to enforce TLS versions.

## TLS support in Java
<a name="tls-support-in-java"></a>

To work with AWS services, the underlying JDK must support a minimum version of TLS 1.2, but TLS 1.3 is recommended. TLS 1.3 is the prerequisite to enable post-quantum cryptography, which may require additional actions or configurations. To learn more, see [Enabling hybrid post-quantum TLS](/sdkref/latest/guide/pqtls-details.html).

TLS 1.2 is supported starting in Java 7. TLS 1.3 is supported starting in Java 11, although some JVM vendors have backported support into earlier Java versions.

## How to check the TLS version
<a name="how-to-check-the-tls-version"></a>

To check which TLS versions are supported in your Java virtual machine (JVM), you can use the following code.

```
println(SSLContext.getDefault().supportedSSLParameters.protocols.joinToString(separator = ", "))
```

To see the SSL handshake in action and what version of TLS is used, you can use the system property **javax.net.debug**.

```
-Djavax.net.debug=ssl
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
