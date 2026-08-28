---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormScoreThreshold.html
---

# EvaluationFormScoreThreshold
<a name="API_EvaluationFormScoreThreshold"></a>

Information about a score threshold for a performance category.

## Contents
<a name="API_EvaluationFormScoreThreshold_Contents"></a>

 ** PerformanceCategory **   <a name="connect-Type-EvaluationFormScoreThreshold-PerformanceCategory"></a>
The performance category name.
Type: String
Valid Values: `NEEDS_IMPROVEMENT | EXCEEDS_EXPECTATIONS`
Required: Yes

 ** MaxScorePercentage **   <a name="connect-Type-EvaluationFormScoreThreshold-MaxScorePercentage"></a>
The maximum score percentage for the performance category.
Type: Double
Required: No

 ** MinScorePercentage **   <a name="connect-Type-EvaluationFormScoreThreshold-MinScorePercentage"></a>
The minimum score percentage for the performance category.
Type: Double
Required: No

## See Also
<a name="API_EvaluationFormScoreThreshold_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormScoreThreshold)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormScoreThreshold)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormScoreThreshold)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
