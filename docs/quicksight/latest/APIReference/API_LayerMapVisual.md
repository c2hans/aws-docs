---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_LayerMapVisual.html
---

# LayerMapVisual
<a name="API_LayerMapVisual"></a>

A layer map visual.

## Contents
<a name="API_LayerMapVisual_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSetIdentifier **   <a name="QS-Type-LayerMapVisual-DataSetIdentifier"></a>
The dataset that is used to create the layer map visual. You can't create a visual without a dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** VisualId **   <a name="QS-Type-LayerMapVisual-VisualId"></a>
The ID of the visual.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** ChartConfiguration **   <a name="QS-Type-LayerMapVisual-ChartConfiguration"></a>
The configuration settings of the visual.
Type: [GeospatialLayerMapConfiguration](API_GeospatialLayerMapConfiguration.md) object
Required: No

 ** Subtitle **   <a name="QS-Type-LayerMapVisual-Subtitle"></a>
The subtitle label options for a visual.
Type: [VisualSubtitleLabelOptions](API_VisualSubtitleLabelOptions.md) object
Required: No

 ** Title **   <a name="QS-Type-LayerMapVisual-Title"></a>
The title label options for a visual.
Type: [VisualTitleLabelOptions](API_VisualTitleLabelOptions.md) object
Required: No

 ** VisualContentAltText **   <a name="QS-Type-LayerMapVisual-VisualContentAltText"></a>
The alt text for the visual.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_LayerMapVisual_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/LayerMapVisual)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/LayerMapVisual)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/LayerMapVisual)
