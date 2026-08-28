---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleCloudFormationOverridePropertyConfiguration.html
---

# AssetBundleCloudFormationOverridePropertyConfiguration
<a name="API_AssetBundleCloudFormationOverridePropertyConfiguration"></a>

An optional collection of CloudFormation property configurations that control how the export job is generated.

## Contents
<a name="API_AssetBundleCloudFormationOverridePropertyConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Analyses **   <a name="QS-Type-AssetBundleCloudFormationOverridePropertyConfiguration-Analyses"></a>
An optional list of structures that control how `Analysis` resources are parameterized in the returned CloudFormation template.
Type: Array of [AssetBundleExportJobAnalysisOverrideProperties](API_AssetBundleExportJobAnalysisOverrideProperties.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** Dashboards **   <a name="QS-Type-AssetBundleCloudFormationOverridePropertyConfiguration-Dashboards"></a>
An optional list of structures that control how `Dashboard` resources are parameterized in the returned CloudFormation template.
Type: Array of [AssetBundleExportJobDashboardOverrideProperties](API_AssetBundleExportJobDashboardOverrideProperties.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** DataSets **   <a name="QS-Type-AssetBundleCloudFormationOverridePropertyConfiguration-DataSets"></a>
An optional list of structures that control how `DataSet` resources are parameterized in the returned CloudFormation template.
Type: Array of [AssetBundleExportJobDataSetOverrideProperties](API_AssetBundleExportJobDataSetOverrideProperties.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** DataSources **   <a name="QS-Type-AssetBundleCloudFormationOverridePropertyConfiguration-DataSources"></a>
An optional list of structures that control how `DataSource` resources are parameterized in the returned CloudFormation template.
Type: Array of [AssetBundleExportJobDataSourceOverrideProperties](API_AssetBundleExportJobDataSourceOverrideProperties.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** Folders **   <a name="QS-Type-AssetBundleCloudFormationOverridePropertyConfiguration-Folders"></a>
An optional list of structures that controls how `Folder` resources are parameterized in the returned CloudFormation template.
Type: Array of [AssetBundleExportJobFolderOverrideProperties](API_AssetBundleExportJobFolderOverrideProperties.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** RefreshSchedules **   <a name="QS-Type-AssetBundleCloudFormationOverridePropertyConfiguration-RefreshSchedules"></a>
An optional list of structures that control how `RefreshSchedule` resources are parameterized in the returned CloudFormation template.
Type: Array of [AssetBundleExportJobRefreshScheduleOverrideProperties](API_AssetBundleExportJobRefreshScheduleOverrideProperties.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** ResourceIdOverrideConfiguration **   <a name="QS-Type-AssetBundleCloudFormationOverridePropertyConfiguration-ResourceIdOverrideConfiguration"></a>
An optional list of structures that control how resource IDs are parameterized in the returned CloudFormation template.
Type: [AssetBundleExportJobResourceIdOverrideConfiguration](API_AssetBundleExportJobResourceIdOverrideConfiguration.md) object
Required: No

 ** Themes **   <a name="QS-Type-AssetBundleCloudFormationOverridePropertyConfiguration-Themes"></a>
An optional list of structures that control how `Theme` resources are parameterized in the returned CloudFormation template.
Type: Array of [AssetBundleExportJobThemeOverrideProperties](API_AssetBundleExportJobThemeOverrideProperties.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** TopicsV2 **   <a name="QS-Type-AssetBundleCloudFormationOverridePropertyConfiguration-TopicsV2"></a>
An optional list of structures that controls how `Topic` resources are parameterized in the returned CloudFormation template.
Type: Array of [AssetBundleExportJobTopicV2OverrideProperties](API_AssetBundleExportJobTopicV2OverrideProperties.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** VPCConnections **   <a name="QS-Type-AssetBundleCloudFormationOverridePropertyConfiguration-VPCConnections"></a>
An optional list of structures that control how `VPCConnection` resources are parameterized in the returned CloudFormation template.
Type: Array of [AssetBundleExportJobVPCConnectionOverrideProperties](API_AssetBundleExportJobVPCConnectionOverrideProperties.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_AssetBundleCloudFormationOverridePropertyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleCloudFormationOverridePropertyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleCloudFormationOverridePropertyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleCloudFormationOverridePropertyConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
