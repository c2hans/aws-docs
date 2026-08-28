---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/config-code.html
---

# Configuring AWS SDK for Swift service clients in code
<a name="config-code"></a>

When configuration is handled directly in code, the configuration scope is limited to the application that uses that code. Within that application, there are options for the global configuration of all service clients, the configuration to all clients of a certain AWS service type, or the configuration to a specific service client instance.

## Configuration data types
<a name="configurations-vary-by-service"></a>

Each AWS service has its own configuration class that you use to specify adjust options for that client type. All of these classes are based on a number of protocols that together describe all the configuration options available for that client. This includes options such as the Region and credentials, which are always needed in order to access an AWS service.

For Amazon S3, the configuration class is called `[S3Client.S3ClientConfiguration](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/s3clientconfiguration)` which is defined like this:

```
extension S3Client {
    public class S3ClientConfiguration: AWSClientRuntime.AWSDefaultClientConfiguration &
            AWSClientRuntime.AWSRegionClientConfiguration &
            ClientRuntime.DefaultClientConfiguration &
            ClientRuntime.DefaultHttpClientConfiguration {

        // Service-specific properties are defined here, including:

        public var region: Swift.String?

        // ... and so on.
   }
}
```

As a result, `S3ClientConfiguration` includes its own properties and also all the properties defined in those protocols, making it a complete description of an Amazon S3 client's configuration. Corresponding configuration classes are defined by every AWS service.

By creating a custom configuration object and using it when creating a service client object, you can customize the client by specifying a configuration source from which credentials and other options are taken. Otherwise, you can directly specify the credentials instead of letting the SDK obtain them automatically.

## Configuring a client
<a name="using-custom-configurations"></a>

When only changing common options, you can often specify the custom values for your configuration when instantiating the service’s client object. If the client class constructor doesn't support the option you need to change, then create and specify a configuration object with the type that corresponds to the client class.

### Creating a client with only a custom Region
<a name="instantiating-a-client-with-only-a-custom-region"></a>

Most services let you directly specify the Region when you call their constructors. For example, to create an Amazon S3 client configured for the Region `af-south-1`, specify the `region` parameter when creating the client, as shown.

```
do {
    let s3 = try S3Client(region: "af-south-1")

    // Use the client.
} catch {
    // Handle the error.
    dump(error, name: "Error accessing S3 service")
}
```

This lets you handle a common client configuration scenario (specifying a Region while using the default values for all other options) without going through the full configuration process. That process is covered in the next topic.

### Creating and using a custom configuration
<a name="creating-and-using-a-custom-configuration"></a>

To customize the configuration of an AWS service, create a configuration object of the appropriate type for the service. Then pass that configuration object into the service client's constructor as the value of its `config` parameter.

For example, to configure an Amazon S3 client, create an object of type `[S3Client.S3ClientConfiguration](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/s3clientconfiguration)`. Set the properties that you want to change, then pass the configuration object into `[S3Client(config:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/init(config:)-8emrd)`.

The following example creates a new Amazon S3 client configured with the following options:
+ The AWS Region is set to `us-east-1`.
+ An exponential backoff strategy with default options is selected instead of the default backoff strategy.
+ The retry mode is set to `RetryStrategyOptions.RateLimitingMode.adaptive`. See [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the *AWS SDKs and Tools Reference Guide* for details.
+ The maximum number of retries is set to 5.

```
        // Create an Amazon S3 client configuration object that specifies the
        // region as "us-east-1", an exponential backoff strategy, the
        // adaptive retry mode, and the maximum number of retries as 5.

        await SDKLoggingSystem().initialize(logLevel: .debug)

        let config: S3Client.S3ClientConfiguration

        do {
            config = try await S3Client.S3ClientConfiguration(
                awsRetryMode: .standard,
                maxAttempts: 3,
                region: "us-east-1"
            )
        } catch {
            print("Error: Unable to create configuration")
            dump(error)
            exit(1)
        }

        // Create an Amazon S3 client using the configuration created above.

        let client = S3Client(config: config)
```

If an error occurs creating the configuration, an error message is displayed and the details are dumped to the console. The program then exits. In a real world application, a more constructive approach should be taken when handling this error, such as falling back to a different configuration or using the default configuration, if doing so is appropriate for your application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Swift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-swift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
