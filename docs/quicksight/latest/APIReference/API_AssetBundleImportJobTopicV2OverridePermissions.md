---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJobTopicV2OverridePermissions.html
---

# AssetBundleImportJobTopicV2OverridePermissions
<a name="API_AssetBundleImportJobTopicV2OverridePermissions"></a>

An object that contains a list of permissions to be applied to a list of topic IDs.

## Contents
<a name="API_AssetBundleImportJobTopicV2OverridePermissions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Permissions **   <a name="QS-Type-AssetBundleImportJobTopicV2OverridePermissions-Permissions"></a>
A list of permissions for the topics that you want to apply overrides to.
Type: [AssetBundleResourcePermissions](API_AssetBundleResourcePermissions.md) object
Required: Yes

 ** TopicIds **   <a name="QS-Type-AssetBundleImportJobTopicV2OverridePermissions-TopicIds"></a>
A list of topic IDs that you want to apply overrides to. You can use `*` to override all topics in this asset bundle.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Pattern: `\*|[\w\-]{1,2048}`
Required: Yes

## See Also
<a name="API_AssetBundleImportJobTopicV2OverridePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportJobTopicV2OverridePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportJobTopicV2OverridePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportJobTopicV2OverridePermissions)
