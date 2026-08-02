---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancegroupconfig-scalingtrigger.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceGroupConfig ScalingTrigger
<a name="aws-properties-emr-instancegroupconfig-scalingtrigger"></a>

`ScalingTrigger` is a subproperty of the `ScalingRule` property type. `ScalingTrigger` determines the conditions that trigger an automatic scaling activity.

## Syntax
<a name="aws-properties-emr-instancegroupconfig-scalingtrigger-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancegroupconfig-scalingtrigger-syntax.json"></a>

```
{
  "[CloudWatchAlarmDefinition](#cfn-emr-instancegroupconfig-scalingtrigger-cloudwatchalarmdefinition)" : {{CloudWatchAlarmDefinition}}
}
```

### YAML
<a name="aws-properties-emr-instancegroupconfig-scalingtrigger-syntax.yaml"></a>

```
  [CloudWatchAlarmDefinition](#cfn-emr-instancegroupconfig-scalingtrigger-cloudwatchalarmdefinition): {{
    CloudWatchAlarmDefinition}}
```

## Properties
<a name="aws-properties-emr-instancegroupconfig-scalingtrigger-properties"></a>

`CloudWatchAlarmDefinition`  <a name="cfn-emr-instancegroupconfig-scalingtrigger-cloudwatchalarmdefinition"></a>
The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.
*Required*: Yes
*Type*: [CloudWatchAlarmDefinition](aws-properties-emr-instancegroupconfig-cloudwatchalarmdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
