---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/peroperation.html
---

# Overriding a single operation configuration of a client in the AWS SDK for Rust
<a name="peroperation"></a>

After you [create a service client](config-code.md), configuration becomes immutable and will apply to all subsequent operations. While configuration can’t be modified at this point, it can be overridden on a per-operation basis.

Each operation builder has a `customize` method available to create a `CustomizableOperation` so that you can override an individual copy of the existing configuration. The original client configuration will remain unmodified.

The following example shows the creation of an Amazon S3 client that calls two operations, the second of which is overridden to send to a different AWS Region. All of Amazon S3's object invocations use the `us-east-1` region except for when the API call is explicitly overridden to use the modified `us-west-2`.

```
use aws_config::{BehaviorVersion, Region};

let config = aws_config::defaults(BehaviorVersion::latest())
    .region("us-east-1")
    .load()
    .await;

let s3 = aws_sdk_s3::Client::new(&config);

// Request will be sent to "us-east-1"
s3.list_buckets()
    .send()
    .await?;

// Unset fields default to using the original config value
let modified = aws_sdk_s3::Config::builder()
    .region(Region::from_static("us-west-2"));

// Request will be sent to "us-west-2"
s3.list_buckets()
   // Creates a CustomizableOperation
    .customize()
    .config_override(modified)
    .send()
    .await?;
```

**Note**
The previous example is for Amazon S3, however the concept is the same for all operations. Certain operations might have additional methods on `CustomizeableOperation`.

For an example of adding an interceptor using `customize` for a single operation, see [Interceptor for only a specific operation](interceptors.md#interceptors-registration-specific).
