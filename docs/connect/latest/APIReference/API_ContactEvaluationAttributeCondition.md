---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactEvaluationAttributeCondition.html
---

# ContactEvaluationAttributeCondition
<a name="API_ContactEvaluationAttributeCondition"></a>

An attribute condition for contact evaluation filtering.

## Contents
<a name="API_ContactEvaluationAttributeCondition_Contents"></a>

 ** AttributeKey **   <a name="connect-Type-ContactEvaluationAttributeCondition-AttributeKey"></a>
The key of the attribute.
Type: String
Valid Values: `ContactAgentId`
Required: No

 ** AttributeValue **   <a name="connect-Type-ContactEvaluationAttributeCondition-AttributeValue"></a>
The value of the attribute.
Type: [ContactEvaluationAttributeValue](API_ContactEvaluationAttributeValue.md) object
Required: No

 ** ComparisonType **   <a name="connect-Type-ContactEvaluationAttributeCondition-ComparisonType"></a>
The comparison type for the condition.
Type: String
Valid Values: `EXACT`
Required: No

## See Also
<a name="API_ContactEvaluationAttributeCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactEvaluationAttributeCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactEvaluationAttributeCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactEvaluationAttributeCondition)
