---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValueSuccessEntry.html
---

# BatchGetAssetPropertyValueSuccessEntry
<a name="API_BatchGetAssetPropertyValueSuccessEntry"></a>

Contains success information for an entry that is associated with the [BatchGetAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValue.html) API.

## Contents
<a name="API_BatchGetAssetPropertyValueSuccessEntry_Contents"></a>

 ** entryId **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueSuccessEntry-entryId"></a>
The ID of the entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** assetPropertyValue **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueSuccessEntry-assetPropertyValue"></a>
Contains asset property value information.
Type: [AssetPropertyValue](API_AssetPropertyValue.md) object
Required: No

## See Also
<a name="API_BatchGetAssetPropertyValueSuccessEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchGetAssetPropertyValueSuccessEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchGetAssetPropertyValueSuccessEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchGetAssetPropertyValueSuccessEntry)
