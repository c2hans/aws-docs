---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/rust_1_route-53_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Route 53 examples using SDK for Rust
<a name="rust_1_route-53_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with Route 53.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `ListHostedZones`
<a name="route-53_ListHostedZones_rust_1_topic"></a>

The following code example shows how to use `ListHostedZones`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/route53#code-examples).

```
async fn show_host_info(client: &aws_sdk_route53::Client) -> Result<(), aws_sdk_route53::Error> {
    let hosted_zone_count = client.get_hosted_zone_count().send().await?;

    println!(
        "Number of hosted zones in region : {}",
        hosted_zone_count.hosted_zone_count(),
    );

    let hosted_zones = client.list_hosted_zones().send().await?;

    println!("Zones:");

    for hz in hosted_zones.hosted_zones() {
        let zone_name = hz.name();
        let zone_id = hz.id();

        println!("  ID :   {}", zone_id);
        println!("  Name : {}", zone_name);
        println!();
    }

    Ok(())
}
```
+  For API details, see [ListHostedZones](https://docs.rs/aws-sdk-route53/latest/aws_sdk_route53/client/struct.Client.html#method.list_hosted_zones) in *AWS SDK for Rust API reference*.
