---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJobDashboardOverridePermissions.html
---

# AssetBundleImportJobDashboardOverridePermissions
<a name="API_AssetBundleImportJobDashboardOverridePermissions"></a>

An object that contains a list of permissions to be applied to a list of dashboard IDs.

## Contents
<a name="API_AssetBundleImportJobDashboardOverridePermissions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DashboardIds **   <a name="QS-Type-AssetBundleImportJobDashboardOverridePermissions-DashboardIds"></a>
A list of dashboard IDs that you want to apply overrides to. You can use `*` to override all dashboards in this asset bundle.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Pattern: `\*|[\w\-]{1,2048}`
Required: Yes

 ** LinkSharingConfiguration **   <a name="QS-Type-AssetBundleImportJobDashboardOverridePermissions-LinkSharingConfiguration"></a>
A structure that contains the link sharing configurations that you want to apply overrides to.
Type: [AssetBundleResourceLinkSharingConfiguration](API_AssetBundleResourceLinkSharingConfiguration.md) object
Required: No

 ** Permissions **   <a name="QS-Type-AssetBundleImportJobDashboardOverridePermissions-Permissions"></a>
A list of permissions for the dashboards that you want to apply overrides to.
Type: [AssetBundleResourcePermissions](API_AssetBundleResourcePermissions.md) object
Required: No

## See Also
<a name="API_AssetBundleImportJobDashboardOverridePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportJobDashboardOverridePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportJobDashboardOverridePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportJobDashboardOverridePermissions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
