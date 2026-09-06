---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FolderSearchFilter.html
---

# FolderSearchFilter
<a name="API_FolderSearchFilter"></a>

A filter to use to search an Quick Sight folder.

## Contents
<a name="API_FolderSearchFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="QS-Type-FolderSearchFilter-Name"></a>
The name of a value that you want to use in the filter. For example, `"Name": "QUICKSIGHT_OWNER"`.
Valid values are defined as follows:
+  `QUICKSIGHT_VIEWER_OR_OWNER`: Provide an ARN of a user or group, and any folders with that ARN listed as one of the folder's owners or viewers are returned. Implicit permissions from folders or groups are considered.
+  `QUICKSIGHT_OWNER`: Provide an ARN of a user or group, and any folders with that ARN listed as one of the owners of the folders are returned. Implicit permissions from folders or groups are considered.
+  `DIRECT_QUICKSIGHT_SOLE_OWNER`: Provide an ARN of a user or group, and any folders with that ARN listed as the only owner of the folder are returned. Implicit permissions from folders or groups are not considered.
+  `DIRECT_QUICKSIGHT_OWNER`: Provide an ARN of a user or group, and any folders with that ARN listed as one of the owners of the folders are returned. Implicit permissions from folders or groups are not considered.
+  `DIRECT_QUICKSIGHT_VIEWER_OR_OWNER`: Provide an ARN of a user or group, and any folders with that ARN listed as one of the owners or viewers of the folders are returned. Implicit permissions from folders or groups are not considered.
+  `FOLDER_NAME`: Any folders whose names have a substring match to this value will be returned.
+  `PARENT_FOLDER_ARN`: Provide an ARN of a folder, and any folders that are directly under that parent folder are returned. If you choose to use this option and leave the value blank, all root-level folders in the account are returned.
Type: String
Valid Values: `PARENT_FOLDER_ARN | DIRECT_QUICKSIGHT_OWNER | DIRECT_QUICKSIGHT_SOLE_OWNER | DIRECT_QUICKSIGHT_VIEWER_OR_OWNER | QUICKSIGHT_OWNER | QUICKSIGHT_VIEWER_OR_OWNER | FOLDER_NAME`
Required: No

 ** Operator **   <a name="QS-Type-FolderSearchFilter-Operator"></a>
The comparison operator that you want to use as a filter, for example `"Operator": "StringEquals"`. Valid values are `"StringEquals"` and `"StringLike"`.
If you set the operator value to `"StringEquals"`, you need to provide an ownership related filter in the `"NAME"` field and the arn of the user or group whose folders you want to search in the `"Value"` field. For example, `"Name":"DIRECT_QUICKSIGHT_OWNER", "Operator": "StringEquals", "Value": "arn:aws:quicksight:us-east-1:1:user/default/UserName1"`.
If you set the value to `"StringLike"`, you need to provide the name of the folders you are searching for. For example, `"Name":"FOLDER_NAME", "Operator": "StringLike", "Value": "Test"`. The `"StringLike"` operator only supports the `NAME` value `FOLDER_NAME`.
Type: String
Valid Values: `StringEquals | StringLike`
Required: No

 ** Value **   <a name="QS-Type-FolderSearchFilter-Value"></a>
The value of the named item (in this example, `PARENT_FOLDER_ARN`), that you want to use as a filter. For example, `"Value": "arn:aws:quicksight:us-east-1:1:folder/folderId"`.
Type: String
Required: No

## See Also
<a name="API_FolderSearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FolderSearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FolderSearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FolderSearchFilter)
