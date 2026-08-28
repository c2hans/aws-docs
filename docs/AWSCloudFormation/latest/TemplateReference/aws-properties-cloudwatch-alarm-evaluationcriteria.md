---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alarm-evaluationcriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alarm EvaluationCriteria
<a name="aws-properties-cloudwatch-alarm-evaluationcriteria"></a>

The evaluation criteria for an alarm. This is a union type that currently supports `PromQLCriteria`.

## Syntax
<a name="aws-properties-cloudwatch-alarm-evaluationcriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alarm-evaluationcriteria-syntax.json"></a>

```
{
  "[PromQLCriteria](#cfn-cloudwatch-alarm-evaluationcriteria-promqlcriteria)" : {{AlarmPromQLCriteria}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alarm-evaluationcriteria-syntax.yaml"></a>

```
  [PromQLCriteria](#cfn-cloudwatch-alarm-evaluationcriteria-promqlcriteria): {{
    AlarmPromQLCriteria}}
```

## Properties
<a name="aws-properties-cloudwatch-alarm-evaluationcriteria-properties"></a>

`PromQLCriteria`  <a name="cfn-cloudwatch-alarm-evaluationcriteria-promqlcriteria"></a>
The PromQL criteria for the alarm evaluation.
*Required*: No
*Type*: [AlarmPromQLCriteria](aws-properties-cloudwatch-alarm-alarmpromqlcriteria.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
