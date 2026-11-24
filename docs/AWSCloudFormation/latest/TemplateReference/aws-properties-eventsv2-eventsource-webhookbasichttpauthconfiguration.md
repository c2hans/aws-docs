---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-eventsource-webhookbasichttpauthconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventSource WebhookBasicHttpAuthConfiguration

The provider sends HTTP Basic authentication credentials: an Authorization header with the value "Basic " followed by the Base64 encoding of username:password. Specify both Username and Password, or omit both and Amazon EventBridge generates the pair. Specifying only one fails the request. EventBridge stores both only in AWS Secrets Manager and never returns them.

## Syntax
<a name="aws-properties-eventsv2-eventsource-webhookbasichttpauthconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-eventsource-webhookbasichttpauthconfiguration-syntax.json"></a>

```json
{
  "[Password](#cfn-eventsv2-eventsource-webhookbasichttpauthconfiguration-password)" : {{String}},
  "[Username](#cfn-eventsv2-eventsource-webhookbasichttpauthconfiguration-username)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-eventsource-webhookbasichttpauthconfiguration-syntax.yaml"></a>

```yaml
  [Password](#cfn-eventsv2-eventsource-webhookbasichttpauthconfiguration-password): {{String}}
  [Username](#cfn-eventsv2-eventsource-webhookbasichttpauthconfiguration-username): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-eventsource-webhookbasichttpauthconfiguration-properties"></a>

`Password`  <a name="cfn-eventsv2-eventsource-webhookbasichttpauthconfiguration-password"></a>
The password. Set on create only: changing this value in a template has no effect. To change the password, call RotateWebhookCredentials. The username and the webhook URL do not change.
*Required*: No
*Type*: String
*Minimum*: `6`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-eventsv2-eventsource-webhookbasichttpauthconfiguration-username"></a>
The username. Cannot contain a colon or whitespace. Changing the username requires replacing the event source, which also requires a new Name and gives the event source a new webhook URL. RotateWebhookCredentials cannot change the username.
*Required*: No
*Type*: String
*Pattern*: `^[^:\s]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
