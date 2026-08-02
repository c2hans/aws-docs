---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationSuggestedAnswer.html
---

# EvaluationSuggestedAnswer
<a name="API_EvaluationSuggestedAnswer"></a>

The information about the suggested answer for the question.

## Contents
<a name="API_EvaluationSuggestedAnswer_Contents"></a>

 ** AnalysisType **   <a name="connect-Type-EvaluationSuggestedAnswer-AnalysisType"></a>
Type of analysis used to provide suggested answer.
Type: String
Valid Values: `CONTACT_LENS_DATA | GEN_AI`
Required: Yes

 ** Status **   <a name="connect-Type-EvaluationSuggestedAnswer-Status"></a>
The status of the suggested answer. D
Type: String
Valid Values: `IN_PROGRESS | FAILED | SUCCEEDED`
Required: Yes

 ** AnalysisDetails **   <a name="connect-Type-EvaluationSuggestedAnswer-AnalysisDetails"></a>
Detailed analysis results.
Type: [EvaluationQuestionAnswerAnalysisDetails](API_EvaluationQuestionAnswerAnalysisDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** Input **   <a name="connect-Type-EvaluationSuggestedAnswer-Input"></a>
Details about the input used to question automation.
Type: [EvaluationQuestionInputDetails](API_EvaluationQuestionInputDetails.md) object
Required: No

 ** Value **   <a name="connect-Type-EvaluationSuggestedAnswer-Value"></a>
Information about answer data for a contact evaluation. Answer data must be either string, numeric, or not applicable.
Type: [EvaluationAnswerData](API_EvaluationAnswerData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_EvaluationSuggestedAnswer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationSuggestedAnswer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationSuggestedAnswer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationSuggestedAnswer)
