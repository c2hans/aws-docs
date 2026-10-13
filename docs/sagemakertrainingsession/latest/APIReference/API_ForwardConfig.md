---
source_url: https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_ForwardConfig.html
---

# ForwardConfig
<a name="API_ForwardConfig"></a>

The configuration for a forward-only pass through the model. This computes loss values without computing gradients.

## Contents
<a name="API_ForwardConfig_Contents"></a>

 ** datumList **   <a name="sagemakertrainingsession-Type-ForwardConfig-datumList"></a>
The list of input data to feed through the model. Must contain at least one datum, and each datum must have a non-empty modelInput with at least one chunk.
Type: Array of [Datum](API_Datum.md) objects
Required: Yes

 ** lossFnName **   <a name="sagemakertrainingsession-Type-ForwardConfig-lossFnName"></a>
The name of the loss function to evaluate during the forward pass.
Type: String
Valid Values: `cross_entropy | importance_sampling | ppo | cispo`
Required: Yes

 ** lossFnConfig **   <a name="sagemakertrainingsession-Type-ForwardConfig-lossFnConfig"></a>
Additional loss function configuration passed to the engine. Supported keys are `clip_low_threshold` (valid range: 0 to 1) and `clip_high_threshold` (valid range: 1 to 10). Unsupported keys are rejected.
Type: JSON value
Required: No

## See Also
<a name="API_ForwardConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/ForwardConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/ForwardConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/ForwardConfig)
