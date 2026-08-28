---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-logdeliveryconfiguration-logconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::LogDeliveryConfiguration LogConfiguration
<a name="aws-properties-cognito-logdeliveryconfiguration-logconfiguration"></a>

The configuration of user event logs to an external AWS service like Amazon Data Firehose, Amazon S3, or Amazon CloudWatch Logs.

## Syntax
<a name="aws-properties-cognito-logdeliveryconfiguration-logconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-logdeliveryconfiguration-logconfiguration-syntax.json"></a>

```
{
  "[CloudWatchLogsConfiguration](#cfn-cognito-logdeliveryconfiguration-logconfiguration-cloudwatchlogsconfiguration)" : {{CloudWatchLogsConfiguration}},
  "[EventSource](#cfn-cognito-logdeliveryconfiguration-logconfiguration-eventsource)" : {{String}},
  "[FirehoseConfiguration](#cfn-cognito-logdeliveryconfiguration-logconfiguration-firehoseconfiguration)" : {{FirehoseConfiguration}},
  "[LogLevel](#cfn-cognito-logdeliveryconfiguration-logconfiguration-loglevel)" : {{String}},
  "[S3Configuration](#cfn-cognito-logdeliveryconfiguration-logconfiguration-s3configuration)" : {{S3Configuration}}
}
```

### YAML
<a name="aws-properties-cognito-logdeliveryconfiguration-logconfiguration-syntax.yaml"></a>

```
  [CloudWatchLogsConfiguration](#cfn-cognito-logdeliveryconfiguration-logconfiguration-cloudwatchlogsconfiguration): {{
    CloudWatchLogsConfiguration}}
  [EventSource](#cfn-cognito-logdeliveryconfiguration-logconfiguration-eventsource): {{String}}
  [FirehoseConfiguration](#cfn-cognito-logdeliveryconfiguration-logconfiguration-firehoseconfiguration): {{
    FirehoseConfiguration}}
  [LogLevel](#cfn-cognito-logdeliveryconfiguration-logconfiguration-loglevel): {{String}}
  [S3Configuration](#cfn-cognito-logdeliveryconfiguration-logconfiguration-s3configuration): {{
    S3Configuration}}
```

## Properties
<a name="aws-properties-cognito-logdeliveryconfiguration-logconfiguration-properties"></a>

`CloudWatchLogsConfiguration`  <a name="cfn-cognito-logdeliveryconfiguration-logconfiguration-cloudwatchlogsconfiguration"></a>
Configuration for the CloudWatch log group destination of user pool detailed activity logging, or of user activity log export with advanced security features.
*Required*: No
*Type*: [CloudWatchLogsConfiguration](aws-properties-cognito-logdeliveryconfiguration-cloudwatchlogsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventSource`  <a name="cfn-cognito-logdeliveryconfiguration-logconfiguration-eventsource"></a>
The source of events that your user pool sends for logging. To send error-level logs about user notification activity, set to `userNotification`. To send info-level logs about threat-protection user activity in user pools with the Plus feature plan, set to `userAuthEvents`.
*Required*: No
*Type*: String
*Allowed values*: `userNotification | userAuthEvents`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirehoseConfiguration`  <a name="cfn-cognito-logdeliveryconfiguration-logconfiguration-firehoseconfiguration"></a>
Configuration for the Amazon Data Firehose stream destination of user activity log export with threat protection.
*Required*: No
*Type*: [FirehoseConfiguration](aws-properties-cognito-logdeliveryconfiguration-firehoseconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogLevel`  <a name="cfn-cognito-logdeliveryconfiguration-logconfiguration-loglevel"></a>
The `errorlevel` selection of logs that a user pool sends for detailed activity logging. To send `userNotification` activity with [information about message delivery](https://docs.aws.amazon.com/cognito/latest/developerguide/exporting-quotas-and-usage.html), choose `ERROR` with `CloudWatchLogsConfiguration`. To send `userAuthEvents` activity with user logs from threat protection with the Plus feature plan, choose `INFO` with one of `CloudWatchLogsConfiguration`, `FirehoseConfiguration`, or `S3Configuration`.
*Required*: No
*Type*: String
*Allowed values*: `ERROR | INFO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Configuration`  <a name="cfn-cognito-logdeliveryconfiguration-logconfiguration-s3configuration"></a>
Configuration for the Amazon S3 bucket destination of user activity log export with threat protection.
*Required*: No
*Type*: [S3Configuration](aws-properties-cognito-logdeliveryconfiguration-s3configuration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
