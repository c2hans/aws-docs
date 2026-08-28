---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Profile.html
---

# Profile
<a name="API_Profile"></a>

A profile.

## Contents
<a name="API_Profile_Contents"></a>

 ** CreatedAt **   <a name="wellarchitected-Type-Profile-CreatedAt"></a>
The date and time recorded in Unix format (seconds).
Type: Timestamp
Required: No

 ** Owner **   <a name="wellarchitected-Type-Profile-Owner"></a>
An AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** ProfileArn **   <a name="wellarchitected-Type-Profile-ProfileArn"></a>
The profile ARN.
Type: String
Length Constraints: Maximum length of 2084.
Pattern: `arn:aws[-a-z]*:wellarchitected:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:profile/[a-z0-9]+`
Required: No

 ** ProfileDescription **   <a name="wellarchitected-Type-Profile-ProfileDescription"></a>
The profile description.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

 ** ProfileName **   <a name="wellarchitected-Type-Profile-ProfileName"></a>
The profile name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

 ** ProfileQuestions **   <a name="wellarchitected-Type-Profile-ProfileQuestions"></a>
Profile questions.
Type: Array of [ProfileQuestion](API_ProfileQuestion.md) objects
Required: No

 ** ProfileVersion **   <a name="wellarchitected-Type-Profile-ProfileVersion"></a>
The profile version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[A-Za-z0-9-]+$`
Required: No

 ** ShareInvitationId **   <a name="wellarchitected-Type-Profile-ShareInvitationId"></a>
The ID assigned to the share invitation.
Type: String
Pattern: `[0-9a-f]{32}`
Required: No

 ** Tags **   <a name="wellarchitected-Type-Profile-Tags"></a>
The tags assigned to the profile.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** UpdatedAt **   <a name="wellarchitected-Type-Profile-UpdatedAt"></a>
The date and time recorded in Unix format (seconds).
Type: Timestamp
Required: No

## See Also
<a name="API_Profile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/Profile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/Profile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/Profile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
