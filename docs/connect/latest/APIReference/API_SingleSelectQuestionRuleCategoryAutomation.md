---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SingleSelectQuestionRuleCategoryAutomation.html
---

# SingleSelectQuestionRuleCategoryAutomation
<a name="API_SingleSelectQuestionRuleCategoryAutomation"></a>

Information about the automation option based on a rule category for a single select question.

## Contents
<a name="API_SingleSelectQuestionRuleCategoryAutomation_Contents"></a>

 ** Category **   <a name="connect-Type-SingleSelectQuestionRuleCategoryAutomation-Category"></a>
 The category name, as defined in Rules.
Type: String
Required: Yes

 ** Condition **   <a name="connect-Type-SingleSelectQuestionRuleCategoryAutomation-Condition"></a>
The condition to apply for the automation option. If the condition is `PRESENT`, then the option is applied when the contact data includes the category. Similarly, if the condition is `NOT_PRESENT`, then the option is applied when the contact data does not include the category.
Type: String
Valid Values: `PRESENT | NOT_PRESENT`
Required: Yes

 ** OptionRefId **   <a name="connect-Type-SingleSelectQuestionRuleCategoryAutomation-OptionRefId"></a>
The identifier of the answer option.
Type: String
Required: Yes

## See Also
<a name="API_SingleSelectQuestionRuleCategoryAutomation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SingleSelectQuestionRuleCategoryAutomation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SingleSelectQuestionRuleCategoryAutomation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SingleSelectQuestionRuleCategoryAutomation)
