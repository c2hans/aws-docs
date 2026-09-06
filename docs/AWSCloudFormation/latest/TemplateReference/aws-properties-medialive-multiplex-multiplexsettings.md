---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-multiplex-multiplexsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Multiplex MultiplexSettings
<a name="aws-properties-medialive-multiplex-multiplexsettings"></a>

Contains configuration for a Multiplex event

## Syntax
<a name="aws-properties-medialive-multiplex-multiplexsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-multiplex-multiplexsettings-syntax.json"></a>

```
{
  "[MaximumVideoBufferDelayMilliseconds](#cfn-medialive-multiplex-multiplexsettings-maximumvideobufferdelaymilliseconds)" : {{Integer}},
  "[TransportStreamBitrate](#cfn-medialive-multiplex-multiplexsettings-transportstreambitrate)" : {{Integer}},
  "[TransportStreamId](#cfn-medialive-multiplex-multiplexsettings-transportstreamid)" : {{Integer}},
  "[TransportStreamReservedBitrate](#cfn-medialive-multiplex-multiplexsettings-transportstreamreservedbitrate)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-multiplex-multiplexsettings-syntax.yaml"></a>

```
  [MaximumVideoBufferDelayMilliseconds](#cfn-medialive-multiplex-multiplexsettings-maximumvideobufferdelaymilliseconds): {{Integer}}
  [TransportStreamBitrate](#cfn-medialive-multiplex-multiplexsettings-transportstreambitrate): {{Integer}}
  [TransportStreamId](#cfn-medialive-multiplex-multiplexsettings-transportstreamid): {{Integer}}
  [TransportStreamReservedBitrate](#cfn-medialive-multiplex-multiplexsettings-transportstreamreservedbitrate): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-multiplex-multiplexsettings-properties"></a>

`MaximumVideoBufferDelayMilliseconds`  <a name="cfn-medialive-multiplex-multiplexsettings-maximumvideobufferdelaymilliseconds"></a>
Maximum video buffer delay in milliseconds.
*Required*: No
*Type*: Integer
*Minimum*: `800`
*Maximum*: `3000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransportStreamBitrate`  <a name="cfn-medialive-multiplex-multiplexsettings-transportstreambitrate"></a>
Transport stream bit rate.
*Required*: Yes
*Type*: Integer
*Minimum*: `1000000`
*Maximum*: `100000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransportStreamId`  <a name="cfn-medialive-multiplex-multiplexsettings-transportstreamid"></a>
Transport stream ID.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransportStreamReservedBitrate`  <a name="cfn-medialive-multiplex-multiplexsettings-transportstreamreservedbitrate"></a>
Transport stream reserved bit rate.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
