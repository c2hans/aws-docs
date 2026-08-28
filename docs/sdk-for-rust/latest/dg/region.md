---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/region.html
---

# Setting the AWS Region for the the AWS SDK for Rust
<a name="region"></a>

You can access AWS services that operate in a specific geographic area by using AWS Regions. This can be useful both for redundancy and to keep your data and applications running close to where you and your users access them. For more information on how Regions are used, see [AWS Region](https://docs.aws.amazon.com/sdkref/latest/guide/feature-region.html) in the *AWS SDKs and Tools Reference Guide*.

**Important**
Most resources reside in a specific AWS Region and you must supply the correct Region for the resource when using the SDK.

You must set a default AWS Region for the SDK for Rust to use for AWS requests. This default is used for any SDK service method calls that aren't specified with a Region.

For examples on how to set the default region through the shared AWS `config` file or environment variables, see [AWS Region](https://docs.aws.amazon.com/sdkref/latest/guide/feature-region.html) in the *AWS SDKs and Tools Reference Guide*.

## AWS Region provider chain
<a name="region-provider-chain"></a>

 The following lookup process is used when loading a service client's configuration from the execution environment. The first value that the SDK finds set is used in the configuration of the client. For more information on creating service clients, see [Configure a client from the environment](config-code.md#configure-a-client-from-the-environment).

1. Any explicit Region set programmatically.

1. The `AWS_REGION` environment variable is checked.
   + If you are using the AWS Lambda service, this environment variable is set automatically by the AWS Lambda container.

1. The `region` property in the shared AWS `config` file is checked.
   + The `AWS_CONFIG_FILE` environment variable can be used to change the location of the shared `config` file. To learn more about where this file is kept, see [Location of the shared `config` and `credentials` files](https://docs.aws.amazon.com/sdkref/latest/guide/file-location.html) in the *AWS SDKs and Tools Reference Guide*.
   + The `AWS_PROFILE` environment variable can be used to select a named profile instead of the default. To learn more about configuring different profiles, see [Shared `config` and `credentials` files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) in the *AWS SDKs and Tools Reference Guide*.

1. The SDK attempts to use the Amazon EC2 Instance Metadata Service to determine the Region of the currently running Amazon EC2 instance.
   + The AWS SDK for Rust only supports IMDSv2.

The `RegionProviderChain` is automatically used with no additional code when creating a basic configuration to use with a service client:

```
let config = aws_config::defaults(BehaviorVersion::latest())
    .load()
    .await;
```

## Setting the AWS Region in code
<a name="RegionProgram"></a>

### Explicitly setting the Region in code
<a name="RegionNew"></a>

Use `Region::new()` directly in your configuration when you want to explicitly set the Region.

The Region provider chain is not used - it does not check the environment, shared `config` file, or Amazon EC2 Instance Metadata Service.

```
use aws_config::{defaults, BehaviorVersion};
use aws_sdk_s3::config::Region;

#[tokio::main]
async fn main() {
    let config = defaults(BehaviorVersion::latest())
        .region(Region::new("us-west-2"))
        .load()
        .await;

    println!("Using Region: {}", config.region().unwrap());
}
```

Be sure you are entering a valid string for an AWS Region; the value provided is not validated.

### Customizing the `RegionProviderChain`
<a name="regionProviderChain"></a>

Use the [AWS Region provider chain](#region-provider-chain) when you want to inject a Region conditionally, override it, or customize the resolution chain.

```
use aws_config::{defaults, BehaviorVersion};
use aws_config::meta::region::RegionProviderChain;
use aws_sdk_s3::config::Region;
use std::env;

#[tokio::main]
async fn main() {
    let region_provider = RegionProviderChain::first_try(env::var("CUSTOM_REGION").ok().map(Region::new))
        .or_default_provider()
        .or_else(Region::new("us-east-2"));

    let config = aws_config::defaults(BehaviorVersion::latest())
        .region(region_provider)
        .load()
        .await;

    println!("Using Region: {}", config.region().unwrap());
}
```

 The previous configuration will:

1. First see if there is a string set in the `CUSTOM_REGION` environment variable.

1. If that's not available, fall back to the default Region provider chain.

1. If that fails, use "us-east-2" as the final fallback.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Rust. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-rust` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
