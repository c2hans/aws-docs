---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_WebhookBasicHttpAuthConfiguration.html
---

# WebhookBasicHttpAuthConfiguration

The provider sends HTTP Basic authentication credentials: an Authorization header with the value "Basic " followed by the Base64 encoding of username:password. Supply both Username and Password, or omit both so that EventBridge generates the pair. Supplying only one fails with InvalidInputException. EventBridge stores both only in AWS Secrets Manager and never returns them, including from DescribeEventSource.

## Contents
<a name="API_WebhookBasicHttpAuthConfiguration_Contents"></a>

 ** Password **   <a name="eventbridgev2-Type-WebhookBasicHttpAuthConfiguration-Password"></a>
The password.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 512.
Required: No

 ** Username **   <a name="eventbridgev2-Type-WebhookBasicHttpAuthConfiguration-Username"></a>
The username.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:\s]+`
Required: No

## See Also
<a name="API_WebhookBasicHttpAuthConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/WebhookBasicHttpAuthConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/WebhookBasicHttpAuthConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/WebhookBasicHttpAuthConfiguration)
