---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ShareInvitation.html
---

# ShareInvitation
<a name="API_ShareInvitation"></a>

The share invitation.

## Contents
<a name="API_ShareInvitation_Contents"></a>

 ** LensAlias **   <a name="wellarchitected-Type-ShareInvitation-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** LensArn **   <a name="wellarchitected-Type-ShareInvitation-LensArn"></a>
The ARN for the lens.
Type: String
Required: No

 ** ProfileArn **   <a name="wellarchitected-Type-ShareInvitation-ProfileArn"></a>
The profile ARN.
Type: String
Length Constraints: Maximum length of 2084.
Pattern: `arn:aws[-a-z]*:wellarchitected:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:profile/[a-z0-9]+`
Required: No

 ** ShareInvitationId **   <a name="wellarchitected-Type-ShareInvitation-ShareInvitationId"></a>
The ID assigned to the share invitation.
Type: String
Pattern: `[0-9a-f]{32}`
Required: No

 ** ShareResourceType **   <a name="wellarchitected-Type-ShareInvitation-ShareResourceType"></a>
The resource type of the share invitation.
Type: String
Valid Values: `WORKLOAD | LENS | PROFILE | TEMPLATE`
Required: No

 ** TemplateArn **   <a name="wellarchitected-Type-ShareInvitation-TemplateArn"></a>
The review template ARN.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 250.
Pattern: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`
Required: No

 ** WorkloadId **   <a name="wellarchitected-Type-ShareInvitation-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: No

## See Also
<a name="API_ShareInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ShareInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ShareInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ShareInvitation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
