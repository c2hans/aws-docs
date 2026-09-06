---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flowoutput-mediastreamoutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::FlowOutput MediaStreamOutputConfiguration
<a name="aws-properties-mediaconnect-flowoutput-mediastreamoutputconfiguration"></a>

 The media stream that is associated with the output, and the parameters for that association.

## Syntax
<a name="aws-properties-mediaconnect-flowoutput-mediastreamoutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flowoutput-mediastreamoutputconfiguration-syntax.json"></a>

```
{
  "[DestinationConfigurations](#cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-destinationconfigurations)" : {{[ DestinationConfiguration, ... ]}},
  "[EncodingName](#cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-encodingname)" : {{String}},
  "[EncodingParameters](#cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-encodingparameters)" : {{EncodingParameters}},
  "[MediaStreamName](#cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-mediastreamname)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flowoutput-mediastreamoutputconfiguration-syntax.yaml"></a>

```
  [DestinationConfigurations](#cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-destinationconfigurations): {{
    - DestinationConfiguration}}
  [EncodingName](#cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-encodingname): {{String}}
  [EncodingParameters](#cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-encodingparameters): {{
    EncodingParameters}}
  [MediaStreamName](#cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-mediastreamname): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flowoutput-mediastreamoutputconfiguration-properties"></a>

`DestinationConfigurations`  <a name="cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-destinationconfigurations"></a>
 The transport parameters that are associated with each outbound media stream.
*Required*: No
*Type*: Array of [DestinationConfiguration](aws-properties-mediaconnect-flowoutput-destinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncodingName`  <a name="cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-encodingname"></a>
 The format that was used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.
*Required*: Yes
*Type*: String
*Allowed values*: `jxsv | raw | smpte291 | pcm`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncodingParameters`  <a name="cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-encodingparameters"></a>
A collection of parameters that determine how MediaConnect will convert the content. These fields only apply to outputs on flows that have a CDI source.
*Required*: No
*Type*: [EncodingParameters](aws-properties-mediaconnect-flowoutput-encodingparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaStreamName`  <a name="cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-mediastreamname"></a>
 The name of the media stream.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
