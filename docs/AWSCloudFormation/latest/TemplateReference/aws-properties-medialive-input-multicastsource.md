---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-multicastsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input MulticastSource
<a name="aws-properties-medialive-input-multicastsource"></a>

A multicast source for a multicast input. A source has a multicast URL and an optional source IP address. For SMPTE 2022-7 seamless protection switching, the source also has a secondary URL and an optional secondary source IP address.

The parent of this entity is MulticastSettings.

## Syntax
<a name="aws-properties-medialive-input-multicastsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-multicastsource-syntax.json"></a>

```
{
  "[SourceIp](#cfn-medialive-input-multicastsource-sourceip)" : {{String}},
  "[Url](#cfn-medialive-input-multicastsource-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-multicastsource-syntax.yaml"></a>

```
  [SourceIp](#cfn-medialive-input-multicastsource-sourceip): {{String}}
  [Url](#cfn-medialive-input-multicastsource-url): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-multicastsource-properties"></a>

`SourceIp`  <a name="cfn-medialive-input-multicastsource-sourceip"></a>
The IP address of the device sending the multicast stream. Specify this address only if you use source-specific multicast (SSM).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-medialive-input-multicastsource-url"></a>
The customer's source URL where the multicast stream is pulled from.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
