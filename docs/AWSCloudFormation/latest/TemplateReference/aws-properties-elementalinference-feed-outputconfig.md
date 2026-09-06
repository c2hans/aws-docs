---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elementalinference-feed-outputconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElementalInference::Feed OutputConfig
<a name="aws-properties-elementalinference-feed-outputconfig"></a>

Contains one output, of a specific type, that you want in this feed.

## Syntax
<a name="aws-properties-elementalinference-feed-outputconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elementalinference-feed-outputconfig-syntax.json"></a>

```
{
  "[Clipping](#cfn-elementalinference-feed-outputconfig-clipping)" : {{ClippingConfig}},
  "[Cropping](#cfn-elementalinference-feed-outputconfig-cropping)" : {{CroppingConfig}},
  "[Subtitling](#cfn-elementalinference-feed-outputconfig-subtitling)" : {{SubtitlingConfig}}
}
```

### YAML
<a name="aws-properties-elementalinference-feed-outputconfig-syntax.yaml"></a>

```
  [Clipping](#cfn-elementalinference-feed-outputconfig-clipping): {{
    ClippingConfig}}
  [Cropping](#cfn-elementalinference-feed-outputconfig-cropping): {{
    CroppingConfig}}
  [Subtitling](#cfn-elementalinference-feed-outputconfig-subtitling): {{
    SubtitlingConfig}}
```

## Properties
<a name="aws-properties-elementalinference-feed-outputconfig-properties"></a>

`Clipping`  <a name="cfn-elementalinference-feed-outputconfig-clipping"></a>
Specifies that this is a clipping output.
*Required*: No
*Type*: [ClippingConfig](aws-properties-elementalinference-feed-clippingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Cropping`  <a name="cfn-elementalinference-feed-outputconfig-cropping"></a>
Specifies that this is a cropping output. Enter empty brace brackets {} as the value.
You might be creating this feed in order to pass it to AWS Elemental MediaLive, because you are using MediaLive to implement cropping. In this case, MediaLive will insert the cropping output in the feed that you pass. Don't include the output yourself when you create the feed.
*Required*: No
*Type*: [CroppingConfig](aws-properties-elementalinference-feed-croppingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subtitling`  <a name="cfn-elementalinference-feed-outputconfig-subtitling"></a>
Property description not available.
*Required*: No
*Type*: [SubtitlingConfig](aws-properties-elementalinference-feed-subtitlingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
