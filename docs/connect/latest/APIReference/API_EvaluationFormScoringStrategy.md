---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormScoringStrategy.html
---

# EvaluationFormScoringStrategy
<a name="API_EvaluationFormScoringStrategy"></a>

Information about scoring strategy for an evaluation form.

## Contents
<a name="API_EvaluationFormScoringStrategy_Contents"></a>

 ** Mode **   <a name="connect-Type-EvaluationFormScoringStrategy-Mode"></a>
The scoring mode of the evaluation form.
Type: String
Valid Values: `QUESTION_ONLY | SECTION_ONLY | POINTS_BASED`
Required: Yes

 ** Status **   <a name="connect-Type-EvaluationFormScoringStrategy-Status"></a>
The scoring status of the evaluation form.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** ScoreThresholds **   <a name="connect-Type-EvaluationFormScoringStrategy-ScoreThresholds"></a>
The score thresholds for performance categories.
Type: Array of [EvaluationFormScoreThreshold](API_EvaluationFormScoreThreshold.md) objects
Required: No

## See Also
<a name="API_EvaluationFormScoringStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormScoringStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormScoringStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormScoringStrategy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
