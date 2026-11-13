---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InvestigationFilterCondition.html
---

# InvestigationFilterCondition
<a name="API_InvestigationFilterCondition"></a>

Contains the values that an investigation attribute must match. Specify `Equals`, `NotEquals`, or both, each with at least one value. If you specify both, an investigation must match both conditions.

## Contents
<a name="API_InvestigationFilterCondition_Contents"></a>

 ** equals **   <a name="guardduty-Type-InvestigationFilterCondition-equals"></a>
The values to match. An investigation matches if its attribute value equals any of the specified values.
Type: Array of strings
Required: No

 ** notEquals **   <a name="guardduty-Type-InvestigationFilterCondition-notEquals"></a>
The values to exclude. An investigation matches only if its attribute value doesn't equal any of the specified values. An investigation that has no value for the attribute also matches.
Type: Array of strings
Required: No

## See Also
<a name="API_InvestigationFilterCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InvestigationFilterCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InvestigationFilterCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InvestigationFilterCondition)
