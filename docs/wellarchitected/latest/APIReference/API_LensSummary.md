---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_LensSummary.html
---

# LensSummary
<a name="API_LensSummary"></a>

A lens summary of a lens.

## Contents
<a name="API_LensSummary_Contents"></a>

 ** CreatedAt **   <a name="wellarchitected-Type-LensSummary-CreatedAt"></a>
The date and time recorded in Unix format (seconds).
Type: Timestamp
Required: No

 ** Description **   <a name="wellarchitected-Type-LensSummary-Description"></a>
The description of the lens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** LensAlias **   <a name="wellarchitected-Type-LensSummary-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](#wellarchitected-Type-LensSummary-LensAlias).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** LensArn **   <a name="wellarchitected-Type-LensSummary-LensArn"></a>
The ARN of the lens.
Type: String
Required: No

 ** LensName **   <a name="wellarchitected-Type-LensSummary-LensName"></a>
The full name of the lens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** LensStatus **   <a name="wellarchitected-Type-LensSummary-LensStatus"></a>
The status of the lens.
Type: String
Valid Values: `CURRENT | NOT_CURRENT | DEPRECATED | DELETED | UNSHARED`
Required: No

 ** LensType **   <a name="wellarchitected-Type-LensSummary-LensType"></a>
The type of the lens.
Type: String
Valid Values: `AWS_OFFICIAL | CUSTOM_SHARED | CUSTOM_SELF`
Required: No

 ** LensVersion **   <a name="wellarchitected-Type-LensSummary-LensVersion"></a>
The version of the lens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** Owner **   <a name="wellarchitected-Type-LensSummary-Owner"></a>
An AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** UpdatedAt **   <a name="wellarchitected-Type-LensSummary-UpdatedAt"></a>
The date and time recorded in Unix format (seconds).
Type: Timestamp
Required: No

## See Also
<a name="API_LensSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/LensSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/LensSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/LensSummary)
