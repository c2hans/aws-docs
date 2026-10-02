---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ReviewTemplateSummary.html
---

# ReviewTemplateSummary
<a name="API_ReviewTemplateSummary"></a>

Summary of a review template.

## Contents
<a name="API_ReviewTemplateSummary_Contents"></a>

 ** Description **   <a name="wellarchitected-Type-ReviewTemplateSummary-Description"></a>
Description of the review template.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 250.
Pattern: `[A-Za-z0-9-_.,:/()@!&?#+'’\s]+`
Required: No

 ** Lenses **   <a name="wellarchitected-Type-ReviewTemplateSummary-Lenses"></a>
Lenses associated with the review template.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Owner **   <a name="wellarchitected-Type-ReviewTemplateSummary-Owner"></a>
An AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** TemplateArn **   <a name="wellarchitected-Type-ReviewTemplateSummary-TemplateArn"></a>
The review template ARN.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 250.
Pattern: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`
Required: No

 ** TemplateName **   <a name="wellarchitected-Type-ReviewTemplateSummary-TemplateName"></a>
The name of the review template.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `[A-Za-z0-9-_.,:/()@!&?#+'’\s]+`
Required: No

 ** UpdatedAt **   <a name="wellarchitected-Type-ReviewTemplateSummary-UpdatedAt"></a>
The date and time when the review template was last updated.
Type: Timestamp
Required: No

 ** UpdateStatus **   <a name="wellarchitected-Type-ReviewTemplateSummary-UpdateStatus"></a>
The latest status of a review template.
Type: String
Valid Values: `CURRENT | LENS_NOT_CURRENT`
Required: No

## See Also
<a name="API_ReviewTemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ReviewTemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ReviewTemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ReviewTemplateSummary)
