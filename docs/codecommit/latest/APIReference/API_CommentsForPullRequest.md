---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_CommentsForPullRequest.html
---

# CommentsForPullRequest
<a name="API_CommentsForPullRequest"></a>

Returns information about comments on a pull request.

## Contents
<a name="API_CommentsForPullRequest_Contents"></a>

 ** afterBlobId **   <a name="CodeCommit-Type-CommentsForPullRequest-afterBlobId"></a>
The full blob ID of the file on which you want to comment on the source commit.
Type: String
Required: No

 ** afterCommitId **   <a name="CodeCommit-Type-CommentsForPullRequest-afterCommitId"></a>
The full commit ID of the commit that was the tip of the source branch at the time the comment was made.
Type: String
Required: No

 ** beforeBlobId **   <a name="CodeCommit-Type-CommentsForPullRequest-beforeBlobId"></a>
The full blob ID of the file on which you want to comment on the destination commit.
Type: String
Required: No

 ** beforeCommitId **   <a name="CodeCommit-Type-CommentsForPullRequest-beforeCommitId"></a>
The full commit ID of the commit that was the tip of the destination branch when the pull request was created. This commit is superceded by the after commit in the source branch when and if you merge the source branch into the destination branch.
Type: String
Required: No

 ** comments **   <a name="CodeCommit-Type-CommentsForPullRequest-comments"></a>
An array of comment objects. Each comment object contains information about a comment on the pull request.
Type: Array of [Comment](API_Comment.md) objects
Required: No

 ** location **   <a name="CodeCommit-Type-CommentsForPullRequest-location"></a>
Location information about the comment on the pull request, including the file name, line number, and whether the version of the file where the comment was made is BEFORE (destination branch) or AFTER (source branch).
Type: [Location](API_Location.md) object
Required: No

 ** pullRequestId **   <a name="CodeCommit-Type-CommentsForPullRequest-pullRequestId"></a>
The system-generated ID of the pull request.
Type: String
Required: No

 ** repositoryName **   <a name="CodeCommit-Type-CommentsForPullRequest-repositoryName"></a>
The name of the repository that contains the pull request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: No

## See Also
<a name="API_CommentsForPullRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/CommentsForPullRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/CommentsForPullRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/CommentsForPullRequest)
