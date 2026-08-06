---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ClientProperties.html
---

# ClientProperties
<a name="API_ClientProperties"></a>

Describes an Amazon WorkSpaces client.

## Contents
<a name="API_ClientProperties_Contents"></a>

 ** ClientExperiencePolicy **   <a name="WorkSpaces-Type-ClientProperties-ClientExperiencePolicy"></a>
The client experience policy that determines which client experience the user sees. Administrators can set this policy to control the client experience for users in a directory. Valid values include `FORCE_CLASSIC`, `FORCE_UI_2026`, and `USER_CHOICE`.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `^[A-Z_0-9]+$`
Required: No

 ** LogUploadEnabled **   <a name="WorkSpaces-Type-ClientProperties-LogUploadEnabled"></a>
Specifies whether users can upload diagnostic log files of Amazon WorkSpaces client directly to WorkSpaces to troubleshoot issues when using the WorkSpaces client. When enabled, the log files will be sent to WorkSpaces automatically and will be applied to all users in the specified directory.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** ReconnectEnabled **   <a name="WorkSpaces-Type-ClientProperties-ReconnectEnabled"></a>
Specifies whether users can cache their credentials on the Amazon WorkSpaces client. When enabled, users can choose to reconnect to their WorkSpaces without re-entering their credentials.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_ClientProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ClientProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ClientProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ClientProperties)
