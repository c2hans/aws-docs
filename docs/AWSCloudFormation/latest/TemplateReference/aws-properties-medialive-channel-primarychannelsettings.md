---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-primarychannelsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel PrimaryChannelSettings
<a name="aws-properties-medialive-channel-primarychannelsettings"></a>

Settings for a primary (leader) channel in a linked pair.

## Syntax
<a name="aws-properties-medialive-channel-primarychannelsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-primarychannelsettings-syntax.json"></a>

```
{
  "[LinkedChannelType](#cfn-medialive-channel-primarychannelsettings-linkedchanneltype)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-primarychannelsettings-syntax.yaml"></a>

```
  [LinkedChannelType](#cfn-medialive-channel-primarychannelsettings-linkedchanneltype): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-primarychannelsettings-properties"></a>

`LinkedChannelType`  <a name="cfn-medialive-channel-primarychannelsettings-linkedchanneltype"></a>
Specifies this as a primary channel.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
