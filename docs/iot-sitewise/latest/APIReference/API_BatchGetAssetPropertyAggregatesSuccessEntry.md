---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregatesSuccessEntry.html
---

# BatchGetAssetPropertyAggregatesSuccessEntry
<a name="API_BatchGetAssetPropertyAggregatesSuccessEntry"></a>

Contains success information for an entry that is associated with the [BatchGetAssetPropertyAggregates](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregates.html) API.

## Contents
<a name="API_BatchGetAssetPropertyAggregatesSuccessEntry_Contents"></a>

 ** aggregatedValues **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesSuccessEntry-aggregatedValues"></a>
The requested aggregated asset property values (for example, average, minimum, and maximum).
Type: Array of [AggregatedValue](API_AggregatedValue.md) objects
Required: Yes

 ** entryId **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesSuccessEntry-entryId"></a>
The ID of the entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## See Also
<a name="API_BatchGetAssetPropertyAggregatesSuccessEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchGetAssetPropertyAggregatesSuccessEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchGetAssetPropertyAggregatesSuccessEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchGetAssetPropertyAggregatesSuccessEntry)
