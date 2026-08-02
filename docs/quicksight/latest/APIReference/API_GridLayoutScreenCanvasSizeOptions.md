---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GridLayoutScreenCanvasSizeOptions.html
---

# GridLayoutScreenCanvasSizeOptions
<a name="API_GridLayoutScreenCanvasSizeOptions"></a>

The options that determine the sizing of the canvas used in a grid layout.

## Contents
<a name="API_GridLayoutScreenCanvasSizeOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ResizeOption **   <a name="QS-Type-GridLayoutScreenCanvasSizeOptions-ResizeOption"></a>
This value determines the layout behavior when the viewport is resized.
+  `FIXED`: A fixed width will be used when optimizing the layout. In the Quick Sight console, this option is called `Classic`.
+  `RESPONSIVE`: The width of the canvas will be responsive and optimized to the view port. In the Quick Sight console, this option is called `Tiled`.
Type: String
Valid Values: `FIXED | RESPONSIVE`
Required: Yes

 ** OptimizedViewPortWidth **   <a name="QS-Type-GridLayoutScreenCanvasSizeOptions-OptimizedViewPortWidth"></a>
The width that the view port will be optimized for when the layout renders.
Type: String
Required: No

## See Also
<a name="API_GridLayoutScreenCanvasSizeOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GridLayoutScreenCanvasSizeOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GridLayoutScreenCanvasSizeOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GridLayoutScreenCanvasSizeOptions)
