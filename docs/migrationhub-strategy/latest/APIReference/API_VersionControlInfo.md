---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_VersionControlInfo.html
---

# VersionControlInfo
<a name="API_VersionControlInfo"></a>

Details about the version control configuration.

## Contents
<a name="API_VersionControlInfo_Contents"></a>

 ** versionControlConfigurationTimeStamp **   <a name="migrationhubstrategy-Type-VersionControlInfo-versionControlConfigurationTimeStamp"></a>
The time when the version control system was last configured.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** versionControlType **   <a name="migrationhubstrategy-Type-VersionControlInfo-versionControlType"></a>
The type of version control.
Type: String
Valid Values: `GITHUB | GITHUB_ENTERPRISE | AZURE_DEVOPS_GIT`
Required: No

## See Also
<a name="API_VersionControlInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/VersionControlInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/VersionControlInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/VersionControlInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
