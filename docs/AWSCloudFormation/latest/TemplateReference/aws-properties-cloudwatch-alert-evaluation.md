---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alert-evaluation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alert Evaluation
<a name="aws-properties-cloudwatch-alert-evaluation"></a>

How often the alert is evaluated, and how long a change must last before the state changes.

## Syntax
<a name="aws-properties-cloudwatch-alert-evaluation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alert-evaluation-syntax.json"></a>

```
{
  "[IntervalSeconds](#cfn-cloudwatch-alert-evaluation-intervalseconds)" : {{Integer}},
  "[PendingDurationSeconds](#cfn-cloudwatch-alert-evaluation-pendingdurationseconds)" : {{Integer}},
  "[RecoveryDurationSeconds](#cfn-cloudwatch-alert-evaluation-recoverydurationseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alert-evaluation-syntax.yaml"></a>

```
  [IntervalSeconds](#cfn-cloudwatch-alert-evaluation-intervalseconds): {{Integer}}
  [PendingDurationSeconds](#cfn-cloudwatch-alert-evaluation-pendingdurationseconds): {{Integer}}
  [RecoveryDurationSeconds](#cfn-cloudwatch-alert-evaluation-recoverydurationseconds): {{Integer}}
```

## Properties
<a name="aws-properties-cloudwatch-alert-evaluation-properties"></a>

`IntervalSeconds`  <a name="cfn-cloudwatch-alert-evaluation-intervalseconds"></a>
The time between evaluations, in seconds. Valid values: 30, 60, 120, 300, 600, 900, 1800, 3600.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PendingDurationSeconds`  <a name="cfn-cloudwatch-alert-evaluation-pendingdurationseconds"></a>
How long a threshold breach must last before the alert changes state, in seconds. Must be a multiple of IntervalSeconds. 0 changes state immediately.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecoveryDurationSeconds`  <a name="cfn-cloudwatch-alert-evaluation-recoverydurationseconds"></a>
How long the result must stay within its thresholds before the alert returns to OK, in seconds. Must be a multiple of IntervalSeconds. 0 returns to OK immediately.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
