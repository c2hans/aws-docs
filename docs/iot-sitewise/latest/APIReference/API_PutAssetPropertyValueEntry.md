---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutAssetPropertyValueEntry.html
---

# PutAssetPropertyValueEntry
<a name="API_PutAssetPropertyValueEntry"></a>

Contains a list of value updates for an asset property in the list of asset entries consumed by the [BatchPutAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyValue.html) API operation.

## Contents
<a name="API_PutAssetPropertyValueEntry_Contents"></a>

 ** entryId **   <a name="iotsitewise-Type-PutAssetPropertyValueEntry-entryId"></a>
The user specified ID for the entry. You can use this ID to identify which entries failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** propertyValues **   <a name="iotsitewise-Type-PutAssetPropertyValueEntry-propertyValues"></a>
The list of property values to upload. You can specify up to 10 `propertyValues` array elements.
Type: Array of [AssetPropertyValue](API_AssetPropertyValue.md) objects
Required: Yes

 ** assetId **   <a name="iotsitewise-Type-PutAssetPropertyValueEntry-assetId"></a>
The ID of the asset to update.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** propertyAlias **   <a name="iotsitewise-Type-PutAssetPropertyValueEntry-propertyAlias"></a>
The alias that identifies the property, such as an OPC-UA server data stream path (for example, `/company/windfarm/3/turbine/7/temperature`). For more information, see [Mapping industrial data streams to asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** propertyId **   <a name="iotsitewise-Type-PutAssetPropertyValueEntry-propertyId"></a>
The ID of the asset property for this entry.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

## See Also
<a name="API_PutAssetPropertyValueEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/PutAssetPropertyValueEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/PutAssetPropertyValueEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/PutAssetPropertyValueEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
