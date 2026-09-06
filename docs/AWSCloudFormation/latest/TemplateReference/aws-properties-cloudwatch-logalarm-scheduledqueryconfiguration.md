---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-logalarm-scheduledqueryconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::LogAlarm ScheduledQueryConfiguration
<a name="aws-properties-cloudwatch-logalarm-scheduledqueryconfiguration"></a>

The configuration of the underlying CloudWatch Logs scheduled query that this alarm evaluates, including the query string, log groups, schedule, and aggregation expression.

## Syntax
<a name="aws-properties-cloudwatch-logalarm-scheduledqueryconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-logalarm-scheduledqueryconfiguration-syntax.json"></a>

```
{
  "[AggregationExpression](#cfn-cloudwatch-logalarm-scheduledqueryconfiguration-aggregationexpression)" : {{String}},
  "[LogGroupIdentifiers](#cfn-cloudwatch-logalarm-scheduledqueryconfiguration-loggroupidentifiers)" : {{[ String, ... ]}},
  "[QueryString](#cfn-cloudwatch-logalarm-scheduledqueryconfiguration-querystring)" : {{String}},
  "[ScheduleConfiguration](#cfn-cloudwatch-logalarm-scheduledqueryconfiguration-scheduleconfiguration)" : {{ScheduleConfiguration}},
  "[ScheduledQueryRoleARN](#cfn-cloudwatch-logalarm-scheduledqueryconfiguration-scheduledqueryrolearn)" : {{String}},
  "[Tags](#cfn-cloudwatch-logalarm-scheduledqueryconfiguration-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudwatch-logalarm-scheduledqueryconfiguration-syntax.yaml"></a>

```
  [AggregationExpression](#cfn-cloudwatch-logalarm-scheduledqueryconfiguration-aggregationexpression): {{String}}
  [LogGroupIdentifiers](#cfn-cloudwatch-logalarm-scheduledqueryconfiguration-loggroupidentifiers): {{
    - String}}
  [QueryString](#cfn-cloudwatch-logalarm-scheduledqueryconfiguration-querystring): {{
    String}}
  [ScheduleConfiguration](#cfn-cloudwatch-logalarm-scheduledqueryconfiguration-scheduleconfiguration): {{
    ScheduleConfiguration}}
  [ScheduledQueryRoleARN](#cfn-cloudwatch-logalarm-scheduledqueryconfiguration-scheduledqueryrolearn): {{String}}
  [Tags](#cfn-cloudwatch-logalarm-scheduledqueryconfiguration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-cloudwatch-logalarm-scheduledqueryconfiguration-properties"></a>

`AggregationExpression`  <a name="cfn-cloudwatch-logalarm-scheduledqueryconfiguration-aggregationexpression"></a>
The expression that defines how to aggregate query results into one or more scalar values for alarm evaluation. For example, `count(*)` or `avg(latency) by host | sort desc`. Length constraints: minimum 1 character, maximum 2048 characters.
*Required*: Yes
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroupIdentifiers`  <a name="cfn-cloudwatch-logalarm-scheduledqueryconfiguration-loggroupidentifiers"></a>
The log groups to query. Each entry can be a log group name or ARN. Use the ARN form when querying log groups in a different account (for example, when running cross-account queries from a monitoring account). The list must contain between 1 and 50 entries.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryString`  <a name="cfn-cloudwatch-logalarm-scheduledqueryconfiguration-querystring"></a>
The CloudWatch Logs query to execute on each scheduled run. Length constraints: maximum of 10,000 characters.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleConfiguration`  <a name="cfn-cloudwatch-logalarm-scheduledqueryconfiguration-scheduleconfiguration"></a>
The schedule and time-range offset configuration for the underlying scheduled query.
*Required*: Yes
*Type*: [ScheduleConfiguration](aws-properties-cloudwatch-logalarm-scheduleconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduledQueryRoleARN`  <a name="cfn-cloudwatch-logalarm-scheduledqueryconfiguration-scheduledqueryrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that CloudWatch assumes when executing the scheduled query against the configured log groups.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudwatch-logalarm-scheduledqueryconfiguration-tags"></a>
A list of key-value pairs to associate with the underlying scheduled query resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-logalarm-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
