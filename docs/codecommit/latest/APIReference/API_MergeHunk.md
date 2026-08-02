---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_MergeHunk.html
---

# MergeHunk
<a name="API_MergeHunk"></a>

Information about merge hunks in a merge or pull request operation.

## Contents
<a name="API_MergeHunk_Contents"></a>

 ** base **   <a name="CodeCommit-Type-MergeHunk-base"></a>
Information about the merge hunk in the base of a merge or pull request.
Type: [MergeHunkDetail](API_MergeHunkDetail.md) object
Required: No

 ** destination **   <a name="CodeCommit-Type-MergeHunk-destination"></a>
Information about the merge hunk in the destination of a merge or pull request.
Type: [MergeHunkDetail](API_MergeHunkDetail.md) object
Required: No

 ** isConflict **   <a name="CodeCommit-Type-MergeHunk-isConflict"></a>
A Boolean value indicating whether a combination of hunks contains a conflict. Conflicts occur when the same file or the same lines in a file were modified in both the source and destination of a merge or pull request. Valid values include true, false, and null. True when the hunk represents a conflict and one or more files contains a line conflict. File mode conflicts in a merge do not set this to true.
Type: Boolean
Required: No

 ** source **   <a name="CodeCommit-Type-MergeHunk-source"></a>
Information about the merge hunk in the source of a merge or pull request.
Type: [MergeHunkDetail](API_MergeHunkDetail.md) object
Required: No

## See Also
<a name="API_MergeHunk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/MergeHunk)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/MergeHunk)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/MergeHunk)
