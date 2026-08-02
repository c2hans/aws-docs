---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJobOverrideTags.html
---

# AssetBundleImportJobOverrideTags
<a name="API_AssetBundleImportJobOverrideTags"></a>

A structure that contains the override tag configuration that modify the tags that are assigned to specified resources before the resource is imported.

## Contents
<a name="API_AssetBundleImportJobOverrideTags_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Analyses **   <a name="QS-Type-AssetBundleImportJobOverrideTags-Analyses"></a>
A list of tag overrides for any `Analysis` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobAnalysisOverrideTags](API_AssetBundleImportJobAnalysisOverrideTags.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** Dashboards **   <a name="QS-Type-AssetBundleImportJobOverrideTags-Dashboards"></a>
A list of tag overrides for any `Dashboard` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobDashboardOverrideTags](API_AssetBundleImportJobDashboardOverrideTags.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** DataSets **   <a name="QS-Type-AssetBundleImportJobOverrideTags-DataSets"></a>
A list of tag overrides for any `DataSet` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobDataSetOverrideTags](API_AssetBundleImportJobDataSetOverrideTags.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** DataSources **   <a name="QS-Type-AssetBundleImportJobOverrideTags-DataSources"></a>
A list of tag overrides for any `DataSource` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobDataSourceOverrideTags](API_AssetBundleImportJobDataSourceOverrideTags.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** Folders **   <a name="QS-Type-AssetBundleImportJobOverrideTags-Folders"></a>
A list of tag overrides for any `Folder` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobFolderOverrideTags](API_AssetBundleImportJobFolderOverrideTags.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** Themes **   <a name="QS-Type-AssetBundleImportJobOverrideTags-Themes"></a>
A list of tag overrides for any `Theme` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobThemeOverrideTags](API_AssetBundleImportJobThemeOverrideTags.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** VPCConnections **   <a name="QS-Type-AssetBundleImportJobOverrideTags-VPCConnections"></a>
A list of tag overrides for any `VPCConnection` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobVPCConnectionOverrideTags](API_AssetBundleImportJobVPCConnectionOverrideTags.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## See Also
<a name="API_AssetBundleImportJobOverrideTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportJobOverrideTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportJobOverrideTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportJobOverrideTags)
