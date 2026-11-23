---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SingleSelectQuestionAutomationRule.html
---

# SingleSelectQuestionAutomationRule

Information about a condition-based automation rule for a single select question. When the condition is satisfied, the specified answer option is selected.

## Contents
<a name="API_SingleSelectQuestionAutomationRule_Contents"></a>

 ** Condition **   <a name="connect-Type-SingleSelectQuestionAutomationRule-Condition"></a>
The condition that must be satisfied for the answer option to be selected. The condition uses the same sources, comparators, and operators as item enablement conditions.
Type: [EvaluationFormItemEnablementCondition](API_EvaluationFormItemEnablementCondition.md) object
Required: Yes

 ** OptionRefId **   <a name="connect-Type-SingleSelectQuestionAutomationRule-OptionRefId"></a>
The identifier of the answer option to select when the condition is satisfied.
Type: String
Required: Yes

## See Also
<a name="API_SingleSelectQuestionAutomationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SingleSelectQuestionAutomationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SingleSelectQuestionAutomationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SingleSelectQuestionAutomationRule)
