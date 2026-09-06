---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/s3_example_cross_DetectFaces_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Detect faces in an image using an AWS SDK
<a name="s3_example_cross_DetectFaces_section"></a>

The following code example shows how to:
+ Save an image in an Amazon S3 bucket.
+ Use Amazon Rekognition to detect facial details, such as age range, gender, and emotion (such as smiling).
+ Display those details.

------
#### [ Rust ]

**SDK for Rust**
 Save the image in an Amazon S3 bucket with an **uploads** prefix, use Amazon Rekognition to detect facial details, such as age range, gender, and emotion (smiling, etc.), and display those details.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/rustv1/cross_service/detect_faces/src/main.rs).

**Services used in this example**
+ Amazon Rekognition
+ Amazon S3

------
