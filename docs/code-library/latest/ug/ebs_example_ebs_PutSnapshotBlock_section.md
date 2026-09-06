---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ebs_example_ebs_PutSnapshotBlock_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `PutSnapshotBlock` with an AWS SDK
<a name="ebs_example_ebs_PutSnapshotBlock_section"></a>

The following code example shows how to use `PutSnapshotBlock`.

------
#### [ Rust ]

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ebs#code-examples).

```
async fn add_block(
    client: &Client,
    id: &str,
    idx: usize,
    block: Vec<u8>,
    checksum: &str,
) -> Result<(), Error> {
    client
        .put_snapshot_block()
        .snapshot_id(id)
        .block_index(idx as i32)
        .block_data(ByteStream::from(block))
        .checksum(checksum)
        .checksum_algorithm(ChecksumAlgorithm::ChecksumAlgorithmSha256)
        .data_length(EBS_BLOCK_SIZE as i32)
        .send()
        .await?;

    Ok(())
}
```
+  For API details, see [PutSnapshotBlock](https://docs.rs/aws-sdk-ebs/latest/aws_sdk_ebs/client/struct.Client.html#method.put_snapshot_block) in *AWS SDK for Rust API reference*.

------
