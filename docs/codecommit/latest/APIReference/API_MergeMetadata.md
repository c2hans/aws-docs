---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_MergeMetadata.html
---

# MergeMetadata
<a name="API_MergeMetadata"></a>

Returns information about a merge or potential merge between a source reference and a destination reference in a pull request.

## Contents
<a name="API_MergeMetadata_Contents"></a>

 ** isMerged **   <a name="CodeCommit-Type-MergeMetadata-isMerged"></a>
A Boolean value indicating whether the merge has been made.
Type: Boolean
Required: No

 ** mergeCommitId **   <a name="CodeCommit-Type-MergeMetadata-mergeCommitId"></a>
The commit ID for the merge commit, if any.
Type: String
Required: No

 ** mergedBy **   <a name="CodeCommit-Type-MergeMetadata-mergedBy"></a>
The Amazon Resource Name (ARN) of the user who merged the branches.
Type: String
Required: No

 ** mergeOption **   <a name="CodeCommit-Type-MergeMetadata-mergeOption"></a>
The merge strategy used in the merge.
Type: String
Valid Values: `FAST_FORWARD_MERGE | SQUASH_MERGE | THREE_WAY_MERGE`
Required: No

## See Also
<a name="API_MergeMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/MergeMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/MergeMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/MergeMetadata)
