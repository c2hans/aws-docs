---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_SourceCodeRepository.html
---

# SourceCodeRepository
<a name="API_SourceCodeRepository"></a>

 Object containing source code information that is linked to an application component.

## Contents
<a name="API_SourceCodeRepository_Contents"></a>

 ** branch **   <a name="migrationhubstrategy-Type-SourceCodeRepository-branch"></a>
 The branch of the source code.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** projectName **   <a name="migrationhubstrategy-Type-SourceCodeRepository-projectName"></a>
The name of the project.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** repository **   <a name="migrationhubstrategy-Type-SourceCodeRepository-repository"></a>
 The repository name for the source code.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** versionControlType **   <a name="migrationhubstrategy-Type-SourceCodeRepository-versionControlType"></a>
 The type of repository to use for the source code.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_SourceCodeRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/SourceCodeRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/SourceCodeRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/SourceCodeRepository)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
