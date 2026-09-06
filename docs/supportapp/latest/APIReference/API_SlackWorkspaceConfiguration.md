---
source_url: https://docs.aws.amazon.com/supportapp/latest/APIReference/API_SlackWorkspaceConfiguration.html
---

# SlackWorkspaceConfiguration
<a name="API_SlackWorkspaceConfiguration"></a>

The configuration for a Slack workspace that you added to an AWS account.

## Contents
<a name="API_SlackWorkspaceConfiguration_Contents"></a>

 ** teamId **   <a name="supportapp-Type-SlackWorkspaceConfiguration-teamId"></a>
The team ID in Slack. This ID uniquely identifies a Slack workspace, such as `T012ABCDEFG`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

 ** allowOrganizationMemberAccount **   <a name="supportapp-Type-SlackWorkspaceConfiguration-allowOrganizationMemberAccount"></a>
Whether to allow member accounts to authorize Slack workspaces. Member accounts must be part of an organization in AWS Organizations.
Type: Boolean
Required: No

 ** teamName **   <a name="supportapp-Type-SlackWorkspaceConfiguration-teamName"></a>
The name of the Slack workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.+`
Required: No

## See Also
<a name="API_SlackWorkspaceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-app-2021-08-20/SlackWorkspaceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-app-2021-08-20/SlackWorkspaceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-app-2021-08-20/SlackWorkspaceConfiguration)
