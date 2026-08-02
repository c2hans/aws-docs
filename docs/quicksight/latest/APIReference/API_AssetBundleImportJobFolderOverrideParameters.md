---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJobFolderOverrideParameters.html
---

# AssetBundleImportJobFolderOverrideParameters
<a name="API_AssetBundleImportJobFolderOverrideParameters"></a>

The override parameters for a single folder that is being imported.

## Contents
<a name="API_AssetBundleImportJobFolderOverrideParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FolderId **   <a name="QS-Type-AssetBundleImportJobFolderOverrideParameters-FolderId"></a>
The ID of the folder that you want to apply overrides to.
Type: String
Required: Yes

 ** Name **   <a name="QS-Type-AssetBundleImportJobFolderOverrideParameters-Name"></a>
A new name for the folder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** ParentFolderArn **   <a name="QS-Type-AssetBundleImportJobFolderOverrideParameters-ParentFolderArn"></a>
A new parent folder arn. This change can only be applied if the import creates a brand new folder. Existing folders cannot be moved.
Type: String
Required: No

## See Also
<a name="API_AssetBundleImportJobFolderOverrideParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportJobFolderOverrideParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportJobFolderOverrideParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportJobFolderOverrideParameters)
