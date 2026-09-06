---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12Delimiters.html
---

# X12Delimiters
<a name="API_X12Delimiters"></a>

In X12 EDI messages, delimiters are used to mark the end of segments or elements, and are defined in the interchange control header. The delimiters are part of the message's syntax and divide up its different elements.

## Contents
<a name="API_X12Delimiters_Contents"></a>

 ** componentSeparator **   <a name="b2bi-Type-X12Delimiters-componentSeparator"></a>
The component, or sub-element, separator. The default value is `:` (colon).
Type: String
Length Constraints: Fixed length of 1.
Pattern: `[!&'()*+,\-./:;?=%@\[\]_{}|<>~^`"]`
Required: No

 ** dataElementSeparator **   <a name="b2bi-Type-X12Delimiters-dataElementSeparator"></a>
The data element separator. The default value is `*` (asterisk).
Type: String
Length Constraints: Fixed length of 1.
Pattern: `[!&'()*+,\-./:;?=%@\[\]_{}|<>~^`"]`
Required: No

 ** segmentTerminator **   <a name="b2bi-Type-X12Delimiters-segmentTerminator"></a>
The segment terminator. The default value is `~` (tilde).
Type: String
Length Constraints: Fixed length of 1.
Pattern: `[!&'()*+,\-./:;?=%@\[\]_{}|<>~^`"]`
Required: No

## See Also
<a name="API_X12Delimiters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/X12Delimiters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/X12Delimiters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/X12Delimiters)
