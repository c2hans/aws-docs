---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_mediapackage_code_examples.html
---

# MediaPackage examples using SDK for Rust
<a name="rust_mediapackage_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with MediaPackage.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `ListChannels`
<a name="mediapackage_ListChannels_rust_topic"></a>

The following code example shows how to use `ListChannels`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/mediapackage#code-examples).
List channel ARNs and descriptions.

```
async fn show_channels(client: &Client) -> Result<(), Error> {
    let list_channels = client.list_channels().send().await?;

    println!("Channels:");

    for c in list_channels.channels() {
        let description = c.description().unwrap_or_default();
        let arn = c.arn().unwrap_or_default();

        println!("  Description : {}", description);
        println!("  ARN :         {}", arn);
        println!();
    }

    Ok(())
}
```
+  For API details, see [ListChannels](https://docs.rs/aws-sdk-mediapackage/latest/aws_sdk_mediapackage/client/struct.Client.html#method.list_channels) in *AWS SDK for Rust API reference*.

### `ListOriginEndpoints`
<a name="mediapackage_ListOriginEndpoints_rust_topic"></a>

The following code example shows how to use `ListOriginEndpoints`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/mediapackage#code-examples).
List your endpoint descriptions and URLs.

```
async fn show_endpoints(client: &Client) -> Result<(), Error> {
    let or_endpoints = client.list_origin_endpoints().send().await?;

    println!("Endpoints:");

    for e in or_endpoints.origin_endpoints() {
        let endpoint_url = e.url().unwrap_or_default();
        let endpoint_description = e.description().unwrap_or_default();
        println!("  Description: {}", endpoint_description);
        println!("  URL :        {}", endpoint_url);
        println!();
    }

    Ok(())
}
```
+  For API details, see [ListOriginEndpoints](https://docs.rs/aws-sdk-mediapackage/latest/aws_sdk_mediapackage/client/struct.Client.html#method.list_origin_endpoints) in *AWS SDK for Rust API reference*.
