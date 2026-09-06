---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-thumbnailconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel ThumbnailConfiguration
<a name="aws-properties-medialive-channel-thumbnailconfiguration"></a>

Thumbnail configuration settings.

The parent of this entity is EncoderSettings.

## Syntax
<a name="aws-properties-medialive-channel-thumbnailconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-thumbnailconfiguration-syntax.json"></a>

```
{
  "[State](#cfn-medialive-channel-thumbnailconfiguration-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-thumbnailconfiguration-syntax.yaml"></a>

```
  [State](#cfn-medialive-channel-thumbnailconfiguration-state): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-thumbnailconfiguration-properties"></a>

`State`  <a name="cfn-medialive-channel-thumbnailconfiguration-state"></a>
Required. Enables the thumbnail feature. The feature generates thumbnails of the incoming video in each pipeline in the channel. AUTO turns the feature on, DISABLE turns the feature off.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
