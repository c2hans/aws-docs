---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ConflictResolution.html
---

# ConflictResolution
<a name="API_ConflictResolution"></a>

If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.

## Contents
<a name="API_ConflictResolution_Contents"></a>

 ** deleteFiles **   <a name="CodeCommit-Type-ConflictResolution-deleteFiles"></a>
Files to be deleted as part of the merge conflict resolution.
Type: Array of [DeleteFileEntry](API_DeleteFileEntry.md) objects
Required: No

 ** replaceContents **   <a name="CodeCommit-Type-ConflictResolution-replaceContents"></a>
Files to have content replaced as part of the merge conflict resolution.
Type: Array of [ReplaceContentEntry](API_ReplaceContentEntry.md) objects
Required: No

 ** setFileModes **   <a name="CodeCommit-Type-ConflictResolution-setFileModes"></a>
File modes that are set as part of the merge conflict resolution.
Type: Array of [SetFileModeEntry](API_SetFileModeEntry.md) objects
Required: No

## See Also
<a name="API_ConflictResolution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ConflictResolution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ConflictResolution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ConflictResolution)
