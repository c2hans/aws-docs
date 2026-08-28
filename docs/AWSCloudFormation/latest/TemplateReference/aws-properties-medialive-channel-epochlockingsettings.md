---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-epochlockingsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel EpochLockingSettings
<a name="aws-properties-medialive-channel-epochlockingsettings"></a>

Epoch Locking Settings

## Syntax
<a name="aws-properties-medialive-channel-epochlockingsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-epochlockingsettings-syntax.json"></a>

```
{
  "[CustomEpoch](#cfn-medialive-channel-epochlockingsettings-customepoch)" : {{String}},
  "[JamSyncTime](#cfn-medialive-channel-epochlockingsettings-jamsynctime)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-epochlockingsettings-syntax.yaml"></a>

```
  [CustomEpoch](#cfn-medialive-channel-epochlockingsettings-customepoch): {{String}}
  [JamSyncTime](#cfn-medialive-channel-epochlockingsettings-jamsynctime): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-epochlockingsettings-properties"></a>

`CustomEpoch`  <a name="cfn-medialive-channel-epochlockingsettings-customepoch"></a>
Optional. Enter a value here to use a custom epoch, instead of the standard epoch (which started at 1970-01-01T00:00:00 UTC). Specify the start time of the custom epoch, in YYYY-MM-DDTHH:MM:SS in UTC. The time must be 2000-01-01T00:00:00 or later. Always set the MM:SS portion to 00:00.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JamSyncTime`  <a name="cfn-medialive-channel-epochlockingsettings-jamsynctime"></a>
Optional. Enter a time for the jam sync. The default is midnight UTC. When epoch locking is enabled, MediaLive performs a daily jam sync on every output encode to ensure timecodes don't diverge from the wall clock. The jam sync applies only to encodes with frame rate of 29.97 or 59.94 FPS. To override, enter a time in HH:MM:SS in UTC. Always set the MM:SS portion to 00:00.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
