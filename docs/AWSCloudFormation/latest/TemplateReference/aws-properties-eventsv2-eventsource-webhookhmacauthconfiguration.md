---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-eventsource-webhookhmacauthconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventSource WebhookHmacAuthConfiguration

The provider signs each request with a hash-based message authentication code (HMAC) of the secret. Amazon EventBridge accepts the request if any signature in SignatureHttpHeader matches.

## Syntax
<a name="aws-properties-eventsv2-eventsource-webhookhmacauthconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-eventsource-webhookhmacauthconfiguration-syntax.json"></a>

```json
{
  "[Algorithm](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-algorithm)" : {{String}},
  "[Delimiter](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-delimiter)" : {{String}},
  "[Encoding](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-encoding)" : {{String}},
  "[MessageIdHttpHeader](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-messageidhttpheader)" : {{String}},
  "[SecretEncoding](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-secretencoding)" : {{String}},
  "[SecretValue](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-secretvalue)" : {{String}},
  "[SignatureHttpHeader](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-signaturehttpheader)" : {{String}},
  "[SignaturePrefix](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-signatureprefix)" : {{String}},
  "[SignedMessageComposition](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-signedmessagecomposition)" : {{String}},
  "[TimestampHttpHeader](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-timestamphttpheader)" : {{String}},
  "[TimestampPrefix](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-timestampprefix)" : {{String}},
  "[TimestampToleranceInSeconds](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-timestamptoleranceinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-eventsv2-eventsource-webhookhmacauthconfiguration-syntax.yaml"></a>

```yaml
  [Algorithm](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-algorithm): {{String}}
  [Delimiter](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-delimiter): {{String}}
  [Encoding](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-encoding): {{String}}
  [MessageIdHttpHeader](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-messageidhttpheader): {{String}}
  [SecretEncoding](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-secretencoding): {{String}}
  [SecretValue](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-secretvalue): {{String}}
  [SignatureHttpHeader](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-signaturehttpheader): {{String}}
  [SignaturePrefix](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-signatureprefix): {{String}}
  [SignedMessageComposition](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-signedmessagecomposition): {{String}}
  [TimestampHttpHeader](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-timestamphttpheader): {{String}}
  [TimestampPrefix](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-timestampprefix): {{String}}
  [TimestampToleranceInSeconds](#cfn-eventsv2-eventsource-webhookhmacauthconfiguration-timestamptoleranceinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-eventsv2-eventsource-webhookhmacauthconfiguration-properties"></a>

`Algorithm`  <a name="cfn-eventsv2-eventsource-webhookhmacauthconfiguration-algorithm"></a>
The hash algorithm the provider uses to compute the signature.
Valid values: - SHA256 - SHA-256. - SHA1 - SHA-1. Not recommended. Use SHA1 only for interoperability with a provider that cannot sign with SHA-256.
*Required*: Yes
*Type*: String
*Allowed values*: `SHA256 | SHA1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Delimiter`  <a name="cfn-eventsv2-eventsource-webhookhmacauthconfiguration-delimiter"></a>
The separator between parts of the signature header value, for example a comma for a header value of t=1727816400,v1=<signature>, or a space when the header carries several signatures. Required when TimestampHttpHeader is the same header as SignatureHttpHeader.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\u007E]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Encoding`  <a name="cfn-eventsv2-eventsource-webhookhmacauthconfiguration-encoding"></a>
How the provider encodes the signature in the header.
Valid values: - HEX - Hexadecimal. - BASE64 - Base64.
*Required*: Yes
*Type*: String
*Allowed values*: `HEX | BASE64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageIdHttpHeader`  <a name="cfn-eventsv2-eventsource-webhookhmacauthconfiguration-messageidhttpheader"></a>
The name of the header that carries the message ID. Required when SignedMessageComposition is MESSAGE\_ID\_DOT\_TIMESTAMP\_DOT\_BODY.
*Required*: No
*Type*: String
*Pattern*: `^[!#$%&'*+\-.^_`|~0-9A-Za-z]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretEncoding`  <a name="cfn-eventsv2-eventsource-webhookhmacauthconfiguration-secretencoding"></a>
How the secret is encoded. RAW uses the secret's characters as the signing key. BASE64 decodes the secret first, as required by providers that issue Base64-encoded signing keys, such as those following the Standard Webhooks specification. If you do not specify an encoding, EventBridge uses RAW. Changing the encoding replaces the event source.
*Required*: No
*Type*: String
*Allowed values*: `RAW | BASE64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecretValue`  <a name="cfn-eventsv2-eventsource-webhookhmacauthconfiguration-secretvalue"></a>
The signing key shared with the provider. If you do not specify a key, EventBridge generates one. EventBridge stores the key only in AWS Secrets Manager and never returns it. Set on create only: changing this value in a template has no effect. To change the key, call RotateWebhookCredentials. The webhook URL does not change.
*Required*: No
*Type*: String
*Minimum*: `6`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SignatureHttpHeader`  <a name="cfn-eventsv2-eventsource-webhookhmacauthconfiguration-signaturehttpheader"></a>
The name of the header that carries the signature, for example X-Hub-Signature-256. When TimestampHttpHeader names the same header, Delimiter, SignaturePrefix and TimestampPrefix are all required.
*Required*: Yes
*Type*: String
*Pattern*: `^[!#$%&'*+\-.^_`|~0-9A-Za-z]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SignaturePrefix`  <a name="cfn-eventsv2-eventsource-webhookhmacauthconfiguration-signatureprefix"></a>
The text that precedes the signature in the header value, for example sha256=. Required when TimestampHttpHeader is the same header as SignatureHttpHeader.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\u007E]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SignedMessageComposition`  <a name="cfn-eventsv2-eventsource-webhookhmacauthconfiguration-signedmessagecomposition"></a>
How the provider assembles the message it signs from the request.
Valid values: - BODY - The request body alone. - TIMESTAMP\_DOT\_BODY - <timestamp>.<body>. Requires TimestampHttpHeader. - MESSAGE\_ID\_DOT\_TIMESTAMP\_DOT\_BODY - <messageId>.<timestamp>.<body>, as in the Standard Webhooks specification. Requires TimestampHttpHeader and MessageIdHttpHeader.
*Required*: Yes
*Type*: String
*Allowed values*: `BODY | TIMESTAMP_DOT_BODY | MESSAGE_ID_DOT_TIMESTAMP_DOT_BODY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimestampHttpHeader`  <a name="cfn-eventsv2-eventsource-webhookhmacauthconfiguration-timestamphttpheader"></a>
The name of the header that carries the request timestamp. Required when SignedMessageComposition is TIMESTAMP\_DOT\_BODY or MESSAGE\_ID\_DOT\_TIMESTAMP\_DOT\_BODY, or when TimestampToleranceInSeconds is set. When it names the same header as SignatureHttpHeader, Delimiter, SignaturePrefix and TimestampPrefix are all required.
*Required*: No
*Type*: String
*Pattern*: `^[!#$%&'*+\-.^_`|~0-9A-Za-z]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimestampPrefix`  <a name="cfn-eventsv2-eventsource-webhookhmacauthconfiguration-timestampprefix"></a>
The text that precedes the timestamp in the header value, for example t=. Required when TimestampHttpHeader is the same header as SignatureHttpHeader.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\u007E]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimestampToleranceInSeconds`  <a name="cfn-eventsv2-eventsource-webhookhmacauthconfiguration-timestamptoleranceinseconds"></a>
The maximum difference, in seconds, allowed between the request timestamp and the time EventBridge receives the request. Requests outside this window are rejected. If you do not specify a tolerance, EventBridge uses 300 seconds. Requires TimestampHttpHeader.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `900`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
