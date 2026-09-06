---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-outputlockingsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel OutputLockingSettings
<a name="aws-properties-medialive-channel-outputlockingsettings"></a>

Advanced output locking settings.

## Syntax
<a name="aws-properties-medialive-channel-outputlockingsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-outputlockingsettings-syntax.json"></a>

```
{
  "[DisabledLockingSettings](#cfn-medialive-channel-outputlockingsettings-disabledlockingsettings)" : {{DisabledLockingSettings}},
  "[EpochLockingSettings](#cfn-medialive-channel-outputlockingsettings-epochlockingsettings)" : {{EpochLockingSettings}},
  "[PipelineLockingSettings](#cfn-medialive-channel-outputlockingsettings-pipelinelockingsettings)" : {{PipelineLockingSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-outputlockingsettings-syntax.yaml"></a>

```
  [DisabledLockingSettings](#cfn-medialive-channel-outputlockingsettings-disabledlockingsettings): {{
    DisabledLockingSettings}}
  [EpochLockingSettings](#cfn-medialive-channel-outputlockingsettings-epochlockingsettings): {{
    EpochLockingSettings}}
  [PipelineLockingSettings](#cfn-medialive-channel-outputlockingsettings-pipelinelockingsettings): {{
    PipelineLockingSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-outputlockingsettings-properties"></a>

`DisabledLockingSettings`  <a name="cfn-medialive-channel-outputlockingsettings-disabledlockingsettings"></a>
Disabled Locking Settings
*Required*: No
*Type*: [DisabledLockingSettings](aws-properties-medialive-channel-disabledlockingsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EpochLockingSettings`  <a name="cfn-medialive-channel-outputlockingsettings-epochlockingsettings"></a>
Epoch Locking Settings
*Required*: No
*Type*: [EpochLockingSettings](aws-properties-medialive-channel-epochlockingsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PipelineLockingSettings`  <a name="cfn-medialive-channel-outputlockingsettings-pipelinelockingsettings"></a>
Pipeline Locking Settings
*Required*: No
*Type*: [PipelineLockingSettings](aws-properties-medialive-channel-pipelinelockingsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
