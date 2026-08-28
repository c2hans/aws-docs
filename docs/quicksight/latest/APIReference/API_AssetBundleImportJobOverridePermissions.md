---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJobOverridePermissions.html
---

# AssetBundleImportJobOverridePermissions
<a name="API_AssetBundleImportJobOverridePermissions"></a>

A structure that contains the override permission configurations that modify the permissions for specified resources before the resource is imported.

## Contents
<a name="API_AssetBundleImportJobOverridePermissions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Analyses **   <a name="QS-Type-AssetBundleImportJobOverridePermissions-Analyses"></a>
A list of permissions overrides for any `Analysis` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobAnalysisOverridePermissions](API_AssetBundleImportJobAnalysisOverridePermissions.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** Dashboards **   <a name="QS-Type-AssetBundleImportJobOverridePermissions-Dashboards"></a>
A list of permissions overrides for any `Dashboard` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobDashboardOverridePermissions](API_AssetBundleImportJobDashboardOverridePermissions.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** DataSets **   <a name="QS-Type-AssetBundleImportJobOverridePermissions-DataSets"></a>
A list of permissions overrides for any `DataSet` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobDataSetOverridePermissions](API_AssetBundleImportJobDataSetOverridePermissions.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** DataSources **   <a name="QS-Type-AssetBundleImportJobOverridePermissions-DataSources"></a>
A list of permissions overrides for any `DataSource` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobDataSourceOverridePermissions](API_AssetBundleImportJobDataSourceOverridePermissions.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** Folders **   <a name="QS-Type-AssetBundleImportJobOverridePermissions-Folders"></a>
A list of permissions for the folders that you want to apply overrides to.
Type: Array of [AssetBundleImportJobFolderOverridePermissions](API_AssetBundleImportJobFolderOverridePermissions.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** Themes **   <a name="QS-Type-AssetBundleImportJobOverridePermissions-Themes"></a>
A list of permissions overrides for any `Theme` resources that are present in the asset bundle that is imported.
Type: Array of [AssetBundleImportJobThemeOverridePermissions](API_AssetBundleImportJobThemeOverridePermissions.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** TopicsV2 **   <a name="QS-Type-AssetBundleImportJobOverridePermissions-TopicsV2"></a>
A list of permissions for the topics that you want to apply overrides to.
Type: Array of [AssetBundleImportJobTopicV2OverridePermissions](API_AssetBundleImportJobTopicV2OverridePermissions.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

## See Also
<a name="API_AssetBundleImportJobOverridePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportJobOverridePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportJobOverridePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportJobOverridePermissions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
