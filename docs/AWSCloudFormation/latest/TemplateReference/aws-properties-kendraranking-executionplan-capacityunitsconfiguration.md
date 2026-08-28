---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendraranking-executionplan-capacityunitsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KendraRanking::ExecutionPlan CapacityUnitsConfiguration
<a name="aws-properties-kendraranking-executionplan-capacityunitsconfiguration"></a>

Sets additional capacity units configured for your rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the `Rescore` API. You can add and remove capacity units to fit your usage requirements.

## Syntax
<a name="aws-properties-kendraranking-executionplan-capacityunitsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendraranking-executionplan-capacityunitsconfiguration-syntax.json"></a>

```
{
  "[RescoreCapacityUnits](#cfn-kendraranking-executionplan-capacityunitsconfiguration-rescorecapacityunits)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-kendraranking-executionplan-capacityunitsconfiguration-syntax.yaml"></a>

```
  [RescoreCapacityUnits](#cfn-kendraranking-executionplan-capacityunitsconfiguration-rescorecapacityunits): {{Integer}}
```

## Properties
<a name="aws-properties-kendraranking-executionplan-capacityunitsconfiguration-properties"></a>

`RescoreCapacityUnits`  <a name="cfn-kendraranking-executionplan-capacityunitsconfiguration-rescorecapacityunits"></a>
The amount of extra capacity for your rescore execution plan.
A single extra capacity unit for a rescore execution plan provides 0.01 rescore requests per second. You can add up to 1000 extra capacity units.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
