---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12Envelope.html
---

# X12Envelope
<a name="API_X12Envelope"></a>

A wrapper structure for an X12 definition object.

the X12 envelope ensures the integrity of the data and the efficiency of the information exchange. The X12 message structure has hierarchical levels. From highest to the lowest, they are:
+ Interchange Envelope
+ Functional Group
+ Transaction Set

## Contents
<a name="API_X12Envelope_Contents"></a>

 ** common **   <a name="b2bi-Type-X12Envelope-common"></a>
A container for the X12 outbound EDI headers.
Type: [X12OutboundEdiHeaders](API_X12OutboundEdiHeaders.md) object
Required: No

 ** wrapOptions **   <a name="b2bi-Type-X12Envelope-wrapOptions"></a>
Contains options for wrapping (line folding) in X12 EDI files. Wrapping controls how long lines are handled in the EDI output.
Type: [WrapOptions](API_WrapOptions.md) object
Required: No

## See Also
<a name="API_X12Envelope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/X12Envelope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/X12Envelope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/X12Envelope)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
