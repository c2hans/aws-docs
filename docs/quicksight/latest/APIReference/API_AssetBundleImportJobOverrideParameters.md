---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJobOverrideParameters.html
---

# AssetBundleImportJobOverrideParameters
<a name="API_AssetBundleImportJobOverrideParameters"></a>

A list of overrides that modify the asset bundle resource configuration before the resource is imported.

## Contents
<a name="API_AssetBundleImportJobOverrideParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Analyses **   <a name="QS-Type-AssetBundleImportJobOverrideParameters-Analyses"></a>
A list of overrides for any `Analysis` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobAnalysisOverrideParameters](API_AssetBundleImportJobAnalysisOverrideParameters.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** Dashboards **   <a name="QS-Type-AssetBundleImportJobOverrideParameters-Dashboards"></a>
A list of overrides for any `Dashboard` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobDashboardOverrideParameters](API_AssetBundleImportJobDashboardOverrideParameters.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** DataSets **   <a name="QS-Type-AssetBundleImportJobOverrideParameters-DataSets"></a>
A list of overrides for any `DataSet` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobDataSetOverrideParameters](API_AssetBundleImportJobDataSetOverrideParameters.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** DataSources **   <a name="QS-Type-AssetBundleImportJobOverrideParameters-DataSources"></a>
 A list of overrides for any `DataSource` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobDataSourceOverrideParameters](API_AssetBundleImportJobDataSourceOverrideParameters.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** Folders **   <a name="QS-Type-AssetBundleImportJobOverrideParameters-Folders"></a>
A list of overrides for any `Folder` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobFolderOverrideParameters](API_AssetBundleImportJobFolderOverrideParameters.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** RefreshSchedules **   <a name="QS-Type-AssetBundleImportJobOverrideParameters-RefreshSchedules"></a>
A list of overrides for any `RefreshSchedule` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobRefreshScheduleOverrideParameters](API_AssetBundleImportJobRefreshScheduleOverrideParameters.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** ResourceIdOverrideConfiguration **   <a name="QS-Type-AssetBundleImportJobOverrideParameters-ResourceIdOverrideConfiguration"></a>
An optional structure that configures resource ID overrides to be applied within the import job.
Type: [AssetBundleImportJobResourceIdOverrideConfiguration](API_AssetBundleImportJobResourceIdOverrideConfiguration.md) object
Required: No

 ** Themes **   <a name="QS-Type-AssetBundleImportJobOverrideParameters-Themes"></a>
A list of overrides for any `Theme` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobThemeOverrideParameters](API_AssetBundleImportJobThemeOverrideParameters.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** VPCConnections **   <a name="QS-Type-AssetBundleImportJobOverrideParameters-VPCConnections"></a>
A list of overrides for any `VPCConnection` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobVPCConnectionOverrideParameters](API_AssetBundleImportJobVPCConnectionOverrideParameters.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_AssetBundleImportJobOverrideParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportJobOverrideParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportJobOverrideParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportJobOverrideParameters)
