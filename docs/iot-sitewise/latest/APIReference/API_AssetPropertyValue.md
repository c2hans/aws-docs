---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetPropertyValue.html
---

# AssetPropertyValue
<a name="API_AssetPropertyValue"></a>

Contains asset property value information.

## Contents
<a name="API_AssetPropertyValue_Contents"></a>

 ** timestamp **   <a name="iotsitewise-Type-AssetPropertyValue-timestamp"></a>
The timestamp of the asset property value.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

 ** value **   <a name="iotsitewise-Type-AssetPropertyValue-value"></a>
The value of the asset property (see `Variant`).
Type: [Variant](API_Variant.md) object
Required: Yes

 ** quality **   <a name="iotsitewise-Type-AssetPropertyValue-quality"></a>
The quality of the asset property value.
Type: String
Valid Values: `GOOD | BAD | UNCERTAIN`
Required: No

## See Also
<a name="API_AssetPropertyValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/AssetPropertyValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/AssetPropertyValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/AssetPropertyValue)
