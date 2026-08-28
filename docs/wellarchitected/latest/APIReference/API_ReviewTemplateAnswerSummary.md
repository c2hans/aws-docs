---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ReviewTemplateAnswerSummary.html
---

# ReviewTemplateAnswerSummary
<a name="API_ReviewTemplateAnswerSummary"></a>

The summary of review template answers.

## Contents
<a name="API_ReviewTemplateAnswerSummary_Contents"></a>

 ** AnswerStatus **   <a name="wellarchitected-Type-ReviewTemplateAnswerSummary-AnswerStatus"></a>
The status of whether or not this question has been answered.
Type: String
Valid Values: `UNANSWERED | ANSWERED`
Required: No

 ** ChoiceAnswerSummaries **   <a name="wellarchitected-Type-ReviewTemplateAnswerSummary-ChoiceAnswerSummaries"></a>
A list of selected choices to a question in the review template.
Type: Array of [ChoiceAnswerSummary](API_ChoiceAnswerSummary.md) objects
Required: No

 ** Choices **   <a name="wellarchitected-Type-ReviewTemplateAnswerSummary-Choices"></a>
List of choices available for a question.
Type: Array of [Choice](API_Choice.md) objects
Required: No

 ** IsApplicable **   <a name="wellarchitected-Type-ReviewTemplateAnswerSummary-IsApplicable"></a>
Defines whether this question is applicable to a lens review.
Type: Boolean
Required: No

 ** PillarId **   <a name="wellarchitected-Type-ReviewTemplateAnswerSummary-PillarId"></a>
The ID used to identify a pillar, for example, `security`.
A pillar is identified by its [PillarReviewSummary:PillarId](API_PillarReviewSummary.md#wellarchitected-Type-PillarReviewSummary-PillarId).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** QuestionId **   <a name="wellarchitected-Type-ReviewTemplateAnswerSummary-QuestionId"></a>
The ID of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** QuestionTitle **   <a name="wellarchitected-Type-ReviewTemplateAnswerSummary-QuestionTitle"></a>
The title of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** QuestionType **   <a name="wellarchitected-Type-ReviewTemplateAnswerSummary-QuestionType"></a>
The type of question.
Type: String
Valid Values: `PRIORITIZED | NON_PRIORITIZED`
Required: No

 ** Reason **   <a name="wellarchitected-Type-ReviewTemplateAnswerSummary-Reason"></a>
The reason why a choice is not-applicable to a question in the review template.
Type: String
Valid Values: `OUT_OF_SCOPE | BUSINESS_PRIORITIES | ARCHITECTURE_CONSTRAINTS | OTHER | NONE`
Required: No

 ** SelectedChoices **   <a name="wellarchitected-Type-ReviewTemplateAnswerSummary-SelectedChoices"></a>
List of selected choice IDs in a question answer.
The values entered replace the previously selected choices.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_ReviewTemplateAnswerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ReviewTemplateAnswerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ReviewTemplateAnswerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ReviewTemplateAnswerSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
