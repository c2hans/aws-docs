---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_Folder.html
---

# Folder
<a name="API_Folder"></a>

Returns information about a folder in a repository.

## Contents
<a name="API_Folder_Contents"></a>

 ** absolutePath **   <a name="CodeCommit-Type-Folder-absolutePath"></a>
The fully qualified path of the folder in the repository.
Type: String
Required: No

 ** relativePath **   <a name="CodeCommit-Type-Folder-relativePath"></a>
The relative path of the specified folder from the folder where the query originated.
Type: String
Required: No

 ** treeId **   <a name="CodeCommit-Type-Folder-treeId"></a>
The full SHA-1 pointer of the tree information for the commit that contains the folder.
Type: String
Required: No

## See Also
<a name="API_Folder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/Folder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/Folder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/Folder)
