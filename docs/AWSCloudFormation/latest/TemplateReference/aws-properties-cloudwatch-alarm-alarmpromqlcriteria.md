---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alarm-alarmpromqlcriteria.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alarm AlarmPromQLCriteria
<a name="aws-properties-cloudwatch-alarm-alarmpromqlcriteria"></a>

Contains the configuration that determines how a PromQL alarm evaluates its contributors, including the query to run and the durations that define when contributors transition between states.

## Syntax
<a name="aws-properties-cloudwatch-alarm-alarmpromqlcriteria-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alarm-alarmpromqlcriteria-syntax.json"></a>

```
{
  "[PendingPeriod](#cfn-cloudwatch-alarm-alarmpromqlcriteria-pendingperiod)" : {{Integer}},
  "[Query](#cfn-cloudwatch-alarm-alarmpromqlcriteria-query)" : {{String}},
  "[RecoveryPeriod](#cfn-cloudwatch-alarm-alarmpromqlcriteria-recoveryperiod)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alarm-alarmpromqlcriteria-syntax.yaml"></a>

```
  [PendingPeriod](#cfn-cloudwatch-alarm-alarmpromqlcriteria-pendingperiod): {{Integer}}
  [Query](#cfn-cloudwatch-alarm-alarmpromqlcriteria-query): {{String}}
  [RecoveryPeriod](#cfn-cloudwatch-alarm-alarmpromqlcriteria-recoveryperiod): {{Integer}}
```

## Properties
<a name="aws-properties-cloudwatch-alarm-alarmpromqlcriteria-properties"></a>

`PendingPeriod`  <a name="cfn-cloudwatch-alarm-alarmpromqlcriteria-pendingperiod"></a>
The duration, in seconds, that a contributor must be continuously breaching before it transitions to the `ALARM` state.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `86400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Query`  <a name="cfn-cloudwatch-alarm-alarmpromqlcriteria-query"></a>
The PromQL query that the alarm evaluates. The query must return a result of vector type. Each entry in the vector result represents an alarm contributor.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecoveryPeriod`  <a name="cfn-cloudwatch-alarm-alarmpromqlcriteria-recoveryperiod"></a>
The duration, in seconds, that a contributor must continuously not be breaching before it transitions back to the `OK` state.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `86400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
