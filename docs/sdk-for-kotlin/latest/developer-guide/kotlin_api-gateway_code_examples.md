---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_api-gateway_code_examples.html
---

# API Gateway examples using SDK for Kotlin
<a name="kotlin_api-gateway_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Kotlin with API Gateway.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Scenarios](#scenarios)

## Scenarios
<a name="scenarios"></a>

### Create a serverless application to manage photos
<a name="cross_PAM_kotlin_topic"></a>

The following code example shows how to create a serverless application that lets users manage photos using labels.

**SDK for Kotlin**
 Shows how to develop a photo asset management application that detects labels in images using Amazon Rekognition and stores them for later retrieval.
For complete source code and instructions on how to set up and run, see the full example on [ GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/usecases/creating_pam).
For a deep dive into the origin of this example see the post on [AWS Community](https://community.aws/posts/cloud-journeys/01-serverless-image-recognition-app).

**Services used in this example**
+ API Gateway
+ DynamoDB
+ Lambda
+ Amazon Rekognition
+ Amazon S3
+ Amazon SNS
