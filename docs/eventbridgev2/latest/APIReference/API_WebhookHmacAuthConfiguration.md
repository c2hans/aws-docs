---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_WebhookHmacAuthConfiguration.html
---

# WebhookHmacAuthConfiguration

The provider signs each request with a hash-based message authentication code (HMAC) of the secret. Amazon EventBridge accepts the request if any signature in SignatureHttpHeader matches.

## Contents
<a name="API_WebhookHmacAuthConfiguration_Contents"></a>

 ** Algorithm **   <a name="eventbridgev2-Type-WebhookHmacAuthConfiguration-Algorithm"></a>
The hash algorithm the provider uses to compute the signature.
Type: String
Valid Values: `SHA256 | SHA1`
Required: Yes

 ** Encoding **   <a name="eventbridgev2-Type-WebhookHmacAuthConfiguration-Encoding"></a>
How the provider encodes the signature in the header.
Type: String
Valid Values: `HEX | BASE64`
Required: Yes

 ** SignatureHttpHeader **   <a name="eventbridgev2-Type-WebhookHmacAuthConfiguration-SignatureHttpHeader"></a>
The name of the header that carries the signature, for example X-Hub-Signature-256. When TimestampHttpHeader names the same header, Delimiter, SignaturePrefix, and TimestampPrefix are all required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[!#$%&'*+\-.^_`|~0-9A-Za-z]+`
Required: Yes

 ** SignedMessageComposition **   <a name="eventbridgev2-Type-WebhookHmacAuthConfiguration-SignedMessageComposition"></a>
The provider assembles the message it signs from the request in one of the following ways:
+ BODY – The request body alone.
+ TIMESTAMP\_DOT\_BODY – <timestamp>.<body>. Requires TimestampHttpHeader.
+ MESSAGE\_ID\_DOT\_TIMESTAMP\_DOT\_BODY – <messageId>.<timestamp>.<body>, as in the Standard Webhooks specification. Requires TimestampHttpHeader and MessageIdHttpHeader.
Type: String
Valid Values: `BODY | TIMESTAMP_DOT_BODY | MESSAGE_ID_DOT_TIMESTAMP_DOT_BODY`
Required: Yes

 ** Delimiter **   <a name="eventbridgev2-Type-WebhookHmacAuthConfiguration-Delimiter"></a>
The separator between parts of the signature header value, for example a comma for a header value of t=1727816400,v1=<signature>, or a space when the header carries several signatures. Required when TimestampHttpHeader is the same header as SignatureHttpHeader.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\u0020-\u007E]+`
Required: No

 ** MessageIdHttpHeader **   <a name="eventbridgev2-Type-WebhookHmacAuthConfiguration-MessageIdHttpHeader"></a>
The name of the header that carries the message ID. Required when SignedMessageComposition is MESSAGE\_ID\_DOT\_TIMESTAMP\_DOT\_BODY.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[!#$%&'*+\-.^_`|~0-9A-Za-z]+`
Required: No

 ** SecretEncoding **   <a name="eventbridgev2-Type-WebhookHmacAuthConfiguration-SecretEncoding"></a>
How the secret is encoded. RAW uses the secret's characters as the signing key. BASE64 decodes the secret first, as providers that follow the Standard Webhooks specification require. The default is RAW.
Type: String
Valid Values: `RAW | BASE64`
Required: No

 ** SecretValue **   <a name="eventbridgev2-Type-WebhookHmacAuthConfiguration-SecretValue"></a>
The signing key shared with the provider. If you omit it, EventBridge generates one. EventBridge stores the key only in AWS Secrets Manager and never returns it, including from DescribeEventSource.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 512.
Required: No

 ** SignaturePrefix **   <a name="eventbridgev2-Type-WebhookHmacAuthConfiguration-SignaturePrefix"></a>
The text that precedes the signature in the header value, for example sha256=. Required when TimestampHttpHeader is the same header as SignatureHttpHeader.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\u0020-\u007E]+`
Required: No

 ** TimestampHttpHeader **   <a name="eventbridgev2-Type-WebhookHmacAuthConfiguration-TimestampHttpHeader"></a>
The name of the header that carries the request timestamp. Required when SignedMessageComposition is TIMESTAMP\_DOT\_BODY or MESSAGE\_ID\_DOT\_TIMESTAMP\_DOT\_BODY, or when TimestampToleranceInSeconds is set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[!#$%&'*+\-.^_`|~0-9A-Za-z]+`
Required: No

 ** TimestampPrefix **   <a name="eventbridgev2-Type-WebhookHmacAuthConfiguration-TimestampPrefix"></a>
The text that precedes the timestamp in the header value, for example t=. Required when TimestampHttpHeader is the same header as SignatureHttpHeader.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\u0020-\u007E]+`
Required: No

 ** TimestampToleranceInSeconds **   <a name="eventbridgev2-Type-WebhookHmacAuthConfiguration-TimestampToleranceInSeconds"></a>
The maximum difference, in seconds, allowed between the request timestamp and the time EventBridge receives the request. Requests outside this window are rejected. The default is 300 seconds. Requires TimestampHttpHeader.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 900.
Required: No

## See Also
<a name="API_WebhookHmacAuthConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/WebhookHmacAuthConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/WebhookHmacAuthConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/WebhookHmacAuthConfiguration)
