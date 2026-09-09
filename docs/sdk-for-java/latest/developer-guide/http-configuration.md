---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration.html
---

# Configure HTTP clients in the AWS SDK for Java 2.x
<a name="http-configuration"></a>

You can change the HTTP client to use for your service client as well as change the default configuration for HTTP clients with the AWS SDK for Java 2.x. This section discusses HTTP clients and settings for the SDK.

## HTTP clients available in the SDK for Java
<a name="http-clients-available"></a>

### Synchronous clients
<a name="http-config-sync"></a>

Synchronous HTTP clients in the SDK for Java implement the [SdkHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/SdkHttpClient.html) interface. A synchronous service client, such as the `S3Client` or the `DynamoDbClient`, requires the use of a synchronous HTTP client. The AWS SDK for Java offers three synchronous HTTP clients.

**Apache5HttpClient (default)**
[Apache5HttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/apache5/Apache5HttpClient.html) is an updated version of `ApacheHttpClient` that is built on the *Apache 5.x HttpClient. Version 5.x * is the version actively maintained by Apache, and improves on the previous version used by `ApacheHttpClient` by bringing modern Java ecosystem compatibility including virtual thread support for Java 21, and enhanced logging flexibility through SLF4J. `Apache5HttpClient` replaced `ApacheHttpClient` as the default synchronous client in version `2.46.0` of the AWS SDK for Java 2.x. It has an identical API and features, making it ideal as a drop-in replacement. For information about configuring the `Apache5HttpClient`, see [Configure the Apache 5.x based HTTP client](http-configuration-apache5.md).

**ApacheHttpClient**
`ApacheHttpClient` is deprecated because Apache HttpClient 4.x is in maintenance mode. Use the Apache HttpClient 5.x based [Apache5HttpClient](http-configuration-apache5.md).
[ApacheHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/apache/ApacheHttpClient.html) is built on the *Apache 4.x HttpClient*. For information about configuring the `ApacheHttpClient`, see [Configure the Apache-based HTTP client](http-configuration-apache.md).

**AwsCrtHttpClient**
[AwsCrtHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/crt/AwsCrtHttpClient.html) provides high throughput and non-blocking IO. It is built on the AWS Common Runtime (CRT) Http Client. For information about configuring the `AwsCrtHttpClient` and using it with service clients, see [Configure AWS CRT-based HTTP clients](http-configuration-crt.md).

**UrlConnectionHttpClient**
To minimize the number of jars and third-party libraries you application uses, you can use the [UrlConnectionHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/urlconnection/UrlConnectionHttpClient.html). For information about configuring the `UrlConnectionHttpClient`, see [Configure the URLConnection-based HTTP client](http-configuration-url.md).

### Asynchronous clients
<a name="http-config-async"></a>

Asynchronous HTTP clients in the SDK for Java implement the [SdkAsyncHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/async/SdkAsyncHttpClient.html) interface. An asynchronous service client, such as the `S3AsyncClient` or the `DynamoDbAsyncClient`, requires the use of an asynchronous HTTP client. The AWS SDK for Java offers two asynchronous HTTP clients.

**NettyNioAsyncHttpClient (default)**
[NettyNioAsyncHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/nio/netty/NettyNioAsyncHttpClient.html) is the default HTTP client used by asynchronous clients. For information about configuring the `NettyNioAsyncHttpClient`, see [Configure the Netty-based HTTP client](http-configuration-netty.md).

**AwsCrtAsyncHttpClient**
The [AwsCrtAsyncHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/crt/AwsCrtAsyncHttpClient.html) is based on the AWS Common Runtime (CRT) HTTP Client. For information about configuring the `AwsCrtAsyncHttpClient`, see [Configure AWS CRT-based HTTP clients](http-configuration-crt.md).

## HTTP client recommendations
<a name="http-clients-recommend"></a>

Several factors come into play when you choose an HTTP client implementation. Use the following information to help you decide.

### HTTP client comparison
<a name="http-clients-recommend-compare"></a>

The following table provides detailed information for each HTTP client.

