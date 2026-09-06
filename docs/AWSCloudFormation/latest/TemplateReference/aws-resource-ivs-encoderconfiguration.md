---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ivs-encoderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::EncoderConfiguration
<a name="aws-resource-ivs-encoderconfiguration"></a>

The `AWS::IVS::EncoderConfiguration` resource specifies an Amazon IVS encoder configuration. An encoder configuration describes a stream’s video configuration. For more information, see [Streaming Configuration](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/streaming-config.html) in the *Amazon IVS Low-Latency Streaming User Guide*.

## Syntax
<a name="aws-resource-ivs-encoderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ivs-encoderconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::IVS::EncoderConfiguration",
  "Properties" : {
      "[Name](#cfn-ivs-encoderconfiguration-name)" : {{String}},
      "[Tags](#cfn-ivs-encoderconfiguration-tags)" : {{[ Tag, ... ]}},
      "[Video](#cfn-ivs-encoderconfiguration-video)" : {{Video}}
    }
}
```

### YAML
<a name="aws-resource-ivs-encoderconfiguration-syntax.yaml"></a>

```
Type: AWS::IVS::EncoderConfiguration
Properties:
  [Name](#cfn-ivs-encoderconfiguration-name): {{String}}
  [Tags](#cfn-ivs-encoderconfiguration-tags): {{
    - Tag}}
  [Video](#cfn-ivs-encoderconfiguration-video): {{
    Video}}
```

## Properties
<a name="aws-resource-ivs-encoderconfiguration-properties"></a>

`Name`  <a name="cfn-ivs-encoderconfiguration-name"></a>
Encoder cnfiguration name.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]*$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ivs-encoderconfiguration-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-encoderconfiguration-tag.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-ivs-encoderconfiguration-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Video`  <a name="cfn-ivs-encoderconfiguration-video"></a>
Video configuration. Default: video resolution 1280x720, bitrate 2500 kbps, 30 fps. See the [Video](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-encoderconfiguration-video.html) property type for more information.
*Required*: No
*Type*: [Video](aws-properties-ivs-encoderconfiguration-video.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ivs-encoderconfiguration-return-values"></a>

### Ref
<a name="aws-resource-ivs-encoderconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the encoder-configuration ARN. For example:

 `{ "Ref": "myEncoderConfiguration" }`

For the Amazon IVS encoder configuration `"myEncoderConfiguration"`, `Ref` returns the encoder-configuration ARN.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ivs-encoderconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ivs-encoderconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The encoder-configuration ARN. For example: `arn:aws:ivs:us-west-2:123456789012:encoder-configuration/abcdABCDefgh`

## Examples
<a name="aws-resource-ivs-encoderconfiguration--examples"></a>

### EncoderConfiguration Template Examples
<a name="aws-resource-ivs-encoderconfiguration--examples--EncoderConfiguration_Template_Examples"></a>

The following examples specify an Amazon IVS encoder configuration.

#### JSON
<a name="aws-resource-ivs-encoderconfiguration--examples--EncoderConfiguration_Template_Examples--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "EncoderConfiguration": {
            "Type": "AWS::IVS::EncoderConfiguration",
            "Properties": {
                "Name": "myEncoderConfiguration",
                "Video": {
                    "Bitrate": 1500000,
                    "Framerate": 1.5,
                    "Height": 100,
                    "Width": 100
                },
                "Tags": [
                    {
                        "Key": "MyKey",
                        "Value": "MyValue"
                    }
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-ivs-encoderconfiguration--examples--EncoderConfiguration_Template_Examples--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  EncoderConfiguration:
    Type: AWS::IVS::EncoderConfiguration
    Properties:
      Video:
        Bitrate: 1500000
        Framerate: 1.5
        Height: 100
        Width: 100
      Name: myEncoderConfiguration
      Tags:
        - Key: myKey
          Value: myValue
```

## See also
<a name="aws-resource-ivs-encoderconfiguration--seealso"></a>
+  [Getting Started with IVS Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started.html)
+  [ Server-Side Composition (Real-Time Streaming)](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/server-side-composition.html)
