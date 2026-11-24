---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-eventsource-webhookstatictokenauthconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventSource WebhookStaticTokenAuthConfiguration

The provider sends the secret as the value of an HTTP header.

## Syntax
<a name="aws-properties-eventsv2-eventsource-webhookstatictokenauthconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-eventsource-webhookstatictokenauthconfiguration-syntax.json"></a>

```json
{
  "[SecretValue](#cfn-eventsv2-eventsource-webhookstatictokenauthconfiguration-secretvalue)" : {{String}},
  "[TokenHttpHeader](#cfn-eventsv2-eventsource-webhookstatictokenauthconfiguration-tokenhttpheader)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-eventsource-webhookstatictokenauthconfiguration-syntax.yaml"></a>

```yaml
  [SecretValue](#cfn-eventsv2-eventsource-webhookstatictokenauthconfiguration-secretvalue): {{String}}
  [TokenHttpHeader](#cfn-eventsv2-eventsource-webhookstatictokenauthconfiguration-tokenhttpheader): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-eventsource-webhookstatictokenauthconfiguration-properties"></a>

`SecretValue`  <a name="cfn-eventsv2-eventsource-webhookstatictokenauthconfiguration-secretvalue"></a>
The token the provider sends in the header. If you do not specify a token, Amazon EventBridge generates one. EventBridge stores the token only in AWS Secrets Manager and never returns it. Set on create only: changing this value in a template has no effect. To change the token, call RotateWebhookCredentials. The webhook URL does not change.
*Required*: No
*Type*: String
*Minimum*: `6`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenHttpHeader`  <a name="cfn-eventsv2-eventsource-webhookstatictokenauthconfiguration-tokenhttpheader"></a>
The name of the header that carries the secret, for example X-Webhook-Secret. Must be a valid header name as defined in RFC 7230.
*Required*: Yes
*Type*: String
*Pattern*: `^[!#$%&'*+\-.^_`|~0-9A-Za-z]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
