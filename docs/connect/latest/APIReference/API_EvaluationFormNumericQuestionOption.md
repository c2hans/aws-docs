---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormNumericQuestionOption.html
---

# EvaluationFormNumericQuestionOption
<a name="API_EvaluationFormNumericQuestionOption"></a>

Information about the option range used for scoring in numeric questions.

## Contents
<a name="API_EvaluationFormNumericQuestionOption_Contents"></a>

 ** MaxValue **   <a name="connect-Type-EvaluationFormNumericQuestionOption-MaxValue"></a>
The maximum answer value of the range option.
Type: Integer
Required: Yes

 ** MinValue **   <a name="connect-Type-EvaluationFormNumericQuestionOption-MinValue"></a>
The minimum answer value of the range option.
Type: Integer
Required: Yes

 ** AutomaticFail **   <a name="connect-Type-EvaluationFormNumericQuestionOption-AutomaticFail"></a>
The flag to mark the option as automatic fail. If an automatic fail answer is provided, the overall evaluation gets a score of 0.
Type: Boolean
Required: No

 ** AutomaticFailConfiguration **   <a name="connect-Type-EvaluationFormNumericQuestionOption-AutomaticFailConfiguration"></a>
A configuration for automatic fail.
Type: [AutomaticFailConfiguration](API_AutomaticFailConfiguration.md) object
Required: No

 ** PointsConfiguration **   <a name="connect-Type-EvaluationFormNumericQuestionOption-PointsConfiguration"></a>
The points configuration for point-based scoring.
Type: [QuestionOptionPointsConfiguration](API_QuestionOptionPointsConfiguration.md) object
Required: No

 ** Score **   <a name="connect-Type-EvaluationFormNumericQuestionOption-Score"></a>
The score assigned to answer values within the range option.
Type: Integer
Required: No

## See Also
<a name="API_EvaluationFormNumericQuestionOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormNumericQuestionOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormNumericQuestionOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormNumericQuestionOption)
