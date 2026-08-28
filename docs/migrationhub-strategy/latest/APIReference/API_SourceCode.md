---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_SourceCode.html
---

# SourceCode
<a name="API_SourceCode"></a>

 Object containing source code information that is linked to an application component.

## Contents
<a name="API_SourceCode_Contents"></a>

 ** location **   <a name="migrationhubstrategy-Type-SourceCode-location"></a>
 The repository name for the source code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** projectName **   <a name="migrationhubstrategy-Type-SourceCode-projectName"></a>
The name of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** sourceVersion **   <a name="migrationhubstrategy-Type-SourceCode-sourceVersion"></a>
 The branch of the source code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `.*\S.*`
Required: No

 ** versionControl **   <a name="migrationhubstrategy-Type-SourceCode-versionControl"></a>
 The type of repository to use for the source code.
Type: String
Valid Values: `GITHUB | GITHUB_ENTERPRISE | AZURE_DEVOPS_GIT`
Required: No

## See Also
<a name="API_SourceCode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/SourceCode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/SourceCode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/SourceCode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
