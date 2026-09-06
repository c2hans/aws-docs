---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PullRequestCreatedEventMetadata.html
---

# PullRequestCreatedEventMetadata
<a name="API_PullRequestCreatedEventMetadata"></a>

Metadata about the pull request that is used when comparing the pull request source with its destination.

## Contents
<a name="API_PullRequestCreatedEventMetadata_Contents"></a>

 ** destinationCommitId **   <a name="CodeCommit-Type-PullRequestCreatedEventMetadata-destinationCommitId"></a>
The commit ID of the tip of the branch specified as the destination branch when the pull request was created.
Type: String
Required: No

 ** mergeBase **   <a name="CodeCommit-Type-PullRequestCreatedEventMetadata-mergeBase"></a>
The commit ID of the most recent commit that the source branch and the destination branch have in common.
Type: String
Required: No

 ** repositoryName **   <a name="CodeCommit-Type-PullRequestCreatedEventMetadata-repositoryName"></a>
The name of the repository where the pull request was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: No

 ** sourceCommitId **   <a name="CodeCommit-Type-PullRequestCreatedEventMetadata-sourceCommitId"></a>
The commit ID on the source branch used when the pull request was created.
Type: String
Required: No

## See Also
<a name="API_PullRequestCreatedEventMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/PullRequestCreatedEventMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/PullRequestCreatedEventMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/PullRequestCreatedEventMetadata)
