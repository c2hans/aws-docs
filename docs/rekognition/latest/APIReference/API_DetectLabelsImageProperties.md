---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabelsImageProperties.html
---

# DetectLabelsImageProperties
<a name="API_DetectLabelsImageProperties"></a>

Information about the quality and dominant colors of an input image. Quality and color information is returned for the entire image, foreground, and background.

## Contents
<a name="API_DetectLabelsImageProperties_Contents"></a>

 ** Background **   <a name="rekognition-Type-DetectLabelsImageProperties-Background"></a>
Information about the properties of an image’s background, including the background’s quality and dominant colors, including the quality and dominant colors of the image.
Type: [DetectLabelsImageBackground](API_DetectLabelsImageBackground.md) object
Required: No

 ** DominantColors **   <a name="rekognition-Type-DetectLabelsImageProperties-DominantColors"></a>
Information about the dominant colors found in an image, described with RGB values, CSS color name, simplified color name, and PixelPercentage (the percentage of image pixels that have a particular color).
Type: Array of [DominantColor](API_DominantColor.md) objects
Required: No

 ** Foreground **   <a name="rekognition-Type-DetectLabelsImageProperties-Foreground"></a>
Information about the properties of an image’s foreground, including the foreground’s quality and dominant colors, including the quality and dominant colors of the image.
Type: [DetectLabelsImageForeground](API_DetectLabelsImageForeground.md) object
Required: No

 ** Quality **   <a name="rekognition-Type-DetectLabelsImageProperties-Quality"></a>
Information about the quality of the image foreground as defined by brightness, sharpness, and contrast. The higher the value the greater the brightness, sharpness, and contrast respectively.
Type: [DetectLabelsImageQuality](API_DetectLabelsImageQuality.md) object
Required: No

## See Also
<a name="API_DetectLabelsImageProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DetectLabelsImageProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DetectLabelsImageProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DetectLabelsImageProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
