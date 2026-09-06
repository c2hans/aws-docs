---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetModelPropertySummary.html
---

# AssetModelPropertySummary
<a name="API_AssetModelPropertySummary"></a>

Contains a summary of a property associated with a model. This includes information about which interfaces the property belongs to, if any.

## Contents
<a name="API_AssetModelPropertySummary_Contents"></a>

 ** dataType **   <a name="iotsitewise-Type-AssetModelPropertySummary-dataType"></a>
The data type of the property.
Type: String
Valid Values: `STRING | INTEGER | DOUBLE | BOOLEAN | STRUCT | VIDEO | ANNOTATION | JSON`
Required: Yes

 ** name **   <a name="iotsitewise-Type-AssetModelPropertySummary-name"></a>
The name of the property.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** type **   <a name="iotsitewise-Type-AssetModelPropertySummary-type"></a>
Contains a property type, which can be one of `attribute`, `measurement`, `metric`, or `transform`.
Type: [PropertyType](API_PropertyType.md) object
Required: Yes

 ** assetModelCompositeModelId **   <a name="iotsitewise-Type-AssetModelPropertySummary-assetModelCompositeModelId"></a>
 The ID of the composite model that contains the asset model property.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** dataTypeSpec **   <a name="iotsitewise-Type-AssetModelPropertySummary-dataTypeSpec"></a>
The data type of the structure for this property. This parameter exists on properties that have the `STRUCT` data type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** externalId **   <a name="iotsitewise-Type-AssetModelPropertySummary-externalId"></a>
The external ID of the property. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** id **   <a name="iotsitewise-Type-AssetModelPropertySummary-id"></a>
The ID of the property.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** interfaceSummaries **   <a name="iotsitewise-Type-AssetModelPropertySummary-interfaceSummaries"></a>
A list of interface summaries that describe which interfaces this property belongs to, including the interface asset model ID and the corresponding property ID in the interface.
Type: Array of [InterfaceSummary](API_InterfaceSummary.md) objects
Required: No

 ** path **   <a name="iotsitewise-Type-AssetModelPropertySummary-path"></a>
The structured path to the property from the root of the asset model.
Type: Array of [AssetModelPropertyPathSegment](API_AssetModelPropertyPathSegment.md) objects
Required: No

 ** unit **   <a name="iotsitewise-Type-AssetModelPropertySummary-unit"></a>
The unit (such as `Newtons` or `RPM`) of the property.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

## See Also
<a name="API_AssetModelPropertySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetModelPropertySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetModelPropertySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetModelPropertySummary)
