---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flowoutput-encodingparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::FlowOutput EncodingParameters
<a name="aws-properties-mediaconnect-flowoutput-encodingparameters"></a>

 A collection of parameters that determine how MediaConnect will convert the content. These fields only apply to outputs on flows that have a CDI source.

## Syntax
<a name="aws-properties-mediaconnect-flowoutput-encodingparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flowoutput-encodingparameters-syntax.json"></a>

```
{
  "[CompressionFactor](#cfn-mediaconnect-flowoutput-encodingparameters-compressionfactor)" : {{Number}},
  "[EncoderProfile](#cfn-mediaconnect-flowoutput-encodingparameters-encoderprofile)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flowoutput-encodingparameters-syntax.yaml"></a>

```
  [CompressionFactor](#cfn-mediaconnect-flowoutput-encodingparameters-compressionfactor): {{Number}}
  [EncoderProfile](#cfn-mediaconnect-flowoutput-encodingparameters-encoderprofile): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flowoutput-encodingparameters-properties"></a>

`CompressionFactor`  <a name="cfn-mediaconnect-flowoutput-encodingparameters-compressionfactor"></a>
 A value that is used to calculate compression for an output. The bitrate of the output is calculated as follows: Output bitrate = (1 / compressionFactor) \* (source bitrate) This property only applies to outputs that use the ST 2110 JPEG XS protocol, with a flow source that uses the CDI protocol. Valid values are floating point numbers in the range of 3.0 to 10.0, inclusive.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncoderProfile`  <a name="cfn-mediaconnect-flowoutput-encodingparameters-encoderprofile"></a>
 A setting on the encoder that drives compression settings. This property only applies to video media streams associated with outputs that use the ST 2110 JPEG XS protocol, with a flow source that uses the CDI protocol.
*Required*: No
*Type*: String
*Allowed values*: `main | high`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
