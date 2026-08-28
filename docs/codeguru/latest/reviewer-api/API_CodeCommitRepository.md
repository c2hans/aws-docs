---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeCommitRepository.html
---

# CodeCommitRepository
<a name="API_CodeCommitRepository"></a>

Information about an AWS CodeCommit repository. The CodeCommit repository must be in the same AWS Region and AWS account where its CodeGuru Reviewer code reviews are configured.

## Contents
<a name="API_CodeCommitRepository_Contents"></a>

 ** Name **   <a name="reviewer-Type-CodeCommitRepository-Name"></a>
The name of the AWS CodeCommit repository. For more information, see [repositoryName](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetRepository.html#CodeCommit-GetRepository-request-repositoryName) in the * AWS CodeCommit API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S[\w.-]*$`
Required: Yes

## See Also
<a name="API_CodeCommitRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/CodeCommitRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/CodeCommitRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/CodeCommitRepository)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
