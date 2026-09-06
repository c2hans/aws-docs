---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchOrchestratorFilter.html
---

# PatchOrchestratorFilter
<a name="API_PatchOrchestratorFilter"></a>

Defines a filter used in Patch Manager APIs. Supported filter keys depend on the API operation that includes the filter. Patch Manager API operations that use `PatchOrchestratorFilter` include the following:
+  [DescribeAvailablePatches](API_DescribeAvailablePatches.md)
+  [DescribeInstancePatches](API_DescribeInstancePatches.md)
+  [DescribePatchBaselines](API_DescribePatchBaselines.md)
+  [DescribePatchGroups](API_DescribePatchGroups.md)

## Contents
<a name="API_PatchOrchestratorFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-PatchOrchestratorFilter-Key"></a>
The key for the filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Values **   <a name="systemsmanager-Type-PatchOrchestratorFilter-Values"></a>
The value for the filter.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_PatchOrchestratorFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/PatchOrchestratorFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/PatchOrchestratorFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/PatchOrchestratorFilter)
