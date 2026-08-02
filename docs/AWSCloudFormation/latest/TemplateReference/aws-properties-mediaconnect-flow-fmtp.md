---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-fmtp.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow Fmtp
<a name="aws-properties-mediaconnect-flow-fmtp"></a>

 A set of parameters that define the media stream.

## Syntax
<a name="aws-properties-mediaconnect-flow-fmtp-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-fmtp-syntax.json"></a>

```
{
  "[ChannelOrder](#cfn-mediaconnect-flow-fmtp-channelorder)" : {{String}},
  "[Colorimetry](#cfn-mediaconnect-flow-fmtp-colorimetry)" : {{String}},
  "[ExactFramerate](#cfn-mediaconnect-flow-fmtp-exactframerate)" : {{String}},
  "[Par](#cfn-mediaconnect-flow-fmtp-par)" : {{String}},
  "[Range](#cfn-mediaconnect-flow-fmtp-range)" : {{String}},
  "[ScanMode](#cfn-mediaconnect-flow-fmtp-scanmode)" : {{String}},
  "[Tcs](#cfn-mediaconnect-flow-fmtp-tcs)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-fmtp-syntax.yaml"></a>

```
  [ChannelOrder](#cfn-mediaconnect-flow-fmtp-channelorder): {{String}}
  [Colorimetry](#cfn-mediaconnect-flow-fmtp-colorimetry): {{String}}
  [ExactFramerate](#cfn-mediaconnect-flow-fmtp-exactframerate): {{String}}
  [Par](#cfn-mediaconnect-flow-fmtp-par): {{String}}
  [Range](#cfn-mediaconnect-flow-fmtp-range): {{String}}
  [ScanMode](#cfn-mediaconnect-flow-fmtp-scanmode): {{String}}
  [Tcs](#cfn-mediaconnect-flow-fmtp-tcs): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-fmtp-properties"></a>

`ChannelOrder`  <a name="cfn-mediaconnect-flow-fmtp-channelorder"></a>
 The format of the audio channel.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Colorimetry`  <a name="cfn-mediaconnect-flow-fmtp-colorimetry"></a>
The format used for the representation of color.
*Required*: No
*Type*: String
*Allowed values*: `BT601 | BT709 | BT2020 | BT2100 | ST2065-1 | ST2065-3 | XYZ`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExactFramerate`  <a name="cfn-mediaconnect-flow-fmtp-exactframerate"></a>
The frame rate for the video stream, in frames/second. For example: 60000/1001.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Par`  <a name="cfn-mediaconnect-flow-fmtp-par"></a>
The pixel aspect ratio (PAR) of the video.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Range`  <a name="cfn-mediaconnect-flow-fmtp-range"></a>
The encoding range of the video.
*Required*: No
*Type*: String
*Allowed values*: `NARROW | FULL | FULLPROTECT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScanMode`  <a name="cfn-mediaconnect-flow-fmtp-scanmode"></a>
The type of compression that was used to smooth the video’s appearance.
*Required*: No
*Type*: String
*Allowed values*: `progressive | interlace | progressive-segmented-frame`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tcs`  <a name="cfn-mediaconnect-flow-fmtp-tcs"></a>
The transfer characteristic system (TCS) that is used in the video.
*Required*: No
*Type*: String
*Allowed values*: `SDR | PQ | HLG | LINEAR | BT2100LINPQ | BT2100LINHLG | ST2065-1 | ST428-1 | DENSITY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
