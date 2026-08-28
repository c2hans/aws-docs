---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/waiters.html
---

# Using waiters in the AWS SDK for Rust
<a name="waiters"></a>

 Waiters are a client-side abstraction used to poll a resource until a desired state is reached, or until it is determined that the resource will not enter the desired state. This is a common task when working with services that are eventually consistent, like Amazon Simple Storage Service, or services that asynchronously create resources, like Amazon Elastic Compute Cloud. Writing logic to continuously poll the status of a resource can be cumbersome and error-prone. The goal of waiters is to move this responsibility out of customer code and into the AWS SDK for Rust, which has in-depth knowledge of the timing aspects for the AWS operation.

AWS services that provide support for waiters include a `{{<service>}}::waiters` module.
+ The `{{<service>}}::client::Waiters` trait provides waiter methods for the client. The methods are implemented for the `Client` struct. All waiter methods follow a standard naming convention of `wait_until_{{<Condition>}}`
  + For Amazon S3, this trait is [`aws_sdk_s3::client::Waiters`](https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/client/trait.Waiters.html).

The following example uses Amazon S3. However, the concepts are the same for any AWS service that has one or more waiters defined.

The following code example shows using a waiter function instead of writing polling logic to wait for a bucket to exist after being created.

```
use std::time::Duration;
use aws_config::BehaviorVersion;
// Import Waiters trait to get `wait_until_<Condition>` methods on Client.
use aws_sdk_s3::client::Waiters;

let config = aws_config::defaults(BehaviorVersion::latest())
    .load()
    .await;

let s3 = aws_sdk_s3::Client::new(&config);

// This initiates creating an S3 bucket and potentially returns before the bucket exists.
s3.create_bucket()
    .bucket("my-bucket")
    .send()
    .await?;

// When this function returns, the bucket either exists or an error is propagated.
s3.wait_until_bucket_exists()
    .bucket("my-bucket")
    .wait(Duration::from_secs(5))
    .await?;

// The bucket now exists.
```

**Note**
 Each wait method returns a `Result<FinalPoll<...>, WaiterError<...>> ` that can be used to get at the final response from reaching the desired condition or an error. See [FinalPoll](https://docs.rs/aws-smithy-runtime-api/latest/aws_smithy_runtime_api/client/waiters/struct.FinalPoll.html) and [WaiterError](https://docs.rs/aws-smithy-runtime-api/latest/aws_smithy_runtime_api/client/waiters/error/enum.WaiterError.html) in the Rust API documentation for details.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Rust. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-rust` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
