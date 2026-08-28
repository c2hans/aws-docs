---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_rekognition_code_examples.html
---

# Amazon Rekognition examples using SDK for Rust
<a name="rust_rekognition_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with Amazon Rekognition.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Scenarios](#scenarios)

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

### Detect faces in an image
<a name="cross_DetectFaces_rust_topic"></a>

The following code example shows how to:
+ Save an image in an Amazon S3 bucket.
+ Use Amazon Rekognition to detect facial details, such as age range, gender, and emotion (such as smiling).
+ Display those details.

**SDK for Rust**
 Save the image in an Amazon S3 bucket with an **uploads** prefix, use Amazon Rekognition to detect facial details, such as age range, gender, and emotion (smiling, etc.), and display those details.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/rustv1/cross_service/detect_faces/src/main.rs).

**Services used in this example**
+ Amazon Rekognition
+ Amazon S3

### Save EXIF and other image information
<a name="cross_DetectLabels_rust_topic"></a>

The following code example shows how to:
+ Get EXIF information from a a JPG, JPEG, or PNG file.
+ Upload the image file to an Amazon S3 bucket.
+ Use Amazon Rekognition to identify the three top attributes (labels) in the file.
+ Add the EXIF and label information to an Amazon DynamoDB table in the Region.

**SDK for Rust**
 Get EXIF information from a JPG, JPEG, or PNG file, upload the image file to an Amazon S3 bucket, use Amazon Rekognition to identify the three top attributes (*labels* in Amazon Rekognition) in the file, and add the EXIF and label information to a Amazon DynamoDB table in the Region.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/rustv1/cross_service/detect_labels/src/main.rs).

**Services used in this example**
+ DynamoDB
+ Amazon Rekognition
+ Amazon S3

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Rust. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-rust` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
