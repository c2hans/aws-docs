---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_application-auto-scaling_code_examples.html
---

# Application Auto Scaling examples using SDK for Rust
<a name="rust_application-auto-scaling_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with Application Auto Scaling.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `DescribeScalingPolicies`
<a name="application-auto-scaling_DescribeScalingPolicies_rust_topic"></a>

The following code example shows how to use `DescribeScalingPolicies`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/applicationautoscaling#code-examples).

```
async fn show_policies(client: &Client) -> Result<(), Error> {
    let response = client
        .describe_scaling_policies()
        .service_namespace(ServiceNamespace::Ec2)
        .send()
        .await?;
    println!("Auto Scaling Policies:");
    for policy in response.scaling_policies() {
        println!("{:?}\n", policy);
    }
    println!("Next token: {:?}", response.next_token());

    Ok(())
}
```
+  For API details, see [DescribeScalingPolicies](https://docs.rs/aws-sdk-applicationautoscaling/latest/aws_sdk_applicationautoscaling/client/struct.Client.html#method.describe_scaling_policies) in *AWS SDK for Rust API reference*.
