---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_apigatewaymanagementapi_code_examples.html
---

# API Gateway Management API examples using SDK for Rust
<a name="rust_apigatewaymanagementapi_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with API Gateway Management API.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `PostToConnection`
<a name="apigatewaymanagementapi_PostToConnection_rust_topic"></a>

The following code example shows how to use `PostToConnection`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/apigatewaymanagement#code-examples).

```
async fn send_data(
    client: &aws_sdk_apigatewaymanagement::Client,
    con_id: &str,
    data: &str,
) -> Result<(), aws_sdk_apigatewaymanagement::Error> {
    client
        .post_to_connection()
        .connection_id(con_id)
        .data(Blob::new(data))
        .send()
        .await?;

    Ok(())
}

    let endpoint_url = format!(
        "https://{api_id}.execute-api.{region}.amazonaws.com/{stage}",
        api_id = api_id,
        region = region,
        stage = stage
    );

    let shared_config = aws_config::from_env().region(region_provider).load().await;
    let api_management_config = config::Builder::from(&shared_config)
        .endpoint_url(endpoint_url)
        .build();
    let client = Client::from_conf(api_management_config);
```
+  For API details, see [PostToConnection](https://docs.rs/aws-sdk-apigatewaymanagementapi/latest/aws_sdk_apigatewaymanagementapi/client/struct.Client.html#method.post_to_connection) in *AWS SDK for Rust API reference*.
