---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cassandra-table-autoscalingspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Table AutoScalingSpecification
<a name="aws-properties-cassandra-table-autoscalingspecification"></a>

The optional auto scaling capacity settings for a table in provisioned capacity mode.

## Syntax
<a name="aws-properties-cassandra-table-autoscalingspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cassandra-table-autoscalingspecification-syntax.json"></a>

```
{
  "[ReadCapacityAutoScaling](#cfn-cassandra-table-autoscalingspecification-readcapacityautoscaling)" : {{AutoScalingSetting}},
  "[WriteCapacityAutoScaling](#cfn-cassandra-table-autoscalingspecification-writecapacityautoscaling)" : {{AutoScalingSetting}}
}
```

### YAML
<a name="aws-properties-cassandra-table-autoscalingspecification-syntax.yaml"></a>

```
  [ReadCapacityAutoScaling](#cfn-cassandra-table-autoscalingspecification-readcapacityautoscaling): {{
    AutoScalingSetting}}
  [WriteCapacityAutoScaling](#cfn-cassandra-table-autoscalingspecification-writecapacityautoscaling): {{
    AutoScalingSetting}}
```

## Properties
<a name="aws-properties-cassandra-table-autoscalingspecification-properties"></a>

`ReadCapacityAutoScaling`  <a name="cfn-cassandra-table-autoscalingspecification-readcapacityautoscaling"></a>
The auto scaling settings for the table's read capacity.
*Required*: No
*Type*: [AutoScalingSetting](aws-properties-cassandra-table-autoscalingsetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WriteCapacityAutoScaling`  <a name="cfn-cassandra-table-autoscalingspecification-writecapacityautoscaling"></a>
The auto scaling settings for the table's write capacity.
*Required*: No
*Type*: [AutoScalingSetting](aws-properties-cassandra-table-autoscalingsetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
