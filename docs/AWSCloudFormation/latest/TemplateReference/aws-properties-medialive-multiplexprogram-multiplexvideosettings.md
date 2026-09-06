---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-multiplexprogram-multiplexvideosettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Multiplexprogram MultiplexVideoSettings
<a name="aws-properties-medialive-multiplexprogram-multiplexvideosettings"></a>

The video configuration for each program in a multiplex.

## Syntax
<a name="aws-properties-medialive-multiplexprogram-multiplexvideosettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-multiplexprogram-multiplexvideosettings-syntax.json"></a>

```
{
  "[ConstantBitrate](#cfn-medialive-multiplexprogram-multiplexvideosettings-constantbitrate)" : {{Integer}},
  "[StatmuxSettings](#cfn-medialive-multiplexprogram-multiplexvideosettings-statmuxsettings)" : {{MultiplexStatmuxVideoSettings}}
}
```

### YAML
<a name="aws-properties-medialive-multiplexprogram-multiplexvideosettings-syntax.yaml"></a>

```
  [ConstantBitrate](#cfn-medialive-multiplexprogram-multiplexvideosettings-constantbitrate): {{Integer}}
  [StatmuxSettings](#cfn-medialive-multiplexprogram-multiplexvideosettings-statmuxsettings): {{
    MultiplexStatmuxVideoSettings}}
```

## Properties
<a name="aws-properties-medialive-multiplexprogram-multiplexvideosettings-properties"></a>

`ConstantBitrate`  <a name="cfn-medialive-multiplexprogram-multiplexvideosettings-constantbitrate"></a>
The constant bitrate configuration for the video encode. When this field is defined, StatmuxSettings must be undefined.
*Required*: No
*Type*: Integer
*Minimum*: `100000`
*Maximum*: `100000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatmuxSettings`  <a name="cfn-medialive-multiplexprogram-multiplexvideosettings-statmuxsettings"></a>
Statmux rate control settings. When this field is defined, ConstantBitrate must be undefined.
*Required*: No
*Type*: [MultiplexStatmuxVideoSettings](aws-properties-medialive-multiplexprogram-multiplexstatmuxvideosettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
