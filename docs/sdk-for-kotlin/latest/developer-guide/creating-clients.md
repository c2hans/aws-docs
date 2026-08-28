---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/creating-clients.html
---

# Create a service client
<a name="creating-clients"></a>

To make a request to an AWS service, you must first instantiate a client for that service.

You can configure common settings for service clients, such as the HTTP client to use, logging level, and retry configuration. Additionally, each service client requires an AWS Region and a credentials provider. The SDK uses these values to send requests to the correct Region and to sign requests with the correct credentials.

You can specify these values programmatically in code or have them automatically loaded from the environment.

## Configure a client in code
<a name="programmatic-config"></a>

To configure a service client with specific values, you can specify them in a lambda function passed to the service client factory method as shown in the following snippet.

```
val dynamoDbClient = DynamoDbClient {
    region = "us-east-1"
    credentialsProvider = ProfileCredentialsProvider(profileName = "myprofile")
}
```

Any values that you don’t specify in the configuration block are set to defaults. For instance, if you don’t specify a credentials provider as the previous code does, the credentials provider defaults to the [default credentials provider chain](credential-providers.md#default-credential-provider-chain).

**Warning**
Some properties such as `region` do not have a default. You must specify them explicitly in the configuration block when you use programmatic configuration. If the SDK can’t resolve the property, API requests may fail.

## Configure a client from the environment
<a name="loading-from-the-environment"></a>

When creating a service client, the SDK can inspect locations in the current execution environment to determine some configuration properties. Those locations include [shared config and credentials files](/sdkref/latest/guide/file-format.html), [environment variables](/sdkref/latest/guide/environment-variables.html), and [JVM system properties](/sdkref/latest/guide/jvm-system-properties.html). The properties available to be resolved include [AWS Region](region-selection.md), [retry strategy](retries.md), [log mode](logging.md#sdk-log-mode), and others. For more information on all the settings that the SDK can resolve from the execution environment, see the [AWS SDKs and Tools Settings Reference Guide](/sdkref/latest/guide/settings-reference.html).

To create a client with environment-sourced configuration, use the static method `suspend fun fromEnvironment()` on the service client interface:

```
val dynamoDbClient = DynamoDbClient.fromEnvironment()
```

Creating a client this way is useful when running on Amazon EC2, AWS Lambda, or any other context where the configuration of a service client is available from the environment. This decouples your code from the environment that it’s running in and makes it easier to deploy your application to multiple Regions without changing the code.

Additionally, you can override specific properties by passing a lambda block to `fromEnvironment`. The following example loads some configuration properties from the environment (e.g., Region) but specifically overrides the credentials provider to use credentials from a profile.

```
val dynamoDbClient = DynamoDbClient.fromEnvironment {
    credentialsProvider = ProfileCredentialsProvider(profileName = "myprofile")
}
```

The SDK uses default values for any configuration property that can’t be determined from programmatic settings or from the environment. For instance, if you don’t specify a credentials provider in code or in an environment setting, the credentials provider defaults to the [default credentials provider chain](credential-providers.md#default-credential-provider-chain).

**Warning**
Some properties such as Region do not have a default. You must specify them in an environment setting or explicitly in the configuration block. If the SDK can’t resolve the property, API requests may fail.

**Note**
Although credentials-related properties—such as temporary access keys and SSO configuration—can be found in the execution environment, the values are not sourced by the client at creation time. Instead, the values are accessed by the credentials provider layer at each request.

## Close the client
<a name="closing-the-client"></a>

When you no longer need the service client, close it to release any resources that it’s using:

```
val dynamoDbClient = DynamoDbClient.fromEnvironment()
// Invoke several DynamoDB operations.
dynamoDbClient.close()
```

Because service clients extend the [Closeable](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime.io/-closeable/index.html) interface, you can use the [use](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime.io/use.html) extension to close the client automatically at the end of a block as shown in the following snippet.

```
DynamoDbClient.fromEnvironment().use { dynamoDbClient ->
    // Invoke several DynamoDB operations.
}
```

In the previous example, the lambda block receives a reference to the client that was just created. You can invoke operations on this client reference and when the block is completed— including by throwing an exception—the client is closed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
