---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetModelPropertyBindingValueFilter.html
---

# AssetModelPropertyBindingValueFilter
<a name="API_AssetModelPropertyBindingValueFilter"></a>

A filter used to match data bindings based on a specific asset model property. This filter identifies all computation models that reference a particular property of an asset model in their data bindings.

## Contents
<a name="API_AssetModelPropertyBindingValueFilter_Contents"></a>

 ** assetModelId **   <a name="iotsitewise-Type-AssetModelPropertyBindingValueFilter-assetModelId"></a>
The ID of the asset model containing the filter property. This identifies the specific asset model that contains the property of interest.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** propertyId **   <a name="iotsitewise-Type-AssetModelPropertyBindingValueFilter-propertyId"></a>
The ID of the property within the asset model to filter by. Only data bindings referencing this specific property of the specified asset model are matched.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## See Also
<a name="API_AssetModelPropertyBindingValueFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetModelPropertyBindingValueFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetModelPropertyBindingValueFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetModelPropertyBindingValueFilter)
