---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ShareInvitationSummary.html
---

# ShareInvitationSummary
<a name="API_ShareInvitationSummary"></a>

A share invitation summary return object.

## Contents
<a name="API_ShareInvitationSummary_Contents"></a>

 ** LensArn **   <a name="wellarchitected-Type-ShareInvitationSummary-LensArn"></a>
The ARN for the lens.
Type: String
Required: No

 ** LensName **   <a name="wellarchitected-Type-ShareInvitationSummary-LensName"></a>
The full name of the lens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** PermissionType **   <a name="wellarchitected-Type-ShareInvitationSummary-PermissionType"></a>
Permission granted on a share request.
Type: String
Valid Values: `READONLY | CONTRIBUTOR`
Required: No

 ** ProfileArn **   <a name="wellarchitected-Type-ShareInvitationSummary-ProfileArn"></a>
The profile ARN.
Type: String
Length Constraints: Maximum length of 2084.
Pattern: `arn:aws[-a-z]*:wellarchitected:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:profile/[a-z0-9]+`
Required: No

 ** ProfileName **   <a name="wellarchitected-Type-ShareInvitationSummary-ProfileName"></a>
The profile name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

 ** SharedBy **   <a name="wellarchitected-Type-ShareInvitationSummary-SharedBy"></a>
An AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** SharedWith **   <a name="wellarchitected-Type-ShareInvitationSummary-SharedWith"></a>
The AWS account ID, organization ID, or organizational unit (OU) ID with which the workload, lens, profile, or review template is shared.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 2048.
Required: No

 ** ShareInvitationId **   <a name="wellarchitected-Type-ShareInvitationSummary-ShareInvitationId"></a>
The ID assigned to the share invitation.
Type: String
Pattern: `[0-9a-f]{32}`
Required: No

 ** ShareResourceType **   <a name="wellarchitected-Type-ShareInvitationSummary-ShareResourceType"></a>
The resource type of the share invitation.
Type: String
Valid Values: `WORKLOAD | LENS | PROFILE | TEMPLATE`
Required: No

 ** TemplateArn **   <a name="wellarchitected-Type-ShareInvitationSummary-TemplateArn"></a>
The review template ARN.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 250.
Pattern: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`
Required: No

 ** TemplateName **   <a name="wellarchitected-Type-ShareInvitationSummary-TemplateName"></a>
The name of the review template.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `^[A-Za-z0-9-_.,:/()@!&?#+'’\s]+$`
Required: No

 ** WorkloadId **   <a name="wellarchitected-Type-ShareInvitationSummary-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: No

 ** WorkloadName **   <a name="wellarchitected-Type-ShareInvitationSummary-WorkloadName"></a>
The name of the workload.
The name must be unique within an account within an AWS Region. Spaces and capitalization are ignored when checking for uniqueness.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

## See Also
<a name="API_ShareInvitationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ShareInvitationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ShareInvitationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ShareInvitationSummary)
