---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/csharp_3_api-gateway_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# API Gateway examples using SDK for .NET
<a name="csharp_3_api-gateway_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for .NET with API Gateway.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

*AWS community contributions* are examples that were created and are maintained by multiple teams across AWS. To provide feedback, use the mechanism provided in the linked repositories.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Scenarios](#scenarios)
+ [AWS community contributions](#aws_community_contributions)

## Scenarios
<a name="scenarios"></a>

### Create a serverless application to manage photos
<a name="cross_PAM_csharp_3_topic"></a>

The following code example shows how to create a serverless application that lets users manage photos using labels.

**SDK for .NET**
 Shows how to develop a photo asset management application that detects labels in images using Amazon Rekognition and stores them for later retrieval.
For complete source code and instructions on how to set up and run, see the full example on [ GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/cross-service/PhotoAssetManager).
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
<a name="tributary-lite_serverless-application_csharp_3_topic"></a>

The following code example shows how to build and test a serverless application using API Gateway with Lambda and DynamoDB

**SDK for .NET**
 Shows how to build and test a serverless application that consists of an API Gateway with Lambda and DynamoDB using the .NET SDK.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/aws-samples/serverless-dotnet-demo).

**Services used in this example**
+ API Gateway
+ DynamoDB
+ Lambda
