---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-embeddedcaptionpositionsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel EmbeddedCaptionPositionSettings
<a name="aws-properties-medialive-channel-embeddedcaptionpositionsettings"></a>

Specifies the position of embedded output captions when `styleControl` is set to `MANUAL`, as a row counted from the top of the output.

## Syntax
<a name="aws-properties-medialive-channel-embeddedcaptionpositionsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-embeddedcaptionpositionsettings-syntax.json"></a>

```
{
  "[YPositionLine](#cfn-medialive-channel-embeddedcaptionpositionsettings-ypositionline)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-embeddedcaptionpositionsettings-syntax.yaml"></a>

```
  [YPositionLine](#cfn-medialive-channel-embeddedcaptionpositionsettings-ypositionline): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-embeddedcaptionpositionsettings-properties"></a>

`YPositionLine`  <a name="cfn-medialive-channel-embeddedcaptionpositionsettings-ypositionline"></a>
Specifies the vertical position of the caption as a row counted from the top of the output. Row 1 is the topmost row. Acceptable values are 1 through 15.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
