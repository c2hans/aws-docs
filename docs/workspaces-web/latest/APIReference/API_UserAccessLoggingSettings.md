---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_UserAccessLoggingSettings.html
---

# UserAccessLoggingSettings
<a name="API_UserAccessLoggingSettings"></a>

A user access logging settings resource that can be associated with a web portal.

## Contents
<a name="API_UserAccessLoggingSettings_Contents"></a>

 ** userAccessLoggingSettingsArn **   <a name="workspacesweb-Type-UserAccessLoggingSettings-userAccessLoggingSettingsArn"></a>
The ARN of the user access logging settings.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: Yes

 ** associatedPortalArns **   <a name="workspacesweb-Type-UserAccessLoggingSettings-associatedPortalArns"></a>
A list of web portal ARNs that this user access logging settings is associated with.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

 ** kinesisStreamArn **   <a name="workspacesweb-Type-UserAccessLoggingSettings-kinesisStreamArn"></a>
The ARN of the Kinesis stream.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:kinesis:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:stream/.+`
Required: No

## See Also
<a name="API_UserAccessLoggingSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/UserAccessLoggingSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/UserAccessLoggingSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/UserAccessLoggingSettings)
