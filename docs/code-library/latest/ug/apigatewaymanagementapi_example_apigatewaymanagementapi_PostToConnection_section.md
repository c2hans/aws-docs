---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/apigatewaymanagementapi_example_apigatewaymanagementapi_PostToConnection_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `PostToConnection` with an AWS SDK or CLI
<a name="apigatewaymanagementapi_example_apigatewaymanagementapi_PostToConnection_section"></a>

The following code examples show how to use `PostToConnection`.

------
#### [ CLI ]

**AWS CLI**
**To send data to a WebSocket connection**
The following `post-to-connection` example sends a message to a client that's connected to the specified WebSocket API.

```
aws apigatewaymanagementapi post-to-connection \
    --connection-id {{L0SM9cOFvHcCIhw=}} \
    --data '{{SGVsbG8gZnJvbSBBUEkgR2F0ZXdheSE=}}' \
    --endpoint-url {{https://aabbccddee.execute-api.us-west-2.amazonaws.com/prod}}
```
This command produces no output.
For more information, see [Use @connections commands in your backend service](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html) in the *Amazon API Gateway Developer Guide*.
+  For API details, see [PostToConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewaymanagementapi/post-to-connection.html) in *AWS CLI Command Reference*.

------
#### [ Rust ]

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

------
