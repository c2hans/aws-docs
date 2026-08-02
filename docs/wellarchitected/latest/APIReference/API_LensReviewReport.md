---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_LensReviewReport.html
---

# LensReviewReport
<a name="API_LensReviewReport"></a>

A report of a lens review.

## Contents
<a name="API_LensReviewReport_Contents"></a>

 ** Base64String **   <a name="wellarchitected-Type-LensReviewReport-Base64String"></a>
The Base64-encoded string representation of a lens review report.
This data can be used to create a PDF file.
Only returned by [GetConsolidatedReport](API_GetConsolidatedReport.md) when `PDF` format is requested.
Type: String
Required: No

 ** LensAlias **   <a name="wellarchitected-Type-LensReviewReport-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** LensArn **   <a name="wellarchitected-Type-LensReviewReport-LensArn"></a>
The ARN for the lens.
Type: String
Required: No

## See Also
<a name="API_LensReviewReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/LensReviewReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/LensReviewReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/LensReviewReport)
