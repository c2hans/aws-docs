---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-colorcorrectionsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel ColorCorrectionSettings
<a name="aws-properties-medialive-channel-colorcorrectionsettings"></a>

Color correction settings.

The parent of this entity is EncoderSettings.

## Syntax
<a name="aws-properties-medialive-channel-colorcorrectionsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-colorcorrectionsettings-syntax.json"></a>

```
{
  "[GlobalColorCorrections](#cfn-medialive-channel-colorcorrectionsettings-globalcolorcorrections)" : {{[ ColorCorrection, ... ]}}
}
```

### YAML
<a name="aws-properties-medialive-channel-colorcorrectionsettings-syntax.yaml"></a>

```
  [GlobalColorCorrections](#cfn-medialive-channel-colorcorrectionsettings-globalcolorcorrections): {{
    - ColorCorrection}}
```

## Properties
<a name="aws-properties-medialive-channel-colorcorrectionsettings-properties"></a>

`GlobalColorCorrections`  <a name="cfn-medialive-channel-colorcorrectionsettings-globalcolorcorrections"></a>
Required. An array of color corrections that applies when you are using 3D LUT files to perform color conversion on video. Each color correction contains one 3D LUT file (that defines the color mapping for converting an input color space to an output color space), and the input/output combination that this 3D LUT file applies to. MediaLive reads the color space in the input metadata, determines the color space that you have specified for the output, and finds and uses the LUT file that applies to this combination.
*Required*: No
*Type*: Array of [ColorCorrection](aws-properties-medialive-channel-colorcorrection.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
