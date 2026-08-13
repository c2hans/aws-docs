---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-medialive-sdisource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::SdiSource
<a name="aws-resource-medialive-sdisource"></a>

Creates an SDI source. An SDI source receives content from SDI-connected devices.

## Syntax
<a name="aws-resource-medialive-sdisource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-medialive-sdisource-syntax.json"></a>

```
{
  "Type" : "AWS::MediaLive::SdiSource",
  "Properties" : {
      "[Mode](#cfn-medialive-sdisource-mode)" : {{String}},
      "[Name](#cfn-medialive-sdisource-name)" : {{String}},
      "[Tags](#cfn-medialive-sdisource-tags)" : {{[ Tags, ... ]}},
      "[Type](#cfn-medialive-sdisource-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-medialive-sdisource-syntax.yaml"></a>

```
Type: AWS::MediaLive::SdiSource
Properties:
  [Mode](#cfn-medialive-sdisource-mode): {{String}}
  [Name](#cfn-medialive-sdisource-name): {{String}}
  [Tags](#cfn-medialive-sdisource-tags): {{
    - Tags}}
  [Type](#cfn-medialive-sdisource-type): {{String}}
```

## Properties
<a name="aws-resource-medialive-sdisource-properties"></a>

`Mode`  <a name="cfn-medialive-sdisource-mode"></a>
The current mode of the SDI source.
*Required*: No
*Type*: String
*Allowed values*: `QUADRANT | INTERLEAVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-medialive-sdisource-name"></a>
The name of the SDI source.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-medialive-sdisource-tags"></a>
Property description not available.
*Required*: No
*Type*: [Array](aws-properties-medialive-sdisource-tags.md) of [Tags](aws-properties-medialive-sdisource-tags.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-medialive-sdisource-type"></a>
The interface mode of the SDI source.
*Required*: Yes
*Type*: String
*Allowed values*: `SINGLE | QUAD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-medialive-sdisource-return-values"></a>

### Ref
<a name="aws-resource-medialive-sdisource-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-medialive-sdisource-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-medialive-sdisource-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The unique ARN of the SDI source.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the SDI source.

`Inputs`  <a name="Inputs-fn::getatt"></a>
The list of inputs currently using this SDI source.

`State`  <a name="State-fn::getatt"></a>
The current state of the SDI source.
