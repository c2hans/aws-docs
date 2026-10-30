---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-multicastsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input MulticastSettings
<a name="aws-properties-medialive-input-multicastsettings"></a>

Multicast input settings.

The parent of this entity is Input.

## Syntax
<a name="aws-properties-medialive-input-multicastsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-multicastsettings-syntax.json"></a>

```
{
  "[Sources](#cfn-medialive-input-multicastsettings-sources)" : {{[ MulticastSource, ... ]}}
}
```

### YAML
<a name="aws-properties-medialive-input-multicastsettings-syntax.yaml"></a>

```
  [Sources](#cfn-medialive-input-multicastsettings-sources): {{
    - MulticastSource}}
```

## Properties
<a name="aws-properties-medialive-input-multicastsettings-properties"></a>

`Sources`  <a name="cfn-medialive-input-multicastsettings-sources"></a>
The list of multicast sources for this input. Each source has a multicast URL and an optional source IP address. For SMPTE 2022-7 seamless protection switching, a source also has a secondary URL and an optional secondary source IP address.
*Required*: No
*Type*: Array of [MulticastSource](aws-properties-medialive-input-multicastsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
