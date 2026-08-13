---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/config-code.html
---

# Configuring AWS SDK for Rust service clients in code
<a name="config-code"></a>

When configuration is handled directly in code, the configuration scope is limited to the application that uses that code. Within that application, there are options for the global configuration of all service clients, the configuration to all clients of a certain AWS service type, or the configuration to a specific service client instance.

To make a request to an AWS service, you first instantiate a client for that service. You can configure common settings for service clients such as timeouts, the HTTP client, and retry configuration.

Each service client requires an AWS Region and a credential provider. The SDK uses these values to send requests to the correct Region for your resources and to sign requests with the correct credentials. You can specify these values programmatically in code or have them automatically loaded from the environment.

**Note**
Service clients can be expensive to construct and are generally meant to be shared. To facilitate this, all `Client` structs implement `Clone`.

## Configure a client from the environment
<a name="configure-a-client-from-the-environment"></a>

To create a client with environment-sourced configuration, use static methods from the `aws-config` crate:

```
let config = aws_config::defaults(BehaviorVersion::latest())
    .load()
    .await;

let s3 = aws_sdk_s3::Client::new(&config);
```

Creating a client this way is useful when running on Amazon Elastic Compute Cloud, AWS Lambda, or any other context where the configuration of a service client is available directly from the environment. This decouples your code from the environment that it's running in and makes it easier to deploy your application to multiple AWS Regions without changing the code.

You can explicitly override specific properties. Explicit configuration takes precedence over configuration resolved from the execution environment. The following example loads configuration from the environment, but explicitly overrides the AWS Region:

```
let config = aws_config::defaults(BehaviorVersion::latest())
    .region("us-east-1")
    .load()
    .await;

let s3 = aws_sdk_s3::Client::new(&config);
```

**Note**
Not all configuration values are sourced by the client at creation time. Credential-related settings, such as temporary access keys and IAM Identity Center configuration, are accessed by the credential provider layer when the client is used to make a request.

The code `BehaviorVersion::latest()` shown in the prior examples indicates the version of the SDK to use for defaults. `BehaviorVersion::latest()` is appropriate for most cases. For details, see [Using behavior versions in the AWS SDK for Rust](behavior-versions.md).

## Use the builder pattern for service-specific settings
<a name="configure-a-client-builder"></a>

There are some options that can only be configured on a specific service client type. However, most often, you'll still want to load the majority of configuration from the environment, and then specifically add the additional options. The builder pattern is a common pattern within the AWS SDK for Rust crates. You first load the general configuration using `aws_config::defaults`, then use the `from` method to load that configuration into the builder for the service you are working with. You can then set any unique configuration values for that service and call `build`. Lastly, the client is created from this modfied configuration.

```
// Call a static method on aws-config that sources default config values.
let config = aws_config::defaults(BehaviorVersion::latest())
    .load()
    .await;

// Use the Builder for S3 to create service-specific config from the default config.
let s3_config = aws_sdk_s3::config::Builder::from(&config)
    .accelerate(true) // Set an S3-only configuration option
    .build();

// Create the client.
let s3 = aws_sdk_s3::Client::from_conf(s3_config);
```

One way to discover additional methods that are available for a specific type of service client is to use the API documentation, such as for [`aws_sdk_s3::config::Builder`](https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/config/struct.Builder.html).

## Advanced explicit client configuration
<a name="configure-a-client-explicitly"></a>

To configure a service client with specific values instead of loading a configuration from the environment, you can specify them on the client `Config` builder as shown in the following:

```
let conf = aws_sdk_s3::Config::builder()
    .region("us-east-1")
    .endpoint_resolver(my_endpoint_resolver)
    .build();

let s3 = aws_sdk_s3::Client::from_conf(conf);
```

When you create a service configuration with `aws_sdk_s3::Config::builder()`, *no default configuration is loaded*. Defaults are only loaded when creating a config based on `aws_config::defaults`.

There are some options that can only be configured on a specific service client type. The previous example shows an example of this by using the `endpoint_resolver` function on a Amazon S3 client.
