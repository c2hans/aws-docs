---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_OutputConversion.html
---

# OutputConversion
<a name="API_OutputConversion"></a>

Contains the formatting options for an outbound transformer (takes JSON or XML as input and converts it to an EDI document (currently only X12 format is supported).

## Contents
<a name="API_OutputConversion_Contents"></a>

 ** toFormat **   <a name="b2bi-Type-OutputConversion-toFormat"></a>
The format for the output from an outbound transformer: only X12 is currently supported.
Type: String
Valid Values: `X12`
Required: Yes

 ** advancedOptions **   <a name="b2bi-Type-OutputConversion-advancedOptions"></a>
A structure that contains advanced options for EDI processing. Currently, only X12 advanced options are supported.
Type: [AdvancedOptions](API_AdvancedOptions.md) object
Required: No

 ** formatOptions **   <a name="b2bi-Type-OutputConversion-formatOptions"></a>
A structure that contains the X12 transaction set and version for the transformer output.
Type: [FormatOptions](API_FormatOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_OutputConversion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/OutputConversion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/OutputConversion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/OutputConversion)
