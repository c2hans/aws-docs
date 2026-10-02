---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Answer.html
---

# Answer
<a name="API_Answer"></a>

An answer of the question.

## Contents
<a name="API_Answer_Contents"></a>

 ** ChoiceAnswers **   <a name="wellarchitected-Type-Answer-ChoiceAnswers"></a>
A list of selected choices to a question in your workload.
Type: Array of [ChoiceAnswer](API_ChoiceAnswer.md) objects
Required: No

 ** Choices **   <a name="wellarchitected-Type-Answer-Choices"></a>
List of choices available for a question.
Type: Array of [Choice](API_Choice.md) objects
Required: No

 ** HelpfulResourceDisplayText **   <a name="wellarchitected-Type-Answer-HelpfulResourceDisplayText"></a>
The helpful resource text to be displayed for a custom lens.
This field does not apply to AWS official lenses.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** HelpfulResourceUrl **   <a name="wellarchitected-Type-Answer-HelpfulResourceUrl"></a>
The helpful resource URL.
For AWS official lenses, this is the helpful resource URL for a question or choice.
For custom lenses, this is the helpful resource URL for a question and is only provided if `HelpfulResourceDisplayText` was specified for the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** ImprovementPlanUrl **   <a name="wellarchitected-Type-Answer-ImprovementPlanUrl"></a>
The improvement plan URL for a question in an AWS official lenses.
This value is only available if the question has been answered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** IsApplicable **   <a name="wellarchitected-Type-Answer-IsApplicable"></a>
Defines whether this question is applicable to a lens review.
Type: Boolean
Required: No

 ** JiraConfiguration **   <a name="wellarchitected-Type-Answer-JiraConfiguration"></a>
Configuration of the Jira integration.
Type: [JiraConfiguration](API_JiraConfiguration.md) object
Required: No

 ** Notes **   <a name="wellarchitected-Type-Answer-Notes"></a>
The notes associated with the workload.
For a review template, these are the notes that will be associated with the workload when the template is applied.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2084.
Required: No

 ** PillarId **   <a name="wellarchitected-Type-Answer-PillarId"></a>
The ID used to identify a pillar, for example, `security`.
A pillar is identified by its [PillarReviewSummary:PillarId](API_PillarReviewSummary.md#wellarchitected-Type-PillarReviewSummary-PillarId).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** QuestionDescription **   <a name="wellarchitected-Type-Answer-QuestionDescription"></a>
The description of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** QuestionId **   <a name="wellarchitected-Type-Answer-QuestionId"></a>
The ID of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** QuestionTitle **   <a name="wellarchitected-Type-Answer-QuestionTitle"></a>
The title of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Reason **   <a name="wellarchitected-Type-Answer-Reason"></a>
The reason why the question is not applicable to your workload.
Type: String
Valid Values: `OUT_OF_SCOPE | BUSINESS_PRIORITIES | ARCHITECTURE_CONSTRAINTS | OTHER | NONE`
Required: No

 ** Risk **   <a name="wellarchitected-Type-Answer-Risk"></a>
The risk for a given workload, lens review, pillar, or question.
Type: String
Valid Values: `UNANSWERED | HIGH | MEDIUM | NONE | NOT_APPLICABLE`
Required: No

 ** SelectedChoices **   <a name="wellarchitected-Type-Answer-SelectedChoices"></a>
List of selected choice IDs in a question answer.
The values entered replace the previously selected choices.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_Answer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/Answer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/Answer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/Answer)
