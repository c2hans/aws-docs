---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetBindingValueFilter.html
---

# AssetBindingValueFilter
<a name="API_AssetBindingValueFilter"></a>

A filter used to match data bindings based on a specific asset. This filter identifies all computation models referencing a particular asset in their data bindings.

## Contents
<a name="API_AssetBindingValueFilter_Contents"></a>

 ** assetId **   <a name="iotsitewise-Type-AssetBindingValueFilter-assetId"></a>
The ID of the asset to filter data bindings by. Only data bindings referencing this specific asset are matched.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## See Also
<a name="API_AssetBindingValueFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetBindingValueFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetBindingValueFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetBindingValueFilter)
