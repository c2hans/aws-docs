---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-videopositionrectangle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel VideoPositionRectangle
<a name="aws-properties-medialive-channel-videopositionrectangle"></a>

A rectangle defined by a position (x, y) and dimensions (width, height), in pixels.

## Syntax
<a name="aws-properties-medialive-channel-videopositionrectangle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-videopositionrectangle-syntax.json"></a>

```
{
  "[Height](#cfn-medialive-channel-videopositionrectangle-height)" : {{Integer}},
  "[Width](#cfn-medialive-channel-videopositionrectangle-width)" : {{Integer}},
  "[X](#cfn-medialive-channel-videopositionrectangle-x)" : {{Integer}},
  "[Y](#cfn-medialive-channel-videopositionrectangle-y)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-videopositionrectangle-syntax.yaml"></a>

```
  [Height](#cfn-medialive-channel-videopositionrectangle-height): {{Integer}}
  [Width](#cfn-medialive-channel-videopositionrectangle-width): {{Integer}}
  [X](#cfn-medialive-channel-videopositionrectangle-x): {{Integer}}
  [Y](#cfn-medialive-channel-videopositionrectangle-y): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-videopositionrectangle-properties"></a>

`Height`  <a name="cfn-medialive-channel-videopositionrectangle-height"></a>
The height of the rectangle, in pixels. Must be an even number.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Width`  <a name="cfn-medialive-channel-videopositionrectangle-width"></a>
The width of the rectangle, in pixels. Must be an even number.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`X`  <a name="cfn-medialive-channel-videopositionrectangle-x"></a>
The offset of the left edge of the rectangle, in pixels. Must be an even number.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Y`  <a name="cfn-medialive-channel-videopositionrectangle-y"></a>
The offset of the top edge of the rectangle, in pixels. Must be an even number.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
