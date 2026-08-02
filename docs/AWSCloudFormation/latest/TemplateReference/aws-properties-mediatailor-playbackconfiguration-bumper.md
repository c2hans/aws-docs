---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-bumper.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration Bumper
<a name="aws-properties-mediatailor-playbackconfiguration-bumper"></a>

The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see [Bumpers](https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html).

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-bumper-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-bumper-syntax.json"></a>

```
{
  "[EndUrl](#cfn-mediatailor-playbackconfiguration-bumper-endurl)" : {{String}},
  "[StartUrl](#cfn-mediatailor-playbackconfiguration-bumper-starturl)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-bumper-syntax.yaml"></a>

```
  [EndUrl](#cfn-mediatailor-playbackconfiguration-bumper-endurl): {{String}}
  [StartUrl](#cfn-mediatailor-playbackconfiguration-bumper-starturl): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-bumper-properties"></a>

`EndUrl`  <a name="cfn-mediatailor-playbackconfiguration-bumper-endurl"></a>
The URL for the end bumper asset.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartUrl`  <a name="cfn-mediatailor-playbackconfiguration-bumper-starturl"></a>
The URL for the start bumper asset.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
