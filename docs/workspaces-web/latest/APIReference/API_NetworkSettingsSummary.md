---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_NetworkSettingsSummary.html
---

# NetworkSettingsSummary
<a name="API_NetworkSettingsSummary"></a>

The summary of network settings.

## Contents
<a name="API_NetworkSettingsSummary_Contents"></a>

 ** networkSettingsArn **   <a name="workspacesweb-Type-NetworkSettingsSummary-networkSettingsArn"></a>
The ARN of the network settings.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: Yes

 ** vpcId **   <a name="workspacesweb-Type-NetworkSettingsSummary-vpcId"></a>
The VPC ID of the network settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `vpc-[0-9a-z]*`
Required: No

## See Also
<a name="API_NetworkSettingsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/NetworkSettingsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/NetworkSettingsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/NetworkSettingsSummary)
