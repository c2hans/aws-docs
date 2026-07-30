---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-associatedalarm.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan AssociatedAlarm
<a name="aws-properties-arcregionswitch-plan-associatedalarm"></a>

An Amazon CloudWatch alarm associated with a Region switch plan. These alarms can be used to trigger automatic execution of the plan.

## Syntax
<a name="aws-properties-arcregionswitch-plan-associatedalarm-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-associatedalarm-syntax.json"></a>

```
{
  "[AlarmType](#cfn-arcregionswitch-plan-associatedalarm-alarmtype)" : {{String}},
  "[CrossAccountRole](#cfn-arcregionswitch-plan-associatedalarm-crossaccountrole)" : {{String}},
  "[ExternalId](#cfn-arcregionswitch-plan-associatedalarm-externalid)" : {{String}},
  "[ResourceIdentifier](#cfn-arcregionswitch-plan-associatedalarm-resourceidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-associatedalarm-syntax.yaml"></a>

```
  [AlarmType](#cfn-arcregionswitch-plan-associatedalarm-alarmtype): {{String}}
  [CrossAccountRole](#cfn-arcregionswitch-plan-associatedalarm-crossaccountrole): {{String}}
  [ExternalId](#cfn-arcregionswitch-plan-associatedalarm-externalid): {{String}}
  [ResourceIdentifier](#cfn-arcregionswitch-plan-associatedalarm-resourceidentifier): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-associatedalarm-properties"></a>

`AlarmType`  <a name="cfn-arcregionswitch-plan-associatedalarm-alarmtype"></a>
The alarm type for an associated alarm. An associated CloudWatch alarm can be an application health alarm or a trigger alarm.
*Required*: Yes
*Type*: String
*Allowed values*: `applicationHealth | trigger`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrossAccountRole`  <a name="cfn-arcregionswitch-plan-associatedalarm-crossaccountrole"></a>
The cross account role for the configuration.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-arcregionswitch-plan-associatedalarm-externalid"></a>
The external ID (secret key) for the configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceIdentifier`  <a name="cfn-arcregionswitch-plan-associatedalarm-resourceidentifier"></a>
The resource identifier for alarms that you associate with a plan.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
