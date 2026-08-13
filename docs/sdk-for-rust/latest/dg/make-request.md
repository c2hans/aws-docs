---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/make-request.html
---

# Making AWS service requests using the AWS SDK for Rust
<a name="make-request"></a>

 To programmatically access AWS services, the AWS SDK for Rust uses a client struct for each AWS service. For example, if your application needs to access Amazon EC2, your application creates an Amazon EC2 client struct to interface with that service. You then use the service client to make requests to that AWS service.

To make a request to an AWS service, you must first create and [configure](configure.md) a service client. For each AWS service your code uses, it has its own crate and its own dedicated type for interacting with it. The client exposes one method for each API operation exposed by the service.

 To interact with AWS services in AWS SDK for Rust, create a service-specific client, use its API methods with fluent builder-style chaining, and call `send()` to execute the request.

The `Client` exposes one method for each API operation exposed by the service. The return value of each of these methods is a "fluent builder", where different inputs for that API are added by builder-style function call chaining. After calling the service's methods, call `send()` to get a [`Future`](https://doc.rust-lang.org/nightly/core/future/trait.Future.html) that will result in either a successful output or a `SdkError`. For more information on `SdkError`, see [Handling errors in the AWS SDK for Rust](error-handling.md).

The following example demonstrates a basic operation using Amazon S3 to create a bucket in the `us-west-2` AWS Region:

```
let config = aws_config::defaults(BehaviorVersion::latest())
    .load()
    .await;

let s3 = aws_sdk_s3::Client::new(&config);

let result = s3.create_bucket()
    // Set some of the inputs for the operation.
    .bucket("my-bucket")
    .create_bucket_configuration(
        CreateBucketConfiguration::builder()
            .location_constraint(aws_sdk_s3::types::BucketLocationConstraint::UsWest2)
            .build()
        )
    // send() returns a Future that does nothing until awaited.
    .send()
    .await;
```

Each service crate has additional modules used for API inputs, such as the following:
+ The `types` module has structs or enums to provide more complex structured information.
+  The `primitives` module has simpler types for representing data such as date times or binary blobs.

 See the [API reference documentation](https://awslabs.github.io/aws-sdk-rust/) for the service crate for more detailed crate organization and information. For example, the `aws-sdk-s3` crate for the Amazon Simple Storage Service has several [Modules](https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/#modules). Two of which are:
+ [`aws_sdk_s3::types`](https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/types/index.html)
+ [`aws_sdk_s3::primitives`](https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/primitives/index.html)
