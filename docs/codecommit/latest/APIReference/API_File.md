---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_File.html
---

# File
<a name="API_File"></a>

Returns information about a file in a repository.

## Contents
<a name="API_File_Contents"></a>

 ** absolutePath **   <a name="CodeCommit-Type-File-absolutePath"></a>
The fully qualified path to the file in the repository.
Type: String
Required: No

 ** blobId **   <a name="CodeCommit-Type-File-blobId"></a>
The blob ID that contains the file information.
Type: String
Required: No

 ** fileMode **   <a name="CodeCommit-Type-File-fileMode"></a>
The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.
Type: String
Valid Values: `EXECUTABLE | NORMAL | SYMLINK`
Required: No

 ** relativePath **   <a name="CodeCommit-Type-File-relativePath"></a>
The relative path of the file from the folder where the query originated.
Type: String
Required: No

## See Also
<a name="API_File_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/File)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/File)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/File)
