---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-channel-channellogginginfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Channel ChannelLoggingInfo
<a name="aws-properties-msk-channel-channellogginginfo"></a>

<a name="aws-properties-msk-channel-channellogginginfo-description"></a>The `ChannelLoggingInfo` property type specifies Property description not available. for an [AWS::MSK::Channel](aws-resource-msk-channel.md).

## Syntax
<a name="aws-properties-msk-channel-channellogginginfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-channel-channellogginginfo-syntax.json"></a>

```
{
  "[CloudWatchLogs](#cfn-msk-channel-channellogginginfo-cloudwatchlogs)" : {{CloudWatchLogsLogDestination}},
  "[Firehose](#cfn-msk-channel-channellogginginfo-firehose)" : {{FirehoseLogDestination}},
  "[S3](#cfn-msk-channel-channellogginginfo-s3)" : {{S3LogDestination}}
}
```

### YAML
<a name="aws-properties-msk-channel-channellogginginfo-syntax.yaml"></a>

```
  [CloudWatchLogs](#cfn-msk-channel-channellogginginfo-cloudwatchlogs): {{
    CloudWatchLogsLogDestination}}
  [Firehose](#cfn-msk-channel-channellogginginfo-firehose): {{
    FirehoseLogDestination}}
  [S3](#cfn-msk-channel-channellogginginfo-s3): {{
    S3LogDestination}}
```

## Properties
<a name="aws-properties-msk-channel-channellogginginfo-properties"></a>

`CloudWatchLogs`  <a name="cfn-msk-channel-channellogginginfo-cloudwatchlogs"></a>
Property description not available.
*Required*: No
*Type*: [CloudWatchLogsLogDestination](aws-properties-msk-channel-cloudwatchlogslogdestination.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Firehose`  <a name="cfn-msk-channel-channellogginginfo-firehose"></a>
Property description not available.
*Required*: No
*Type*: [FirehoseLogDestination](aws-properties-msk-channel-firehoselogdestination.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3`  <a name="cfn-msk-channel-channellogginginfo-s3"></a>
Property description not available.
*Required*: No
*Type*: [S3LogDestination](aws-properties-msk-channel-s3logdestination.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
