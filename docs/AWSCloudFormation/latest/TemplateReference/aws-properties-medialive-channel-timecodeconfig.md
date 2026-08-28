---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-timecodeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel TimecodeConfig
<a name="aws-properties-medialive-channel-timecodeconfig"></a>

The configuration of the timecode in the output.

The parent of this entity is EncoderSettings.

## Syntax
<a name="aws-properties-medialive-channel-timecodeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-timecodeconfig-syntax.json"></a>

```
{
  "[Source](#cfn-medialive-channel-timecodeconfig-source)" : {{String}},
  "[SyncThreshold](#cfn-medialive-channel-timecodeconfig-syncthreshold)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-timecodeconfig-syntax.yaml"></a>

```
  [Source](#cfn-medialive-channel-timecodeconfig-source): {{String}}
  [SyncThreshold](#cfn-medialive-channel-timecodeconfig-syncthreshold): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-timecodeconfig-properties"></a>

`Source`  <a name="cfn-medialive-channel-timecodeconfig-source"></a>
Identifies the source for the timecode that will be associated with the channel outputs. Embedded (embedded): Initialize the output timecode with timecode from the source. If no embedded timecode is detected in the source, the system falls back to using "Start at 0" (zerobased). System Clock (systemclock): Use the UTC time. Start at 0 (zerobased): The time of the first frame of the channel will be 00:00:00:00.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SyncThreshold`  <a name="cfn-medialive-channel-timecodeconfig-syncthreshold"></a>
The threshold in frames beyond which output timecode is resynchronized to the input timecode. Discrepancies below this threshold are permitted to avoid unnecessary discontinuities in the output timecode. There is no timecode sync when this is not specified.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
