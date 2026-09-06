---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-motiongraphicssettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MotionGraphicsSettings
<a name="aws-properties-medialive-channel-motiongraphicssettings"></a>

Settings to enable and configure the motion graphics overlay feature in the channel.

The parent of this entity is MotionGraphicsConfiguration.

## Syntax
<a name="aws-properties-medialive-channel-motiongraphicssettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-motiongraphicssettings-syntax.json"></a>

```
{
  "[HtmlMotionGraphicsSettings](#cfn-medialive-channel-motiongraphicssettings-htmlmotiongraphicssettings)" : {{Json}}
}
```

### YAML
<a name="aws-properties-medialive-channel-motiongraphicssettings-syntax.yaml"></a>

```
  [HtmlMotionGraphicsSettings](#cfn-medialive-channel-motiongraphicssettings-htmlmotiongraphicssettings): {{Json}}
```

## Properties
<a name="aws-properties-medialive-channel-motiongraphicssettings-properties"></a>

`HtmlMotionGraphicsSettings`  <a name="cfn-medialive-channel-motiongraphicssettings-htmlmotiongraphicssettings"></a>
Settings to configure the motion graphics overlay to use an HTML asset.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
