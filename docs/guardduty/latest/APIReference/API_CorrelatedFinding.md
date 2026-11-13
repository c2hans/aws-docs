---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CorrelatedFinding.html
---

# CorrelatedFinding
<a name="API_CorrelatedFinding"></a>

Contains information about a group of correlated findings that have the same finding type.

## Contents
<a name="API_CorrelatedFinding_Contents"></a>

 ** correlationReasons **   <a name="guardduty-Type-CorrelatedFinding-correlationReasons"></a>
The reasons why GuardDuty correlated the findings. Possible values are `HIGH_SEVERITY`, `SAME_RESOURCE`, and `SAME_BEHAVIOR`. A value can appear more than once.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Valid Values: `HIGH_SEVERITY | SAME_RESOURCE | SAME_BEHAVIOR`
Required: No

 ** count **   <a name="guardduty-Type-CorrelatedFinding-count"></a>
The number of correlated findings of this type. This value can be greater than the number of IDs in `FindingIds`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** findingIds **   <a name="guardduty-Type-CorrelatedFinding-findingIds"></a>
A sample of the IDs of the findings in the group.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** findingType **   <a name="guardduty-Type-CorrelatedFinding-findingType"></a>
The finding type of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** severityMax **   <a name="guardduty-Type-CorrelatedFinding-severityMax"></a>
The highest severity score among the findings in the group, from 0 to 10.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 10.
Required: No

 ** sharedBehaviors **   <a name="guardduty-Type-CorrelatedFinding-sharedBehaviors"></a>
The behaviors that the findings in the group share with the investigated activity.
Type: Array of [SharedBehavior](API_SharedBehavior.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** sharedResources **   <a name="guardduty-Type-CorrelatedFinding-sharedResources"></a>
The resources that the findings in the group share with the investigated activity.
Type: Array of [SharedResource](API_SharedResource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## See Also
<a name="API_CorrelatedFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CorrelatedFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CorrelatedFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CorrelatedFinding)
