---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_medialive_code_examples.html
---

# MediaLive examples using SDK for Rust
<a name="rust_medialive_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with MediaLive.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `ListInputs`
<a name="medialive_ListInputs_rust_topic"></a>

The following code example shows how to use `ListInputs`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/medialive#code-examples).
List your MediaLive input names and ARNs in the Region.

```
async fn show_inputs(client: &Client) -> Result<(), Error> {
    let input_list = client.list_inputs().send().await?;

    for i in input_list.inputs() {
        let input_arn = i.arn().unwrap_or_default();
        let input_name = i.name().unwrap_or_default();

        println!("Input Name : {}", input_name);
        println!("Input ARN : {}", input_arn);
        println!();
    }

    Ok(())
}
```
+  For API details, see [ListInputs](https://docs.rs/aws-sdk-medialive/latest/aws_sdk_medialive/client/struct.Client.html#method.list_inputs) in *AWS SDK for Rust API reference*.
