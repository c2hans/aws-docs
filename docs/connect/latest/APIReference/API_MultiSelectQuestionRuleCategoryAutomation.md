---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_MultiSelectQuestionRuleCategoryAutomation.html
---

# MultiSelectQuestionRuleCategoryAutomation
<a name="API_MultiSelectQuestionRuleCategoryAutomation"></a>

Automation rule for multi-select questions based on rule categories.

## Contents
<a name="API_MultiSelectQuestionRuleCategoryAutomation_Contents"></a>

 ** Category **   <a name="connect-Type-MultiSelectQuestionRuleCategoryAutomation-Category"></a>
The category name for this automation rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

 ** Condition **   <a name="connect-Type-MultiSelectQuestionRuleCategoryAutomation-Condition"></a>
The condition for this automation rule.
Type: String
Valid Values: `PRESENT | NOT_PRESENT`
Required: Yes

 ** OptionRefIds **   <a name="connect-Type-MultiSelectQuestionRuleCategoryAutomation-OptionRefIds"></a>
Reference IDs of options for this automation rule.
Type: Array of strings
Required: Yes

## See Also
<a name="API_MultiSelectQuestionRuleCategoryAutomation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/MultiSelectQuestionRuleCategoryAutomation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/MultiSelectQuestionRuleCategoryAutomation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/MultiSelectQuestionRuleCategoryAutomation)
