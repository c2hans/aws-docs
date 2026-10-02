---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ProfileSummary.html
---

# ProfileSummary
<a name="API_ProfileSummary"></a>

Summary of a profile.

## Contents
<a name="API_ProfileSummary_Contents"></a>

 ** CreatedAt **   <a name="wellarchitected-Type-ProfileSummary-CreatedAt"></a>
The date and time when the profile was created.
Type: Timestamp
Required: No

 ** Owner **   <a name="wellarchitected-Type-ProfileSummary-Owner"></a>
An AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** ProfileArn **   <a name="wellarchitected-Type-ProfileSummary-ProfileArn"></a>
The profile ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2084.
Pattern: `arn:aws[-a-z]*:wellarchitected:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:profile/[a-z0-9]+`
Required: No

 ** ProfileDescription **   <a name="wellarchitected-Type-ProfileSummary-ProfileDescription"></a>
The profile description.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

 ** ProfileName **   <a name="wellarchitected-Type-ProfileSummary-ProfileName"></a>
The profile name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

 ** ProfileVersion **   <a name="wellarchitected-Type-ProfileSummary-ProfileVersion"></a>
The profile version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[A-Za-z0-9-]+`
Required: No

 ** UpdatedAt **   <a name="wellarchitected-Type-ProfileSummary-UpdatedAt"></a>
The date and time when the profile was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ProfileSummary)
