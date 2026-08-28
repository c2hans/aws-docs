---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancegroupconfig-metricdimension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceGroupConfig MetricDimension
<a name="aws-properties-emr-instancegroupconfig-metricdimension"></a>

`MetricDimension` is a subproperty of the `CloudWatchAlarmDefinition` property type. `MetricDimension` specifies a CloudWatch dimension, which is specified with a `Key``Value` pair. The key is known as a `Name` in CloudWatch. By default, Amazon EMR uses one dimension whose `Key` is `JobFlowID` and `Value` is a variable representing the cluster ID, which is `${emr.clusterId}`. This enables the automatic scaling rule for EMR to bootstrap when the cluster ID becomes available during cluster creation.

## Syntax
<a name="aws-properties-emr-instancegroupconfig-metricdimension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancegroupconfig-metricdimension-syntax.json"></a>

```
{
  "[Key](#cfn-emr-instancegroupconfig-metricdimension-key)" : {{String}},
  "[Value](#cfn-emr-instancegroupconfig-metricdimension-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-emr-instancegroupconfig-metricdimension-syntax.yaml"></a>

```
  [Key](#cfn-emr-instancegroupconfig-metricdimension-key): {{String}}
  [Value](#cfn-emr-instancegroupconfig-metricdimension-value): {{String}}
```

## Properties
<a name="aws-properties-emr-instancegroupconfig-metricdimension-properties"></a>

`Key`  <a name="cfn-emr-instancegroupconfig-metricdimension-key"></a>
The dimension name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-emr-instancegroupconfig-metricdimension-value"></a>
The dimension value.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
