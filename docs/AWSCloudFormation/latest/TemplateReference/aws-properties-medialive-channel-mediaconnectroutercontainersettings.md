---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-mediaconnectroutercontainersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MediaConnectRouterContainerSettings
<a name="aws-properties-medialive-channel-mediaconnectroutercontainersettings"></a>

MediaConnect Router container settings.

The parent of this entity is MediaConnectRouterOutputSettings.

## Syntax
<a name="aws-properties-medialive-channel-mediaconnectroutercontainersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-mediaconnectroutercontainersettings-syntax.json"></a>

```
{
  "[M2tsSettings](#cfn-medialive-channel-mediaconnectroutercontainersettings-m2tssettings)" : {{M2tsSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-mediaconnectroutercontainersettings-syntax.yaml"></a>

```
  [M2tsSettings](#cfn-medialive-channel-mediaconnectroutercontainersettings-m2tssettings): {{
    M2tsSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-mediaconnectroutercontainersettings-properties"></a>

`M2tsSettings`  <a name="cfn-medialive-channel-mediaconnectroutercontainersettings-m2tssettings"></a>
M2TS settings for the MediaConnect Router output container.
*Required*: No
*Type*: [M2tsSettings](aws-properties-medialive-channel-m2tssettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
