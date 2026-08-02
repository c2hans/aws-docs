---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ebs_example_ebs_CompleteSnapshot_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CompleteSnapshot` with an AWS SDK
<a name="ebs_example_ebs_CompleteSnapshot_section"></a>

The following code example shows how to use `CompleteSnapshot`.

------
#### [ Rust ]

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ebs#code-examples).

```
async fn finish(client: &Client, id: &str) -> Result<(), Error> {
    client
        .complete_snapshot()
        .changed_blocks_count(2)
        .snapshot_id(id)
        .send()
        .await?;

    println!("Snapshot ID {}", id);
    println!("The state is 'completed' when all of the modified blocks have been transferred to Amazon S3.");
    println!("Use the get-snapshot-state code example to get the state of the snapshot.");

    Ok(())
}
```
+  For API details, see [CompleteSnapshot](https://docs.rs/aws-sdk-ebs/latest/aws_sdk_ebs/client/struct.Client.html#method.complete_snapshot) in *AWS SDK for Rust API reference*.

------
