---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetModelPropertyBindingValue.html
---

# AssetModelPropertyBindingValue
<a name="API_AssetModelPropertyBindingValue"></a>

Contains information about an `assetModelProperty` binding value.

## Contents
<a name="API_AssetModelPropertyBindingValue_Contents"></a>

 ** assetModelId **   <a name="iotsitewise-Type-AssetModelPropertyBindingValue-assetModelId"></a>
The ID of the asset model, in UUID format.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** propertyId **   <a name="iotsitewise-Type-AssetModelPropertyBindingValue-propertyId"></a>
The ID of the asset model property used in data binding value.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## See Also
<a name="API_AssetModelPropertyBindingValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetModelPropertyBindingValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetModelPropertyBindingValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetModelPropertyBindingValue)
