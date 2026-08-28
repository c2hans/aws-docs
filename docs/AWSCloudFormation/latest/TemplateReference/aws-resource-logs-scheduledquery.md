---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-scheduledquery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::ScheduledQuery
<a name="aws-resource-logs-scheduledquery"></a>

Creates a scheduled query that runs CloudWatch Logs Insights queries at regular intervals. Scheduled queries enable proactive monitoring by automatically executing queries to detect patterns and anomalies in your log data. Query results can be delivered to Amazon S3 for analysis or further processing.

## Syntax
<a name="aws-resource-logs-scheduledquery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-logs-scheduledquery-syntax.json"></a>

```
{
  "Type" : "AWS::Logs::ScheduledQuery",
  "Properties" : {
      "[Description](#cfn-logs-scheduledquery-description)" : {{String}},
      "[DestinationConfiguration](#cfn-logs-scheduledquery-destinationconfiguration)" : {{DestinationConfiguration}},
      "[ExecutionRoleArn](#cfn-logs-scheduledquery-executionrolearn)" : {{String}},
      "[LogGroupIdentifiers](#cfn-logs-scheduledquery-loggroupidentifiers)" : {{[ String, ... ]}},
      "[Name](#cfn-logs-scheduledquery-name)" : {{String}},
      "[QueryLanguage](#cfn-logs-scheduledquery-querylanguage)" : {{String}},
      "[QueryString](#cfn-logs-scheduledquery-querystring)" : {{String}},
      "[ScheduleEndTime](#cfn-logs-scheduledquery-scheduleendtime)" : {{Number}},
      "[ScheduleExpression](#cfn-logs-scheduledquery-scheduleexpression)" : {{String}},
      "[ScheduleStartTime](#cfn-logs-scheduledquery-schedulestarttime)" : {{Number}},
      "[StartTimeOffset](#cfn-logs-scheduledquery-starttimeoffset)" : {{Integer}},
      "[State](#cfn-logs-scheduledquery-state)" : {{String}},
      "[Tags](#cfn-logs-scheduledquery-tags)" : {{[ TagsItems, ... ]}},
      "[Timezone](#cfn-logs-scheduledquery-timezone)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-logs-scheduledquery-syntax.yaml"></a>

```
Type: AWS::Logs::ScheduledQuery
Properties:
  [Description](#cfn-logs-scheduledquery-description): {{String}}
  [DestinationConfiguration](#cfn-logs-scheduledquery-destinationconfiguration): {{
    DestinationConfiguration}}
  [ExecutionRoleArn](#cfn-logs-scheduledquery-executionrolearn): {{String}}
  [LogGroupIdentifiers](#cfn-logs-scheduledquery-loggroupidentifiers): {{
    - String}}
  [Name](#cfn-logs-scheduledquery-name): {{String}}
  [QueryLanguage](#cfn-logs-scheduledquery-querylanguage): {{String}}
  [QueryString](#cfn-logs-scheduledquery-querystring): {{
    String}}
  [ScheduleEndTime](#cfn-logs-scheduledquery-scheduleendtime): {{Number}}
  [ScheduleExpression](#cfn-logs-scheduledquery-scheduleexpression): {{String}}
  [ScheduleStartTime](#cfn-logs-scheduledquery-schedulestarttime): {{Number}}
  [StartTimeOffset](#cfn-logs-scheduledquery-starttimeoffset): {{Integer}}
  [State](#cfn-logs-scheduledquery-state): {{String}}
  [Tags](#cfn-logs-scheduledquery-tags): {{
    - TagsItems}}
  [Timezone](#cfn-logs-scheduledquery-timezone): {{String}}
```

## Properties
<a name="aws-resource-logs-scheduledquery-properties"></a>

`Description`  <a name="cfn-logs-scheduledquery-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationConfiguration`  <a name="cfn-logs-scheduledquery-destinationconfiguration"></a>
Configuration for where query results are delivered.
*Required*: No
*Type*: [DestinationConfiguration](aws-properties-logs-scheduledquery-destinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleArn`  <a name="cfn-logs-scheduledquery-executionrolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroupIdentifiers`  <a name="cfn-logs-scheduledquery-loggroupidentifiers"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-logs-scheduledquery-name"></a>
The name of the scheduled query.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-/.#]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QueryLanguage`  <a name="cfn-logs-scheduledquery-querylanguage"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryString`  <a name="cfn-logs-scheduledquery-querystring"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleEndTime`  <a name="cfn-logs-scheduledquery-scheduleendtime"></a>
Property description not available.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleExpression`  <a name="cfn-logs-scheduledquery-scheduleexpression"></a>
The cron expression that defines when the scheduled query runs.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleStartTime`  <a name="cfn-logs-scheduledquery-schedulestarttime"></a>
Property description not available.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTimeOffset`  <a name="cfn-logs-scheduledquery-starttimeoffset"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-logs-scheduledquery-state"></a>
The current state of the scheduled query.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-logs-scheduledquery-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-logs-scheduledquery-tagsitems.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timezone`  <a name="cfn-logs-scheduledquery-timezone"></a>
The timezone used for evaluating the schedule expression.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-logs-scheduledquery-return-values"></a>

### Ref
<a name="aws-resource-logs-scheduledquery-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-logs-scheduledquery-return-values-fn--getatt"></a>

####
<a name="aws-resource-logs-scheduledquery-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The timestamp when the scheduled query was created.

`LastExecutionStatus`  <a name="LastExecutionStatus-fn::getatt"></a>
The status of the most recent execution.

`LastTriggeredTime`  <a name="LastTriggeredTime-fn::getatt"></a>
The timestamp when the scheduled query was last executed.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The timestamp when the scheduled query was last updated.

`ScheduledQueryArn`  <a name="ScheduledQueryArn-fn::getatt"></a>
The ARN of the scheduled query.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
