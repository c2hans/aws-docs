---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabelsImageForeground.html
---

# DetectLabelsImageForeground
<a name="API_DetectLabelsImageForeground"></a>

The foreground of the image with regard to image quality and dominant colors.

## Contents
<a name="API_DetectLabelsImageForeground_Contents"></a>

 ** DominantColors **   <a name="rekognition-Type-DetectLabelsImageForeground-DominantColors"></a>
The dominant colors found in the foreground of an image, defined with RGB values, CSS color name, simplified color name, and PixelPercentage (the percentage of image pixels that have a particular color).
Type: Array of [DominantColor](API_DominantColor.md) objects
Required: No

 ** Quality **   <a name="rekognition-Type-DetectLabelsImageForeground-Quality"></a>
The quality of the image foreground as defined by brightness and sharpness.
Type: [DetectLabelsImageQuality](API_DetectLabelsImageQuality.md) object
Required: No

## See Also
<a name="API_DetectLabelsImageForeground_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DetectLabelsImageForeground)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DetectLabelsImageForeground)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DetectLabelsImageForeground)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
