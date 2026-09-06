---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValueHistorySuccessEntry.html
---

# BatchGetAssetPropertyValueHistorySuccessEntry
<a name="API_BatchGetAssetPropertyValueHistorySuccessEntry"></a>

Contains success information for an entry that is associated with the [BatchGetAssetPropertyValueHistory](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValue.html) API.

## Contents
<a name="API_BatchGetAssetPropertyValueHistorySuccessEntry_Contents"></a>

 ** assetPropertyValueHistory **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueHistorySuccessEntry-assetPropertyValueHistory"></a>
The requested historical values for the specified asset property.
Type: Array of [AssetPropertyValue](API_AssetPropertyValue.md) objects
Required: Yes

 ** entryId **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueHistorySuccessEntry-entryId"></a>
The ID of the entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## See Also
<a name="API_BatchGetAssetPropertyValueHistorySuccessEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistorySuccessEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistorySuccessEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistorySuccessEntry)
