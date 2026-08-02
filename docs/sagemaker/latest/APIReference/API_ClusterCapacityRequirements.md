---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterCapacityRequirements.html
---

# ClusterCapacityRequirements
<a name="API_ClusterCapacityRequirements"></a>

Defines the instance capacity requirements for an instance group, including configurations for both Spot and On-Demand capacity types.

## Contents
<a name="API_ClusterCapacityRequirements_Contents"></a>

 ** OnDemand **   <a name="sagemaker-Type-ClusterCapacityRequirements-OnDemand"></a>
Configuration options specific to On-Demand instances.
Type: [ClusterOnDemandOptions](API_ClusterOnDemandOptions.md) object
Required: No

 ** Spot **   <a name="sagemaker-Type-ClusterCapacityRequirements-Spot"></a>
Configuration options specific to Spot instances.
Type: [ClusterSpotOptions](API_ClusterSpotOptions.md) object
Required: No

## See Also
<a name="API_ClusterCapacityRequirements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterCapacityRequirements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterCapacityRequirements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterCapacityRequirements)
