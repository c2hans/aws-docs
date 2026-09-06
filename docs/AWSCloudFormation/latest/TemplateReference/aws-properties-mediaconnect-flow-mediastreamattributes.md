---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-mediastreamattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow MediaStreamAttributes
<a name="aws-properties-mediaconnect-flow-mediastreamattributes"></a>

Attributes that are related to the media stream.

## Syntax
<a name="aws-properties-mediaconnect-flow-mediastreamattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-mediastreamattributes-syntax.json"></a>

```
{
  "[Fmtp](#cfn-mediaconnect-flow-mediastreamattributes-fmtp)" : {{Fmtp}},
  "[Lang](#cfn-mediaconnect-flow-mediastreamattributes-lang)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-mediastreamattributes-syntax.yaml"></a>

```
  [Fmtp](#cfn-mediaconnect-flow-mediastreamattributes-fmtp): {{
    Fmtp}}
  [Lang](#cfn-mediaconnect-flow-mediastreamattributes-lang): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-mediastreamattributes-properties"></a>

`Fmtp`  <a name="cfn-mediaconnect-flow-mediastreamattributes-fmtp"></a>
The settings that you want to use to define the media stream.
*Required*: No
*Type*: [Fmtp](aws-properties-mediaconnect-flow-fmtp.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Lang`  <a name="cfn-mediaconnect-flow-mediastreamattributes-lang"></a>
The audio language, in a format that is recognized by the receiver.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
