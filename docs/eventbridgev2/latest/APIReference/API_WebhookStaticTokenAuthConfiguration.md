---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_WebhookStaticTokenAuthConfiguration.html
---

# WebhookStaticTokenAuthConfiguration

The provider sends the secret as the value of an HTTP header.

## Contents
<a name="API_WebhookStaticTokenAuthConfiguration_Contents"></a>

 ** TokenHttpHeader **   <a name="eventbridgev2-Type-WebhookStaticTokenAuthConfiguration-TokenHttpHeader"></a>
The name of the header that carries the secret, for example X-Webhook-Secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[!#$%&'*+\-.^_`|~0-9A-Za-z]+`
Required: Yes

 ** SecretValue **   <a name="eventbridgev2-Type-WebhookStaticTokenAuthConfiguration-SecretValue"></a>
The token the provider sends in the header. If you omit it, EventBridge generates one. EventBridge stores the token only in AWS Secrets Manager and never returns it, including from DescribeEventSource.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 512.
Required: No

## See Also
<a name="API_WebhookStaticTokenAuthConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/WebhookStaticTokenAuthConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/WebhookStaticTokenAuthConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/WebhookStaticTokenAuthConfiguration)
