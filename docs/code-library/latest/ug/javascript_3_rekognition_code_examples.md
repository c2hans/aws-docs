---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/javascript_3_rekognition_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon Rekognition examples using SDK for JavaScript (v3)
<a name="javascript_3_rekognition_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for JavaScript (v3) with Amazon Rekognition.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Scenarios](#scenarios)

## Scenarios
<a name="scenarios"></a>

### Create a serverless application to manage photos
<a name="cross_PAM_javascript_3_topic"></a>

The following code example shows how to create a serverless application that lets users manage photos using labels.

**SDK for JavaScript (v3)**
 Shows how to develop a photo asset management application that detects labels in images using Amazon Rekognition and stores them for later retrieval.
For complete source code and instructions on how to set up and run, see the full example on [ GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cross-services/photo-asset-manager).
For a deep dive into the origin of this example see the post on [AWS Community](https://community.aws/posts/cloud-journeys/01-serverless-image-recognition-app).

**Services used in this example**
+ API Gateway
+ DynamoDB
+ Lambda
+ Amazon Rekognition
+ Amazon S3
+ Amazon SNS

### Detect objects in images
<a name="cross_RekognitionPhotoAnalyzer_javascript_3_topic"></a>

The following code example shows how to build an app that uses Amazon Rekognition to detect objects by category in images.

**SDK for JavaScript (v3)**
 Shows how to use Amazon Rekognition with the AWS SDK for JavaScript to create an app that uses Amazon Rekognition to identify objects by category in images located in an Amazon Simple Storage Service (Amazon S3) bucket. The app sends the admin an email notification with the results using Amazon Simple Email Service (Amazon SES).
Learn how to:
+ Create an unauthenticated user using Amazon Cognito.
+ Analyze images for objects using Amazon Rekognition.
+ Verify an email address for Amazon SES.
+ Send an email notification using Amazon SES.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cross-services/photo_analyzer).

**Services used in this example**
+ Amazon Rekognition
+ Amazon S3
+ Amazon SES
