---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_Commit.html
---

# Commit
<a name="API_Commit"></a>

Returns information about a specific commit.

## Contents
<a name="API_Commit_Contents"></a>

 ** additionalData **   <a name="CodeCommit-Type-Commit-additionalData"></a>
Any other data associated with the specified commit.
Type: String
Required: No

 ** author **   <a name="CodeCommit-Type-Commit-author"></a>
Information about the author of the specified commit. Information includes the date in timestamp format with GMT offset, the name of the author, and the email address for the author, as configured in Git.
Type: [UserInfo](API_UserInfo.md) object
Required: No

 ** commitId **   <a name="CodeCommit-Type-Commit-commitId"></a>
The full SHA ID of the specified commit.
Type: String
Required: No

 ** committer **   <a name="CodeCommit-Type-Commit-committer"></a>
Information about the person who committed the specified commit, also known as the committer. Information includes the date in timestamp format with GMT offset, the name of the committer, and the email address for the committer, as configured in Git.
For more information about the difference between an author and a committer in Git, see [Viewing the Commit History](http://git-scm.com/book/ch2-3.html) in Pro Git by Scott Chacon and Ben Straub.
Type: [UserInfo](API_UserInfo.md) object
Required: No

 ** message **   <a name="CodeCommit-Type-Commit-message"></a>
The commit message associated with the specified commit.
Type: String
Required: No

 ** parents **   <a name="CodeCommit-Type-Commit-parents"></a>
A list of parent commits for the specified commit. Each parent commit ID is the full commit ID.
Type: Array of strings
Required: No

 ** treeId **   <a name="CodeCommit-Type-Commit-treeId"></a>
Tree information for the specified commit.
Type: String
Required: No

## See Also
<a name="API_Commit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/Commit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/Commit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/Commit)
