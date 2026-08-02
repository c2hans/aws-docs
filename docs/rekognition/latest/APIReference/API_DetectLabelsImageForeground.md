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