| HTTP client | Sync or async | When to use | Limitation/drawback |
| --- | --- | --- | --- |
|  Apache 5.x based HTTP client *(default sync HTTP client)* | Sync | Use it if you prefer low latency over high throughput  | Slower startup time compared to other HTTP clients |
| URLConnection-based HTTP client | Sync | Use it if you have a hard requirement for limiting third-party dependencies | • Does not support the HTTP PATCH method, required by some APIs like Amazon APIGateway Update operations<br />• Does not support a configurable idle connection timeout. See [Configure the URLConnection-based HTTP client](http-configuration-url.md) for details. |
| AWS CRT-based sync HTTP client1  | Sync | • Use it if your application is running in AWS Lambda<br />• Use it if you prefer high throughput over low latency<br />• Use it if you prefer sync SDK clients | The following Java system properties are not supported:+  javax.net.ssl.keyStore <br />+  javax.net.ssl.keyStorePassword <br />+   javax.net.ssl.trustStore <br />+  javax.net.ssl.trustStorePassword  |
|  Netty-based HTTP client *(default async HTTP client)* | Async | • Use it if your application relies on Java system properties for TLS configuration (such as `javax.net.ssl.keyStore`) | Slower startup time compared to other HTTP clients |
|  AWS CRT-based async HTTP client1  | Async | • Use it if your application is running in AWS Lambda<br />• Use it if you prefer high throughput over low latency• Use it if you prefer async SDK clients | The following Java system properties are not supported:+  javax.net.ssl.keyStore <br />+  javax.net.ssl.keyStorePassword <br />+   javax.net.ssl.trustStore <br />+  javax.net.ssl.trustStorePassword  |

1Because of their added benefits, we recommend that you use the AWS CRT-based HTTP clients if possible.

## Smart configuration defaults
<a name="http-config-smart-defaults"></a>

The AWS SDK for Java 2.x (version 2.17.102 or later) offers a smart configuration defaults feature. This feature optimizes two HTTP client properties along with other properties that don't affect the HTTP client.

The smart configuration defaults set sensible values for the `connectTimeoutInMillis` and `tlsNegotiationTimeoutInMillis` properties based on a defaults mode value that you provide. You choose the defaults mode value based on your application's characteristics.

For more information about smart configuration defaults and how to choose the defaults mode value that is best suited for your applications, see the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/feature-smart-config-defaults.html).

Following are four ways to set the defaults mode for your application.

------
#### [ Service client ]

Use the service client builder to configure the defaults mode directly on the service client. The following example sets the defaults mode to `auto` for the `DynamoDbClient`.

```
DynamoDbClient ddbClient = DynamoDbClient.builder()
                            .defaultsMode(DefaultsMode.AUTO)
                            .build();
```

------
#### [ System property ]

You can use the `aws.defaultsMode` system property to specify the defaults mode. If you set the system property in Java, you need to set the property before initializing any service client.

The following example shows you how to set the defaults mode to `auto` using a system property set in Java.

```
System.setProperty("aws.defaultsMode", "auto");
```

The following example demonstrates how you set the defaults mode to `auto` using a `-D` option of the `java` command.

```
java -Daws.defaultsMode=auto
```

------
#### [ Environment variable ]

Set a value for environment variable `AWS_DEFAULTS_MODE` to select the defaults mode for your application.

The following information shows the command to run to set the value for the defaults mode to `auto` using an environment variable.

| Operating system | Command to set environment variables |
| --- | --- |
| Linux, macOS, or Unix | export AWS\_DEFAULTS\_MODE=auto |
| Windows | set AWS\_DEFAULTS\_MODE=auto |

------
#### [ AWS config file ]

You can add a `defaults_mode` configuration property to the shared AWS `config` file as the following example shows.

```
[default]
defaults_mode = auto
```

------

If you set the defaults mode globally with the system property, environment variable, or AWS config file, you can override the settings when you build an HTTP client.

When you build an HTTP client with the `httpClientBuilder()` method, settings apply only to the instance that you are building. An example of this is shown [here](http-configuration-netty.md#http-config-netty-one-client). The Netty-based HTTP client in this example overrides any default mode values set globally for `connectTimeoutInMillis` and `tlsNegotiationTimeoutInMillis`.
