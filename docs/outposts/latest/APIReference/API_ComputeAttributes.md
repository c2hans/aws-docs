---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_ComputeAttributes.html
---

# ComputeAttributes
<a name="API_ComputeAttributes"></a>

 Information about compute hardware assets.

## Contents
<a name="API_ComputeAttributes_Contents"></a>

 ** HostId **   <a name="outposts-Type-ComputeAttributes-HostId"></a>
 The host ID of the Dedicated Host on the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^[A-Za-z0-9-]*$`
Required: No

 ** InstanceFamilies **   <a name="outposts-Type-ComputeAttributes-InstanceFamilies"></a>
A list of the names of instance families that are currently associated with a given asset.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^(?:.{1,200}/)?(?:[a-z0-9-_A-Z])+$`
Required: No

 ** InstanceTypeCapacities **   <a name="outposts-Type-ComputeAttributes-InstanceTypeCapacities"></a>
The instance type capacities configured for this asset. This can be changed through a capacity task.
Type: Array of [AssetInstanceTypeCapacity](API_AssetInstanceTypeCapacity.md) objects
Required: No

 ** MaxVcpus **   <a name="outposts-Type-ComputeAttributes-MaxVcpus"></a>
The maximum number of vCPUs possible for the specified asset.
Type: Integer
Required: No

 ** State **   <a name="outposts-Type-ComputeAttributes-State"></a>
The state.
+ ACTIVE - The asset is available and can provide capacity for new compute resources.
+ ISOLATED - The asset is undergoing maintenance and can't provide capacity for new compute resources. Existing compute resources on the asset are not affected.
+ RETIRING - The underlying hardware for the asset is degraded. Capacity for new compute resources is reduced. AWS sends notifications for resources that must be stopped before the asset can be replaced.
+ INSTALLING - The asset is being installed and can't yet provide capacity for new compute resources.
Type: String
Valid Values: `ACTIVE | ISOLATED | RETIRING | INSTALLING`
Required: No

## See Also
<a name="API_ComputeAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/ComputeAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/ComputeAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/ComputeAttributes)
