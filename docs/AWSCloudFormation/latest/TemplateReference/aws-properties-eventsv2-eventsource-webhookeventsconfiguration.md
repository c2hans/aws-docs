---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-eventsource-webhookeventsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventSource WebhookEventsConfiguration

Receive events from an external provider, such as a SaaS application, that sends them as HTTPS POST requests to a webhook URL. The provider authenticates with an HTTP scheme instead of AWS credentials.

## Syntax
<a name="aws-properties-eventsv2-eventsource-webhookeventsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-eventsource-webhookeventsconfiguration-syntax.json"></a>

```json
{
  "[AuthConfiguration](#cfn-eventsv2-eventsource-webhookeventsconfiguration-authconfiguration)" : {{WebhookAuthConfiguration}},
  "[DeduplicationConfiguration](#cfn-eventsv2-eventsource-webhookeventsconfiguration-deduplicationconfiguration)" : {{WebhookDeduplicationConfiguration}},
  "[KmsKeyIdentifier](#cfn-eventsv2-eventsource-webhookeventsconfiguration-kmskeyidentifier)" : {{String}},
  "[LogConfiguration](#cfn-eventsv2-eventsource-webhookeventsconfiguration-logconfiguration)" : {{LogConfiguration}},
  "[MetadataHttpHeaders](#cfn-eventsv2-eventsource-webhookeventsconfiguration-metadatahttpheaders)" : {{[ String, ... ]}},
  "[RoleArn](#cfn-eventsv2-eventsource-webhookeventsconfiguration-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-eventsource-webhookeventsconfiguration-syntax.yaml"></a>

```yaml
  [AuthConfiguration](#cfn-eventsv2-eventsource-webhookeventsconfiguration-authconfiguration): {{
    WebhookAuthConfiguration}}
  [DeduplicationConfiguration](#cfn-eventsv2-eventsource-webhookeventsconfiguration-deduplicationconfiguration): {{
    WebhookDeduplicationConfiguration}}
  [KmsKeyIdentifier](#cfn-eventsv2-eventsource-webhookeventsconfiguration-kmskeyidentifier): {{String}}
  [LogConfiguration](#cfn-eventsv2-eventsource-webhookeventsconfiguration-logconfiguration): {{
    LogConfiguration}}
  [MetadataHttpHeaders](#cfn-eventsv2-eventsource-webhookeventsconfiguration-metadatahttpheaders): {{
    - String}}
  [RoleArn](#cfn-eventsv2-eventsource-webhookeventsconfiguration-rolearn): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-eventsource-webhookeventsconfiguration-properties"></a>

`AuthConfiguration`  <a name="cfn-eventsv2-eventsource-webhookeventsconfiguration-authconfiguration"></a>
How the provider authenticates its requests. Set exactly one authentication type. You can't change the type after you create the event source.
*Required*: Yes
*Type*: [WebhookAuthConfiguration](aws-properties-eventsv2-eventsource-webhookauthconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeduplicationConfiguration`  <a name="cfn-eventsv2-eventsource-webhookeventsconfiguration-deduplicationconfiguration"></a>
Deduplicates the event source's events on the event bus. If you do not specify a configuration, EventBridge does not deduplicate events.
*Required*: No
*Type*: [WebhookDeduplicationConfiguration](aws-properties-eventsv2-eventsource-webhookdeduplicationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyIdentifier`  <a name="cfn-eventsv2-eventsource-webhookeventsconfiguration-kmskeyidentifier"></a>
The AWS KMS key that encrypts the event source's secret in AWS Secrets Manager. If you do not specify a key, the secret is encrypted with the AWS managed key aws/secretsmanager. A key you specify must be an enabled customer managed key in your account and Region. Changing the key re-encrypts the secret under the new key. The previous key can still decrypt the stored versions until the credential is next rotated.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-/:]*$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogConfiguration`  <a name="cfn-eventsv2-eventsource-webhookeventsconfiguration-logconfiguration"></a>
The log records Amazon EventBridge delivers for the webhook requests this event source receives. If you do not specify a configuration, EventBridge delivers no logs. Logs are delivered to the destinations you configure with Amazon CloudWatch Logs vended log delivery.
*Required*: No
*Type*: [LogConfiguration](aws-properties-eventsv2-eventsource-logconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetadataHttpHeaders`  <a name="cfn-eventsv2-eventsource-webhookeventsconfiguration-metadatahttpheaders"></a>
The HTTP request headers to add to each event's metadata, up to 20. Header names are case-insensitive and cannot repeat. Amazon EventBridge adds each header under its lowercase name. If you do not specify headers, EventBridge adds none. You cannot list headers that carry credentials or describe the network path, or the header that carries the static token.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `128 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-eventsv2-eventsource-webhookeventsconfiguration-rolearn"></a>
The ARN of the IAM role that Amazon EventBridge assumes to put the webhook's events on the event bus. The role must belong to the calling account.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z0-9]+)*:iam::\d{12}:role\/[\w+=,.@/-]+$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
