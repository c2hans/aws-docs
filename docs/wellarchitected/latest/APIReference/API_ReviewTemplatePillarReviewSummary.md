---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ReviewTemplatePillarReviewSummary.html
---

# ReviewTemplatePillarReviewSummary
<a name="API_ReviewTemplatePillarReviewSummary"></a>

Summary of a review template.

## Contents
<a name="API_ReviewTemplatePillarReviewSummary_Contents"></a>

 ** Notes **   <a name="wellarchitected-Type-ReviewTemplatePillarReviewSummary-Notes"></a>
The notes associated with the workload.
For a review template, these are the notes that will be associated with the workload when the template is applied.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2084.
Required: No

 ** PillarId **   <a name="wellarchitected-Type-ReviewTemplatePillarReviewSummary-PillarId"></a>
The ID used to identify a pillar, for example, `security`.
A pillar is identified by its [PillarReviewSummary:PillarId](API_PillarReviewSummary.md#wellarchitected-Type-PillarReviewSummary-PillarId).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** PillarName **   <a name="wellarchitected-Type-ReviewTemplatePillarReviewSummary-PillarName"></a>
The name of the pillar.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** QuestionCounts **   <a name="wellarchitected-Type-ReviewTemplatePillarReviewSummary-QuestionCounts"></a>
A count of how many questions are answered and unanswered in the requested pillar of the lens review.
Type: String to integer map
Valid Keys: `UNANSWERED | ANSWERED`
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ReviewTemplatePillarReviewSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ReviewTemplatePillarReviewSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ReviewTemplatePillarReviewSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ReviewTemplatePillarReviewSummary)
