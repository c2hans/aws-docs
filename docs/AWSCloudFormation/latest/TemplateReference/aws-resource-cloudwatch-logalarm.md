---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-logalarm.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::LogAlarm
<a name="aws-resource-cloudwatch-logalarm"></a>

Creates or updates a log alarm. A log alarm evaluates the results of a CloudWatch Logs scheduled query against the configured threshold and comparison operator to determine its state.

When you create a log alarm, the operation creates a service-managed CloudWatch Logs scheduled query that runs the query string you provide on the schedule you configure. Each scheduled query execution returns one or more aggregated values determined by the `AggregationExpression`, and each aggregated value is compared against the alarm `Threshold` to determine the alarm state. The alarm uses M-out-of-N evaluation: if `QueryResultsToAlarm` out of the most recent `QueryResultsToEvaluate` query results breach the threshold, the alarm transitions to `ALARM`.

Log alarms support the alarm states (`OK`, `ALARM`, `INSUFFICIENT_DATA`). Configure transition actions using `OKActions`, `AlarmActions`, and `InsufficientDataActions`.

If you call this operation with the name of an existing log alarm, the operation replaces the previous configuration of that alarm.

 **Permissions**

To create or update a log alarm, you must have the `cloudwatch:PutLogAlarm` permission. The IAM role specified in `ScheduledQueryRoleARN` must grant the CloudWatch Alarms service permission to execute scheduled queries on the specified log groups. If you set `ActionLogLineCount`, the role specified in `ActionLogLineRoleArn` must grant permission to retrieve log events for inclusion in alarm notifications.

