---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetModelPropertyDefinition.html
---

# AssetModelPropertyDefinition
<a name="API_AssetModelPropertyDefinition"></a>

Contains an asset model property definition. This property definition is applied to all assets created from the asset model.

## Contents
<a name="API_AssetModelPropertyDefinition_Contents"></a>

 ** dataType **   <a name="iotsitewise-Type-AssetModelPropertyDefinition-dataType"></a>
The data type of the property definition.
The `VIDEO`, `ANNOTATION`, and `JSON` data types aren't supported for asset model properties. These types are used only by time series that store data for datasets in a workspace.
If you specify `STRUCT`, you must also specify `dataTypeSpec` to identify the type of the structure for this property.
Type: String
Valid Values: `STRING | INTEGER | DOUBLE | BOOLEAN | STRUCT | VIDEO | ANNOTATION | JSON`
Required: Yes

 ** name **   <a name="iotsitewise-Type-AssetModelPropertyDefinition-name"></a>
The name of the property definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** type **   <a name="iotsitewise-Type-AssetModelPropertyDefinition-type"></a>
The property definition type (see `PropertyType`). You can only specify one type in a property definition.
Type: [PropertyType](API_PropertyType.md) object
Required: Yes

 ** dataTypeSpec **   <a name="iotsitewise-Type-AssetModelPropertyDefinition-dataTypeSpec"></a>
The data type of the structure for this property. This parameter is required on properties that have the `STRUCT` data type.
The options for this parameter depend on the type of the composite model in which you define this property. Use `AWS/ALARM_STATE` for alarm state in alarm composite models.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** externalId **   <a name="iotsitewise-Type-AssetModelPropertyDefinition-externalId"></a>
An external ID to assign to the property definition. The external ID must be unique among property definitions within this asset model. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Pattern: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: No

 ** id **   <a name="iotsitewise-Type-AssetModelPropertyDefinition-id"></a>
The ID to assign to the asset model property, if desired. AWS IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** unit **   <a name="iotsitewise-Type-AssetModelPropertyDefinition-unit"></a>
The unit of the property definition, such as `Newtons` or `RPM`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

## See Also
<a name="API_AssetModelPropertyDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetModelPropertyDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetModelPropertyDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetModelPropertyDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
