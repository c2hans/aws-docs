---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/paginating.html
---

# Using paginated results in the AWS SDK for Rust
<a name="paginating"></a>

Many AWS operations return truncated results when the payload is too large to return in a single response. Instead, the service returns a portion of the data and a token to retrieve the next set of items. This pattern is known as pagination.

The AWS SDK for Rust includes extension methods `into_paginator` on operation builders that can be used to automatically paginate the results for you. You only have to write the code that processes the results. All pagination operation builders have an `into_paginator()` method available that exposes a [`PaginationStream<Item>`](https://docs.rs/aws-smithy-async/latest/aws_smithy_async/future/pagination_stream/struct.PaginationStream.html) to paginate over the results.
+ In Amazon S3, one example of this is [`aws_sdk_s3::operation::list_objects_v2::builders::ListObjectsV2FluentBuilder::into_paginator`](https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/operation/list_objects_v2/builders/struct.ListObjectsV2FluentBuilder.html#method.into_paginator).

The following examples use Amazon Simple Storage Service. However, the concepts are the same for any service that has one or more paginated APIs.

 The following code example shows the simplest example that uses the [`try_collect()`](https://docs.rs/aws-smithy-async/latest/aws_smithy_async/future/pagination_stream/struct.PaginationStream.html#method.try_collect) method to collect all paginated results into a `Vec`:

```
let config = aws_config::defaults(BehaviorVersion::latest())
    .load()
    .await;

let s3 = aws_sdk_s3::Client::new(&config);

let all_objects = s3.list_objects_v2()
    .bucket("my-bucket")
    .into_paginator()
    .send()
    .try_collect()
    .await?
    .into_iter()
    .flat_map(|o| o.contents.unwrap_or_default())
    .collect::<Vec<_>>();
```

Sometimes, you want to have more control over paging and not pull everything into memory all at once. The following example iterates over objects in an Amazon S3 bucket until there are no more.

```
let config = aws_config::defaults(BehaviorVersion::latest())
    .load()
    .await;

let s3 = aws_sdk_s3::Client::new(&config);

let mut paginator = s3.list_objects_v2()
    .bucket("my-bucket")
    .into_paginator()
    // customize the page size (max results per/response)
    .page_size(10)
    .send();

println!("Objects in bucket:");

while let Some(result) = paginator.next().await {
    let resp = result?;
    for obj in resp.contents() {
        println!("\t{:?}", obj);
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Rust. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-rust` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
