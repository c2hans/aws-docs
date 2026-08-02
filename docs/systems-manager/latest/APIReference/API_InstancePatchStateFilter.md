---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_InstancePatchStateFilter.html
---

# InstancePatchStateFilter
<a name="API_InstancePatchStateFilter"></a>

Defines a filter used in [DescribeInstancePatchStatesForPatchGroup](API_DescribeInstancePatchStatesForPatchGroup.md) to scope down the information returned by the API.

 **Example**: To filter for all managed nodes in a patch group having more than three patches with a `FailedCount` status, use the following for the filter:
+ Value for `Key`: `FailedCount`
+ Value for `Type`: `GreaterThan`
+ Value for `Values`: `3`

## Contents
<a name="API_InstancePatchStateFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-InstancePatchStateFilter-Key"></a>
The key for the filter. Supported values include the following:
+  `InstalledCount`
+  `InstalledOtherCount`
+  `InstalledPendingRebootCount`
+  `InstalledRejectedCount`
+  `MissingCount`
+  `FailedCount`
+  `UnreportedNotApplicableCount`
+  `NotApplicableCount`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** Type **   <a name="systemsmanager-Type-InstancePatchStateFilter-Type"></a>
The type of comparison that should be performed for the value.
Type: String
Valid Values: `Equal | NotEqual | LessThan | GreaterThan`
Required: Yes

 ** Values **   <a name="systemsmanager-Type-InstancePatchStateFilter-Values"></a>
The value for the filter. Must be an integer greater than or equal to 0.
Type: Array of strings
Array Members: Fixed number of 1 item.
Required: Yes

## See Also
<a name="API_InstancePatchStateFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/InstancePatchStateFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/InstancePatchStateFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/InstancePatchStateFilter)
