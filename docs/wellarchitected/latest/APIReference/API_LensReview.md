---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_LensReview.html
---

# LensReview
<a name="API_LensReview"></a>

A lens review of a question.

## Contents
<a name="API_LensReview_Contents"></a>

 ** JiraConfiguration **   <a name="wellarchitected-Type-LensReview-JiraConfiguration"></a>
Jira configuration status of the Lens review.
Type: [JiraSelectedQuestionConfiguration](API_JiraSelectedQuestionConfiguration.md) object
Required: No

 ** LensAlias **   <a name="wellarchitected-Type-LensReview-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** LensArn **   <a name="wellarchitected-Type-LensReview-LensArn"></a>
The ARN for the lens.
Type: String
Required: No

 ** LensName **   <a name="wellarchitected-Type-LensReview-LensName"></a>
The full name of the lens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** LensStatus **   <a name="wellarchitected-Type-LensReview-LensStatus"></a>
The status of the lens.
Type: String
Valid Values: `CURRENT | NOT_CURRENT | DEPRECATED | DELETED | UNSHARED`
Required: No

 ** LensVersion **   <a name="wellarchitected-Type-LensReview-LensVersion"></a>
The version of the lens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** NextToken **   <a name="wellarchitected-Type-LensReview-NextToken"></a>
The token to use to retrieve the next set of results.
Type: String
Required: No

 ** Notes **   <a name="wellarchitected-Type-LensReview-Notes"></a>
The notes associated with the workload.
For a review template, these are the notes that will be associated with the workload when the template is applied.
Type: String
Length Constraints: Maximum length of 2084.
Required: No

 ** PillarReviewSummaries **   <a name="wellarchitected-Type-LensReview-PillarReviewSummaries"></a>
List of pillar review summaries of lens review in a workload.
Type: Array of [PillarReviewSummary](API_PillarReviewSummary.md) objects
Required: No

 ** PrioritizedRiskCounts **   <a name="wellarchitected-Type-LensReview-PrioritizedRiskCounts"></a>
A map from risk names to the count of how many questions have that rating.
Type: String to integer map
Valid Keys: `UNANSWERED | HIGH | MEDIUM | NONE | NOT_APPLICABLE`
Valid Range: Minimum value of 0.
Required: No

 ** Profiles **   <a name="wellarchitected-Type-LensReview-Profiles"></a>
The profiles associated with the workload.
Type: Array of [WorkloadProfile](API_WorkloadProfile.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** RiskCounts **   <a name="wellarchitected-Type-LensReview-RiskCounts"></a>
A map from risk names to the count of how many questions have that rating.
Type: String to integer map
Valid Keys: `UNANSWERED | HIGH | MEDIUM | NONE | NOT_APPLICABLE`
Valid Range: Minimum value of 0.
Required: No

 ** UpdatedAt **   <a name="wellarchitected-Type-LensReview-UpdatedAt"></a>
The date and time recorded in Unix format (seconds).
Type: Timestamp
Required: No

## See Also
<a name="API_LensReview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/LensReview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/LensReview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/LensReview)
