---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValueHistoryEntry.html
---

# BatchGetAssetPropertyValueHistoryEntry
<a name="API_BatchGetAssetPropertyValueHistoryEntry"></a>

Contains information for an asset property historical value entry that is associated with the [BatchGetAssetPropertyValueHistory](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchGetAssetPropertyValue.html) API.

To identify an asset property, you must specify one of the following:
+ The `assetId` and `propertyId` of an asset property.
+ A `propertyAlias`, which is a data stream alias (for example, `/company/windfarm/3/turbine/7/temperature`). To define an asset property's alias, see [UpdateAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html).

## Contents
<a name="API_BatchGetAssetPropertyValueHistoryEntry_Contents"></a>

 ** entryId **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueHistoryEntry-entryId"></a>
The ID of the entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** assetId **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueHistoryEntry-assetId"></a>
The ID of the asset in which the asset property was created.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** endDate **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueHistoryEntry-endDate"></a>
The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.
Type: Timestamp
Required: No

 ** propertyAlias **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueHistoryEntry-propertyAlias"></a>
The alias that identifies the property, such as an OPC-UA server data stream path (for example, `/company/windfarm/3/turbine/7/temperature`). For more information, see [Mapping industrial data streams to asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** propertyId **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueHistoryEntry-propertyId"></a>
The ID of the asset property, in UUID format.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** qualities **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueHistoryEntry-qualities"></a>
The quality by which to filter asset data.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `GOOD | BAD | UNCERTAIN`
Required: No

 ** startDate **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueHistoryEntry-startDate"></a>
The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.
Type: Timestamp
Required: No

 ** timeOrdering **   <a name="iotsitewise-Type-BatchGetAssetPropertyValueHistoryEntry-timeOrdering"></a>
The chronological sorting order of the requested information.
Default: `ASCENDING`
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## See Also
<a name="API_BatchGetAssetPropertyValueHistoryEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistoryEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistoryEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchGetAssetPropertyValueHistoryEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
