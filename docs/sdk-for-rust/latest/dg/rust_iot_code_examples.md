---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_iot_code_examples.html
---

# AWS IoT examples using SDK for Rust
<a name="rust_iot_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with AWS IoT.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `DescribeEndpoint`
<a name="iot_DescribeEndpoint_rust_topic"></a>

The following code example shows how to use `DescribeEndpoint`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iot#code-examples).

```
async fn show_address(client: &Client, endpoint_type: &str) -> Result<(), Error> {
    let resp = client
        .describe_endpoint()
        .endpoint_type(endpoint_type)
        .send()
        .await?;

    println!("Endpoint address: {}", resp.endpoint_address.unwrap());

    println!();

    Ok(())
}
```
+  For API details, see [DescribeEndpoint](https://docs.rs/aws-sdk-iot/latest/aws_sdk_iot/client/struct.Client.html#method.describe_endpoint) in *AWS SDK for Rust API reference*.

### `ListThings`
<a name="iot_ListThings_rust_topic"></a>

The following code example shows how to use `ListThings`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/iot#code-examples).

```
async fn show_things(client: &Client) -> Result<(), Error> {
    let resp = client.list_things().send().await?;

    println!("Things:");

    for thing in resp.things.unwrap() {
        println!(
            "  Name:  {}",
            thing.thing_name.as_deref().unwrap_or_default()
        );
        println!(
            "  Type:  {}",
            thing.thing_type_name.as_deref().unwrap_or_default()
        );
        println!(
            "  ARN:   {}",
            thing.thing_arn.as_deref().unwrap_or_default()
        );
        println!();
    }

    println!();

    Ok(())
}
```
+  For API details, see [ListThings](https://docs.rs/aws-sdk-iot/latest/aws_sdk_iot/client/struct.Client.html#method.list_things) in *AWS SDK for Rust API reference*.
