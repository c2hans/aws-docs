---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ApplicationSettings.html
---

# ApplicationSettings
<a name="API_ApplicationSettings"></a>

The persistent application settings for users of a stack.

## Contents
<a name="API_ApplicationSettings_Contents"></a>

 ** Enabled **   <a name="WorkSpacesApplications-Type-ApplicationSettings-Enabled"></a>
Enables or disables persistent application settings for users during their streaming sessions.
Type: Boolean
Required: Yes

 ** SettingsGroup **   <a name="WorkSpacesApplications-Type-ApplicationSettings-SettingsGroup"></a>
The path prefix for the S3 bucket where users’ persistent application settings are stored. You can allow the same persistent application settings to be used across multiple stacks by specifying the same settings group for each stack.
Type: String
Length Constraints: Maximum length of 100.
Required: No

## See Also
<a name="API_ApplicationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ApplicationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ApplicationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ApplicationSettings)
