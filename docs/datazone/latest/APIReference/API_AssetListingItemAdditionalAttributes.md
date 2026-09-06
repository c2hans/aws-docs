---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AssetListingItemAdditionalAttributes.html
---

# AssetListingItemAdditionalAttributes
<a name="API_AssetListingItemAdditionalAttributes"></a>

Additional attributes of an inventory asset.

## Contents
<a name="API_AssetListingItemAdditionalAttributes_Contents"></a>

 ** forms **   <a name="datazone-Type-AssetListingItemAdditionalAttributes-forms"></a>
The metadata forms that form additional attributes of the metadata asset.
Type: String
Required: No

 ** latestTimeSeriesDataPointForms **   <a name="datazone-Type-AssetListingItemAdditionalAttributes-latestTimeSeriesDataPointForms"></a>
The latest time series data points forms included in the additional attributes of an asset.
Type: Array of [TimeSeriesDataPointSummaryFormOutput](API_TimeSeriesDataPointSummaryFormOutput.md) objects
Required: No

 ** matchRationale **   <a name="datazone-Type-AssetListingItemAdditionalAttributes-matchRationale"></a>
List of rationales indicating why this item was matched by search.
Type: Array of [MatchRationaleItem](API_MatchRationaleItem.md) objects
Required: No

## See Also
<a name="API_AssetListingItemAdditionalAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AssetListingItemAdditionalAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AssetListingItemAdditionalAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AssetListingItemAdditionalAttributes)
