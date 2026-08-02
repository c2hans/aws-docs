---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnabledControlFilter.html
---

# EnabledControlFilter
<a name="API_EnabledControlFilter"></a>

A structure that returns a set of control identifiers, the control status for each control in the set, and the drift status for each control in the set.

## Contents
<a name="API_EnabledControlFilter_Contents"></a>

 ** controlIdentifiers **   <a name="controltower-Type-EnabledControlFilter-controlIdentifiers"></a>
The set of `controlIdentifier` returned by the filter.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** driftStatuses **   <a name="controltower-Type-EnabledControlFilter-driftStatuses"></a>
A list of `DriftStatus` items.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `DRIFTED | IN_SYNC | NOT_CHECKING | UNKNOWN`
Required: No

 ** inheritanceDriftStatuses **   <a name="controltower-Type-EnabledControlFilter-inheritanceDriftStatuses"></a>
Filters enabled controls by their inheritance drift status, allowing you to find controls with specific inheritance-related drift conditions.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `DRIFTED | IN_SYNC | NOT_CHECKING | UNKNOWN`
Required: No

 ** parentIdentifiers **   <a name="controltower-Type-EnabledControlFilter-parentIdentifiers"></a>
Filters enabled controls by their parent control identifiers, allowing you to find child controls of specific parent controls.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: No

 ** resourceDriftStatuses **   <a name="controltower-Type-EnabledControlFilter-resourceDriftStatuses"></a>
Filters enabled controls by their resource drift status, allowing you to find controls with specific resource-related drift conditions.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `DRIFTED | IN_SYNC | NOT_CHECKING | UNKNOWN`
Required: No

 ** statuses **   <a name="controltower-Type-EnabledControlFilter-statuses"></a>
A list of `EnablementStatus` items.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `SUCCEEDED | FAILED | UNDER_CHANGE`
Required: No

## See Also
<a name="API_EnabledControlFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/EnabledControlFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/EnabledControlFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/EnabledControlFilter)
