---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_RepositoryInput.html
---

# RepositoryInput
<a name="API_RepositoryInput"></a>

Information about a repository that will be cloned to a Dev Environment.

## Contents
<a name="API_RepositoryInput_Contents"></a>

 ** repositoryName **   <a name="codecatalyst-Type-RepositoryInput-repositoryName"></a>
The name of the source repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!.*[.]git$)[\w\-.]*`
Required: Yes

 ** branchName **   <a name="codecatalyst-Type-RepositoryInput-branchName"></a>
The name of the branch in a source repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_RepositoryInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/RepositoryInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/RepositoryInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/RepositoryInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
