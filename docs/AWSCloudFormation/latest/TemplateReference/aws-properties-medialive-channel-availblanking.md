---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-availblanking.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AvailBlanking
<a name="aws-properties-medialive-channel-availblanking"></a>

The configuration of ad avail blanking in the output.

The parent of this entity is EncoderSettings.

## Syntax
<a name="aws-properties-medialive-channel-availblanking-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-availblanking-syntax.json"></a>

```
{
  "[AvailBlankingImage](#cfn-medialive-channel-availblanking-availblankingimage)" : {{InputLocation}},
  "[State](#cfn-medialive-channel-availblanking-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-availblanking-syntax.yaml"></a>

```
  [AvailBlankingImage](#cfn-medialive-channel-availblanking-availblankingimage): {{
    InputLocation}}
  [State](#cfn-medialive-channel-availblanking-state): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-availblanking-properties"></a>

`AvailBlankingImage`  <a name="cfn-medialive-channel-availblanking-availblankingimage"></a>
The blanking image to be used. Keep empty for solid black. Only .bmp and .png images are supported.
*Required*: No
*Type*: [InputLocation](aws-properties-medialive-channel-inputlocation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-medialive-channel-availblanking-state"></a>
When set to enabled, the video, audio, and captions are blanked when insertion metadata is added.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
