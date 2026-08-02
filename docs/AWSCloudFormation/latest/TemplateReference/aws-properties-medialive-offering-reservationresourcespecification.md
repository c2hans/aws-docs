---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-offering-reservationresourcespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Offering ReservationResourceSpecification
<a name="aws-properties-medialive-offering-reservationresourcespecification"></a>

Resource configuration (codec, resolution, bitrate, ...)

## Syntax
<a name="aws-properties-medialive-offering-reservationresourcespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-offering-reservationresourcespecification-syntax.json"></a>

```
{
  "[ChannelClass](#cfn-medialive-offering-reservationresourcespecification-channelclass)" : {{String}},
  "[Codec](#cfn-medialive-offering-reservationresourcespecification-codec)" : {{String}},
  "[MaximumBitrate](#cfn-medialive-offering-reservationresourcespecification-maximumbitrate)" : {{String}},
  "[MaximumFramerate](#cfn-medialive-offering-reservationresourcespecification-maximumframerate)" : {{String}},
  "[Resolution](#cfn-medialive-offering-reservationresourcespecification-resolution)" : {{String}},
  "[ResourceType](#cfn-medialive-offering-reservationresourcespecification-resourcetype)" : {{String}},
  "[SpecialFeature](#cfn-medialive-offering-reservationresourcespecification-specialfeature)" : {{String}},
  "[VideoQuality](#cfn-medialive-offering-reservationresourcespecification-videoquality)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-offering-reservationresourcespecification-syntax.yaml"></a>

```
  [ChannelClass](#cfn-medialive-offering-reservationresourcespecification-channelclass): {{String}}
  [Codec](#cfn-medialive-offering-reservationresourcespecification-codec): {{String}}
  [MaximumBitrate](#cfn-medialive-offering-reservationresourcespecification-maximumbitrate): {{String}}
  [MaximumFramerate](#cfn-medialive-offering-reservationresourcespecification-maximumframerate): {{String}}
  [Resolution](#cfn-medialive-offering-reservationresourcespecification-resolution): {{String}}
  [ResourceType](#cfn-medialive-offering-reservationresourcespecification-resourcetype): {{String}}
  [SpecialFeature](#cfn-medialive-offering-reservationresourcespecification-specialfeature): {{String}}
  [VideoQuality](#cfn-medialive-offering-reservationresourcespecification-videoquality): {{String}}
```

## Properties
<a name="aws-properties-medialive-offering-reservationresourcespecification-properties"></a>

`ChannelClass`  <a name="cfn-medialive-offering-reservationresourcespecification-channelclass"></a>
Channel class, e.g. 'STANDARD'
*Required*: No
*Type*: String
*Allowed values*: `STANDARD | SINGLE_PIPELINE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Codec`  <a name="cfn-medialive-offering-reservationresourcespecification-codec"></a>
Codec, e.g. 'AVC'
*Required*: No
*Type*: String
*Allowed values*: `MPEG2 | AVC | HEVC | AUDIO | LINK | AV1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumBitrate`  <a name="cfn-medialive-offering-reservationresourcespecification-maximumbitrate"></a>
Maximum bitrate, e.g. 'MAX\_20\_MBPS'
*Required*: No
*Type*: String
*Allowed values*: `MAX_10_MBPS | MAX_20_MBPS | MAX_50_MBPS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumFramerate`  <a name="cfn-medialive-offering-reservationresourcespecification-maximumframerate"></a>
Maximum framerate, e.g. 'MAX\_30\_FPS' (Outputs only)
*Required*: No
*Type*: String
*Allowed values*: `MAX_30_FPS | MAX_60_FPS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Resolution`  <a name="cfn-medialive-offering-reservationresourcespecification-resolution"></a>
Resolution, e.g. 'HD'
*Required*: No
*Type*: String
*Allowed values*: `SD | HD | FHD | UHD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-medialive-offering-reservationresourcespecification-resourcetype"></a>
Resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL'
*Required*: No
*Type*: String
*Allowed values*: `INPUT | OUTPUT | MULTIPLEX | CHANNEL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpecialFeature`  <a name="cfn-medialive-offering-reservationresourcespecification-specialfeature"></a>
Special feature, e.g. 'AUDIO\_NORMALIZATION' (Channels only)
*Required*: No
*Type*: String
*Allowed values*: `ADVANCED_AUDIO | AUDIO_NORMALIZATION | MGHD | MGUHD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VideoQuality`  <a name="cfn-medialive-offering-reservationresourcespecification-videoquality"></a>
Video quality, e.g. 'STANDARD' (Outputs only)
*Required*: No
*Type*: String
*Allowed values*: `STANDARD | ENHANCED | PREMIUM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
