---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-maintenance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow Maintenance
<a name="aws-properties-mediaconnect-flow-maintenance"></a>

 The maintenance setting of a flow.

## Syntax
<a name="aws-properties-mediaconnect-flow-maintenance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-maintenance-syntax.json"></a>

```
{
  "[MaintenanceDay](#cfn-mediaconnect-flow-maintenance-maintenanceday)" : {{String}},
  "[MaintenanceStartHour](#cfn-mediaconnect-flow-maintenance-maintenancestarthour)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-maintenance-syntax.yaml"></a>

```
  [MaintenanceDay](#cfn-mediaconnect-flow-maintenance-maintenanceday): {{String}}
  [MaintenanceStartHour](#cfn-mediaconnect-flow-maintenance-maintenancestarthour): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-maintenance-properties"></a>

`MaintenanceDay`  <a name="cfn-mediaconnect-flow-maintenance-maintenanceday"></a>
 A day of a week when the maintenance will happen. Use Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday.
*Required*: Yes
*Type*: String
*Allowed values*: `Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaintenanceStartHour`  <a name="cfn-mediaconnect-flow-maintenance-maintenancestarthour"></a>
 UTC time when the maintenance will happen. Use 24-hour HH:MM format. Minutes must be 00. Example: 13:00. The default value is 02:00.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
