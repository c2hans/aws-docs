---
source_url: https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_SaveWeightsConfig.html
---

# SaveWeightsConfig
<a name="API_SaveWeightsConfig"></a>

The configuration for saving model weights as a checkpoint.

## Contents
<a name="API_SaveWeightsConfig_Contents"></a>

 ** description **   <a name="sagemakertrainingsession-Type-SaveWeightsConfig-description"></a>
A human-readable description for the saved checkpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** mergeWeights **   <a name="sagemakertrainingsession-Type-SaveWeightsConfig-mergeWeights"></a>
Specifies whether to merge LoRA adapter weights into the base model before saving. When true, the saved checkpoint contains the full merged model weights.
Type: Boolean
Required: No

## See Also
<a name="API_SaveWeightsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/SaveWeightsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/SaveWeightsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/SaveWeightsConfig)
