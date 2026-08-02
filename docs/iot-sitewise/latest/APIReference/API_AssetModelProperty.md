---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetModelProperty.html
---

# AssetModelProperty
<a name="API_AssetModelProperty"></a>

Contains information about an asset model property.

## Contents
<a name="API_AssetModelProperty_Contents"></a>

 ** dataType **   <a name="iotsitewise-Type-AssetModelProperty-dataType"></a>
The data type of the asset model property.
The `VIDEO`, `ANNOTATION`, and `JSON` data types aren't supported for asset model properties. These types are used only by time series that store data for datasets in a workspace.
If you specify `STRUCT`, you must also specify `dataTypeSpec` to identify the type of the structure for this property.
Type: String
Valid Values: `STRING | INTEGER | DOUBLE | BOOLEAN | STRUCT | VIDEO | ANNOTATION | JSON`
Required: Yes

 ** name **   <a name="iotsitewise-Type-AssetModelProperty-name"></a>
The name of the asset model property.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** type **   <a name="iotsitewise-Type-AssetModelProperty-type"></a>
The property type (see `PropertyType`).
Type: [PropertyType](API_PropertyType.md) object
Required: Yes

 ** dataTypeSpec **   <a name="iotsitewise-Type-AssetModelProperty-dataTypeSpec"></a>
The data type of the structure for this property. This parameter exists on properties that have the `STRUCT` data type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** externalId **   <a name="iotsitewise-Type-AssetModelProperty-externalId"></a>
The external ID (if any) provided in the [CreateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html) or [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) operation. You can assign an external ID by specifying this value as part of a call to [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html). However, you can't change the external ID if one is already assigned. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** id **   <a name="iotsitewise-Type-AssetModelProperty-id"></a>
The ID of the asset model property.
+ If you are callling [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) to create a *new* property: You can specify its ID here, if desired. AWS IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.
+ If you are calling UpdateAssetModel to modify an *existing* property: This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** path **   <a name="iotsitewise-Type-AssetModelProperty-path"></a>
The structured path to the property from the root of the asset model.
Type: Array of [AssetModelPropertyPathSegment](API_AssetModelPropertyPathSegment.md) objects
Required: No

 ** unit **   <a name="iotsitewise-Type-AssetModelProperty-unit"></a>
The unit of the asset model property, such as `Newtons` or `RPM`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

## See Also
<a name="API_AssetModelProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetModelProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetModelProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetModelProperty)
