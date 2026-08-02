---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_UserSettings.html
---

# UserSettings
<a name="API_UserSettings"></a>

A user settings resource that can be associated with a web portal. Once associated with a web portal, user settings control how users can transfer data between a streaming session and the their local devices.

## Contents
<a name="API_UserSettings_Contents"></a>

 ** userSettingsArn **   <a name="workspacesweb-Type-UserSettings-userSettingsArn"></a>
The ARN of the user settings.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: Yes

 ** additionalEncryptionContext **   <a name="workspacesweb-Type-UserSettings-additionalEncryptionContext"></a>
The additional encryption context of the user settings.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 131072.
Key Pattern: `[\s\S]*`
Value Length Constraints: Minimum length of 0. Maximum length of 131072.
Value Pattern: `[\s\S]*`
Required: No

 ** associatedPortalArns **   <a name="workspacesweb-Type-UserSettings-associatedPortalArns"></a>
A list of web portal ARNs that this user settings is associated with.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

 ** brandingConfiguration **   <a name="workspacesweb-Type-UserSettings-brandingConfiguration"></a>
The branding configuration output that customizes the appearance of the web portal for end users.
Type: [BrandingConfiguration](API_BrandingConfiguration.md) object
Required: No

 ** cookieSynchronizationConfiguration **   <a name="workspacesweb-Type-UserSettings-cookieSynchronizationConfiguration"></a>
The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.
Type: [CookieSynchronizationConfiguration](API_CookieSynchronizationConfiguration.md) object
Required: No

 ** copyAllowed **   <a name="workspacesweb-Type-UserSettings-copyAllowed"></a>
Specifies whether the user can copy text from the streaming session to the local device.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** customerManagedKey **   <a name="workspacesweb-Type-UserSettings-customerManagedKey"></a>
The customer managed key used to encrypt sensitive information in the user settings.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:kms:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:key\/[a-zA-Z0-9-]+`
Required: No

 ** deepLinkAllowed **   <a name="workspacesweb-Type-UserSettings-deepLinkAllowed"></a>
Specifies whether the user can use deep links that open automatically when connecting to a session.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** disconnectTimeoutInMinutes **   <a name="workspacesweb-Type-UserSettings-disconnectTimeoutInMinutes"></a>
The amount of time that a streaming session remains active after users disconnect.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 600.
Required: No

 ** downloadAllowed **   <a name="workspacesweb-Type-UserSettings-downloadAllowed"></a>
Specifies whether the user can download files from the streaming session to the local device.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** idleDisconnectTimeoutInMinutes **   <a name="workspacesweb-Type-UserSettings-idleDisconnectTimeoutInMinutes"></a>
The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 60.
Required: No

 ** pasteAllowed **   <a name="workspacesweb-Type-UserSettings-pasteAllowed"></a>
Specifies whether the user can paste text from the local device to the streaming session.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** printAllowed **   <a name="workspacesweb-Type-UserSettings-printAllowed"></a>
Specifies whether the user can print to the local device.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** toolbarConfiguration **   <a name="workspacesweb-Type-UserSettings-toolbarConfiguration"></a>
The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.
Type: [ToolbarConfiguration](API_ToolbarConfiguration.md) object
Required: No

 ** uploadAllowed **   <a name="workspacesweb-Type-UserSettings-uploadAllowed"></a>
Specifies whether the user can upload files from the local device to the streaming session.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** webAuthnAllowed **   <a name="workspacesweb-Type-UserSettings-webAuthnAllowed"></a>
Specifies whether the user can use WebAuthn redirection for passwordless login to websites within the streaming session.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

## See Also
<a name="API_UserSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/UserSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/UserSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/UserSettings)
