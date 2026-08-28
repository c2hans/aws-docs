---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/interceptors.html
---

# Configuring interceptors in the AWS SDK for Rust
<a name="interceptors"></a>

You can use interceptors to hook into the execution of API requests and responses. Interceptors are open-ended mechanisms in which the SDK calls code that you write to inject behavior into the request/response lifecycle. This way, you can modify an in-flight request, debug request processing, view errors, and more.

The following example shows a simple interceptor that adds an additional header to all outgoing requests before the retry loop is entered:

```
use std::borrow::Cow;
use aws_smithy_runtime_api::client::interceptors::{
    Intercept,
    context::BeforeTransmitInterceptorContextMut,
};
use aws_smithy_runtime_api::client::runtime_components::RuntimeComponents;
use aws_smithy_types::config_bag::ConfigBag;
use aws_smithy_runtime_api::box_error::BoxError;

#[derive(Debug)]
struct AddHeaderInterceptor {
    key: Cow<'static, str>,
    value: Cow<'static, str>,
}

impl AddHeaderInterceptor {
    fn new(key: &'static str, value: &'static str) -> Self {
        Self {
            key: Cow::Borrowed(key),
            value: Cow::Borrowed(value),
        }
    }
}

impl Intercept for AddHeaderInterceptor {
    fn name(&self) -> &'static str {
        "AddHeader"
    }

    fn modify_before_retry_loop(
        &self,
        context: &mut BeforeTransmitInterceptorContextMut<'_>,
        _runtime_components: &RuntimeComponents,
        _cfg: &mut ConfigBag,
    ) -> Result<(), BoxError> {
        let headers = context.request_mut().headers_mut();
        headers.insert(self.key.clone(), self.value.clone());

        Ok(())
    }
}
```

For more information and the available interceptor hooks, see the [Intercept](https://docs.rs/aws-smithy-runtime-api/latest/aws_smithy_runtime_api/client/interceptors/trait.Intercept.html) trait.

## Interceptor registration
<a name="interceptors-registration"></a>

You register interceptors when you construct a service client or when you override configuration for a specific operation. The registration in different depending on whether you want the interceptor to apply to all operations for your client or only specific ones.

### Interceptor for all operations on a service client
<a name="interceptors-registration-all"></a>

To register an interceptor for the entire client, add the interceptor using the `Builder` pattern.

```
let config = aws_config::defaults(BehaviorVersion::latest())
    .load()
    .await;

// All service operations invoked using 's3' will have the header added.
let s3_conf = aws_sdk_s3::config::Builder::from(&config)
    .interceptor(AddHeaderInterceptor::new("x-foo-version", "2.7"))
    .build();

let s3 = aws_sdk_s3::Client::from_conf(s3_conf);
```

### Interceptor for only a specific operation
<a name="interceptors-registration-specific"></a>

To register an interceptor for only a single operation, use the `customize` extension. You can override your service client configurations at the per-operation level using this method. For more information on customizable operations, see [Overriding a single operation configuration of a client in the AWS SDK for Rust](peroperation.md).

```
// Only the list_buckets operation will have the header added.
s3.list_buckets()
    .customize()
    .interceptor(AddHeaderInterceptor::new("x-bar-version", "3.7"))
    .send()
    .await?;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Rust. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-rust` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
