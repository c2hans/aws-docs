---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Folder.html
---

# Folder
<a name="API_Folder"></a>

A folder in Quick Sight.

## Contents
<a name="API_Folder_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-Folder-Arn"></a>
The Amazon Resource Name (ARN) for the folder.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-Folder-CreatedTime"></a>
The time that the folder was created.
Type: Timestamp
Required: No

 ** FolderId **   <a name="QS-Type-Folder-FolderId"></a>
The ID of the folder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w\-]+`
Required: No

 ** FolderPath **   <a name="QS-Type-Folder-FolderPath"></a>
An array of ancestor ARN strings for the folder.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** FolderType **   <a name="QS-Type-Folder-FolderType"></a>
The type of folder it is.
Type: String
Valid Values: `SHARED | RESTRICTED`
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-Folder-LastUpdatedTime"></a>
The time that the folder was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="QS-Type-Folder-Name"></a>
A display name for the folder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** SharingModel **   <a name="QS-Type-Folder-SharingModel"></a>
The sharing scope of the folder.
Type: String
Valid Values: `ACCOUNT | NAMESPACE`
Required: No

## See Also
<a name="API_Folder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Folder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Folder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Folder)
