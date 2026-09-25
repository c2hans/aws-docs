---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-logconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber LogConfiguration
<a name="aws-properties-eventsv2-subscriber-logconfiguration"></a>

Delivery logging configuration.

## Syntax
<a name="aws-properties-eventsv2-subscriber-logconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-logconfiguration-syntax.json"></a>

```
{
  "[IncludePayload](#cfn-eventsv2-subscriber-logconfiguration-includepayload)" : {{String}},
  "[Level](#cfn-eventsv2-subscriber-logconfiguration-level)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-logconfiguration-syntax.yaml"></a>

```
  [IncludePayload](#cfn-eventsv2-subscriber-logconfiguration-includepayload): {{String}}
  [Level](#cfn-eventsv2-subscriber-logconfiguration-level): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-logconfiguration-properties"></a>

`IncludePayload`  <a name="cfn-eventsv2-subscriber-logconfiguration-includepayload"></a>
Whether the event payload is included in emitted log records: FULL includes it in every emitted record, and ON\_ERROR\_ONLY includes it only in error records. The default is ON\_ERROR\_ONLY.
*Required*: No
*Type*: String
*Allowed values*: `FULL | ON_ERROR_ONLY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Level`  <a name="cfn-eventsv2-subscriber-logconfiguration-level"></a>
The minimum log level: OFF (no logging), ERROR, or INFO. Records below this level are not emitted. The default is OFF.
*Required*: No
*Type*: String
*Allowed values*: `OFF | ERROR | INFO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
