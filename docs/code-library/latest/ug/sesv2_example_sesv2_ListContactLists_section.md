---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sesv2_example_sesv2_ListContactLists_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListContactLists` with an AWS SDK
<a name="sesv2_example_sesv2_ListContactLists_section"></a>

The following code example shows how to use `ListContactLists`.

------
#### [ Rust ]

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ses#code-examples).

```
async fn show_lists(client: &Client) -> Result<(), Error> {
    let resp = client.list_contact_lists().send().await?;

    println!("Contact lists:");

    for list in resp.contact_lists() {
        println!("  {}", list.contact_list_name().unwrap_or_default());
    }

    Ok(())
}
```
+  For API details, see [ListContactLists](https://docs.rs/aws-sdk-sesv2/latest/aws_sdk_sesv2/client/struct.Client.html#method.list_contact_lists) in *AWS SDK for Rust API reference*.

------
