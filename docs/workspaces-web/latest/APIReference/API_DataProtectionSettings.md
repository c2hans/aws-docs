---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_DataProtectionSettings.html
---

# DataProtectionSettings
<a name="API_DataProtectionSettings"></a>

The data protection settings resource that can be associated with a web portal.

## Contents
<a name="API_DataProtectionSettings_Contents"></a>

 ** dataProtectionSettingsArn **   <a name="workspacesweb-Type-DataProtectionSettings-dataProtectionSettingsArn"></a>
The ARN of the data protection settings resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: Yes

 ** additionalEncryptionContext **   <a name="workspacesweb-Type-DataProtectionSettings-additionalEncryptionContext"></a>
The additional encryption context of the data protection settings.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 131072.
Key Pattern: `[\s\S]*`
Value Length Constraints: Minimum length of 0. Maximum length of 131072.
Value Pattern: `[\s\S]*`
Required: No

 ** associatedPortalArns **   <a name="workspacesweb-Type-DataProtectionSettings-associatedPortalArns"></a>
A list of web portal ARNs that this data protection settings resource is associated with.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

 ** creationDate **   <a name="workspacesweb-Type-DataProtectionSettings-creationDate"></a>
The creation date timestamp of the data protection settings.
Type: Timestamp
Required: No

 ** customerManagedKey **   <a name="workspacesweb-Type-DataProtectionSettings-customerManagedKey"></a>
The customer managed key used to encrypt sensitive information in the data protection settings.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:kms:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:key\/[a-zA-Z0-9-]+`
Required: No

 ** description **   <a name="workspacesweb-Type-DataProtectionSettings-description"></a>
The description of the data protection settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ _\-\d\w]+`
Required: No

 ** displayName **   <a name="workspacesweb-Type-DataProtectionSettings-displayName"></a>
The display name of the data protection settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[ _\-\d\w]+`
Required: No

 ** inlineRedactionConfiguration **   <a name="workspacesweb-Type-DataProtectionSettings-inlineRedactionConfiguration"></a>
The inline redaction configuration for the data protection settings.
Type: [InlineRedactionConfiguration](API_InlineRedactionConfiguration.md) object
Required: No

## See Also
<a name="API_DataProtectionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/DataProtectionSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/DataProtectionSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/DataProtectionSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
