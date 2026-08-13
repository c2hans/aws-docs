---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-composition-channeldestinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::Composition ChannelDestinationConfiguration
<a name="aws-properties-ivs-composition-channeldestinationconfiguration"></a>

<a name="aws-properties-ivs-composition-channeldestinationconfiguration-description"></a>The `ChannelDestinationConfiguration` property type specifies Property description not available. for an [AWS::IVS::Composition](aws-resource-ivs-composition.md).

## Syntax
<a name="aws-properties-ivs-composition-channeldestinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-composition-channeldestinationconfiguration-syntax.json"></a>

```
{
  "[ChannelArn](#cfn-ivs-composition-channeldestinationconfiguration-channelarn)" : {{String}},
  "[EncoderConfigurationArn](#cfn-ivs-composition-channeldestinationconfiguration-encoderconfigurationarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ivs-composition-channeldestinationconfiguration-syntax.yaml"></a>

```
  [ChannelArn](#cfn-ivs-composition-channeldestinationconfiguration-channelarn): {{String}}
  [EncoderConfigurationArn](#cfn-ivs-composition-channeldestinationconfiguration-encoderconfigurationarn): {{String}}
```

## Properties
<a name="aws-properties-ivs-composition-channeldestinationconfiguration-properties"></a>

`ChannelArn`  <a name="cfn-ivs-composition-channeldestinationconfiguration-channelarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncoderConfigurationArn`  <a name="cfn-ivs-composition-channeldestinationconfiguration-encoderconfigurationarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws:ivs:[a-z0-9-]+:[0-9]+:encoder-configuration/[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
