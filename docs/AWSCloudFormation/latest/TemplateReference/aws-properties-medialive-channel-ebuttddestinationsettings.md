---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-ebuttddestinationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel EbuTtDDestinationSettings
<a name="aws-properties-medialive-channel-ebuttddestinationsettings"></a>

Settings for EBU-TT captions in the output.

The parent of this entity is CaptionDestinationSettings.

## Syntax
<a name="aws-properties-medialive-channel-ebuttddestinationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-ebuttddestinationsettings-syntax.json"></a>

```
{
  "[CopyrightHolder](#cfn-medialive-channel-ebuttddestinationsettings-copyrightholder)" : {{String}},
  "[DefaultFontSize](#cfn-medialive-channel-ebuttddestinationsettings-defaultfontsize)" : {{Integer}},
  "[DefaultLineHeight](#cfn-medialive-channel-ebuttddestinationsettings-defaultlineheight)" : {{Integer}},
  "[FillLineGap](#cfn-medialive-channel-ebuttddestinationsettings-filllinegap)" : {{String}},
  "[FontFamily](#cfn-medialive-channel-ebuttddestinationsettings-fontfamily)" : {{String}},
  "[StyleControl](#cfn-medialive-channel-ebuttddestinationsettings-stylecontrol)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-ebuttddestinationsettings-syntax.yaml"></a>

```
  [CopyrightHolder](#cfn-medialive-channel-ebuttddestinationsettings-copyrightholder): {{String}}
  [DefaultFontSize](#cfn-medialive-channel-ebuttddestinationsettings-defaultfontsize): {{Integer}}
  [DefaultLineHeight](#cfn-medialive-channel-ebuttddestinationsettings-defaultlineheight): {{Integer}}
  [FillLineGap](#cfn-medialive-channel-ebuttddestinationsettings-filllinegap): {{String}}
  [FontFamily](#cfn-medialive-channel-ebuttddestinationsettings-fontfamily): {{String}}
  [StyleControl](#cfn-medialive-channel-ebuttddestinationsettings-stylecontrol): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-ebuttddestinationsettings-properties"></a>

`CopyrightHolder`  <a name="cfn-medialive-channel-ebuttddestinationsettings-copyrightholder"></a>
Applies only if you plan to convert these source captions to EBU-TT-D or TTML in an output. Complete this field if you want to include the name of the copyright holder in the copyright metadata tag in the TTML
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultFontSize`  <a name="cfn-medialive-channel-ebuttddestinationsettings-defaultfontsize"></a>
Specifies the default font size as a percentage of the computed cell size. Valid only if the default line height is also set. If you leave this field empty, the default font size is 80% of the cell size.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultLineHeight`  <a name="cfn-medialive-channel-ebuttddestinationsettings-defaultlineheight"></a>
Specifies the default line height as a percentage of the computed cell size.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FillLineGap`  <a name="cfn-medialive-channel-ebuttddestinationsettings-filllinegap"></a>
Specifies how to handle the gap between the lines (in multi-line captions). - enabled: Fill with the captions background color (as specified in the input captions). - disabled: Leave the gap unfilled.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FontFamily`  <a name="cfn-medialive-channel-ebuttddestinationsettings-fontfamily"></a>
Specifies the font family to include in the font data attached to the EBU-TT captions. Valid only if styleControl is set to include. If you leave this field empty, the font family is set to "monospaced". (If styleControl is set to exclude, the font family is always set to "monospaced".) You specify only the font family. All other style information (color, bold, position and so on) is copied from the input captions. The size is always set to 100% to allow the downstream player to choose the size. - Enter a list of font families, as a comma-separated list of font names, in order of preference. The name can be a font family (such as “Arial”), or a generic font family (such as “serif”), or “default” (to let the downstream player choose the font). - Leave blank to set the family to “monospace”.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StyleControl`  <a name="cfn-medialive-channel-ebuttddestinationsettings-stylecontrol"></a>
Specifies the style information (font color, font position, and so on) to include in the font data that is attached to the EBU-TT captions. - include: Take the style information (font color, font position, and so on) from the source captions and include that information in the font data attached to the EBU-TT captions. This option is valid only if the source captions are Embedded or Teletext. - exclude: In the font data attached to the EBU-TT captions, set the font family to "monospaced". Do not include any other style information.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
