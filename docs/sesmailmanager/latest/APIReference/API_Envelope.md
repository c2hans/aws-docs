---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_Envelope.html
---

# Envelope
<a name="API_Envelope"></a>

The SMTP envelope information of the email.

## Contents
<a name="API_Envelope_Contents"></a>

 ** From **   <a name="sesmailmanager-Type-Envelope-From"></a>
The RCPT FROM given by the host from which the email was received.
Type: String
Required: No

 ** Helo **   <a name="sesmailmanager-Type-Envelope-Helo"></a>
The HELO used by the host from which the email was received.
Type: String
Required: No

 ** To **   <a name="sesmailmanager-Type-Envelope-To"></a>
All SMTP TO entries given by the host from which the email was received.
Type: Array of strings
Required: No

## See Also
<a name="API_Envelope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/Envelope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/Envelope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/Envelope)
