---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/configuring-service-clients-ext.html
---

# Configuring service clients for the AWS SDK for Java 2.x externally
<a name="configuring-service-clients-ext"></a>

Many configuration settings can be handled outside of your code. When you handle configuration externally, it can apply to all your applications in the same Java process. Most configuration settings can be set as either environment variables, JVM system properties, or in a separate shared AWS `config` file. The shared `config` file can maintain separate sets of settings, called profiles, to provide different configurations for different environments or tests.

Most environment variables and shared `config` file settings are standardized and shared across AWS SDKs and tools to support consistent functionality across different programming languages and applications. In most cases, the JVM system properties that the SDK for Java can use mirror the environment variables.

See the *[AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/overview.html)* to learn about configuring your application through these methods, plus details on each cross-sdk setting. To see all the all settings that the SDK can resolve from the environment variables, JVM system properties, or configuration files, see the [Settings reference](https://docs.aws.amazon.com/sdkref/latest/guide/settings-reference.html) in the *AWS SDKs and Tools Reference Guide*.

## Configuration provider chain for client configuration
<a name="configuration-provider-chain"></a>

The SDK checks several places (or sources) to find configuration values.

1. Any explicit setting set in the code or on a service client itself takes precedence over anything else.

1. JVM system properties
   + For details on setting JVM system properties, see [How to set JVM system properties](https://docs.aws.amazon.com/sdkref/latest/guide/jvm-system-properties.html#jvm-sys-props-set) in the *AWS SDKs and Tools Reference Guide*.

1. Environment variables
   + For details on setting environment variables, see [environment variables](https://docs.aws.amazon.com/sdkref/latest/guide/environment-variables.html) in the *AWS SDKs and Tools Reference Guide*.
   + Note that you can configure environment variables for a shell at different levels of scope: system-wide, user-wide, and for a specific terminal session.

1. Shared `config` and `credentials` files
   + For details on setting up these files, see the [Shared `config` and `credentials` files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) in the *AWS SDKs and Tools Reference Guide*.

1. Any default value provided by the SDK source code itself is used last.
   + Some properties, such as Region, don't have a default. You must specify them either explicitly in code, in an environment setting, or in the shared `config` file. If the SDK can't resolve required configuration, API requests can fail at runtime.

Besides this general configuration chain, the SDK for Java 2.x also uses specialized provider chains including the [credentials provider chain](credentials-chain.md) and the [AWS Region provider chain](region-selection.md#default-region-provider-chain). These specialized chains add additional providers that take into account the environment that the SDK is running in. For example, in a container or an EC2 instance.

## Create a service client configured using external settings
<a name="create-client-ext-conf"></a>

You need to create a service client in your application to talk to an AWS service. Service clients are your essential connection to AWS services, handling all the complex communication details so you don't have to worry about them. They take care of important tasks like security, error handling, and retries automatically, letting you focus on building your application rather than dealing with technical complications.

### Use the `create()` method
<a name="create-client-ext-builder"></a>

If all configuration settings that you need are coming from external sources, you can create a service client with a simple method:

```
S3Client s3Client = S3Client.create();
```

The previous code snippet creates an `S3Client` instance. During creation, the SDK looks through the configuration provider chain for settings. Once the SDK finds a setting value, the value will be used even if configuration exists that is later in the chain.

For example, assume a users sets the JVM setting for the AWS Region by setting the system property `-Daws.region=us-west-2`. If the `AWS_REGION` environment variable is also set, its value is ignored.

The default region provider chain and the default credentials provider chain will also be used in the creation process. Somewhere in the chain, the SDK must resolve the AWS Region to use and find settings that enable it to retrieve credentials for signing requests. If the SDKs files to find those values, the client creation fails.

Although you can create a client by using this empty builder pattern, you generally use this pattern when you want to [add configuration in code](configuring-service-clients-code.md#conf-service-client-code-basic).

## SDK for Java 2.x environment variables and JVM system properties
<a name="java-ext-config"></a>

Beyond the [cross-sdk settings](https://docs.aws.amazon.com/sdkref/latest/guide/settings-reference.html#settingsPages) supported by most AWS SDKs, the SDK for Java 2.x provides the following settings.

**Note**
These environment variables and JVM system properties are primarily intended for advanced use cases, testing, or specific deployment scenarios. In most application code, it's preferable to use the programmatic configuration options provided by the SDK's client builders for better type safety and IDE support.

### Container Credential Provider Environment Variables
<a name="java-cred-profvider-envars"></a>

In addition to the standard container credential environment variables documented in the reference guide, the SDK also supports:

`AWS_CONTAINER_SERVICE_ENDPOINT`–This environment variable specifies the endpoint for the container metadata service when using the container credentials provider.

Java system property: `aws.containerServiceEndpoint`

Default value: `http://169.254.170.2`

### HTTP Client Implementation Environment Variables
<a name="java-http-cli-impl-envars"></a>

`SYNC_HTTP_SERVICE_IMPL`–Explicitly identifies the default [synchronous HTTP implementation](http-configuration.md#http-config-sync) the SDK will use. This is useful when there are multiple implementations on the classpath or as a performance optimization since implementation discovery requires classpath scanning.

Java system property: `software.amazon.awssdk.http.service.impl`

`ASYNC_HTTP_SERVICE_IMPL`–Explicitly identifies the default [asynchronous HTTP implementation](http-configuration.md#http-config-async) the SDK will use. This is useful when there are multiple implementations on the classpath or as a performance optimization since implementation discovery requires classpath scanning.

Java system property: `software.amazon.awssdk.http.async.service.impl`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
