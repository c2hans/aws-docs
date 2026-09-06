---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amazonmq-broker-maintenancewindow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmazonMQ::Broker MaintenanceWindow
<a name="aws-properties-amazonmq-broker-maintenancewindow"></a>

The parameters that determine the WeeklyStartTime.

## Syntax
<a name="aws-properties-amazonmq-broker-maintenancewindow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amazonmq-broker-maintenancewindow-syntax.json"></a>

```
{
  "[DayOfWeek](#cfn-amazonmq-broker-maintenancewindow-dayofweek)" : {{String}},
  "[TimeOfDay](#cfn-amazonmq-broker-maintenancewindow-timeofday)" : {{String}},
  "[TimeZone](#cfn-amazonmq-broker-maintenancewindow-timezone)" : {{String}}
}
```

### YAML
<a name="aws-properties-amazonmq-broker-maintenancewindow-syntax.yaml"></a>

```
  [DayOfWeek](#cfn-amazonmq-broker-maintenancewindow-dayofweek): {{String}}
  [TimeOfDay](#cfn-amazonmq-broker-maintenancewindow-timeofday): {{String}}
  [TimeZone](#cfn-amazonmq-broker-maintenancewindow-timezone): {{String}}
```

## Properties
<a name="aws-properties-amazonmq-broker-maintenancewindow-properties"></a>

`DayOfWeek`  <a name="cfn-amazonmq-broker-maintenancewindow-dayofweek"></a>
Required. The day of the week.
*Required*: Yes
*Type*: String
*Allowed values*: `MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeOfDay`  <a name="cfn-amazonmq-broker-maintenancewindow-timeofday"></a>
Required. The time, in 24-hour format.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{1,2}:[0-9]{2}(:[0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeZone`  <a name="cfn-amazonmq-broker-maintenancewindow-timezone"></a>
The time zone, UTC by default, in either the Country/City format, or the UTC offset format.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
