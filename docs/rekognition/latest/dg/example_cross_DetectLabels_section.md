---
source_url: https://docs.aws.amazon.com/rekognition/latest/dg/example_cross_DetectLabels_section.html
---

# Save EXIF and other image information using an AWS SDK
<a name="example_cross_DetectLabels_section"></a>

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

For a complete list of AWS SDK developer guides and code examples, see [Using Rekognition with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
