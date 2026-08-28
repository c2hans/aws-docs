---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_InputConversion.html
---

# InputConversion
<a name="API_InputConversion"></a>

Contains the input formatting options for an inbound transformer (takes an X12-formatted EDI document as input and converts it to JSON or XML.

## Contents
<a name="API_InputConversion_Contents"></a>

 ** fromFormat **   <a name="b2bi-Type-InputConversion-fromFormat"></a>
The format for the transformer input: currently on `X12` is supported.
Type: String
Valid Values: `X12`
Required: Yes

 ** advancedOptions **   <a name="b2bi-Type-InputConversion-advancedOptions"></a>
Specifies advanced options for the input conversion process. These options provide additional control over how EDI files are processed during transformation.
Type: [AdvancedOptions](API_AdvancedOptions.md) object
Required: No

 ** formatOptions **   <a name="b2bi-Type-InputConversion-formatOptions"></a>
A structure that contains the formatting options for an inbound transformer.
Type: [FormatOptions](API_FormatOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_InputConversion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/InputConversion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/InputConversion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/InputConversion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
