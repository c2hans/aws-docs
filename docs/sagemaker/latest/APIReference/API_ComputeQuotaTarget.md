---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ComputeQuotaTarget.html
---

# ComputeQuotaTarget
<a name="API_ComputeQuotaTarget"></a>

The target entity to allocate compute resources to.

## Contents
<a name="API_ComputeQuotaTarget_Contents"></a>

 ** TeamName **   <a name="sagemaker-Type-ComputeQuotaTarget-TeamName"></a>
Name of the team to allocate compute resources to.
Type: String
Pattern: `[a-z0-9]([-a-z0-9]*[a-z0-9]){0,39}?`
Required: Yes

 ** FairShareWeight **   <a name="sagemaker-Type-ComputeQuotaTarget-FairShareWeight"></a>
Assigned entity fair-share weight. Idle compute will be shared across entities based on these assigned weights. This weight is only used when `FairShare` is enabled.
A weight of 0 is the lowest priority and 100 is the highest. Weight 0 is the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_ComputeQuotaTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ComputeQuotaTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ComputeQuotaTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ComputeQuotaTarget)
