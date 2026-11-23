---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_WebhookAuthConfiguration.html
---

# WebhookAuthConfiguration

How the provider authenticates its webhook requests. Exactly one variant must be set.

## Contents
<a name="API_WebhookAuthConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** BasicHttpAuthConfiguration **   <a name="eventbridgev2-Type-WebhookAuthConfiguration-BasicHttpAuthConfiguration"></a>
The provider uses HTTP Basic authentication.
Type: [WebhookBasicHttpAuthConfiguration](API_WebhookBasicHttpAuthConfiguration.md) object
Required: No

 ** HmacAuthConfiguration **   <a name="eventbridgev2-Type-WebhookAuthConfiguration-HmacAuthConfiguration"></a>
The provider signs each request with an HMAC of the secret.
Type: [WebhookHmacAuthConfiguration](API_WebhookHmacAuthConfiguration.md) object
Required: No

 ** StaticTokenAuthConfiguration **   <a name="eventbridgev2-Type-WebhookAuthConfiguration-StaticTokenAuthConfiguration"></a>
The provider sends a static token in an HTTP header.
Type: [WebhookStaticTokenAuthConfiguration](API_WebhookStaticTokenAuthConfiguration.md) object
Required: No

## See Also
<a name="API_WebhookAuthConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/WebhookAuthConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/WebhookAuthConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/WebhookAuthConfiguration)
