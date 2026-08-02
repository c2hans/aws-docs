---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJobAnalysisOverrideTags.html
---

# AssetBundleImportJobAnalysisOverrideTags
<a name="API_AssetBundleImportJobAnalysisOverrideTags"></a>

An object that contains a list of tags to be assigned to a list of analysis IDs.

## Contents
<a name="API_AssetBundleImportJobAnalysisOverrideTags_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AnalysisIds **   <a name="QS-Type-AssetBundleImportJobAnalysisOverrideTags-AnalysisIds"></a>
A list of analysis IDs that you want to apply overrides to. You can use `*` to override all analyses in this asset bundle.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Pattern: `\*|[\w\-]{1,2048}`
Required: Yes

 ** Tags **   <a name="QS-Type-AssetBundleImportJobAnalysisOverrideTags-Tags"></a>
A list of tags for the analyses that you want to apply overrides to.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: Yes

## See Also
<a name="API_AssetBundleImportJobAnalysisOverrideTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportJobAnalysisOverrideTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportJobAnalysisOverrideTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportJobAnalysisOverrideTags)
