---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormQuestion.html
---

# EvaluationFormQuestion
<a name="API_EvaluationFormQuestion"></a>

Information about a question from an evaluation form.

## Contents
<a name="API_EvaluationFormQuestion_Contents"></a>

 ** QuestionType **   <a name="connect-Type-EvaluationFormQuestion-QuestionType"></a>
The type of the question.
Type: String
Valid Values: `TEXT | SINGLESELECT | NUMERIC | MULTISELECT | DATETIME`
Required: Yes

 ** RefId **   <a name="connect-Type-EvaluationFormQuestion-RefId"></a>
The identifier of the question. An identifier must be unique within the evaluation form.
Type: String
Required: Yes

 ** Title **   <a name="connect-Type-EvaluationFormQuestion-Title"></a>
The title of the question.
Type: String
Required: Yes

 ** Enablement **   <a name="connect-Type-EvaluationFormQuestion-Enablement"></a>
A question conditional enablement.
Type: [EvaluationFormItemEnablementConfiguration](API_EvaluationFormItemEnablementConfiguration.md) object
Required: No

 ** Instructions **   <a name="connect-Type-EvaluationFormQuestion-Instructions"></a>
The instructions of the section.
Type: String
Required: No

 ** NotApplicableEnabled **   <a name="connect-Type-EvaluationFormQuestion-NotApplicableEnabled"></a>
The flag to enable not applicable answers to the question.
Type: Boolean
Required: No

 ** QuestionTypeProperties **   <a name="connect-Type-EvaluationFormQuestion-QuestionTypeProperties"></a>
The properties of the type of question. Text questions do not have to define question type properties.
Type: [EvaluationFormQuestionTypeProperties](API_EvaluationFormQuestionTypeProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** ScoringConfiguration **   <a name="connect-Type-EvaluationFormQuestion-ScoringConfiguration"></a>
The scoring configuration of the question.
Type: [EvaluationFormQuestionScoringConfiguration](API_EvaluationFormQuestionScoringConfiguration.md) object
Required: No

 ** Weight **   <a name="connect-Type-EvaluationFormQuestion-Weight"></a>
The scoring weight of the section.
Type: Double
Required: No

## See Also
<a name="API_EvaluationFormQuestion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormQuestion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormQuestion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormQuestion)
