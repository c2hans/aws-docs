---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_MergeHunkDetail.html
---

# MergeHunkDetail
<a name="API_MergeHunkDetail"></a>

Information about the details of a merge hunk that contains a conflict in a merge or pull request operation.

## Contents
<a name="API_MergeHunkDetail_Contents"></a>

 ** endLine **   <a name="CodeCommit-Type-MergeHunkDetail-endLine"></a>
The end position of the hunk in the merge result.
Type: Integer
Required: No

 ** hunkContent **   <a name="CodeCommit-Type-MergeHunkDetail-hunkContent"></a>
The base-64 encoded content of the hunk merged region that might contain a conflict.
Type: String
Required: No

 ** startLine **   <a name="CodeCommit-Type-MergeHunkDetail-startLine"></a>
The start position of the hunk in the merge result.
Type: Integer
Required: No

## See Also
<a name="API_MergeHunkDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/MergeHunkDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/MergeHunkDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/MergeHunkDetail)
