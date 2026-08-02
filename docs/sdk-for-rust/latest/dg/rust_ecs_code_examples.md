---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_ecs_code_examples.html
---

# Amazon ECS examples using SDK for Rust
<a name="rust_ecs_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with Amazon ECS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `CreateCluster`
<a name="ecs_CreateCluster_rust_topic"></a>

The following code example shows how to use `CreateCluster`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ecs#code-examples).

```
async fn make_cluster(client: &aws_sdk_ecs::Client, name: &str) -> Result<(), aws_sdk_ecs::Error> {
    let cluster = client.create_cluster().cluster_name(name).send().await?;
    println!("cluster created: {:?}", cluster);

    Ok(())
}
```
+  For API details, see [CreateCluster](https://docs.rs/aws-sdk-ecs/latest/aws_sdk_ecs/client/struct.Client.html#method.create_cluster) in *AWS SDK for Rust API reference*.

### `DeleteCluster`
<a name="ecs_DeleteCluster_rust_topic"></a>

The following code example shows how to use `DeleteCluster`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ecs#code-examples).

```
async fn remove_cluster(
    client: &aws_sdk_ecs::Client,
    name: &str,
) -> Result<(), aws_sdk_ecs::Error> {
    let cluster_deleted = client.delete_cluster().cluster(name).send().await?;
    println!("cluster deleted: {:?}", cluster_deleted);

    Ok(())
}
```
+  For API details, see [DeleteCluster](https://docs.rs/aws-sdk-ecs/latest/aws_sdk_ecs/client/struct.Client.html#method.delete_cluster) in *AWS SDK for Rust API reference*.

### `DescribeClusters`
<a name="ecs_DescribeClusters_rust_topic"></a>

The following code example shows how to use `DescribeClusters`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ecs#code-examples).

```
async fn show_clusters(client: &aws_sdk_ecs::Client) -> Result<(), aws_sdk_ecs::Error> {
    let resp = client.list_clusters().send().await?;

    let cluster_arns = resp.cluster_arns();
    println!("Found {} clusters:", cluster_arns.len());

    let clusters = client
        .describe_clusters()
        .set_clusters(Some(cluster_arns.into()))
        .send()
        .await?;

    for cluster in clusters.clusters() {
        println!("  ARN:  {}", cluster.cluster_arn().unwrap());
        println!("  Name: {}", cluster.cluster_name().unwrap());
    }

    Ok(())
}
```
+  For API details, see [DescribeClusters](https://docs.rs/aws-sdk-ecs/latest/aws_sdk_ecs/client/struct.Client.html#method.describe_clusters) in *AWS SDK for Rust API reference*.
