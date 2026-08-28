---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_FileMetadata.html
---

# FileMetadata
<a name="API_FileMetadata"></a>

A file to be added, updated, or deleted as part of a commit.

## Contents
<a name="API_FileMetadata_Contents"></a>

 ** absolutePath **   <a name="CodeCommit-Type-FileMetadata-absolutePath"></a>
The full path to the file to be added or updated, including the name of the file.
Type: String
Required: No

 ** blobId **   <a name="CodeCommit-Type-FileMetadata-blobId"></a>
The blob ID that contains the file information.
Type: String
Required: No

 ** fileMode **   <a name="CodeCommit-Type-FileMetadata-fileMode"></a>
The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.
Type: String
Valid Values: `EXECUTABLE | NORMAL | SYMLINK`
Required: No

## See Also
<a name="API_FileMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/FileMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/FileMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/FileMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
