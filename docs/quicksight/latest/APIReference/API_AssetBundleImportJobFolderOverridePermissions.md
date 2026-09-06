---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJobFolderOverridePermissions.html
---

# AssetBundleImportJobFolderOverridePermissions
<a name="API_AssetBundleImportJobFolderOverridePermissions"></a>

An object that contains a list of permissions to be applied to a list of folder IDs.

## Contents
<a name="API_AssetBundleImportJobFolderOverridePermissions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FolderIds **   <a name="QS-Type-AssetBundleImportJobFolderOverridePermissions-FolderIds"></a>
A list of folder IDs that you want to apply overrides to. You can use `*` to override all folders in this asset bundle.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Pattern: `\*|[\w\-]{1,2048}`
Required: Yes

 ** Permissions **   <a name="QS-Type-AssetBundleImportJobFolderOverridePermissions-Permissions"></a>
A structure that contains the permissions for the resource that you want to override in an asset bundle import job.
Type: [AssetBundleResourcePermissions](API_AssetBundleResourcePermissions.md) object
Required: No

## See Also
<a name="API_AssetBundleImportJobFolderOverridePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportJobFolderOverridePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportJobFolderOverridePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportJobFolderOverridePermissions)
