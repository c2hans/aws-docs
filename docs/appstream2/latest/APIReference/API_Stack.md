---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_Stack.html
---

# Stack
<a name="API_Stack"></a>

Describes a stack.

## Contents
<a name="API_Stack_Contents"></a>

 ** Name **   <a name="WorkSpacesApplications-Type-Stack-Name"></a>
The name of the stack.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** AccessEndpoints **   <a name="WorkSpacesApplications-Type-Stack-AccessEndpoints"></a>
The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack can connect to WorkSpaces Applications only through the specified endpoints.
Type: Array of [AccessEndpoint](API_AccessEndpoint.md) objects
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Required: No

 ** AgentAccessConfig **   <a name="WorkSpacesApplications-Type-Stack-AgentAccessConfig"></a>
The agent access configuration of the stack, if agent access is enabled.
Type: [AgentAccessConfig](API_AgentAccessConfig.md) object
Required: No

 ** ApplicationSettings **   <a name="WorkSpacesApplications-Type-Stack-ApplicationSettings"></a>
The persistent application settings for users of the stack.
Type: [ApplicationSettingsResponse](API_ApplicationSettingsResponse.md) object
Required: No

 ** Arn **   <a name="WorkSpacesApplications-Type-Stack-Arn"></a>
The ARN of the stack.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** CreatedTime **   <a name="WorkSpacesApplications-Type-Stack-CreatedTime"></a>
The time the stack was created.
Type: Timestamp
Required: No

 ** Description **   <a name="WorkSpacesApplications-Type-Stack-Description"></a>
The description to display.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** DisplayName **   <a name="WorkSpacesApplications-Type-Stack-DisplayName"></a>
The stack name to display.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** EmbedHostDomains **   <a name="WorkSpacesApplications-Type-Stack-EmbedHostDomains"></a>
The domains where WorkSpaces Applications streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded WorkSpaces Applications streaming sessions.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Maximum length of 128.
Pattern: `(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]`
Required: No

 ** FeedbackURL **   <a name="WorkSpacesApplications-Type-Stack-FeedbackURL"></a>
The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.
Type: String
Length Constraints: Maximum length of 1000.
Required: No

 ** RedirectURL **   <a name="WorkSpacesApplications-Type-Stack-RedirectURL"></a>
The URL that users are redirected to after their streaming session ends.
Type: String
Length Constraints: Maximum length of 1000.
Required: No

 ** StackErrors **   <a name="WorkSpacesApplications-Type-Stack-StackErrors"></a>
The errors for the stack.
Type: Array of [StackError](API_StackError.md) objects
Required: No

 ** StorageConnectors **   <a name="WorkSpacesApplications-Type-Stack-StorageConnectors"></a>
The storage connectors to enable.
Type: Array of [StorageConnector](API_StorageConnector.md) objects
Required: No

 ** StreamingExperienceSettings **   <a name="WorkSpacesApplications-Type-Stack-StreamingExperienceSettings"></a>
The streaming protocol you want your stack to prefer. This can be UDP or TCP. Currently, UDP is only supported in the Windows native client.
Type: [StreamingExperienceSettings](API_StreamingExperienceSettings.md) object
Required: No

 ** UserSettings **   <a name="WorkSpacesApplications-Type-Stack-UserSettings"></a>
The actions that are enabled or disabled for users during their streaming sessions. By default these actions are enabled.
Type: Array of [UserSetting](API_UserSetting.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_Stack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/Stack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/Stack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/Stack)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
