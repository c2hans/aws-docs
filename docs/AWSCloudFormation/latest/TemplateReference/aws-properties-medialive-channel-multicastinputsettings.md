---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-multicastinputsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MulticastInputSettings
<a name="aws-properties-medialive-channel-multicastinputsettings"></a>

Specifies multicast input settings when the URI is for a multicast event.

The parent of this entity is NetworkInputSettings.

## Syntax
<a name="aws-properties-medialive-channel-multicastinputsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-multicastinputsettings-syntax.json"></a>

```
{
  "[SourceIpAddress](#cfn-medialive-channel-multicastinputsettings-sourceipaddress)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-multicastinputsettings-syntax.yaml"></a>

```
  [SourceIpAddress](#cfn-medialive-channel-multicastinputsettings-sourceipaddress): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-multicastinputsettings-properties"></a>

`SourceIpAddress`  <a name="cfn-medialive-channel-multicastinputsettings-sourceipaddress"></a>
Optionally, a source IP address to filter by for Source-specific Multicast (SSM).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
