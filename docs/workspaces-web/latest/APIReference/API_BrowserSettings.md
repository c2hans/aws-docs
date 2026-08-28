---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_BrowserSettings.html
---

# BrowserSettings
<a name="API_BrowserSettings"></a>

The browser settings resource that can be associated with a web portal. Once associated with a web portal, browser settings control how the browser will behave once a user starts a streaming session for the web portal.

## Contents
<a name="API_BrowserSettings_Contents"></a>

 ** browserSettingsArn **   <a name="workspacesweb-Type-BrowserSettings-browserSettingsArn"></a>
The ARN of the browser settings.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: Yes

 ** additionalEncryptionContext **   <a name="workspacesweb-Type-BrowserSettings-additionalEncryptionContext"></a>
The additional encryption context of the browser settings.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 131072.
Key Pattern: `[\s\S]*`
Value Length Constraints: Minimum length of 0. Maximum length of 131072.
Value Pattern: `[\s\S]*`
Required: No

 ** associatedPortalArns **   <a name="workspacesweb-Type-BrowserSettings-associatedPortalArns"></a>
A list of web portal ARNs that this browser settings is associated with.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

 ** browserPolicy **   <a name="workspacesweb-Type-BrowserSettings-browserPolicy"></a>
A JSON string containing Chrome Enterprise policies that will be applied to all streaming sessions.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 131072.
Pattern: `\{[\S\s]*\}\s*`
Required: No

 ** customerManagedKey **   <a name="workspacesweb-Type-BrowserSettings-customerManagedKey"></a>
The customer managed key used to encrypt sensitive information in the browser settings.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:kms:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:key\/[a-zA-Z0-9-]+`
Required: No

 ** webContentFilteringPolicy **   <a name="workspacesweb-Type-BrowserSettings-webContentFilteringPolicy"></a>
The policy that specifies which URLs end users are allowed to access or which URLs or domain categories they are restricted from accessing for enhanced security.
Type: [WebContentFilteringPolicy](API_WebContentFilteringPolicy.md) object
Required: No

## See Also
<a name="API_BrowserSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/BrowserSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/BrowserSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/BrowserSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
