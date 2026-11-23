---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_WebhookCredential.html
---

# WebhookCredential

A new webhook credential. Exactly one variant must be set.

## Contents
<a name="API_WebhookCredential_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** BasicHttpPassword **   <a name="eventbridgev2-Type-WebhookCredential-BasicHttpPassword"></a>
The new password for HTTP Basic authentication. The username does not change.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 512.
Required: No

 ** HmacSecretValue **   <a name="eventbridgev2-Type-WebhookCredential-HmacSecretValue"></a>
The new HMAC secret, in the SecretEncoding of the EventSource. With BASE64, EventBridge removes a leading "whsec\_".
Type: String
Length Constraints: Minimum length of 6. Maximum length of 512.
Required: No

 ** StaticTokenSecretValue **   <a name="eventbridgev2-Type-WebhookCredential-StaticTokenSecretValue"></a>
The new token for static token authentication.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 512.
Required: No

## See Also
<a name="API_WebhookCredential_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/WebhookCredential)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/WebhookCredential)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/WebhookCredential)
