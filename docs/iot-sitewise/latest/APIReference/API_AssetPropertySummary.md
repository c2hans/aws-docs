---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetPropertySummary.html
---

# AssetPropertySummary
<a name="API_AssetPropertySummary"></a>

Contains a summary of a property associated with an asset.

## Contents
<a name="API_AssetPropertySummary_Contents"></a>

 ** id **   <a name="iotsitewise-Type-AssetPropertySummary-id"></a>
The ID of the property.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** alias **   <a name="iotsitewise-Type-AssetPropertySummary-alias"></a>
The alias that identifies the property, such as an OPC-UA server data stream path (for example, `/company/windfarm/3/turbine/7/temperature`). For more information, see [Mapping industrial data streams to asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** assetCompositeModelId **   <a name="iotsitewise-Type-AssetPropertySummary-assetCompositeModelId"></a>
 The ID of the composite model that contains the asset property.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** externalId **   <a name="iotsitewise-Type-AssetPropertySummary-externalId"></a>
The external ID of the property. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** notification **   <a name="iotsitewise-Type-AssetPropertySummary-notification"></a>
Contains asset property value notification information. When the notification state is enabled, AWS IoT SiteWise publishes property value updates to a unique MQTT topic. For more information, see [Interacting with other services](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interact-with-other-services.html) in the * AWS IoT SiteWise User Guide*.
Type: [PropertyNotification](API_PropertyNotification.md) object
Required: No

 ** path **   <a name="iotsitewise-Type-AssetPropertySummary-path"></a>
The structured path to the property from the root of the asset.
Type: Array of [AssetPropertyPathSegment](API_AssetPropertyPathSegment.md) objects
Required: No

 ** unit **   <a name="iotsitewise-Type-AssetPropertySummary-unit"></a>
 The unit of measure (such as Newtons or RPM) of the asset property.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

## See Also
<a name="API_AssetPropertySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetPropertySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetPropertySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetPropertySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
