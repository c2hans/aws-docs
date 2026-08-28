---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_BoundingBox.html
---

# BoundingBox
<a name="API_rekognitionstreaming_BoundingBox"></a>

Identifies the bounding box around a given label, face, text, object of interest, or personal protective equipment. The left (x-coordinate) and top (y-coordinate) are coordinates representing the top and left sides of the bounding box. Note that the upper-left corner of the image is the origin (0,0).

The top and left values returned are ratios of the overall image size. For example, if the input image is 700x200 pixels, and the top-left coordinate of the bounding box is 350x50 pixels, the API returns a left value of 0.5 (350/700) and a top value of 0.25 (50/200).

The width and height values represent the dimensions of the bounding box as a ratio of the overall image dimension. For example, if the input image is 700x200 pixels, and the bounding box width is 70 pixels, the width returned is 0.1.

## Contents
<a name="API_rekognitionstreaming_BoundingBox_Contents"></a>

 ** Height **   <a name="rekognition-Type-rekognitionstreaming_BoundingBox-Height"></a>
Height of the bounding box as a ratio of the overall image height.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

 ** Left **   <a name="rekognition-Type-rekognitionstreaming_BoundingBox-Left"></a>
Left coordinate of the bounding box as a ratio of overall image width.
Type: Float
Valid Range: Minimum value of -1. Maximum value of 1.
Required: Yes

 ** Top **   <a name="rekognition-Type-rekognitionstreaming_BoundingBox-Top"></a>
Top coordinate of the bounding box as a ratio of overall image height.
Type: Float
Valid Range: Minimum value of -1. Maximum value of 1.
Required: Yes

 ** Width **   <a name="rekognition-Type-rekognitionstreaming_BoundingBox-Width"></a>
Width of the bounding box as a ratio of the overall image width.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

## See Also
<a name="API_rekognitionstreaming_BoundingBox_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognitionstreaming-2022-05-30/BoundingBox)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognitionstreaming-2022-05-30/BoundingBox)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognitionstreaming-2022-05-30/BoundingBox)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
