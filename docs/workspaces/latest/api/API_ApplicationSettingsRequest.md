---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ApplicationSettingsRequest.html
---

# ApplicationSettingsRequest
<a name="API_ApplicationSettingsRequest"></a>

The persistent application settings for WorkSpaces Pools users.

## Contents
<a name="API_ApplicationSettingsRequest_Contents"></a>

 ** Status **   <a name="WorkSpaces-Type-ApplicationSettingsRequest-Status"></a>
Enables or disables persistent application settings for users during their pool sessions.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: Yes

 ** SettingsGroup **   <a name="WorkSpaces-Type-ApplicationSettingsRequest-SettingsGroup"></a>
The path prefix for the S3 bucket where users’ persistent application settings are stored. You can allow the same persistent application settings to be used across multiple pools by specifying the same settings group for each pool.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^[A-Za-z0-9_./()!*'-]+$`
Required: No

## See Also
<a name="API_ApplicationSettingsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ApplicationSettingsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ApplicationSettingsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ApplicationSettingsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
