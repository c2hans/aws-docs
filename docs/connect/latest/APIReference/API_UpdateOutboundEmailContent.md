---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateOutboundEmailContent.html
---

# UpdateOutboundEmailContent
<a name="API_UpdateOutboundEmailContent"></a>

Contains the updated body content for an outbound email draft.

## Contents
<a name="API_UpdateOutboundEmailContent_Contents"></a>

 ** MessageSourceType **   <a name="connect-Type-UpdateOutboundEmailContent-MessageSourceType"></a>
The message source type. The only supported value is `RAW`.
Type: String
Valid Values: `RAW`
Required: Yes

 ** RawMessage **   <a name="connect-Type-UpdateOutboundEmailContent-RawMessage"></a>
The raw email body content.
Type: [UpdateOutboundRawMessage](API_UpdateOutboundRawMessage.md) object
Required: Yes

## See Also
<a name="API_UpdateOutboundEmailContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateOutboundEmailContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateOutboundEmailContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateOutboundEmailContent)
