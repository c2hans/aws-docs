---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/dynamodb_example_cross_DetectLabels_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Save EXIF and other image information using an AWS SDK
<a name="dynamodb_example_cross_DetectLabels_section"></a>

The following code example shows how to:
+ Get EXIF information from a a JPG, JPEG, or PNG file.
+ Upload the image file to an Amazon S3 bucket.
+ Use Amazon Rekognition to identify the three top attributes (labels) in the file.
+ Add the EXIF and label information to an Amazon DynamoDB table in the Region.

------
#### [ Rust ]

**SDK for Rust**
 Get EXIF information from a JPG, JPEG, or PNG file, upload the image file to an Amazon S3 bucket, use Amazon Rekognition to identify the three top attributes (*labels* in Amazon Rekognition) in the file, and add the EXIF and label information to a Amazon DynamoDB table in the Region.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/rustv1/cross_service/detect_labels/src/main.rs).

**Services used in this example**
+ DynamoDB
+ Amazon Rekognition
+ Amazon S3

------
