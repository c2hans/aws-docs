---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledBaselineFilter.html
---

# EnabledBaselineFilter
<a name="API_EnabledBaselineFilter"></a>

A filter applied on the `ListEnabledBaseline` operation. Allowed filters are `baselineIdentifiers` and `targetIdentifiers`. The filter can be applied for either, or both.

## Contents
<a name="API_EnabledBaselineFilter_Contents"></a>

 ** baselineIdentifiers **   <a name="controltower-Type-EnabledBaselineFilter-baselineIdentifiers"></a>
Identifiers for the `Baseline` objects returned as part of the filter operation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** inheritanceDriftStatuses **   <a name="controltower-Type-EnabledBaselineFilter-inheritanceDriftStatuses"></a>
A list of `EnabledBaselineDriftStatus` items for enabled baselines.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `IN_SYNC | DRIFTED`
Required: No

 ** parentIdentifiers **   <a name="controltower-Type-EnabledBaselineFilter-parentIdentifiers"></a>
An optional filter that sets up a list of `parentIdentifiers` to filter the results of the `ListEnabledBaseline` output.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** statuses **   <a name="controltower-Type-EnabledBaselineFilter-statuses"></a>
A list of `EnablementStatus` items.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `SUCCEEDED | FAILED | UNDER_CHANGE`
Required: No

 ** targetIdentifiers **   <a name="controltower-Type-EnabledBaselineFilter-targetIdentifiers"></a>
Identifiers for the targets of the `Baseline` filter operation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

## See Also
<a name="API_EnabledBaselineFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/EnabledBaselineFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/EnabledBaselineFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/EnabledBaselineFilter)
