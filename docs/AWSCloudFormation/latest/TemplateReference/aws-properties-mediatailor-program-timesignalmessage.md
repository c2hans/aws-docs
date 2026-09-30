---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-program-timesignalmessage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Program TimeSignalMessage
<a name="aws-properties-mediatailor-program-timesignalmessage"></a>

The SCTE-35 `time_signal` message can be sent with one or more `segmentation_descriptor` messages. A `time_signal` message can be sent only if a single `segmentation_descriptor` message is sent.

The `time_signal` message contains only the `splice_time` field which is constructed using a given presentation timestamp. When sending a `time_signal` message, the `splice_command_type` field in the `splice_info_section` message is set to 6 (0x06).

See the `time_signal()` table of the 2022 SCTE-35 specification for more information.

## Syntax
<a name="aws-properties-mediatailor-program-timesignalmessage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-program-timesignalmessage-syntax.json"></a>

```
{
  "[SegmentationDescriptors](#cfn-mediatailor-program-timesignalmessage-segmentationdescriptors)" : {{[ SegmentationDescriptor, ... ]}}
}
```

### YAML
<a name="aws-properties-mediatailor-program-timesignalmessage-syntax.yaml"></a>

```
  [SegmentationDescriptors](#cfn-mediatailor-program-timesignalmessage-segmentationdescriptors): {{
    - SegmentationDescriptor}}
```

## Properties
<a name="aws-properties-mediatailor-program-timesignalmessage-properties"></a>

`SegmentationDescriptors`  <a name="cfn-mediatailor-program-timesignalmessage-segmentationdescriptors"></a>
The configurations for the SCTE-35 `segmentation_descriptor` message(s) sent with the `time_signal` message.
*Required*: No
*Type*: Array of [SegmentationDescriptor](aws-properties-mediatailor-program-segmentationdescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
