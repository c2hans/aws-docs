---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_ConflictMetadata.html
---

# ConflictMetadata
<a name="API_ConflictMetadata"></a>

Information about the metadata for a conflict in a merge operation.

## Contents
<a name="API_ConflictMetadata_Contents"></a>

 ** contentConflict **   <a name="CodeCommit-Type-ConflictMetadata-contentConflict"></a>
A boolean value indicating whether there are conflicts in the content of a file.
Type: Boolean
Required: No

 ** fileModeConflict **   <a name="CodeCommit-Type-ConflictMetadata-fileModeConflict"></a>
A boolean value indicating whether there are conflicts in the file mode of a file.
Type: Boolean
Required: No

 ** fileModes **   <a name="CodeCommit-Type-ConflictMetadata-fileModes"></a>
The file modes of the file in the source, destination, and base of the merge.
Type: [FileModes](API_FileModes.md) object
Required: No

 ** filePath **   <a name="CodeCommit-Type-ConflictMetadata-filePath"></a>
The path of the file that contains conflicts.
Type: String
Required: No

 ** fileSizes **   <a name="CodeCommit-Type-ConflictMetadata-fileSizes"></a>
The file sizes of the file in the source, destination, and base of the merge.
Type: [FileSizes](API_FileSizes.md) object
Required: No

 ** isBinaryFile **   <a name="CodeCommit-Type-ConflictMetadata-isBinaryFile"></a>
A boolean value (true or false) indicating whether the file is binary or textual in the source, destination, and base of the merge.
Type: [IsBinaryFile](API_IsBinaryFile.md) object
Required: No

 ** mergeOperations **   <a name="CodeCommit-Type-ConflictMetadata-mergeOperations"></a>
Whether an add, modify, or delete operation caused the conflict between the source and destination of the merge.
Type: [MergeOperations](API_MergeOperations.md) object
Required: No

 ** numberOfConflicts **   <a name="CodeCommit-Type-ConflictMetadata-numberOfConflicts"></a>
The number of conflicts, including both hunk conflicts and metadata conflicts.
Type: Integer
Required: No

 ** objectTypeConflict **   <a name="CodeCommit-Type-ConflictMetadata-objectTypeConflict"></a>
A boolean value (true or false) indicating whether there are conflicts between the branches in the object type of a file, folder, or submodule.
Type: Boolean
Required: No

 ** objectTypes **   <a name="CodeCommit-Type-ConflictMetadata-objectTypes"></a>
Information about any object type conflicts in a merge operation.
Type: [ObjectTypes](API_ObjectTypes.md) object
Required: No

## See Also
<a name="API_ConflictMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/ConflictMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/ConflictMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/ConflictMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
