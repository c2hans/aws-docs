---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-pipetargetcloudwatchlogsparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe PipeTargetCloudWatchLogsParameters
<a name="aws-properties-pipes-pipe-pipetargetcloudwatchlogsparameters"></a>

The parameters for using an CloudWatch Logs log stream as a target.

## Syntax
<a name="aws-properties-pipes-pipe-pipetargetcloudwatchlogsparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-pipetargetcloudwatchlogsparameters-syntax.json"></a>

```
{
  "[LogStreamName](#cfn-pipes-pipe-pipetargetcloudwatchlogsparameters-logstreamname)" : {{String}},
  "[Timestamp](#cfn-pipes-pipe-pipetargetcloudwatchlogsparameters-timestamp)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-pipetargetcloudwatchlogsparameters-syntax.yaml"></a>

```
  [LogStreamName](#cfn-pipes-pipe-pipetargetcloudwatchlogsparameters-logstreamname): {{String}}
  [Timestamp](#cfn-pipes-pipe-pipetargetcloudwatchlogsparameters-timestamp): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-pipetargetcloudwatchlogsparameters-properties"></a>

`LogStreamName`  <a name="cfn-pipes-pipe-pipetargetcloudwatchlogsparameters-logstreamname"></a>
The name of the log stream.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timestamp`  <a name="cfn-pipes-pipe-pipetargetcloudwatchlogsparameters-timestamp"></a>
A [ dynamic path parameter](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html) to a field in the payload containing the time the event occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
The value cannot be a static timestamp as the provided timestamp would be applied to all events delivered by the Pipe, regardless of when they are actually delivered.
If no dynamic path parameter is provided, the default value is the time the invocation is processed by the Pipe.
*Required*: No
*Type*: String
*Pattern*: `^\$(\.[\w_-]+(\[(\d+|\*)\])*)*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
