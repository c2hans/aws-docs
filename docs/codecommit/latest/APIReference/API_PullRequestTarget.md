---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PullRequestTarget.html
---

# PullRequestTarget
<a name="API_PullRequestTarget"></a>

Returns information about a pull request target.

## Contents
<a name="API_PullRequestTarget_Contents"></a>

 ** destinationCommit **   <a name="CodeCommit-Type-PullRequestTarget-destinationCommit"></a>
The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.
Type: String
Required: No

 ** destinationReference **   <a name="CodeCommit-Type-PullRequestTarget-destinationReference"></a>
The branch of the repository where the pull request changes are merged. Also known as the destination branch.
Type: String
Required: No

 ** mergeBase **   <a name="CodeCommit-Type-PullRequestTarget-mergeBase"></a>
The commit ID of the most recent commit that the source branch and the destination branch have in common.
Type: String
Required: No

 ** mergeMetadata **   <a name="CodeCommit-Type-PullRequestTarget-mergeMetadata"></a>
Returns metadata about the state of the merge, including whether the merge has been made.
Type: [MergeMetadata](API_MergeMetadata.md) object
Required: No

 ** repositoryName **   <a name="CodeCommit-Type-PullRequestTarget-repositoryName"></a>
The name of the repository that contains the pull request source and destination branches.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: No

 ** sourceCommit **   <a name="CodeCommit-Type-PullRequestTarget-sourceCommit"></a>
The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID changes to reflect the new tip of the branch.
Type: String
Required: No

 ** sourceReference **   <a name="CodeCommit-Type-PullRequestTarget-sourceReference"></a>
The branch of the repository that contains the changes for the pull request. Also known as the source branch.
Type: String
Required: No

## See Also
<a name="API_PullRequestTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/PullRequestTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/PullRequestTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/PullRequestTarget)
