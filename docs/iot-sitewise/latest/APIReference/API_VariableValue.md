---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_VariableValue.html
---

# VariableValue
<a name="API_VariableValue"></a>

Identifies a property value used in an expression.

## Contents
<a name="API_VariableValue_Contents"></a>

 ** hierarchyId **   <a name="iotsitewise-Type-VariableValue-hierarchyId"></a>
The ID of the hierarchy to query for the property ID. You can use the hierarchy's name instead of the hierarchy's ID. If the hierarchy has an external ID, you can specify `externalId:` followed by the external ID. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
You use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same `propertyId`. For example, you might have separately grouped assets that come from the same asset model. For more information, see [Asset hierarchies](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** propertyId **   <a name="iotsitewise-Type-VariableValue-propertyId"></a>
The ID of the property to use as the variable. You can use the property `name` if it's from the same asset model. If the property has an external ID, you can specify `externalId:` followed by the external ID. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** propertyPath **   <a name="iotsitewise-Type-VariableValue-propertyPath"></a>
The path of the property.
Type: Array of [AssetModelPropertyPathSegment](API_AssetModelPropertyPathSegment.md) objects
Required: No

## See Also
<a name="API_VariableValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/VariableValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/VariableValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/VariableValue)
