---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PullRequestSourceReferenceUpdatedEventMetadata.html
---

# PullRequestSourceReferenceUpdatedEventMetadata
<a name="API_PullRequestSourceReferenceUpdatedEventMetadata"></a>

Information about an update to the source branch of a pull request.

## Contents
<a name="API_PullRequestSourceReferenceUpdatedEventMetadata_Contents"></a>

 ** afterCommitId **   <a name="CodeCommit-Type-PullRequestSourceReferenceUpdatedEventMetadata-afterCommitId"></a>
The full commit ID of the commit in the source branch that was the tip of the branch at the time the pull request was updated.
Type: String
Required: No

 ** beforeCommitId **   <a name="CodeCommit-Type-PullRequestSourceReferenceUpdatedEventMetadata-beforeCommitId"></a>
The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was updated.
Type: String
Required: No

 ** mergeBase **   <a name="CodeCommit-Type-PullRequestSourceReferenceUpdatedEventMetadata-mergeBase"></a>
The commit ID of the most recent commit that the source branch and the destination branch have in common.
Type: String
Required: No

 ** repositoryName **   <a name="CodeCommit-Type-PullRequestSourceReferenceUpdatedEventMetadata-repositoryName"></a>
The name of the repository where the pull request was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: No

## See Also
<a name="API_PullRequestSourceReferenceUpdatedEventMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/PullRequestSourceReferenceUpdatedEventMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/PullRequestSourceReferenceUpdatedEventMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/PullRequestSourceReferenceUpdatedEventMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
