---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_EncodingParameters.html
---

# EncodingParameters
<a name="API_EncodingParameters"></a>

 A collection of parameters that determine how MediaConnect will convert the content. These fields only apply to outputs on flows that have a CDI source.

## Contents
<a name="API_EncodingParameters_Contents"></a>

 ** compressionFactor **   <a name="mediaconnect-Type-EncodingParameters-compressionFactor"></a>
 A value that is used to calculate compression for an output. The bitrate of the output is calculated as follows: Output bitrate = (1 / compressionFactor) \* (source bitrate) This property only applies to outputs that use the ST 2110 JPEG XS protocol, with a flow source that uses the CDI protocol. Valid values are floating point numbers in the range of 3.0 to 10.0, inclusive.
Type: Double
Required: Yes

 ** encoderProfile **   <a name="mediaconnect-Type-EncodingParameters-encoderProfile"></a>
 A setting on the encoder that drives compression settings. This property only applies to video media streams associated with outputs that use the ST 2110 JPEG XS protocol, with a flow source that uses the CDI protocol.
Type: String
Valid Values: `main | high`
Required: Yes

## See Also
<a name="API_EncodingParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/EncodingParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/EncodingParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/EncodingParameters)
