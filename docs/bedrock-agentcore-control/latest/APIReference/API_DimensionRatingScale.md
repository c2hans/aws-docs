---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DimensionRatingScale.html
---

# DimensionRatingScale
<a name="API_DimensionRatingScale"></a>

 The rating scale for one dimension of an LLM-as-a-judge evaluator, supporting either a numerical or a categorical scale.

## Contents
<a name="API_DimensionRatingScale_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** categorical **   <a name="bedrockagentcorecontrol-Type-DimensionRatingScale-categorical"></a>
 The categorical rating scale with named categories and definitions for qualitative evaluation of the dimension.
Type: Array of [CategoricalScaleDefinition](API_CategoricalScaleDefinition.md) objects
Required: No

 ** numerical **   <a name="bedrockagentcorecontrol-Type-DimensionRatingScale-numerical"></a>
 The numerical rating scale with defined score values and descriptions for quantitative evaluation of the dimension.
Type: Array of [NumericalScaleDefinition](API_NumericalScaleDefinition.md) objects
Required: No

## See Also
<a name="API_DimensionRatingScale_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DimensionRatingScale)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DimensionRatingScale)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DimensionRatingScale)
