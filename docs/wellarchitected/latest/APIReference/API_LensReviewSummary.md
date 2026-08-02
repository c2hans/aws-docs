---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_LensReviewSummary.html
---

# LensReviewSummary
<a name="API_LensReviewSummary"></a>

A lens review summary of a workload.

## Contents
<a name="API_LensReviewSummary_Contents"></a>

 ** LensAlias **   <a name="wellarchitected-Type-LensReviewSummary-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** LensArn **   <a name="wellarchitected-Type-LensReviewSummary-LensArn"></a>
The ARN for the lens.
Type: String
Required: No

 ** LensName **   <a name="wellarchitected-Type-LensReviewSummary-LensName"></a>
The full name of the lens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** LensStatus **   <a name="wellarchitected-Type-LensReviewSummary-LensStatus"></a>
The status of the lens.
Type: String
Valid Values: `CURRENT | NOT_CURRENT | DEPRECATED | DELETED | UNSHARED`
Required: No

 ** LensVersion **   <a name="wellarchitected-Type-LensReviewSummary-LensVersion"></a>
The version of the lens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** PrioritizedRiskCounts **   <a name="wellarchitected-Type-LensReviewSummary-PrioritizedRiskCounts"></a>
A map from risk names to the count of how many questions have that rating.
Type: String to integer map
Valid Keys: `UNANSWERED | HIGH | MEDIUM | NONE | NOT_APPLICABLE`
Valid Range: Minimum value of 0.
Required: No

 ** Profiles **   <a name="wellarchitected-Type-LensReviewSummary-Profiles"></a>
The profiles associated with the workload.
Type: Array of [WorkloadProfile](API_WorkloadProfile.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** RiskCounts **   <a name="wellarchitected-Type-LensReviewSummary-RiskCounts"></a>
A map from risk names to the count of how many questions have that rating.
Type: String to integer map
Valid Keys: `UNANSWERED | HIGH | MEDIUM | NONE | NOT_APPLICABLE`
Valid Range: Minimum value of 0.
Required: No

 ** UpdatedAt **   <a name="wellarchitected-Type-LensReviewSummary-UpdatedAt"></a>
The date and time recorded in Unix format (seconds).
Type: Timestamp
Required: No

## See Also
<a name="API_LensReviewSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/LensReviewSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/LensReviewSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/LensReviewSummary)
