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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
