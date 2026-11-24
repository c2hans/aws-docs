---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-eventsource-webhookdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventSource WebhookDetails

Values Amazon EventBridge generated for a webhook event source.

## Syntax
<a name="aws-properties-eventsv2-eventsource-webhookdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-eventsource-webhookdetails-syntax.json"></a>

```json
{
  "[SecretArn](#cfn-eventsv2-eventsource-webhookdetails-secretarn)" : {{String}},
  "[WebhookUrl](#cfn-eventsv2-eventsource-webhookdetails-webhookurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-eventsource-webhookdetails-syntax.yaml"></a>

```yaml
  [SecretArn](#cfn-eventsv2-eventsource-webhookdetails-secretarn): {{String}}
  [WebhookUrl](#cfn-eventsv2-eventsource-webhookdetails-webhookurl): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-eventsource-webhookdetails-properties"></a>

`SecretArn`  <a name="cfn-eventsv2-eventsource-webhookdetails-secretarn"></a>
The ARN of the AWS Secrets Manager secret, in your account, that holds the webhook credential.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[a-z0-9]+)*:secretsmanager:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):secret:events-webhook(-preprod)?[!/].+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebhookUrl`  <a name="cfn-eventsv2-eventsource-webhookdetails-webhookurl"></a>
The HTTPS URL to configure at the event provider. The URL does not change for the life of the event source. Treat the URL as a credential. The URL appears in stack describe output and in drift detection results.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
