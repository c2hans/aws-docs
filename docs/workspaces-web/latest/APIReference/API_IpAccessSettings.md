---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_IpAccessSettings.html
---

# IpAccessSettings
<a name="API_IpAccessSettings"></a>

The IP access settings resource that can be associated with a web portal.

## Contents
<a name="API_IpAccessSettings_Contents"></a>

 ** ipAccessSettingsArn **   <a name="workspacesweb-Type-IpAccessSettings-ipAccessSettingsArn"></a>
The ARN of the IP access settings resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: Yes

 ** additionalEncryptionContext **   <a name="workspacesweb-Type-IpAccessSettings-additionalEncryptionContext"></a>
The additional encryption context of the IP access settings.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 131072.
Key Pattern: `[\s\S]*`
Value Length Constraints: Minimum length of 0. Maximum length of 131072.
Value Pattern: `[\s\S]*`
Required: No

 ** associatedPortalArns **   <a name="workspacesweb-Type-IpAccessSettings-associatedPortalArns"></a>
A list of web portal ARNs that this IP access settings resource is associated with.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

 ** creationDate **   <a name="workspacesweb-Type-IpAccessSettings-creationDate"></a>
The creation date timestamp of the IP access settings.
Type: Timestamp
Required: No

 ** customerManagedKey **   <a name="workspacesweb-Type-IpAccessSettings-customerManagedKey"></a>
The customer managed key used to encrypt sensitive information in the IP access settings.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:kms:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:key\/[a-zA-Z0-9-]+`
Required: No

 ** description **   <a name="workspacesweb-Type-IpAccessSettings-description"></a>
The description of the IP access settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.+`
Required: No

 ** displayName **   <a name="workspacesweb-Type-IpAccessSettings-displayName"></a>
 The display name of the IP access settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.+`
Required: No

 ** ipRules **   <a name="workspacesweb-Type-IpAccessSettings-ipRules"></a>
The IP rules of the IP access settings.
Type: Array of [IpRule](API_IpRule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## See Also
<a name="API_IpAccessSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/IpAccessSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/IpAccessSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/IpAccessSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
