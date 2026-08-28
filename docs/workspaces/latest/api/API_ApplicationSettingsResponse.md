---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ApplicationSettingsResponse.html
---

# ApplicationSettingsResponse
<a name="API_ApplicationSettingsResponse"></a>

Describes the persistent application settings for WorkSpaces Pools users.

## Contents
<a name="API_ApplicationSettingsResponse_Contents"></a>

 ** Status **   <a name="WorkSpaces-Type-ApplicationSettingsResponse-Status"></a>
Specifies whether persistent application settings are enabled for users during their pool sessions.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: Yes

 ** S3BucketName **   <a name="WorkSpaces-Type-ApplicationSettingsResponse-S3BucketName"></a>
The S3 bucket where users’ persistent application settings are stored. When persistent application settings are enabled for the first time for an account in an AWS Region, an S3 bucket is created. The bucket is unique to the AWS account and the Region.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
Required: No

 ** SettingsGroup **   <a name="WorkSpaces-Type-ApplicationSettingsResponse-SettingsGroup"></a>
The path prefix for the S3 bucket where users’ persistent application settings are stored.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^[A-Za-z0-9_./()!*'-]+$`
Required: No

## See Also
<a name="API_ApplicationSettingsResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ApplicationSettingsResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ApplicationSettingsResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ApplicationSettingsResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
