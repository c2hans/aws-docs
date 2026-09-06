---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceComponentRuntimeConfigSummary.html
---

# InferenceComponentRuntimeConfigSummary
<a name="API_InferenceComponentRuntimeConfigSummary"></a>

Details about the runtime settings for the model that is deployed with the inference component.

## Contents
<a name="API_InferenceComponentRuntimeConfigSummary_Contents"></a>

 ** CurrentCopyCount **   <a name="sagemaker-Type-InferenceComponentRuntimeConfigSummary-CurrentCopyCount"></a>
The number of runtime copies of the model container that are currently deployed.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** DesiredCopyCount **   <a name="sagemaker-Type-InferenceComponentRuntimeConfigSummary-DesiredCopyCount"></a>
The number of runtime copies of the model container that you requested to deploy with the inference component.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PlacementStatus **   <a name="sagemaker-Type-InferenceComponentRuntimeConfigSummary-PlacementStatus"></a>
The placement status of the inference component across instance types. Shows how the inference component copies are distributed across instance types.
Type: Array of [InferenceComponentPlacementStatus](API_InferenceComponentPlacementStatus.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_InferenceComponentRuntimeConfigSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceComponentRuntimeConfigSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceComponentRuntimeConfigSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceComponentRuntimeConfigSummary)
