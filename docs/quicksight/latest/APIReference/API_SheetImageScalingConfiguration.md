---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SheetImageScalingConfiguration.html
---

# SheetImageScalingConfiguration
<a name="API_SheetImageScalingConfiguration"></a>

Determines how the image is scaled

## Contents
<a name="API_SheetImageScalingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ScalingType **   <a name="QS-Type-SheetImageScalingConfiguration-ScalingType"></a>
The scaling option to use when fitting the image inside the container.
Valid values are defined as follows:
+  `SCALE_TO_WIDTH`: The image takes up the entire width of the container. The image aspect ratio is preserved.
+  `SCALE_TO_HEIGHT`: The image takes up the entire height of the container. The image aspect ratio is preserved.
+  `SCALE_TO_CONTAINER`: The image takes up the entire width and height of the container. The image aspect ratio is not preserved.
+  `SCALE_NONE`: The image is displayed in its original size and is not scaled to the container.
Type: String
Valid Values: `SCALE_TO_WIDTH | SCALE_TO_HEIGHT | SCALE_TO_CONTAINER | SCALE_NONE`
Required: No

## See Also
<a name="API_SheetImageScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SheetImageScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SheetImageScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SheetImageScalingConfiguration)
