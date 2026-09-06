---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_StringCriteriaCondition.html
---

# StringCriteriaCondition
<a name="API_automation_StringCriteriaCondition"></a>

Criteria condition for filtering based on string values, including comparison operators and target values.

## Contents
<a name="API_automation_StringCriteriaCondition_Contents"></a>

 ** comparison **   <a name="computeoptimizer-Type-automation_StringCriteriaCondition-comparison"></a>
The comparison operator used to evaluate the string criteria, such as equals, not equals, or contains.
Type: String
Valid Values: `StringEquals | StringNotEquals | StringEqualsIgnoreCase | StringNotEqualsIgnoreCase | StringLike | StringNotLike | NumericEquals | NumericNotEquals | NumericLessThan | NumericLessThanEquals | NumericGreaterThan | NumericGreaterThanEquals`
Required: No

 ** values **   <a name="computeoptimizer-Type-automation_StringCriteriaCondition-values"></a>
List of string values to compare against when applying the criteria condition.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\s\.\-\:\/\=\+\@\*\?]+`
Required: No

## See Also
<a name="API_automation_StringCriteriaCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/StringCriteriaCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/StringCriteriaCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/StringCriteriaCondition)
