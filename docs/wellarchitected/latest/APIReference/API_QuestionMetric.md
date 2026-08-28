---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_QuestionMetric.html
---

# QuestionMetric
<a name="API_QuestionMetric"></a>

A metric for a particular question in the pillar.

## Contents
<a name="API_QuestionMetric_Contents"></a>

 ** BestPractices **   <a name="wellarchitected-Type-QuestionMetric-BestPractices"></a>
The best practices, or choices, that have been identified as contributing to risk in a question.
Type: Array of [BestPractice](API_BestPractice.md) objects
Required: No

 ** QuestionId **   <a name="wellarchitected-Type-QuestionMetric-QuestionId"></a>
The ID of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Risk **   <a name="wellarchitected-Type-QuestionMetric-Risk"></a>
The risk for a given workload, lens review, pillar, or question.
Type: String
Valid Values: `UNANSWERED | HIGH | MEDIUM | NONE | NOT_APPLICABLE`
Required: No

## See Also
<a name="API_QuestionMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/QuestionMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/QuestionMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/QuestionMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
