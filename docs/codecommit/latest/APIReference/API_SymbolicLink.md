---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_SymbolicLink.html
---

# SymbolicLink
<a name="API_SymbolicLink"></a>

Returns information about a symbolic link in a repository folder.

## Contents
<a name="API_SymbolicLink_Contents"></a>

 ** absolutePath **   <a name="CodeCommit-Type-SymbolicLink-absolutePath"></a>
The fully qualified path to the folder that contains the symbolic link.
Type: String
Required: No

 ** blobId **   <a name="CodeCommit-Type-SymbolicLink-blobId"></a>
The blob ID that contains the information about the symbolic link.
Type: String
Required: No

 ** fileMode **   <a name="CodeCommit-Type-SymbolicLink-fileMode"></a>
The file mode permissions of the blob that cotains information about the symbolic link.
Type: String
Valid Values: `EXECUTABLE | NORMAL | SYMLINK`
Required: No

 ** relativePath **   <a name="CodeCommit-Type-SymbolicLink-relativePath"></a>
The relative path of the symbolic link from the folder where the query originated.
Type: String
Required: No

## See Also
<a name="API_SymbolicLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/SymbolicLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/SymbolicLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/SymbolicLink)
