---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_DataProtectionSettingsSummary.html
---

# DataProtectionSettingsSummary
<a name="API_DataProtectionSettingsSummary"></a>

The summary of the data protection settings.

## Contents
<a name="API_DataProtectionSettingsSummary_Contents"></a>

 ** dataProtectionSettingsArn **   <a name="workspacesweb-Type-DataProtectionSettingsSummary-dataProtectionSettingsArn"></a>
The ARN of the data protection settings.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: Yes

 ** creationDate **   <a name="workspacesweb-Type-DataProtectionSettingsSummary-creationDate"></a>
The creation date timestamp of the data protection settings.
Type: Timestamp
Required: No

 ** description **   <a name="workspacesweb-Type-DataProtectionSettingsSummary-description"></a>
The description of the data protection settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ _\-\d\w]+`
Required: No

 ** displayName **   <a name="workspacesweb-Type-DataProtectionSettingsSummary-displayName"></a>
The display name of the data protection settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[ _\-\d\w]+`
Required: No

## See Also
<a name="API_DataProtectionSettingsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/DataProtectionSettingsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/DataProtectionSettingsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/DataProtectionSettingsSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
