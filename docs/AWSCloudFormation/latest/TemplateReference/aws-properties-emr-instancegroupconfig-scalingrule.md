---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancegroupconfig-scalingrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceGroupConfig ScalingRule
<a name="aws-properties-emr-instancegroupconfig-scalingrule"></a>

`ScalingRule` is a subproperty of the `AutoScalingPolicy` property type. `ScalingRule` defines the scale-in or scale-out rules for scaling activity, including the CloudWatch metric alarm that triggers activity, how EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.

## Syntax
<a name="aws-properties-emr-instancegroupconfig-scalingrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancegroupconfig-scalingrule-syntax.json"></a>

```
{
  "[Action](#cfn-emr-instancegroupconfig-scalingrule-action)" : {{ScalingAction}},
  "[Description](#cfn-emr-instancegroupconfig-scalingrule-description)" : {{String}},
  "[Name](#cfn-emr-instancegroupconfig-scalingrule-name)" : {{String}},
  "[Trigger](#cfn-emr-instancegroupconfig-scalingrule-trigger)" : {{ScalingTrigger}}
}
```

### YAML
<a name="aws-properties-emr-instancegroupconfig-scalingrule-syntax.yaml"></a>

```
  [Action](#cfn-emr-instancegroupconfig-scalingrule-action): {{
    ScalingAction}}
  [Description](#cfn-emr-instancegroupconfig-scalingrule-description): {{String}}
  [Name](#cfn-emr-instancegroupconfig-scalingrule-name): {{String}}
  [Trigger](#cfn-emr-instancegroupconfig-scalingrule-trigger): {{
    ScalingTrigger}}
```

## Properties
<a name="aws-properties-emr-instancegroupconfig-scalingrule-properties"></a>

`Action`  <a name="cfn-emr-instancegroupconfig-scalingrule-action"></a>
The conditions that trigger an automatic scaling activity.
*Required*: Yes
*Type*: [ScalingAction](aws-properties-emr-instancegroupconfig-scalingaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-emr-instancegroupconfig-scalingrule-description"></a>
A friendly, more verbose description of the automatic scaling rule.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-emr-instancegroupconfig-scalingrule-name"></a>
The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Trigger`  <a name="cfn-emr-instancegroupconfig-scalingrule-trigger"></a>
The CloudWatch alarm definition that determines when automatic scaling activity is triggered.
*Required*: Yes
*Type*: [ScalingTrigger](aws-properties-emr-instancegroupconfig-scalingtrigger.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
