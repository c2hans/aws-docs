---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-textcaptionpositionsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel TextCaptionPositionSettings
<a name="aws-properties-medialive-channel-textcaptionpositionsettings"></a>

Specifies the position of TTML or WebVTT output captions when `styleControl` is set to `MANUAL`, as a percentage from the top of the output.

## Syntax
<a name="aws-properties-medialive-channel-textcaptionpositionsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-textcaptionpositionsettings-syntax.json"></a>

```
{
  "[YPositionPercentage](#cfn-medialive-channel-textcaptionpositionsettings-ypositionpercentage)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-textcaptionpositionsettings-syntax.yaml"></a>

```
  [YPositionPercentage](#cfn-medialive-channel-textcaptionpositionsettings-ypositionpercentage): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-textcaptionpositionsettings-properties"></a>

`YPositionPercentage`  <a name="cfn-medialive-channel-textcaptionpositionsettings-ypositionpercentage"></a>
Specifies the vertical position of the top edge of the caption relative to the top of the output as a percentage. A value of 0 places the caption at the top of the output and 100 at the bottom.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
