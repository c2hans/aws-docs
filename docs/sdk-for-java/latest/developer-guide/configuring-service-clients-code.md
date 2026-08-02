---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/configuring-service-clients-code.html
---

# Configuring service clients in code for the AWS SDK for Java 2.x
<a name="configuring-service-clients-code"></a>

As an alternative to—or in addition to—[configuring service clients externally](configuring-service-clients-ext.md), you can configure them programmatically in code.

By configuring service clients in code, you gain fine-grained control of the many options available to you. Most of the configuration that you can set externally are also available for you to set in code.

## Basic configuration in code
<a name="conf-service-client-code-basic"></a>

For example, the following snippet sets the AWS Region to `EU_SOUTH_2` for an Amazon S3 service client in code:

```
S3Client s3Client = S3Client.builder()
        .region(Region.EU_SOUTH_2)
        .build();
```

The previous snippet shows the static factory method, `builder()`. The `builder()` method returns a `builder` object that allows you to customize the service client. The fluent setter methods return the `builder` object—in this case, an [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3ClientBuilder.html](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3ClientBuilder.html) instance—so that you can chain the method calls for convenience and for more readable code. After you configure the properties you want, call the `build()` method to create the client.

## Advanced configuration in code
<a name="conf-service-client-code-several"></a>

The following snippet shows additional configuration options:

```
ClientOverrideConfiguration clientOverrideConfiguration =
        ClientOverrideConfiguration.builder()
                .apiCallAttemptTimeout(Duration.ofSeconds(1))
                .addMetricPublisher(CloudWatchMetricPublisher.create())
                .build();

S3Client s3Client = S3Client.builder()
        .region(Region.EU_SOUTH_2)
        .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
        .overrideConfiguration(clientOverrideConfiguration)
        .httpClientBuilder(
                ApacheHttpClient.builder()
                        .maxConnections(100)
                        .connectionTimeout(Duration.ofSeconds(5))
                        .proxyConfiguration(ProxyConfiguration.builder()
                                .endpoint(URI.create("http://proxy:8080"))
                                .build())
        ).build();
```

In the previous snippet, you can see several entry points to configure a service client:
+ [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/client/config/ClientOverrideConfiguration.Builder.html](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/client/config/ClientOverrideConfiguration.Builder.html) that provides configuration options common across all service clients. These settings are AWS-specific behaviors independent of any HTTP implementation.
+ **HTTP client configuration through a separate HTTP client builder implementation.** The `ApacheHttpClient.Builder` is an example. The service client provides the `httpClientBuilder()` method to associate the configured HTTP client to the service client.
+ **Methods on the [client builder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3ClientBuilder.html) itself,** such as `region()` and `credentialsProvider()`

### Same configuration using configuration blocks
<a name="service-client-config-lambda"></a>

Instead of creating separate objects and then passing them to service client methods, the AWS SDK for Java 2.x provides methods that accept lambda expressions to build these objects inline. The configuration methods on the builder are named the same, but have different signatures. For example:
+ [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/client/builder/SdkClientBuilder.html#overrideConfiguration(software.amazon.awssdk.core.client.config.ClientOverrideConfiguration)](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/client/builder/SdkClientBuilder.html#overrideConfiguration(software.amazon.awssdk.core.client.config.ClientOverrideConfiguration))
+ [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/client/builder/SdkClientBuilder.html#overrideConfiguration(java.util.function.Consumer)](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/client/builder/SdkClientBuilder.html#overrideConfiguration(java.util.function.Consumer))

The configuration of the S3 client shown earlier using this approach can be done in one block of code:

```
S3Client s3Client = S3Client.builder()
        .region(Region.EU_SOUTH_2)
        .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
        .overrideConfiguration(b -> b
                .apiCallAttemptTimeout(Duration.ofSeconds(1))
                .addMetricPublisher(CloudWatchMetricPublisher.create()))
        .httpClientBuilder(ApacheHttpClient.builder()
                .maxConnections(100)
                .connectionTimeout(Duration.ofSeconds(5))
                .proxyConfiguration(ProxyConfiguration.builder()
                        .endpoint(URI.create("http://proxy:8080"))
                        .build()))
        .build();
```

## Configuration options unavailable in code
<a name="conf-servic-client-only-ext"></a>

Because the following setting affect fundamental initialization processes in the SDK, you can set the following configuration settings only externally and not in code:

### File Location Settings
<a name="code-only-conf-file-loc"></a>

These settings control the location of the shared config and credentials files and cannot be overridden programmatically after the SDK has loaded them:
+ **AWS\_CONFIG\_FILE** (environment variable) / **aws.configFile**(JVM system property)
+ **AWS\_SHARED\_CREDENTIALS\_FILE** (environment variable) / **aws.sharedCredentialsFile** (JVM system property)

These settings must be set before the SDK loads the configuration files, as they determine where the SDK looks for configuration. Once the SDK has initialized, changing these values has no effect.

### Instance Metadata Service Disablement
<a name="code-only-conf-imds"></a>
+ **AWS\_EC2\_METADATA\_DISABLED** (environment variable) / **aws.disableEc2Metadata** (JVM system property)

This setting controls whether the SDK attempts to use the EC2 Instance Metadata Service at all. Once the SDK has initialized, you can't change this setting programmatically.

### Profile Selection
<a name="code-only-conf-profile"></a>
+ **AWS\_PROFILE** (environment variable) / **aws.profile** (JVM system property)

This setting tells the SDK which profile to load from the shared config and credentials files. Once loaded, changing this value has no effect.

### Container Credential Paths
<a name="code-only-conf-container-cred-path"></a>
+ **AWS\_CONTAINER\_CREDENTIALS\_RELATIVE\_URI**
+ **AWS\_CONTAINER\_CREDENTIALS\_FULL\_URI**
+ **AWS\_CONTAINER\_AUTHORIZATION\_TOKEN**
+ **AWS\_CONTAINER\_AUTHORIZATION\_TOKEN\_FILE**

You use these environment variables to tell the SDK how to fetch credentials from container services. After the credential provider chain has been established during service client initialization, you can't change these settings.

### Default HTTP Implementation Selection
<a name="code-only-conf-http-impl"></a>
+ **SYNC\_HTTP\_SERVICE\_IMPL** (environment variable) / **software.amazon.awssdk.http.service.impl** (JVM system property)
+ **ASYNC\_HTTP\_SERVICE\_IMPL** (environment variable) / **software.amazon.awssdk.http.async.service.impl** (JVM system property)

These global settings determine which HTTP client implementation the SDK uses for all service clients unless overridden in code for individual service clients. You must set these before the SDK initializes its HTTP clients and cannot be changed afterward.
