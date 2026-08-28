---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Point.html
---

# Point
<a name="API_Point"></a>

The X and Y coordinates of a point on an image or video frame. The X and Y values are ratios of the overall image size or video resolution. For example, if an input image is 700x200 and the values are X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the image.

An array of `Point` objects, `Polygon`, is returned by [DetectText](API_DetectText.md) and [DetectCustomLabels](API_DetectCustomLabels.md) or used to define regions of interest in Amazon Rekognition Video operations such as `CreateStreamProcessor`. `Polygon` represents a fine-grained polygon around a detected item. For more information, see [Geometry](API_Geometry.md).

## Contents
<a name="API_Point_Contents"></a>

 ** X **   <a name="rekognition-Type-Point-X"></a>
The value of the X coordinate for a point on a `Polygon`.
Type: Float
Required: No

 ** Y **   <a name="rekognition-Type-Point-Y"></a>
The value of the Y coordinate for a point on a `Polygon`.
Type: Float
Required: No

## See Also
<a name="API_Point_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/Point)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/Point)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/Point)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
