---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ebs_example_ebs_StartSnapshot_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `StartSnapshot` with an AWS SDK
<a name="ebs_example_ebs_StartSnapshot_section"></a>

The following code example shows how to use `StartSnapshot`.

------
#### [ Rust ]

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ebs#code-examples).

```
async fn start(client: &Client, description: &str) -> Result<String, Error> {
    let snapshot = client
        .start_snapshot()
        .description(description)
        .encrypted(false)
        .volume_size(1)
        .send()
        .await?;

    Ok(snapshot.snapshot_id.unwrap())
}
```
+  For API details, see [StartSnapshot](https://docs.rs/aws-sdk-ebs/latest/aws_sdk_ebs/client/struct.Client.html#method.start_snapshot) in *AWS SDK for Rust API reference*.

------
