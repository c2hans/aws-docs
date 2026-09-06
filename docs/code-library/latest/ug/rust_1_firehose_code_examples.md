---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/rust_1_firehose_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Firehose examples using SDK for Rust
<a name="rust_1_firehose_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with Firehose.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `PutRecordBatch`
<a name="firehose_PutRecordBatch_rust_1_topic"></a>

The following code example shows how to use `PutRecordBatch`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/firehose#code-examples).

```
async fn put_record_batch(
    client: &Client,
    stream: &str,
    data: Vec<Record>,
) -> Result<PutRecordBatchOutput, SdkError<PutRecordBatchError>> {
    client
        .put_record_batch()
        .delivery_stream_name(stream)
        .set_records(Some(data))
        .send()
        .await
}
```
+  For API details, see [PutRecordBatch](https://docs.rs/aws-sdk-firehose/latest/aws_sdk_firehose/client/struct.Client.html#method.put_record_batch) in *AWS SDK for Rust API reference*.
