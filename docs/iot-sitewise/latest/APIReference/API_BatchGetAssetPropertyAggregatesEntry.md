---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregatesEntry.html
---

# BatchGetAssetPropertyAggregatesEntry
<a name="API_BatchGetAssetPropertyAggregatesEntry"></a>

Contains information for an asset property aggregate entry that is associated with the [BatchGetAssetPropertyAggregates](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyAggregates.html) API.

To identify an asset property, you must specify one of the following:
+ The `assetId` and `propertyId` of an asset property.
+ A `propertyAlias`, which is a data stream alias (for example, `/company/windfarm/3/turbine/7/temperature`). To define an asset property's alias, see [UpdateAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html).

## Contents
<a name="API_BatchGetAssetPropertyAggregatesEntry_Contents"></a>

 ** aggregateTypes **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesEntry-aggregateTypes"></a>
The data aggregating function.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `AVERAGE | COUNT | MAXIMUM | MINIMUM | SUM | STANDARD_DEVIATION`
Required: Yes

 ** endDate **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesEntry-endDate"></a>
The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.
Type: Timestamp
Required: Yes

 ** entryId **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesEntry-entryId"></a>
The ID of the entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** resolution **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesEntry-resolution"></a>
The time interval over which to aggregate data.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `1m|15m|1h|1d`
Required: Yes

 ** startDate **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesEntry-startDate"></a>
The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.
Type: Timestamp
Required: Yes

 ** assetId **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesEntry-assetId"></a>
The ID of the asset in which the asset property was created.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** propertyAlias **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesEntry-propertyAlias"></a>
The alias that identifies the property, such as an OPC-UA server data stream path (for example, `/company/windfarm/3/turbine/7/temperature`). For more information, see [Mapping industrial data streams to asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** propertyId **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesEntry-propertyId"></a>
The ID of the asset property, in UUID format.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** qualities **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesEntry-qualities"></a>
The quality by which to filter asset data.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `GOOD | BAD | UNCERTAIN`
Required: No

 ** timeOrdering **   <a name="iotsitewise-Type-BatchGetAssetPropertyAggregatesEntry-timeOrdering"></a>
The chronological sorting order of the requested information.
Default: `ASCENDING`
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## See Also
<a name="API_BatchGetAssetPropertyAggregatesEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchGetAssetPropertyAggregatesEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchGetAssetPropertyAggregatesEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchGetAssetPropertyAggregatesEntry)
