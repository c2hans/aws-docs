---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationAnswerOutput.html
---

# EvaluationAnswerOutput
<a name="API_EvaluationAnswerOutput"></a>

Information about output answers for a contact evaluation.

## Contents
<a name="API_EvaluationAnswerOutput_Contents"></a>

 ** SuggestedAnswers **   <a name="connect-Type-EvaluationAnswerOutput-SuggestedAnswers"></a>
Automation suggested answers for the questions.
Type: Array of [EvaluationSuggestedAnswer](API_EvaluationSuggestedAnswer.md) objects
Required: No

 ** SystemSuggestedValue **   <a name="connect-Type-EvaluationAnswerOutput-SystemSuggestedValue"></a>
The system suggested value for an answer in a contact evaluation.
Type: [EvaluationAnswerData](API_EvaluationAnswerData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** Value **   <a name="connect-Type-EvaluationAnswerOutput-Value"></a>
The value for an answer in a contact evaluation.
Type: [EvaluationAnswerData](API_EvaluationAnswerData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_EvaluationAnswerOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationAnswerOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationAnswerOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationAnswerOutput)
