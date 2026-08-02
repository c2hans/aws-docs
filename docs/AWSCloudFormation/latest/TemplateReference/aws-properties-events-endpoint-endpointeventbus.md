---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-endpoint-endpointeventbus.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Endpoint EndpointEventBus
<a name="aws-properties-events-endpoint-endpointeventbus"></a>

The event buses the endpoint is associated with.

## Syntax
<a name="aws-properties-events-endpoint-endpointeventbus-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-endpoint-endpointeventbus-syntax.json"></a>

```
{
  "[EventBusArn](#cfn-events-endpoint-endpointeventbus-eventbusarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-events-endpoint-endpointeventbus-syntax.yaml"></a>

```
  [EventBusArn](#cfn-events-endpoint-endpointeventbus-eventbusarn): {{String}}
```

## Properties
<a name="aws-properties-events-endpoint-endpointeventbus-properties"></a>

`EventBusArn`  <a name="cfn-events-endpoint-endpointeventbus-eventbusarn"></a>
The ARN of the event bus the endpoint is associated with.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z-]*:events:[a-z]+-[a-z-]+-\d+:\d{12}:event-bus/[\w.-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
