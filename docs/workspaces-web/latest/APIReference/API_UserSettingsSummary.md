---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_UserSettingsSummary.html
---

# UserSettingsSummary
<a name="API_UserSettingsSummary"></a>

The summary of user settings.

## Contents
<a name="API_UserSettingsSummary_Contents"></a>

 ** userSettingsArn **   <a name="workspacesweb-Type-UserSettingsSummary-userSettingsArn"></a>
The ARN of the user settings.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: Yes

 ** brandingConfiguration **   <a name="workspacesweb-Type-UserSettingsSummary-brandingConfiguration"></a>
The branding configuration output that customizes the appearance of the web portal for end users.
Type: [BrandingConfiguration](API_BrandingConfiguration.md) object
Required: No

 ** cookieSynchronizationConfiguration **   <a name="workspacesweb-Type-UserSettingsSummary-cookieSynchronizationConfiguration"></a>
The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.
Type: [CookieSynchronizationConfiguration](API_CookieSynchronizationConfiguration.md) object
Required: No

 ** copyAllowed **   <a name="workspacesweb-Type-UserSettingsSummary-copyAllowed"></a>
Specifies whether the user can copy text from the streaming session to the local device.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** deepLinkAllowed **   <a name="workspacesweb-Type-UserSettingsSummary-deepLinkAllowed"></a>
Specifies whether the user can use deep links that open automatically when connecting to a session.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** disconnectTimeoutInMinutes **   <a name="workspacesweb-Type-UserSettingsSummary-disconnectTimeoutInMinutes"></a>
The amount of time that a streaming session remains active after users disconnect.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 600.
Required: No

 ** downloadAllowed **   <a name="workspacesweb-Type-UserSettingsSummary-downloadAllowed"></a>
Specifies whether the user can download files from the streaming session to the local device.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** idleDisconnectTimeoutInMinutes **   <a name="workspacesweb-Type-UserSettingsSummary-idleDisconnectTimeoutInMinutes"></a>
The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 60.
Required: No

 ** pasteAllowed **   <a name="workspacesweb-Type-UserSettingsSummary-pasteAllowed"></a>
Specifies whether the user can paste text from the local device to the streaming session.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** printAllowed **   <a name="workspacesweb-Type-UserSettingsSummary-printAllowed"></a>
Specifies whether the user can print to the local device.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** toolbarConfiguration **   <a name="workspacesweb-Type-UserSettingsSummary-toolbarConfiguration"></a>
The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.
Type: [ToolbarConfiguration](API_ToolbarConfiguration.md) object
Required: No

 ** uploadAllowed **   <a name="workspacesweb-Type-UserSettingsSummary-uploadAllowed"></a>
Specifies whether the user can upload files from the local device to the streaming session.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** webAuthnAllowed **   <a name="workspacesweb-Type-UserSettingsSummary-webAuthnAllowed"></a>
Specifies whether the user can use WebAuthn redirection for passwordless login to websites within the streaming session.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

## See Also
<a name="API_UserSettingsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/UserSettingsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/UserSettingsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/UserSettingsSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
