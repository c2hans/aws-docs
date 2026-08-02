---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_api-gateway_code_examples.html
---

# API Gateway examples using SDK for Rust
<a name="rust_api-gateway_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with API Gateway.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

*AWS community contributions* are examples that were created and are maintained by multiple teams across AWS. To provide feedback, use the mechanism provided in the linked repositories.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)
+ [Scenarios](#scenarios)
+ [AWS community contributions](#aws_community_contributions)

## Actions
<a name="actions"></a>

### `GetRestApis`
<a name="api-gateway_GetRestApis_rust_topic"></a>

The following code example shows how to use `GetRestApis`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/apigateway#code-examples).
Displays the Amazon API Gateway REST APIs in the Region.

```
async fn show_apis(client: &Client) -> Result<(), Error> {
    let resp = client.get_rest_apis().send().await?;

    for api in resp.items() {
        println!("ID:          {}", api.id().unwrap_or_default());
        println!("Name:        {}", api.name().unwrap_or_default());
        println!("Description: {}", api.description().unwrap_or_default());
        println!("Version:     {}", api.version().unwrap_or_default());
        println!(
            "Created:     {}",
            api.created_date().unwrap().to_chrono_utc()?
        );
        println!();
    }

    Ok(())
}
```
+  For API details, see [GetRestApis](https://docs.rs/aws-sdk-apigateway/latest/aws_sdk_apigateway/client/struct.Client.html#method.get_rest_apis) in *AWS SDK for Rust API reference*.

## Scenarios
<a name="scenarios"></a>

### Create a serverless application to manage photos
<a name="cross_PAM_rust_topic"></a>

The following code example shows how to create a serverless application that lets users manage photos using labels.

**SDK for Rust**
 Shows how to develop a photo asset management application that detects labels in images using Amazon Rekognition and stores them for later retrieval.
For complete source code and instructions on how to set up and run, see the full example on [ GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/cross_service/photo_asset_management).
For a deep dive into the origin of this example see the post on [AWS Community](https://community.aws/posts/cloud-journeys/01-serverless-image-recognition-app).

**Services used in this example**
+ API Gateway
+ DynamoDB
+ Lambda
+ Amazon Rekognition
+ Amazon S3
+ Amazon SNS

## AWS community contributions
<a name="aws_community_contributions"></a>

### Build and test a serverless application
<a name="tributary-lite_serverless-application_rust_topic"></a>

The following code example shows how to build and test a serverless application using API Gateway with Lambda and DynamoDB

**SDK for Rust**
 Shows how to build and test a serverless application that consists of an API Gateway with Lambda and DynamoDB using the Rust SDK.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/aws-samples/serverless-rust-demo).

**Services used in this example**
+ API Gateway
+ DynamoDB
+ Lambda
