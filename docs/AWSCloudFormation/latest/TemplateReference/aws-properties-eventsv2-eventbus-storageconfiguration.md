---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-eventbus-storageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::EventBus StorageConfiguration
<a name="aws-properties-eventsv2-eventbus-storageconfiguration"></a>

Storage (retention) configuration for the event bus.

## Syntax
<a name="aws-properties-eventsv2-eventbus-storageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-eventbus-storageconfiguration-syntax.json"></a>

```
{
  "[RetentionPeriodInDays](#cfn-eventsv2-eventbus-storageconfiguration-retentionperiodindays)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-eventsv2-eventbus-storageconfiguration-syntax.yaml"></a>

```
  [RetentionPeriodInDays](#cfn-eventsv2-eventbus-storageconfiguration-retentionperiodindays): {{Integer}}
```

## Properties
<a name="aws-properties-eventsv2-eventbus-storageconfiguration-properties"></a>

`RetentionPeriodInDays`  <a name="cfn-eventsv2-eventbus-storageconfiguration-retentionperiodindays"></a>
The number of days events are retained on the event bus for replay, 1-365.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `365`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
