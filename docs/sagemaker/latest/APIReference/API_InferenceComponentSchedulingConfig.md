---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceComponentSchedulingConfig.html
---

# InferenceComponentSchedulingConfig
<a name="API_InferenceComponentSchedulingConfig"></a>

The scheduling configuration that determines how inference component copies are placed across available instances when copies are added or removed.

## Contents
<a name="API_InferenceComponentSchedulingConfig_Contents"></a>

 ** PlacementStrategy **   <a name="sagemaker-Type-InferenceComponentSchedulingConfig-PlacementStrategy"></a>
The strategy for placing inference component copies across available instances. If you also set `AvailabilityZoneBalance`, this strategy applies to placement within each Availability Zone.
SPREAD
Distributes copies evenly across available instances for better resilience.
BINPACK
Packs copies onto fewer instances to optimize resource utilization.
Type: String
Valid Values: `SPREAD | BINPACK`
Required: Yes

 ** AvailabilityZoneBalance **   <a name="sagemaker-Type-InferenceComponentSchedulingConfig-AvailabilityZoneBalance"></a>
Configuration for balancing inference component copies across Availability Zones.
Type: [InferenceComponentAvailabilityZoneBalance](API_InferenceComponentAvailabilityZoneBalance.md) object
Required: No

## See Also
<a name="API_InferenceComponentSchedulingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceComponentSchedulingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceComponentSchedulingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceComponentSchedulingConfig)
