---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-scalingrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster ScalingRule
<a name="aws-properties-emr-cluster-scalingrule"></a>

`ScalingRule` is a subproperty of the `AutoScalingPolicy` property type. `ScalingRule` defines the scale-in or scale-out rules for scaling activity, including the CloudWatch metric alarm that triggers activity, how EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.

## Syntax
<a name="aws-properties-emr-cluster-scalingrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-scalingrule-syntax.json"></a>

```
{
  "[Action](#cfn-emr-cluster-scalingrule-action)" : {{ScalingAction}},
  "[Description](#cfn-emr-cluster-scalingrule-description)" : {{String}},
  "[Name](#cfn-emr-cluster-scalingrule-name)" : {{String}},
  "[Trigger](#cfn-emr-cluster-scalingrule-trigger)" : {{ScalingTrigger}}
}
```

### YAML
<a name="aws-properties-emr-cluster-scalingrule-syntax.yaml"></a>

```
  [Action](#cfn-emr-cluster-scalingrule-action): {{
    ScalingAction}}
  [Description](#cfn-emr-cluster-scalingrule-description): {{String}}
  [Name](#cfn-emr-cluster-scalingrule-name): {{String}}
  [Trigger](#cfn-emr-cluster-scalingrule-trigger): {{
    ScalingTrigger}}
```

## Properties
<a name="aws-properties-emr-cluster-scalingrule-properties"></a>

`Action`  <a name="cfn-emr-cluster-scalingrule-action"></a>
The conditions that trigger an automatic scaling activity.
*Required*: Yes
*Type*: [ScalingAction](aws-properties-emr-cluster-scalingaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-emr-cluster-scalingrule-description"></a>
A friendly, more verbose description of the automatic scaling rule.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-emr-cluster-scalingrule-name"></a>
The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Trigger`  <a name="cfn-emr-cluster-scalingrule-trigger"></a>
The CloudWatch alarm definition that determines when automatic scaling activity is triggered.
*Required*: Yes
*Type*: [ScalingTrigger](aws-properties-emr-cluster-scalingtrigger.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
