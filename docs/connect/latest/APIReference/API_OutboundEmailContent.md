---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_OutboundEmailContent.html
---

# OutboundEmailContent
<a name="API_OutboundEmailContent"></a>

Information about email body content.

## Contents
<a name="API_OutboundEmailContent_Contents"></a>

 ** MessageSourceType **   <a name="connect-Type-OutboundEmailContent-MessageSourceType"></a>
The message source type, that is, `RAW` or `TEMPLATE`.
Type: String
Valid Values: `TEMPLATE | RAW`
Required: Yes

 ** RawMessage **   <a name="connect-Type-OutboundEmailContent-RawMessage"></a>
The raw email body content.
Type: [OutboundRawMessage](API_OutboundRawMessage.md) object
Required: No

 ** TemplatedMessageConfig **   <a name="connect-Type-OutboundEmailContent-TemplatedMessageConfig"></a>
Information about template message configuration.
Type: [TemplatedMessageConfig](API_TemplatedMessageConfig.md) object
Required: No

## See Also
<a name="API_OutboundEmailContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/OutboundEmailContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/OutboundEmailContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/OutboundEmailContent)