## Syntax
<a name="aws-resource-cloudwatch-logalarm-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-logalarm-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::LogAlarm",
  "Properties" : {
      "[ActionLogLineCount](#cfn-cloudwatch-logalarm-actionloglinecount)" : {{Integer}},
      "[ActionLogLineRoleArn](#cfn-cloudwatch-logalarm-actionloglinerolearn)" : {{String}},
      "[ActionsEnabled](#cfn-cloudwatch-logalarm-actionsenabled)" : {{Boolean}},
      "[AlarmActions](#cfn-cloudwatch-logalarm-alarmactions)" : {{[ String, ... ]}},
      "[AlarmDescription](#cfn-cloudwatch-logalarm-alarmdescription)" : {{String}},
      "[AlarmName](#cfn-cloudwatch-logalarm-alarmname)" : {{String}},
      "[ComparisonOperator](#cfn-cloudwatch-logalarm-comparisonoperator)" : {{String}},
      "[InsufficientDataActions](#cfn-cloudwatch-logalarm-insufficientdataactions)" : {{[ String, ... ]}},
      "[OKActions](#cfn-cloudwatch-logalarm-okactions)" : {{[ String, ... ]}},
      "[QueryResultsToAlarm](#cfn-cloudwatch-logalarm-queryresultstoalarm)" : {{Integer}},
      "[QueryResultsToEvaluate](#cfn-cloudwatch-logalarm-queryresultstoevaluate)" : {{Integer}},
      "[ScheduledQueryConfiguration](#cfn-cloudwatch-logalarm-scheduledqueryconfiguration)" : {{ScheduledQueryConfiguration}},
      "[Tags](#cfn-cloudwatch-logalarm-tags)" : {{[ Tag, ... ]}},
      "[Threshold](#cfn-cloudwatch-logalarm-threshold)" : {{Number}},
      "[TreatMissingData](#cfn-cloudwatch-logalarm-treatmissingdata)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-logalarm-syntax.yaml"></a>

```
Type: AWS::CloudWatch::LogAlarm
Properties:
  [ActionLogLineCount](#cfn-cloudwatch-logalarm-actionloglinecount): {{Integer}}
  [ActionLogLineRoleArn](#cfn-cloudwatch-logalarm-actionloglinerolearn): {{String}}
  [ActionsEnabled](#cfn-cloudwatch-logalarm-actionsenabled): {{Boolean}}
  [AlarmActions](#cfn-cloudwatch-logalarm-alarmactions): {{
    - String}}
  [AlarmDescription](#cfn-cloudwatch-logalarm-alarmdescription): {{String}}
  [AlarmName](#cfn-cloudwatch-logalarm-alarmname): {{String}}
  [ComparisonOperator](#cfn-cloudwatch-logalarm-comparisonoperator): {{String}}
  [InsufficientDataActions](#cfn-cloudwatch-logalarm-insufficientdataactions): {{
    - String}}
  [OKActions](#cfn-cloudwatch-logalarm-okactions): {{
    - String}}
  [QueryResultsToAlarm](#cfn-cloudwatch-logalarm-queryresultstoalarm): {{Integer}}
  [QueryResultsToEvaluate](#cfn-cloudwatch-logalarm-queryresultstoevaluate): {{Integer}}
  [ScheduledQueryConfiguration](#cfn-cloudwatch-logalarm-scheduledqueryconfiguration): {{
    ScheduledQueryConfiguration}}
  [Tags](#cfn-cloudwatch-logalarm-tags): {{
    - Tag}}
  [Threshold](#cfn-cloudwatch-logalarm-threshold): {{Number}}
  [TreatMissingData](#cfn-cloudwatch-logalarm-treatmissingdata): {{String}}
```

## Properties
<a name="aws-resource-cloudwatch-logalarm-properties"></a>

`ActionLogLineCount`  <a name="cfn-cloudwatch-logalarm-actionloglinecount"></a>
The number of log lines from the most recent scheduled query execution to include in alarm action notifications. Valid range is 0 through 50. The default is 0, which means no log lines are included.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ActionLogLineRoleArn`  <a name="cfn-cloudwatch-logalarm-actionloglinerolearn"></a>
The Amazon Resource Name (ARN) of an IAM role that CloudWatch assumes to retrieve log events for inclusion in alarm action notifications. Required when `ActionLogLineCount` is greater than 0.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ActionsEnabled`  <a name="cfn-cloudwatch-logalarm-actionsenabled"></a>
Indicates whether actions should be executed during any changes to the alarm state. The default is `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AlarmActions`  <a name="cfn-cloudwatch-logalarm-alarmactions"></a>
The actions to execute when this alarm transitions to the `ALARM` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
Valid Values:
 **Amazon SNS actions:**
 `arn:aws:sns:region:account-id:sns-topic-name`
 **Lambda actions:**
+ Invoke the latest version of a Lambda function: `arn:aws:lambda:region:account-id:function:function-name`
+ Invoke a specific version of a Lambda function: `arn:aws:lambda:region:account-id:function:function-name:version-number`
+ Invoke a function by using an alias Lambda function: `arn:aws:lambda:region:account-id:function:function-name:alias-name`
 **Systems Manager actions:**
 `arn:aws:ssm:region:account-id:opsitem:severity`
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AlarmDescription`  <a name="cfn-cloudwatch-logalarm-alarmdescription"></a>
The description for the alarm.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AlarmName`  <a name="cfn-cloudwatch-logalarm-alarmname"></a>
The name for the alarm. This name must be unique within the AWS account and Region.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ComparisonOperator`  <a name="cfn-cloudwatch-logalarm-comparisonoperator"></a>
The arithmetic operation to use when comparing the aggregated query result and the threshold. The aggregated query result is used as the first operand. Valid values are `GreaterThanThreshold`, `GreaterThanOrEqualToThreshold`, `LessThanThreshold`, and `LessThanOrEqualToThreshold`.
*Required*: Yes
*Type*: String
*Allowed values*: `GreaterThanOrEqualToThreshold | GreaterThanThreshold | LessThanThreshold | LessThanOrEqualToThreshold | LessThanLowerOrGreaterThanUpperThreshold | LessThanLowerThreshold | GreaterThanUpperThreshold`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InsufficientDataActions`  <a name="cfn-cloudwatch-logalarm-insufficientdataactions"></a>
The actions to execute when this alarm transitions to the `INSUFFICIENT_DATA` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
Valid Values:
 **Amazon SNS actions:**
 `arn:aws:sns:region:account-id:sns-topic-name`
 **Lambda actions:**
+ Invoke the latest version of a Lambda function: `arn:aws:lambda:region:account-id:function:function-name`
+ Invoke a specific version of a Lambda function: `arn:aws:lambda:region:account-id:function:function-name:version-number`
+ Invoke a function by using an alias Lambda function: `arn:aws:lambda:region:account-id:function:function-name:alias-name`
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OKActions`  <a name="cfn-cloudwatch-logalarm-okactions"></a>
The actions to execute when this alarm transitions to the `OK` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
Valid Values:
 **Amazon SNS actions:**
 `arn:aws:sns:region:account-id:sns-topic-name`
 **Lambda actions:**
+ Invoke the latest version of a Lambda function: `arn:aws:lambda:region:account-id:function:function-name`
+ Invoke a specific version of a Lambda function: `arn:aws:lambda:region:account-id:function:function-name:version-number`
+ Invoke a function by using an alias Lambda function: `arn:aws:lambda:region:account-id:function:function-name:alias-name`
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryResultsToAlarm`  <a name="cfn-cloudwatch-logalarm-queryresultstoalarm"></a>
The number of query results, out of the most recent `QueryResultsToEvaluate` results, that must breach the threshold to trigger the alarm to transition to `ALARM` (the M in M-of-N evaluation). Must be less than or equal to `QueryResultsToEvaluate`.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryResultsToEvaluate`  <a name="cfn-cloudwatch-logalarm-queryresultstoevaluate"></a>
The number of most recent scheduled query results to evaluate against the threshold (the N in M-of-N evaluation). Valid range is 1 through 100.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduledQueryConfiguration`  <a name="cfn-cloudwatch-logalarm-scheduledqueryconfiguration"></a>
The configuration of the underlying CloudWatch Logs scheduled query, including the query string, log groups, schedule, aggregation expression, and the ARN of the managed scheduled query.
*Required*: Yes
*Type*: [ScheduledQueryConfiguration](aws-properties-cloudwatch-logalarm-scheduledqueryconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudwatch-logalarm-tags"></a>
A list of key-value pairs to associate with the alarm. You can use tags to categorize and manage your alarms.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-logalarm-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Threshold`  <a name="cfn-cloudwatch-logalarm-threshold"></a>
The value to compare with the aggregated query result.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TreatMissingData`  <a name="cfn-cloudwatch-logalarm-treatmissingdata"></a>
Sets how this alarm is to handle missing data points. Valid values are `breaching`, `notBreaching`, `ignore`, and `missing`. If this parameter is omitted, the default behavior of `missing` is used.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-logalarm-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-logalarm-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudwatch-logalarm-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudwatch-logalarm-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.
