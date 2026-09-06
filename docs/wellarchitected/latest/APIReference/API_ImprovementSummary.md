---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ImprovementSummary.html
---

# ImprovementSummary
<a name="API_ImprovementSummary"></a>

An improvement summary of a lens review in a workload.

## Contents
<a name="API_ImprovementSummary_Contents"></a>

 ** ImprovementPlans **   <a name="wellarchitected-Type-ImprovementSummary-ImprovementPlans"></a>
The improvement plan details.
This value is only applicable to custom lenses.
Type: Array of [ChoiceImprovementPlan](API_ChoiceImprovementPlan.md) objects
Required: No

 ** ImprovementPlanUrl **   <a name="wellarchitected-Type-ImprovementSummary-ImprovementPlanUrl"></a>
The improvement plan URL for a question in an AWS official lenses.
This value is only available if the question has been answered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** JiraConfiguration **   <a name="wellarchitected-Type-ImprovementSummary-JiraConfiguration"></a>
Configuration of the Jira integration.
Type: [JiraConfiguration](API_JiraConfiguration.md) object
Required: No

 ** PillarId **   <a name="wellarchitected-Type-ImprovementSummary-PillarId"></a>
The ID used to identify a pillar, for example, `security`.
A pillar is identified by its [PillarReviewSummary:PillarId](API_PillarReviewSummary.md#wellarchitected-Type-PillarReviewSummary-PillarId).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** QuestionId **   <a name="wellarchitected-Type-ImprovementSummary-QuestionId"></a>
The ID of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** QuestionTitle **   <a name="wellarchitected-Type-ImprovementSummary-QuestionTitle"></a>
The title of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Risk **   <a name="wellarchitected-Type-ImprovementSummary-Risk"></a>
The risk for a given workload, lens review, pillar, or question.
Type: String
Valid Values: `UNANSWERED | HIGH | MEDIUM | NONE | NOT_APPLICABLE`
Required: No

## See Also
<a name="API_ImprovementSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ImprovementSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ImprovementSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ImprovementSummary)
