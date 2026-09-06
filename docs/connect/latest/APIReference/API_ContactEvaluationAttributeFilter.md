---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactEvaluationAttributeFilter.html
---

# ContactEvaluationAttributeFilter
<a name="API_ContactEvaluationAttributeFilter"></a>

An object that can be used to specify tag conditions and attribute conditions inside the `SearchFilter` for contact evaluations. This accepts an `OR` or `AND` (List of List) input where:
+ The top level list specifies conditions that need to be applied with `OR` operator.
+ The inner list specifies conditions that need to be applied with `AND` operator.

## Contents
<a name="API_ContactEvaluationAttributeFilter_Contents"></a>

 ** AndCondition **   <a name="connect-Type-ContactEvaluationAttributeFilter-AndCondition"></a>
A list of conditions which would be applied together with an `AND` condition.
Type: [ContactEvaluationAttributeAndCondition](API_ContactEvaluationAttributeAndCondition.md) object
Required: No

 ** ContactEvaluationAttributeCondition **   <a name="connect-Type-ContactEvaluationAttributeFilter-ContactEvaluationAttributeCondition"></a>
An attribute condition to apply.
Type: [ContactEvaluationAttributeCondition](API_ContactEvaluationAttributeCondition.md) object
Required: No

 ** OrConditions **   <a name="connect-Type-ContactEvaluationAttributeFilter-OrConditions"></a>
A list of conditions which would be applied together with an `OR` condition.
Type: Array of [ContactEvaluationAttributeAndCondition](API_ContactEvaluationAttributeAndCondition.md) objects
Required: No

 ** TagCondition **   <a name="connect-Type-ContactEvaluationAttributeFilter-TagCondition"></a>
A tag condition to apply.
Type: [TagCondition](API_TagCondition.md) object
Required: No

## See Also
<a name="API_ContactEvaluationAttributeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactEvaluationAttributeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactEvaluationAttributeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactEvaluationAttributeFilter)
