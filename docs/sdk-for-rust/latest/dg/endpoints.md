---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/endpoints.html
---

# Configuring client endpoints in the AWS SDK for Rust
<a name="endpoints"></a>

When the AWS SDK for Rust calls an AWS service, one of its first steps is to determine where to route the request. This process is known as endpoint resolution.

You can configure endpoint resolution for the SDK when you create a service client. The default configuration for endpoint resolution is usually fine, but there are several reasons why you might want to modify the default configuration. Two example reasons are as follows:
+ To make requests to a pre-release version of a service or to a local deployment of a service.
+ To access to specific service features not yet modeled in the SDK.

**Warning**
Endpoint resolution is an advanced SDK topic. If you change the default settings, you risk breaking your code. The default settings apply to most users in production environments.

Custom endpoints can be set globally so that they are used for all service requests, or you can set a custom endpoint for a specific AWS service.

Custom endpoints can be configured using environment variables or settings in the shared AWS `config` file. For information on this approach, see [Service-specific endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-ss-endpoints.html) in the *AWS SDKs and Tools Reference Guide*. For the complete list of shared `config` file settings and environment variables for all AWS services, see [Identifiers for service-specific endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/ss-endpoints-table.html).

 Alternatively, this customization can also be configured in your code, as shown in the following sections.

## Custom Configuration
<a name="custom-configuration"></a>

You can customize endpoint resolution of a service client with two methods that are available when you build the client:

1. `endpoint_url(url: Into<String>)`

1. `endpoint_resolver(resolver: impl crate::config::endpoint::ResolveEndpoint + `static)`

You can set both properties. However, most often you provide only one. For general usage, `endpoint_url` is most frequently customized.

### Set endpoint URL
<a name="set-endpoint-url"></a>

You can set a value for `endpoint_url` to indicate a "base" hostname for the service. This value, however, is not final since it is passed as a parameter to the client's `ResolveEndpoint` instance. The `ResolveEndpoint` implementation can then inspect and potentially modify that value to determine the final endpoint.

### Set endpoint resolver
<a name="set-endpoint-resolver"></a>

A service client's `ResolveEndpoint` implementation determines the final resolved endpoint that the SDK uses for any given request. A service client calls the `resolve_endpoint` method for every request and uses the [https://docs.rs/aws-smithy-runtime-api/latest/aws_smithy_runtime_api/client/endpoint/struct.EndpointFuture.html](https://docs.rs/aws-smithy-runtime-api/latest/aws_smithy_runtime_api/client/endpoint/struct.EndpointFuture.html) value that is returned by the resolver with no further changes.

The following example demonstrates supplying a custom endpoint resolver implementation for an Amazon S3 client that resolves a different endpoint per-stage, such as staging and production:

```
use aws_sdk_s3::config::endpoint::{ResolveEndpoint, EndpointFuture, Params, Endpoint};

#[derive(Debug)]
struct StageResolver { stage: String }
impl ResolveEndpoint for StageResolver {
    fn resolve_endpoint(&self, params: &Params) -> EndpointFuture<'_> {
        let stage = &self.stage;
        EndpointFuture::ready(Ok(Endpoint::builder().url(format!("{stage}.myservice.com")).build()))
    }
}

let config = aws_config::defaults(BehaviorVersion::latest())
    .load()
    .await;

let resolver = StageResolver { stage: std::env::var("STAGE").unwrap() };

let s3_config = aws_sdk_s3::config::Builder::from(&config)
    .endpoint_resolver(resolver)
    .build();

