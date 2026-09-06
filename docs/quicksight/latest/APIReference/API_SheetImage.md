---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SheetImage.html
---

# SheetImage
<a name="API_SheetImage"></a>

An image that is located on a sheet.

## Contents
<a name="API_SheetImage_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SheetImageId **   <a name="QS-Type-SheetImage-SheetImageId"></a>
The ID of the sheet image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** Source **   <a name="QS-Type-SheetImage-Source"></a>
The source of the image.
Type: [SheetImageSource](API_SheetImageSource.md) object
Required: Yes

 ** Actions **   <a name="QS-Type-SheetImage-Actions"></a>
A list of custom actions that are configured for an image.
Type: Array of [ImageCustomAction](API_ImageCustomAction.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** ImageContentAltText **   <a name="QS-Type-SheetImage-ImageContentAltText"></a>
The alt text for the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Interactions **   <a name="QS-Type-SheetImage-Interactions"></a>
The general image interactions setup for an image.
Type: [ImageInteractionOptions](API_ImageInteractionOptions.md) object
Required: No

 ** Scaling **   <a name="QS-Type-SheetImage-Scaling"></a>
Determines how the image is scaled.
Type: [SheetImageScalingConfiguration](API_SheetImageScalingConfiguration.md) object
Required: No

 ** Tooltip **   <a name="QS-Type-SheetImage-Tooltip"></a>
The tooltip to be shown when hovering over the image.
Type: [SheetImageTooltipConfiguration](API_SheetImageTooltipConfiguration.md) object
Required: No

## See Also
<a name="API_SheetImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SheetImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SheetImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SheetImage)
