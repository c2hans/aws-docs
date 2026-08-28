---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12OutboundEdiHeaders.html
---

# X12OutboundEdiHeaders
<a name="API_X12OutboundEdiHeaders"></a>

A structure containing the details for an outbound EDI object.

## Contents
<a name="API_X12OutboundEdiHeaders_Contents"></a>

 ** controlNumbers **   <a name="b2bi-Type-X12OutboundEdiHeaders-controlNumbers"></a>
Specifies control number configuration for outbound X12 EDI headers. These settings determine the starting values for interchange, functional group, and transaction set control numbers.
Type: [X12ControlNumbers](API_X12ControlNumbers.md) object
Required: No

 ** delimiters **   <a name="b2bi-Type-X12OutboundEdiHeaders-delimiters"></a>
The delimiters, for example semicolon (`;`), that separates sections of the headers for the X12 object.
Type: [X12Delimiters](API_X12Delimiters.md) object
Required: No

 ** functionalGroupHeaders **   <a name="b2bi-Type-X12OutboundEdiHeaders-functionalGroupHeaders"></a>
The functional group headers for the X12 object.
Type: [X12FunctionalGroupHeaders](API_X12FunctionalGroupHeaders.md) object
Required: No

 ** gs05TimeFormat **   <a name="b2bi-Type-X12OutboundEdiHeaders-gs05TimeFormat"></a>
Specifies the time format in the GS05 element (time) of the functional group header. The following formats use 24-hour clock time:
+  `HHMM` - Hours and minutes
+  `HHMMSS` - Hours, minutes, and seconds
+  `HHMMSSDD` - Hours, minutes, seconds, and decimal seconds
Where:
+  `HH` - Hours (00-23)
+  `MM` - Minutes (00-59)
+  `SS` - Seconds (00-59)
+  `DD` - Hundredths of seconds (00-99)
Type: String
Valid Values: `HHMM | HHMMSS | HHMMSSDD`
Required: No

 ** interchangeControlHeaders **   <a name="b2bi-Type-X12OutboundEdiHeaders-interchangeControlHeaders"></a>
In X12 EDI messages, delimiters are used to mark the end of segments or elements, and are defined in the interchange control header.
Type: [X12InterchangeControlHeaders](API_X12InterchangeControlHeaders.md) object
Required: No

 ** validateEdi **   <a name="b2bi-Type-X12OutboundEdiHeaders-validateEdi"></a>
Specifies whether or not to validate the EDI for this X12 object: `TRUE` or `FALSE`. When enabled, this performs both standard EDI validation and applies any configured custom validation rules including element length constraints, code list validations, and element requirement checks. Validation results are returned in the response validation messages.
Type: Boolean
Required: No

## See Also
<a name="API_X12OutboundEdiHeaders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/X12OutboundEdiHeaders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/X12OutboundEdiHeaders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/X12OutboundEdiHeaders)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
