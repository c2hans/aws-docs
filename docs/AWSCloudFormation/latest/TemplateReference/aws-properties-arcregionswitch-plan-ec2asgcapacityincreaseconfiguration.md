---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan Ec2AsgCapacityIncreaseConfiguration
<a name="aws-properties-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration"></a>

Configuration for increasing the capacity of Amazon EC2 Auto Scaling groups during a Region switch.

## Syntax
<a name="aws-properties-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-syntax.json"></a>

```
{
  "[Asgs](#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-asgs)" : {{[ Asg, ... ]}},
  "[CapacityMonitoringApproach](#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-capacitymonitoringapproach)" : {{}},
  "[TargetPercent](#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-targetpercent)" : {{Number}},
  "[TimeoutMinutes](#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-timeoutminutes)" : {{Number}},
  "[Ungraceful](#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-ungraceful)" : {{Ec2Ungraceful}},
  "[WaitELBTargetGroupHealthy](#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-waitelbtargetgrouphealthy)" : {{String}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-syntax.yaml"></a>

```
  [Asgs](#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-asgs): {{
    - Asg}}
  [CapacityMonitoringApproach](#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-capacitymonitoringapproach): {{
    }}
  [TargetPercent](#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-targetpercent): {{Number}}
  [TimeoutMinutes](#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-timeoutminutes): {{Number}}
  [Ungraceful](#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-ungraceful): {{
    Ec2Ungraceful}}
  [WaitELBTargetGroupHealthy](#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-waitelbtargetgrouphealthy): {{String}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-properties"></a>

`Asgs`  <a name="cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-asgs"></a>
The EC2 Auto Scaling groups for the configuration.
*Required*: Yes
*Type*: Array of [Asg](aws-properties-arcregionswitch-plan-asg.md)
*Minimum*: `2`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapacityMonitoringApproach`  <a name="cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-capacitymonitoringapproach"></a>
The monitoring approach that you specify EC2 Auto Scaling groups for the configuration.
*Required*: No
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetPercent`  <a name="cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-targetpercent"></a>
The target percentage that you specify for EC2 Auto Scaling groups. The default is 100.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutMinutes`  <a name="cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-timeoutminutes"></a>
The timeout value specified for the configuration.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ungraceful`  <a name="cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-ungraceful"></a>
The settings for ungraceful execution.
*Required*: No
*Type*: [Ec2Ungraceful](aws-properties-arcregionswitch-plan-ec2ungraceful.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WaitELBTargetGroupHealthy`  <a name="cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-waitelbtargetgrouphealthy"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `enabled | disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
