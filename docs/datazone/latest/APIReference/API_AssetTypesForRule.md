---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AssetTypesForRule.html
---

# AssetTypesForRule
<a name="API_AssetTypesForRule"></a>

The asset type for the rule details.

## Contents
<a name="API_AssetTypesForRule_Contents"></a>

 ** selectionMode **   <a name="datazone-Type-AssetTypesForRule-selectionMode"></a>
The selection mode for the rule.
Type: String
Valid Values: `ALL | SPECIFIC`
Required: Yes

 ** specificAssetTypes **   <a name="datazone-Type-AssetTypesForRule-specificAssetTypes"></a>
The specific asset types that are included in the rule.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 513.
Pattern: `(?!\.)[\w\.]*\w`
Required: No

## See Also
<a name="API_AssetTypesForRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AssetTypesForRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AssetTypesForRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AssetTypesForRule)
