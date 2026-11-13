---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_SignalGroup.html
---

# SignalGroup
<a name="API_SignalGroup"></a>

Contains information about a group of runtime signals that have the same finding type.

## Contents
<a name="API_SignalGroup_Contents"></a>

 ** count **   <a name="guardduty-Type-SignalGroup-count"></a>
The number of signals in the group.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** findingType **   <a name="guardduty-Type-SignalGroup-findingType"></a>
The finding type of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** severity **   <a name="guardduty-Type-SignalGroup-severity"></a>
The severity score of the signals in the group, from 0 to 10.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 10.
Required: No

## See Also
<a name="API_SignalGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/SignalGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/SignalGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/SignalGroup)
