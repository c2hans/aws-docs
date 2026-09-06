---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cassandra-table-autoscalingsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Table AutoScalingSetting
<a name="aws-properties-cassandra-table-autoscalingsetting"></a>

The optional auto scaling settings for a table with provisioned throughput capacity.

To turn on auto scaling for a table in `throughputMode:PROVISIONED`, you must specify the following parameters.

Configure the minimum and maximum capacity units. The auto scaling policy ensures that capacity never goes below the minimum or above the maximum range.
+ `minimumUnits`: The minimum level of throughput the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).
+ `maximumUnits`: The maximum level of throughput the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).
+ `scalingPolicy`: Amazon Keyspaces supports the `target tracking` scaling policy. The auto scaling target is a percentage of the provisioned capacity of the table.

For more information, see [Managing throughput capacity automatically with Amazon Keyspaces auto scaling](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html) in the *Amazon Keyspaces Developer Guide*.

## Syntax
<a name="aws-properties-cassandra-table-autoscalingsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cassandra-table-autoscalingsetting-syntax.json"></a>

```
{
  "[AutoScalingDisabled](#cfn-cassandra-table-autoscalingsetting-autoscalingdisabled)" : {{Boolean}},
  "[MaximumUnits](#cfn-cassandra-table-autoscalingsetting-maximumunits)" : {{Integer}},
  "[MinimumUnits](#cfn-cassandra-table-autoscalingsetting-minimumunits)" : {{Integer}},
  "[ScalingPolicy](#cfn-cassandra-table-autoscalingsetting-scalingpolicy)" : {{ScalingPolicy}}
}
```

### YAML
<a name="aws-properties-cassandra-table-autoscalingsetting-syntax.yaml"></a>

```
  [AutoScalingDisabled](#cfn-cassandra-table-autoscalingsetting-autoscalingdisabled): {{Boolean}}
  [MaximumUnits](#cfn-cassandra-table-autoscalingsetting-maximumunits): {{Integer}}
  [MinimumUnits](#cfn-cassandra-table-autoscalingsetting-minimumunits): {{Integer}}
  [ScalingPolicy](#cfn-cassandra-table-autoscalingsetting-scalingpolicy): {{
    ScalingPolicy}}
```

## Properties
<a name="aws-properties-cassandra-table-autoscalingsetting-properties"></a>

`AutoScalingDisabled`  <a name="cfn-cassandra-table-autoscalingsetting-autoscalingdisabled"></a>
This optional parameter enables auto scaling for the table if set to `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumUnits`  <a name="cfn-cassandra-table-autoscalingsetting-maximumunits"></a>
Manage costs by specifying the maximum amount of throughput to provision. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumUnits`  <a name="cfn-cassandra-table-autoscalingsetting-minimumunits"></a>
The minimum level of throughput the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingPolicy`  <a name="cfn-cassandra-table-autoscalingsetting-scalingpolicy"></a>
Amazon Keyspaces supports the `target tracking` auto scaling policy. With this policy, Amazon Keyspaces auto scaling ensures that the table's ratio of consumed to provisioned capacity stays at or near the target value that you specify. You define the target value as a percentage between 20 and 90.
*Required*: No
*Type*: [ScalingPolicy](aws-properties-cassandra-table-scalingpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
