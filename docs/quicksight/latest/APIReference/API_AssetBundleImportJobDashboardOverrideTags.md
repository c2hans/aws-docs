---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJobDashboardOverrideTags.html
---

# AssetBundleImportJobDashboardOverrideTags
<a name="API_AssetBundleImportJobDashboardOverrideTags"></a>

An object that contains a list of tags to be assigned to a list of dashboard IDs.

## Contents
<a name="API_AssetBundleImportJobDashboardOverrideTags_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DashboardIds **   <a name="QS-Type-AssetBundleImportJobDashboardOverrideTags-DashboardIds"></a>
A list of dashboard IDs that you want to apply overrides to. You can use `*` to override all dashboards in this asset bundle.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Pattern: `\*|[\w\-]{1,2048}`
Required: Yes

 ** Tags **   <a name="QS-Type-AssetBundleImportJobDashboardOverrideTags-Tags"></a>
A list of tags for the dashboards that you want to apply overrides to.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: Yes

## See Also
<a name="API_AssetBundleImportJobDashboardOverrideTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportJobDashboardOverrideTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportJobDashboardOverrideTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportJobDashboardOverrideTags)
