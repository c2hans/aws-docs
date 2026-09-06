---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-archivecontainersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel ArchiveContainerSettings
<a name="aws-properties-medialive-channel-archivecontainersettings"></a>

The archive container settings.

The parent of this entity is ArchiveOutputSettings.

## Syntax
<a name="aws-properties-medialive-channel-archivecontainersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-archivecontainersettings-syntax.json"></a>

```
{
  "[M2tsSettings](#cfn-medialive-channel-archivecontainersettings-m2tssettings)" : {{M2tsSettings}},
  "[RawSettings](#cfn-medialive-channel-archivecontainersettings-rawsettings)" : {{Json}}
}
```

### YAML
<a name="aws-properties-medialive-channel-archivecontainersettings-syntax.yaml"></a>

```
  [M2tsSettings](#cfn-medialive-channel-archivecontainersettings-m2tssettings): {{
    M2tsSettings}}
  [RawSettings](#cfn-medialive-channel-archivecontainersettings-rawsettings): {{Json}}
```

## Properties
<a name="aws-properties-medialive-channel-archivecontainersettings-properties"></a>

`M2tsSettings`  <a name="cfn-medialive-channel-archivecontainersettings-m2tssettings"></a>
The settings for the M2TS in the archive output.
*Required*: No
*Type*: [M2tsSettings](aws-properties-medialive-channel-m2tssettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RawSettings`  <a name="cfn-medialive-channel-archivecontainersettings-rawsettings"></a>
The settings for Raw archive output type.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
