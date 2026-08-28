---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-pipelogconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe PipeLogConfiguration
<a name="aws-properties-pipes-pipe-pipelogconfiguration"></a>

Represents the configuration settings for the logs to which this pipe should report events.

## Syntax
<a name="aws-properties-pipes-pipe-pipelogconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-pipelogconfiguration-syntax.json"></a>

```
{
  "[CloudwatchLogsLogDestination](#cfn-pipes-pipe-pipelogconfiguration-cloudwatchlogslogdestination)" : {{CloudwatchLogsLogDestination}},
  "[FirehoseLogDestination](#cfn-pipes-pipe-pipelogconfiguration-firehoselogdestination)" : {{FirehoseLogDestination}},
  "[IncludeExecutionData](#cfn-pipes-pipe-pipelogconfiguration-includeexecutiondata)" : {{[ String, ... ]}},
  "[Level](#cfn-pipes-pipe-pipelogconfiguration-level)" : {{String}},
  "[S3LogDestination](#cfn-pipes-pipe-pipelogconfiguration-s3logdestination)" : {{S3LogDestination}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-pipelogconfiguration-syntax.yaml"></a>

```
  [CloudwatchLogsLogDestination](#cfn-pipes-pipe-pipelogconfiguration-cloudwatchlogslogdestination): {{
    CloudwatchLogsLogDestination}}
  [FirehoseLogDestination](#cfn-pipes-pipe-pipelogconfiguration-firehoselogdestination): {{
    FirehoseLogDestination}}
  [IncludeExecutionData](#cfn-pipes-pipe-pipelogconfiguration-includeexecutiondata): {{
    - String}}
  [Level](#cfn-pipes-pipe-pipelogconfiguration-level): {{String}}
  [S3LogDestination](#cfn-pipes-pipe-pipelogconfiguration-s3logdestination): {{
    S3LogDestination}}
```

## Properties
<a name="aws-properties-pipes-pipe-pipelogconfiguration-properties"></a>

`CloudwatchLogsLogDestination`  <a name="cfn-pipes-pipe-pipelogconfiguration-cloudwatchlogslogdestination"></a>
The logging configuration settings for the pipe.
*Required*: No
*Type*: [CloudwatchLogsLogDestination](aws-properties-pipes-pipe-cloudwatchlogslogdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirehoseLogDestination`  <a name="cfn-pipes-pipe-pipelogconfiguration-firehoselogdestination"></a>
The Amazon Data Firehose logging configuration settings for the pipe.
*Required*: No
*Type*: [FirehoseLogDestination](aws-properties-pipes-pipe-firehoselogdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeExecutionData`  <a name="cfn-pipes-pipe-pipelogconfiguration-includeexecutiondata"></a>
Whether the execution data (specifically, the `payload`, `awsRequest`, and `awsResponse` fields) is included in the log messages for this pipe.
This applies to all log destinations for the pipe.
For more information, see [Including execution data in logs](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs.html#eb-pipes-logs-execution-data) in the *Amazon EventBridge User Guide*.
 *Allowed values:* `ALL`
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Level`  <a name="cfn-pipes-pipe-pipelogconfiguration-level"></a>
The level of logging detail to include. This applies to all log destinations for the pipe.
*Required*: No
*Type*: String
*Allowed values*: `OFF | ERROR | INFO | TRACE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3LogDestination`  <a name="cfn-pipes-pipe-pipelogconfiguration-s3logdestination"></a>
The Amazon S3 logging configuration settings for the pipe.
*Required*: No
*Type*: [S3LogDestination](aws-properties-pipes-pipe-s3logdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
