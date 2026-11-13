---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ObservedFindingType.html
---

# ObservedFindingType
<a name="API_ObservedFindingType"></a>

Contains information about a finding type that GuardDuty observed.

## Contents
<a name="API_ObservedFindingType_Contents"></a>

 ** count **   <a name="guardduty-Type-ObservedFindingType-count"></a>
The number of findings of this type.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** findingType **   <a name="guardduty-Type-ObservedFindingType-findingType"></a>
The finding type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** severityMax **   <a name="guardduty-Type-ObservedFindingType-severityMax"></a>
The highest severity score among the findings of this type, from 0 to 10.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 10.
Required: No

 ** sharedResources **   <a name="guardduty-Type-ObservedFindingType-sharedResources"></a>
The resources that the findings of this type share with the investigated activity.
Type: Array of [SharedResource](API_SharedResource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## See Also
<a name="API_ObservedFindingType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ObservedFindingType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ObservedFindingType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ObservedFindingType)
