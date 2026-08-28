---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJobAnalysisOverridePermissions.html
---

# AssetBundleImportJobAnalysisOverridePermissions
<a name="API_AssetBundleImportJobAnalysisOverridePermissions"></a>

An object that contains a list of permissions to be applied to a list of analysis IDs.

## Contents
<a name="API_AssetBundleImportJobAnalysisOverridePermissions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AnalysisIds **   <a name="QS-Type-AssetBundleImportJobAnalysisOverridePermissions-AnalysisIds"></a>
A list of analysis IDs that you want to apply overrides to. You can use `*` to override all analyses in this asset bundle.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Pattern: `\*|[\w\-]{1,2048}`
Required: Yes

 ** Permissions **   <a name="QS-Type-AssetBundleImportJobAnalysisOverridePermissions-Permissions"></a>
A list of permissions for the analyses that you want to apply overrides to.
Type: [AssetBundleResourcePermissions](API_AssetBundleResourcePermissions.md) object
Required: Yes

## See Also
<a name="API_AssetBundleImportJobAnalysisOverridePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportJobAnalysisOverridePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportJobAnalysisOverridePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportJobAnalysisOverridePermissions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
