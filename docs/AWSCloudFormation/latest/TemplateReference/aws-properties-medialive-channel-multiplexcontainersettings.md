---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-multiplexcontainersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MultiplexContainerSettings
<a name="aws-properties-medialive-channel-multiplexcontainersettings"></a>

Multiplex container settings.

The parent of this entity is MultiplexOutputSettings.

## Syntax
<a name="aws-properties-medialive-channel-multiplexcontainersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-multiplexcontainersettings-syntax.json"></a>

```
{
  "[MultiplexM2tsSettings](#cfn-medialive-channel-multiplexcontainersettings-multiplexm2tssettings)" : {{MultiplexM2tsSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-multiplexcontainersettings-syntax.yaml"></a>

```
  [MultiplexM2tsSettings](#cfn-medialive-channel-multiplexcontainersettings-multiplexm2tssettings): {{
    MultiplexM2tsSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-multiplexcontainersettings-properties"></a>

`MultiplexM2tsSettings`  <a name="cfn-medialive-channel-multiplexcontainersettings-multiplexm2tssettings"></a>
Multiplex M2TS settings for the container.
*Required*: No
*Type*: [MultiplexM2tsSettings](aws-properties-medialive-channel-multiplexm2tssettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
