---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-composition-destinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::Composition DestinationConfiguration
<a name="aws-properties-ivs-composition-destinationconfiguration"></a>

A complex type that describes a location where recorded videos will be stored. Each member represents a type of destination configuration. For recording, you define one and only one type of destination configuration.

## Syntax
<a name="aws-properties-ivs-composition-destinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-composition-destinationconfiguration-syntax.json"></a>

```
{
  "[Channel](#cfn-ivs-composition-destinationconfiguration-channel)" : {{ChannelDestinationConfiguration}},
  "[Name](#cfn-ivs-composition-destinationconfiguration-name)" : {{String}},
  "[S3](#cfn-ivs-composition-destinationconfiguration-s3)" : {{S3DestinationConfiguration}}
}
```

### YAML
<a name="aws-properties-ivs-composition-destinationconfiguration-syntax.yaml"></a>

```
  [Channel](#cfn-ivs-composition-destinationconfiguration-channel): {{
    ChannelDestinationConfiguration}}
  [Name](#cfn-ivs-composition-destinationconfiguration-name): {{String}}
  [S3](#cfn-ivs-composition-destinationconfiguration-s3): {{
    S3DestinationConfiguration}}
```

## Properties
<a name="aws-properties-ivs-composition-destinationconfiguration-properties"></a>

`Channel`  <a name="cfn-ivs-composition-destinationconfiguration-channel"></a>
Property description not available.
*Required*: No
*Type*: [ChannelDestinationConfiguration](aws-properties-ivs-composition-channeldestinationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-ivs-composition-destinationconfiguration-name"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]*$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3`  <a name="cfn-ivs-composition-destinationconfiguration-s3"></a>
An S3 destination configuration where recorded videos will be stored.
*Required*: No
*Type*: [S3DestinationConfiguration](aws-properties-ivs-composition-s3destinationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
