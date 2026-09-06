---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/configure-http-tls.html
---

# Enforce a minimum TLS version
<a name="configure-http-tls"></a>

With the AWS SDK for Kotlin, you can configure the minimum TLS version when you connect to service endpoints. The SDK offers different configuration options. In order of highest to lowest precedence, the options are:
+ Explicitly configure the HTTP engine
+ Set the `sdk.minTls` JVM system property
+ Set the `SDK_MIN_TLS` environment variable

## Configure the HTTP engine
<a name="configure-http-tls-engine"></a>

When you specify a non-default HTTP engine for a service client, you can set the `tlsContext.minVersion` field.

The following example configures the HTTP engine and any service client that uses it to use TLS v1.2 at a minimum.

```
DynamoDbClient {
    region = "us-east-2"
    httpClient {
        tlsContext {
            minVersion = TlsVersion.TLS_1_2
        }
    }
}.use { ddb ->

    // Perform some actions with Amazon DynamoDB.
}
```

## Set the `sdk.minTls` JVM system property
<a name="configure-http-tls-sysprop"></a>

You can set the `sdk.minTls` JVM system property. When you launch an application with the system property set, all HTTP engines constructed by the AWS SDK for Kotlin use the specified minimum TLS version by default. However, you can explicitly override this in the HTTP engine configuration. The allowable values are:
+ TLS\_1\_0
+ TLS\_1\_1
+ TLS\_1\_2
+ TLS\_1\_3

## Set the `SDK_MIN_TLS` environment variable
<a name="configure-http-tls-envvar"></a>

You can set the `SDK_MIN_TLS` environment variable. When you launch an application with the environment variable set, all HTTP engines constructed by the AWS SDK for Kotlin use the specified minimum TLS version, unless overridden by another option.

The allowable values are:
+ TLS\_1\_0
+ TLS\_1\_1
+ TLS\_1\_2
+ TLS\_1\_3
