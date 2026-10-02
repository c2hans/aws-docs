---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ReviewTemplate.html
---

# ReviewTemplate
<a name="API_ReviewTemplate"></a>

A review template.

## Contents
<a name="API_ReviewTemplate_Contents"></a>

 ** Description **   <a name="wellarchitected-Type-ReviewTemplate-Description"></a>
The review template description.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 250.
Pattern: `[A-Za-z0-9-_.,:/()@!&?#+'’\s]+`
Required: No

 ** Lenses **   <a name="wellarchitected-Type-ReviewTemplate-Lenses"></a>
The lenses applied to the review template.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Notes **   <a name="wellarchitected-Type-ReviewTemplate-Notes"></a>
The notes associated with the workload.
For a review template, these are the notes that will be associated with the workload when the template is applied.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2084.
Required: No

 ** Owner **   <a name="wellarchitected-Type-ReviewTemplate-Owner"></a>
An AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** QuestionCounts **   <a name="wellarchitected-Type-ReviewTemplate-QuestionCounts"></a>
A count of how many total questions are answered and unanswered in the review template.
Type: String to integer map
Valid Keys: `UNANSWERED | ANSWERED`
Valid Range: Minimum value of 0.
Required: No

 ** ShareInvitationId **   <a name="wellarchitected-Type-ReviewTemplate-ShareInvitationId"></a>
The ID assigned to the template share invitation.
Type: String
Pattern: `[0-9a-f]{32}`
Required: No

 ** Tags **   <a name="wellarchitected-Type-ReviewTemplate-Tags"></a>
The tags assigned to the review template.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}\p{N}\p{Z}_.:/=+@-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** TemplateArn **   <a name="wellarchitected-Type-ReviewTemplate-TemplateArn"></a>
The review template ARN.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 250.
Pattern: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`
Required: No

 ** TemplateName **   <a name="wellarchitected-Type-ReviewTemplate-TemplateName"></a>
The name of the review template.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `[A-Za-z0-9-_.,:/()@!&?#+'’\s]+`
Required: No

 ** UpdatedAt **   <a name="wellarchitected-Type-ReviewTemplate-UpdatedAt"></a>
The date and time when the review template was last updated.
Type: Timestamp
Required: No

 ** UpdateStatus **   <a name="wellarchitected-Type-ReviewTemplate-UpdateStatus"></a>
The latest status of a review template.
Type: String
Valid Values: `CURRENT | LENS_NOT_CURRENT`
Required: No

## See Also
<a name="API_ReviewTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ReviewTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ReviewTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ReviewTemplate)
