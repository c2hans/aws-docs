---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_GitHubRepository.html
---

# GitHubRepository
<a name="API_GitHubRepository"></a>

Information about a GitHub repository for code analysis.

## Contents
<a name="API_GitHubRepository_Contents"></a>

 ** AccessToken **   <a name="reviewer-Type-GitHubRepository-AccessToken"></a>
The access token for authenticating with the GitHub repository.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 2048.
Pattern: `\S+`
Required: Yes

 ** Name **   <a name="reviewer-Type-GitHubRepository-Name"></a>
The name of the GitHub repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S[\w.-]*$`
Required: Yes

 ** Owner **   <a name="reviewer-Type-GitHubRepository-Owner"></a>
The owner of the GitHub repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`
Required: Yes

## See Also
<a name="API_GitHubRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/GitHubRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/GitHubRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/GitHubRepository)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
