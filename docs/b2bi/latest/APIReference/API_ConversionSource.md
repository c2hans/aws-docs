---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ConversionSource.html
---

# ConversionSource
<a name="API_ConversionSource"></a>

Describes the input for an outbound transformation.

## Contents
<a name="API_ConversionSource_Contents"></a>

 ** fileFormat **   <a name="b2bi-Type-ConversionSource-fileFormat"></a>
The format for the input file: either JSON or XML.
Type: String
Valid Values: `JSON | XML`
Required: Yes

 ** inputFile **   <a name="b2bi-Type-ConversionSource-inputFile"></a>
The input file to use for an outbound transformation.
Type: [InputFileSource](API_InputFileSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_ConversionSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/ConversionSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/ConversionSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/ConversionSource)
