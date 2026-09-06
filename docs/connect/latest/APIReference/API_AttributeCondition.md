---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AttributeCondition.html
---

# AttributeCondition
<a name="API_AttributeCondition"></a>

An object to specify the predefined attribute condition.

## Contents
<a name="API_AttributeCondition_Contents"></a>

 ** ComparisonOperator **   <a name="connect-Type-AttributeCondition-ComparisonOperator"></a>
The operator of the condition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

 ** MatchCriteria **   <a name="connect-Type-AttributeCondition-MatchCriteria"></a>
An object to define `AgentsCriteria`.
Type: [MatchCriteria](API_MatchCriteria.md) object
Required: No

 ** Name **   <a name="connect-Type-AttributeCondition-Name"></a>
The name of predefined attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** ProficiencyLevel **   <a name="connect-Type-AttributeCondition-ProficiencyLevel"></a>
The proficiency level of the condition.
Type: Float
Valid Range: Minimum value of 1.0. Maximum value of 5.0.
Required: No

 ** Range **   <a name="connect-Type-AttributeCondition-Range"></a>
An Object to define the minimum and maximum proficiency levels.
Type: [Range](API_Range.md) object
Required: No

 ** Value **   <a name="connect-Type-AttributeCondition-Value"></a>
The value of predefined attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_AttributeCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AttributeCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AttributeCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AttributeCondition)
