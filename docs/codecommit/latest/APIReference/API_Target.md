---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_Target.html
---

# Target
<a name="API_Target"></a>

Returns information about a target for a pull request.

## Contents
<a name="API_Target_Contents"></a>

 ** repositoryName **   <a name="CodeCommit-Type-Target-repositoryName"></a>
The name of the repository that contains the pull request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

 ** sourceReference **   <a name="CodeCommit-Type-Target-sourceReference"></a>
The branch of the repository that contains the changes for the pull request. Also known as the source branch.
Type: String
Required: Yes

 ** destinationReference **   <a name="CodeCommit-Type-Target-destinationReference"></a>
The branch of the repository where the pull request changes are merged. Also known as the destination branch.
Type: String
Required: No

## See Also
<a name="API_Target_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/Target)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/Target)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/Target)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
