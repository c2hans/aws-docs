---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_secrets-manager_code_examples.html
---

# Secrets Manager examples using SDK for Rust
<a name="rust_secrets-manager_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with Secrets Manager.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `GetSecretValue`
<a name="secrets-manager_GetSecretValue_rust_topic"></a>

The following code example shows how to use `GetSecretValue`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/secretsmanager#code-examples).

```
async fn show_secret(client: &Client, name: &str) -> Result<(), Error> {
    let resp = client.get_secret_value().secret_id(name).send().await?;

    println!("Value: {}", resp.secret_string().unwrap_or("No value!"));

    Ok(())
}
```
+  For API details, see [GetSecretValue](https://docs.rs/aws-sdk-secretsmanager/latest/aws_sdk_secretsmanager/client/struct.Client.html#method.get_secret_value) in *AWS SDK for Rust API reference*.
