---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/medialive_example_medialive_ListInputs_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListInputs` with an AWS SDK
<a name="medialive_example_medialive_ListInputs_section"></a>

The following code example shows how to use `ListInputs`.

------
#### [ Rust ]

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

------
