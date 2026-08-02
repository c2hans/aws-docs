---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/rust_1_sts_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS STS examples using SDK for Rust
<a name="rust_1_sts_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with AWS STS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `AssumeRole`
<a name="sts_AssumeRole_rust_1_topic"></a>

The following code example shows how to use `AssumeRole`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/sts/#code-examples).

```
async fn assume_role(config: &SdkConfig, role_name: String, session_name: Option<String>) {
    let provider = aws_config::sts::AssumeRoleProvider::builder(role_name)
        .session_name(session_name.unwrap_or("rust_sdk_example_session".into()))
        .configure(config)
        .build()
        .await;

    let local_config = aws_config::from_env()
        .credentials_provider(provider)
        .load()
        .await;
    let client = Client::new(&local_config);
    let req = client.get_caller_identity();
    let resp = req.send().await;
    match resp {
        Ok(e) => {
            println!("UserID :               {}", e.user_id().unwrap_or_default());
            println!("Account:               {}", e.account().unwrap_or_default());
            println!("Arn    :               {}", e.arn().unwrap_or_default());
        }
        Err(e) => println!("{:?}", e),
    }
}
```
+  For API details, see [AssumeRole](https://docs.rs/aws-sdk-sts/latest/aws_sdk_sts/client/struct.Client.html#method.assume_role) in *AWS SDK for Rust API reference*.
