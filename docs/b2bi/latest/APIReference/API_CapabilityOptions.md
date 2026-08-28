---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CapabilityOptions.html
---

# CapabilityOptions
<a name="API_CapabilityOptions"></a>

Contains the details for an Outbound EDI capability.

## Contents
<a name="API_CapabilityOptions_Contents"></a>

 ** inboundEdi **   <a name="b2bi-Type-CapabilityOptions-inboundEdi"></a>
A structure that contains the inbound EDI options for the capability.
Type: [InboundEdiOptions](API_InboundEdiOptions.md) object
Required: No

 ** outboundEdi **   <a name="b2bi-Type-CapabilityOptions-outboundEdi"></a>
A structure that contains the outbound EDI options.
Type: [OutboundEdiOptions](API_OutboundEdiOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_CapabilityOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/CapabilityOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/CapabilityOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/CapabilityOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
