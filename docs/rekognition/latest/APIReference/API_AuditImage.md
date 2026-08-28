---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_AuditImage.html
---

# AuditImage
<a name="API_AuditImage"></a>

An image that is picked from the Face Liveness video and returned for audit trail purposes, returned as Base64-encoded bytes.

## Contents
<a name="API_AuditImage_Contents"></a>

 ** BoundingBox **   <a name="rekognition-Type-AuditImage-BoundingBox"></a>
Identifies the bounding box around the label, face, text, object of interest, or personal protective equipment. The `left` (x-coordinate) and `top` (y-coordinate) are coordinates representing the top and left sides of the bounding box. Note that the upper-left corner of the image is the origin (0,0).
The `top` and `left` values returned are ratios of the overall image size. For example, if the input image is 700x200 pixels, and the top-left coordinate of the bounding box is 350x50 pixels, the API returns a `left` value of 0.5 (350/700) and a `top` value of 0.25 (50/200).
The `width` and `height` values represent the dimensions of the bounding box as a ratio of the overall image dimension. For example, if the input image is 700x200 pixels, and the bounding box width is 70 pixels, the width returned is 0.1.
 The bounding box coordinates can have negative values. For example, if Amazon Rekognition is able to detect a face that is at the image edge and is only partially visible, the service can return coordinates that are outside the image bounds and, depending on the image edge, you might get negative values or values greater than 1 for the `left` or `top` values.
Type: [BoundingBox](API_BoundingBox.md) object
Required: No

 ** Bytes **   <a name="rekognition-Type-AuditImage-Bytes"></a>
The Base64-encoded bytes representing an image selected from the Face Liveness video and returned for audit purposes.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 204800.
Required: No

 ** S3Object **   <a name="rekognition-Type-AuditImage-S3Object"></a>
Provides the S3 bucket name and object name.
The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.
For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see [How Amazon Rekognition works with IAM](https://docs.aws.amazon.com/rekognition/latest/dg/security_iam_service-with-iam.html).
Type: [S3Object](API_S3Object.md) object
Required: No

## See Also
<a name="API_AuditImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/AuditImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/AuditImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/AuditImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
