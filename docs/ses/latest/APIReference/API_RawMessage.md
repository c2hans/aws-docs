---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_RawMessage.html
---

# RawMessage
<a name="API_RawMessage"></a>

Represents the raw data of the message.

## Contents
<a name="API_RawMessage_Contents"></a>

 ** Data **
The raw data of the message. This data needs to base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an AWS SDK, the SDK takes care of the base 64-encoding for you. In all cases, the client must ensure that the message format complies with Internet email standards regarding email header fields, MIME types, and MIME encoding.
The To:, CC:, and BCC: headers in the raw message can contain a group list.
If you are using `SendRawEmail` with sending authorization, you can include X-headers in the raw message to specify the "Source," "From," and "Return-Path" addresses. For more information, see the documentation for `SendRawEmail`.
Do not include these X-headers in the DKIM signature, because they are removed by Amazon SES before sending the email.
For more information, go to the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html).
Type: Base64-encoded binary data object
Required: Yes

## See Also
<a name="API_RawMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/RawMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/RawMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/RawMessage)
