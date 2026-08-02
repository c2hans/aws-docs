---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormQuestionScoringConfiguration.html
---

# EvaluationFormQuestionScoringConfiguration
<a name="API_EvaluationFormQuestionScoringConfiguration"></a>

Scoring configuration for a question in an evaluation form.

## Contents
<a name="API_EvaluationFormQuestionScoringConfiguration_Contents"></a>

 ** IsExcludedFromScoring **   <a name="connect-Type-EvaluationFormQuestionScoringConfiguration-IsExcludedFromScoring"></a>
The flag to exclude the question from scoring.
Type: Boolean
Required: No

 ** PointsConfiguration **   <a name="connect-Type-EvaluationFormQuestionScoringConfiguration-PointsConfiguration"></a>
The points configuration for point-based scoring.
Type: [QuestionPointsConfiguration](API_QuestionPointsConfiguration.md) object
Required: No

 ** ScoreThresholds **   <a name="connect-Type-EvaluationFormQuestionScoringConfiguration-ScoreThresholds"></a>
The score thresholds for performance categories.
Type: Array of [EvaluationFormScoreThreshold](API_EvaluationFormScoreThreshold.md) objects
Required: No

## See Also
<a name="API_EvaluationFormQuestionScoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormQuestionScoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormQuestionScoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormQuestionScoringConfiguration)
