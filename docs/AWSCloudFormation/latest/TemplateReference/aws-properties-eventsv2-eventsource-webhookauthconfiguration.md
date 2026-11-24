---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-eventsource-webhookauthconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventSource WebhookAuthConfiguration

How the provider authenticates its webhook requests. Exactly one of the three variants must be set.

## Syntax
<a name="aws-properties-eventsv2-eventsource-webhookauthconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-eventsource-webhookauthconfiguration-syntax.json"></a>

```json
{
  "[BasicHttpAuthConfiguration](#cfn-eventsv2-eventsource-webhookauthconfiguration-basichttpauthconfiguration)" : {{WebhookBasicHttpAuthConfiguration}},
  "[HmacAuthConfiguration](#cfn-eventsv2-eventsource-webhookauthconfiguration-hmacauthconfiguration)" : {{WebhookHmacAuthConfiguration}},
  "[StaticTokenAuthConfiguration](#cfn-eventsv2-eventsource-webhookauthconfiguration-statictokenauthconfiguration)" : {{WebhookStaticTokenAuthConfiguration}}
}
```

### YAML
<a name="aws-properties-eventsv2-eventsource-webhookauthconfiguration-syntax.yaml"></a>

```yaml
  [BasicHttpAuthConfiguration](#cfn-eventsv2-eventsource-webhookauthconfiguration-basichttpauthconfiguration): {{
    WebhookBasicHttpAuthConfiguration}}
  [HmacAuthConfiguration](#cfn-eventsv2-eventsource-webhookauthconfiguration-hmacauthconfiguration): {{
    WebhookHmacAuthConfiguration}}
  [StaticTokenAuthConfiguration](#cfn-eventsv2-eventsource-webhookauthconfiguration-statictokenauthconfiguration): {{
    WebhookStaticTokenAuthConfiguration}}
```

## Properties
<a name="aws-properties-eventsv2-eventsource-webhookauthconfiguration-properties"></a>

`BasicHttpAuthConfiguration`  <a name="cfn-eventsv2-eventsource-webhookauthconfiguration-basichttpauthconfiguration"></a>
The provider sends HTTP Basic authentication credentials.
*Required*: No
*Type*: [WebhookBasicHttpAuthConfiguration](aws-properties-eventsv2-eventsource-webhookbasichttpauthconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HmacAuthConfiguration`  <a name="cfn-eventsv2-eventsource-webhookauthconfiguration-hmacauthconfiguration"></a>
The provider signs each request with a hash-based message authentication code (HMAC) of the secret.
*Required*: No
*Type*: [WebhookHmacAuthConfiguration](aws-properties-eventsv2-eventsource-webhookhmacauthconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticTokenAuthConfiguration`  <a name="cfn-eventsv2-eventsource-webhookauthconfiguration-statictokenauthconfiguration"></a>
The provider sends the secret as the value of an HTTP header.
*Required*: No
*Type*: [WebhookStaticTokenAuthConfiguration](aws-properties-eventsv2-eventsource-webhookstatictokenauthconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
