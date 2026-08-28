---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-scalingtrigger.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster ScalingTrigger
<a name="aws-properties-emr-cluster-scalingtrigger"></a>

`ScalingTrigger` is a subproperty of the `ScalingRule` property type. `ScalingTrigger` determines the conditions that trigger an automatic scaling activity.

## Syntax
<a name="aws-properties-emr-cluster-scalingtrigger-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-scalingtrigger-syntax.json"></a>

```
{
  "[CloudWatchAlarmDefinition](#cfn-emr-cluster-scalingtrigger-cloudwatchalarmdefinition)" : {{CloudWatchAlarmDefinition}}
}
```

### YAML
<a name="aws-properties-emr-cluster-scalingtrigger-syntax.yaml"></a>

```
  [CloudWatchAlarmDefinition](#cfn-emr-cluster-scalingtrigger-cloudwatchalarmdefinition): {{
    CloudWatchAlarmDefinition}}
```

## Properties
<a name="aws-properties-emr-cluster-scalingtrigger-properties"></a>

`CloudWatchAlarmDefinition`  <a name="cfn-emr-cluster-scalingtrigger-cloudwatchalarmdefinition"></a>
The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.
*Required*: Yes
*Type*: [CloudWatchAlarmDefinition](aws-properties-emr-cluster-cloudwatchalarmdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
