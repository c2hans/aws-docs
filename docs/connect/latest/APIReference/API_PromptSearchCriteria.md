---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PromptSearchCriteria.html
---

# PromptSearchCriteria
<a name="API_PromptSearchCriteria"></a>

The search criteria to be used to return prompts.

## Contents
<a name="API_PromptSearchCriteria_Contents"></a>

 ** AndConditions **   <a name="connect-Type-PromptSearchCriteria-AndConditions"></a>
A list of conditions which would be applied together with an AND condition.
Type: Array of [PromptSearchCriteria](#API_PromptSearchCriteria) objects
Required: No

 ** OrConditions **   <a name="connect-Type-PromptSearchCriteria-OrConditions"></a>
A list of conditions which would be applied together with an OR condition.
Type: Array of [PromptSearchCriteria](#API_PromptSearchCriteria) objects
Required: No

 ** StringCondition **   <a name="connect-Type-PromptSearchCriteria-StringCondition"></a>
A leaf node condition which can be used to specify a string condition.
The currently supported values for `FieldName` are `name`, `description`, and `resourceID`.
Type: [StringCondition](API_StringCondition.md) object
Required: No

## See Also
<a name="API_PromptSearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PromptSearchCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PromptSearchCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PromptSearchCriteria)
