---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormSingleSelectQuestionOption.html
---

# EvaluationFormSingleSelectQuestionOption
<a name="API_EvaluationFormSingleSelectQuestionOption"></a>

Information about the automation configuration in single select questions.

## Contents
<a name="API_EvaluationFormSingleSelectQuestionOption_Contents"></a>

 ** RefId **   <a name="connect-Type-EvaluationFormSingleSelectQuestionOption-RefId"></a>
The identifier of the answer option. An identifier must be unique within the question.
Type: String
Required: Yes

 ** Text **   <a name="connect-Type-EvaluationFormSingleSelectQuestionOption-Text"></a>
The title of the answer option.
Type: String
Required: Yes

 ** AutomaticFail **   <a name="connect-Type-EvaluationFormSingleSelectQuestionOption-AutomaticFail"></a>
The flag to mark the option as automatic fail. If an automatic fail answer is provided, the overall evaluation gets a score of 0.
Type: Boolean
Required: No

 ** AutomaticFailConfiguration **   <a name="connect-Type-EvaluationFormSingleSelectQuestionOption-AutomaticFailConfiguration"></a>
Whether automatic fail is configured on a single select question.
Type: [AutomaticFailConfiguration](API_AutomaticFailConfiguration.md) object
Required: No

 ** PointsConfiguration **   <a name="connect-Type-EvaluationFormSingleSelectQuestionOption-PointsConfiguration"></a>
The points configuration for point-based scoring.
Type: [QuestionOptionPointsConfiguration](API_QuestionOptionPointsConfiguration.md) object
Required: No

 ** Score **   <a name="connect-Type-EvaluationFormSingleSelectQuestionOption-Score"></a>
The score assigned to the answer option.
Type: Integer
Required: No

## See Also
<a name="API_EvaluationFormSingleSelectQuestionOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormSingleSelectQuestionOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormSingleSelectQuestionOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormSingleSelectQuestionOption)
