---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FilterCondition.html
---

# FilterCondition
<a name="API_FilterCondition"></a>

Contains information about the condition.

## Contents
<a name="API_FilterCondition_Contents"></a>

 ** equalsValue **   <a name="guardduty-Type-FilterCondition-equalsValue"></a>
Represents an *equal* **** condition to be applied to a single field when querying for scan entries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** greaterThan **   <a name="guardduty-Type-FilterCondition-greaterThan"></a>
Represents a *greater than* condition to be applied to a single field when querying for scan entries.
Type: Long
Required: No

 ** lessThan **   <a name="guardduty-Type-FilterCondition-lessThan"></a>
Represents a *less than* condition to be applied to a single field when querying for scan entries.
Type: Long
Required: No

## See Also
<a name="API_FilterCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/FilterCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/FilterCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/FilterCondition)
