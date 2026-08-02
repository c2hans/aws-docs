---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-configurationseteventdestination-eventbridgedestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ConfigurationSetEventDestination EventBridgeDestination
<a name="aws-properties-ses-configurationseteventdestination-eventbridgedestination"></a>

An object that defines an Amazon EventBridge destination for email events. You can use Amazon EventBridge to send notifications when certain email events occur.

## Syntax
<a name="aws-properties-ses-configurationseteventdestination-eventbridgedestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-configurationseteventdestination-eventbridgedestination-syntax.json"></a>

```
{
  "[EventBusArn](#cfn-ses-configurationseteventdestination-eventbridgedestination-eventbusarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-configurationseteventdestination-eventbridgedestination-syntax.yaml"></a>

```
  [EventBusArn](#cfn-ses-configurationseteventdestination-eventbridgedestination-eventbusarn): {{String}}
```

## Properties
<a name="aws-properties-ses-configurationseteventdestination-eventbridgedestination-properties"></a>

`EventBusArn`  <a name="cfn-ses-configurationseteventdestination-eventbridgedestination-eventbusarn"></a>
The Amazon Resource Name (ARN) of the Amazon EventBridge bus to publish email events to. Only the default bus is supported.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z0-9-]*:events:[a-z0-9-]+:\d{12}:event-bus/[^:]+$`
*Minimum*: `36`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
