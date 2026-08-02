---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PropertyMapping.html
---

# PropertyMapping
<a name="API_PropertyMapping"></a>

Maps a property from an interface asset model to a property in the asset model where the interface is applied.

## Contents
<a name="API_PropertyMapping_Contents"></a>

 ** assetModelPropertyId **   <a name="iotsitewise-Type-PropertyMapping-assetModelPropertyId"></a>
The ID of the property in the asset model where the interface is applied.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

 ** interfaceAssetModelPropertyId **   <a name="iotsitewise-Type-PropertyMapping-interfaceAssetModelPropertyId"></a>
The ID of the property in the interface asset model.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 139.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$|^externalId:[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
Required: Yes

## See Also
<a name="API_PropertyMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/PropertyMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/PropertyMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/PropertyMapping)
