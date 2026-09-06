---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Variant.html
---

# Variant
<a name="API_Variant"></a>

Contains an asset property value (of a single type only).

## Contents
<a name="API_Variant_Contents"></a>

 ** booleanValue **   <a name="iotsitewise-Type-Variant-booleanValue"></a>
Asset property data of type Boolean (true or false).
Type: Boolean
Required: No

 ** doubleValue **   <a name="iotsitewise-Type-Variant-doubleValue"></a>
 Asset property data of type double (floating point number). The min value is -10^10. The max value is 10^10. Double.NaN is allowed.
Type: Double
Required: No

 ** integerValue **   <a name="iotsitewise-Type-Variant-integerValue"></a>
Asset property data of type integer (whole number).
Type: Integer
Required: No

 ** nullValue **   <a name="iotsitewise-Type-Variant-nullValue"></a>
The type of null asset property data with BAD and UNCERTAIN qualities.
Type: [PropertyValueNullValue](API_PropertyValueNullValue.md) object
Required: No

 ** stringValue **   <a name="iotsitewise-Type-Variant-stringValue"></a>
 Asset property data of type string (sequence of characters). The allowed pattern: "^$\|[^\\u0000-\\u001F\\u007F]\+". The max length is 1024.
Type: String
Required: No

## See Also
<a name="API_Variant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/Variant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/Variant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/Variant)
