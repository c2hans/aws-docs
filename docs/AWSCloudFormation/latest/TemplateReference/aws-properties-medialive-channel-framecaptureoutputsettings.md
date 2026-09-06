---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-framecaptureoutputsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel FrameCaptureOutputSettings
<a name="aws-properties-medialive-channel-framecaptureoutputsettings"></a>

The frame capture output settings.

The parent of this entity is OutputSettings.

## Syntax
<a name="aws-properties-medialive-channel-framecaptureoutputsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-framecaptureoutputsettings-syntax.json"></a>

```
{
  "[NameModifier](#cfn-medialive-channel-framecaptureoutputsettings-namemodifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-framecaptureoutputsettings-syntax.yaml"></a>

```
  [NameModifier](#cfn-medialive-channel-framecaptureoutputsettings-namemodifier): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-framecaptureoutputsettings-properties"></a>

`NameModifier`  <a name="cfn-medialive-channel-framecaptureoutputsettings-namemodifier"></a>
Required if the output group contains more than one output. This modifier forms part of the output file name.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