let s3 = aws_sdk_s3::Client::from_conf(s3_config);
```

**Note**
Endpoint resolvers, and by extension the `ResolveEndpoint` trait, are specific to each service, and thus can only be configured on the service client config. Endpoint URL, on the other hand, can be configured either using shared config (applying to all services derived from it) or for a specific service.

#### ResolveEndpoint parameters
<a name="resolveendpoint-parameters"></a>

The `resolve_endpoint` method accepts service-specific parameters that contain properties used in endpoint resolution.

Every service includes the following base properties:

| Name | Type | Description |
| --- | --- | --- |
| region | String | The client's AWS Region |
| endpoint | String | A string representation of the value set of endpointUrl |
| use\_fips | Boolean | Whether FIPS endpoints are enabled in the client's configuration |
| use\_dual\_stack | Boolean | Whether dual-stack endpoints are enabled in the client's configuration |

AWS services can specify additional properties required for resolution. For example, Amazon S3 [endpoint parameters](https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/config/endpoint/struct.Params.html) includes the bucket name and also several Amazon S3-specific feature settings. For example, the `force_path_style` property determines whether virtual host addressing can be used.

If you implement your own provider, you shouldn't need to construct your own instance of endpoint parameters. The SDK provides the properties for each request and passes them to your implementation of `resolve_endpoint`.

### Compare using `endpoint_url` to using `endpoint_resolver`
<a name="endpoint-url-or-endpoint-resolver"></a>

It is important to understand that the following two configurations, one that uses `endpoint_url` and the other that uses `endpoint_resolver`, do NOT produce clients with equivalent endpoint resolution behavior.

```
use aws_sdk_s3::config::endpoint::{ResolveEndpoint, EndpointFuture, Params, Endpoint};

#[derive(Debug, Default)]
struct CustomResolver;
impl ResolveEndpoint for CustomResolver {
    fn resolve_endpoint(&self, _params: &Params) -> EndpointFuture<'_> {
        EndpointFuture::ready(Ok(Endpoint::builder().url("https://endpoint.example").build()))
    }
}

let config = aws_config::defaults(BehaviorVersion::latest())
    .load()
    .await;

// use endpoint url
aws_sdk_s3::config::Builder::from(&config)
    .endpoint_url("https://endpoint.example")
    .build();

// Use endpoint resolver
aws_sdk_s3::config::Builder::from(&config)
    .endpoint_resolver(CustomResolver::default())
    .build();
```

The client that sets the `endpoint_url` specifies a *base* URL that is passed to the (default) provider, that can be modified as part of endpoint resolution.

The client that sets the `endpoint_resolver` specifies the *final* URL the Amazon S3 client uses.

## Examples
<a name="endpointsExamples"></a>

Custom endpoints are often used for testing. Instead of making calls out to the cloud-based service, calls are routed to a locally-hosted, simulated service. Two such options are:
+ [DynamoDB local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) – a local version of the Amazon DynamoDB service.
+ [LocalStack](https://github.com/localstack/localstack) – a cloud service emulator that runs in a container on your local machine.

 The following examples illustrate two different ways to specify a custom endpoint to use these two testing options.

### Use DynamoDB local directly in code
<a name="endpointsExamplesddb"></a>

As described in the previous sections, you can set `endpoint_url` directly in code to override the base endpoint to point to the local DynamoDB server. In your code:

```
    let config = aws_config::defaults(aws_config::BehaviorVersion::latest())
        .test_credentials()
        // DynamoDB run locally uses port 8000 by default.
        .endpoint_url("http://localhost:8000")
        .load()
        .await;
    let dynamodb_local_config = aws_sdk_dynamodb::config::Builder::from(&config).build();

    let client = aws_sdk_dynamodb::Client::from_conf(dynamodb_local_config);
```

The [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/dynamodb/src/bin/list-tables-local.rs) is available on GitHub.

### Use LocalStack using the `config` file
<a name="endpointsExamplesLs"></a>

You can set [service-specific endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-ss-endpoints.html) in your shared AWS `config` file. The following configuration profile sets `endpoint_url` to connect to `localhost` on port `4566`. For more information on LocalStack configuration, see [Accessing LocalStack via the endpoint URL](https://docs.localstack.cloud/references/network-troubleshooting/endpoint-url/) on the *LocalStack docs* website.

```
[profile {{localstack}}]
region=us-east-1
endpoint_url = http://localhost:4566
```

The SDK will pick up the changes in the shared `config` file and apply them to your SDK clients when you use the `localstack` profile. Using this approach, your code doesn't need to include any reference to endpoints, and would look like:

```
    // set the environment variable `AWS_PROFILE=localstack` when running
    // the application to source `endpoint_url` and point the SDK at the
    // localstack instance
    let config = aws_config::defaults(BehaviorVersion::latest()).load().await;

    let s3_config = aws_sdk_s3::config::Builder::from(&config)
        .force_path_style(true)
        .build();

    let s3 = aws_sdk_s3::Client::from_conf(s3_config);
```

The [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/localstack) is available on GitHub.
