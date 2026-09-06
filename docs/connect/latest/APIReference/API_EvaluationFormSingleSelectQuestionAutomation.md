---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormSingleSelectQuestionAutomation.html
---

# EvaluationFormSingleSelectQuestionAutomation
<a name="API_EvaluationFormSingleSelectQuestionAutomation"></a>

Information about the automation configuration in single select questions. Automation options are evaluated in order, and the first matched option is applied. If no automation option matches, and there is a default option, then the default option is applied.

## Contents
<a name="API_EvaluationFormSingleSelectQuestionAutomation_Contents"></a>

 ** AnswerSource **   <a name="connect-Type-EvaluationFormSingleSelectQuestionAutomation-AnswerSource"></a>
Automation answer source.
Type: [EvaluationFormQuestionAutomationAnswerSource](API_EvaluationFormQuestionAutomationAnswerSource.md) object
Required: No

 ** DefaultOptionRefId **   <a name="connect-Type-EvaluationFormSingleSelectQuestionAutomation-DefaultOptionRefId"></a>
The identifier of the default answer option, when none of the automation options match the criteria.
Type: String
Required: No

 ** Options **   <a name="connect-Type-EvaluationFormSingleSelectQuestionAutomation-Options"></a>
The automation options of the single select question.
Type: Array of [EvaluationFormSingleSelectQuestionAutomationOption](API_EvaluationFormSingleSelectQuestionAutomationOption.md) objects
Required: No

## See Also
<a name="API_EvaluationFormSingleSelectQuestionAutomation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormSingleSelectQuestionAutomation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormSingleSelectQuestionAutomation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormSingleSelectQuestionAutomation)
