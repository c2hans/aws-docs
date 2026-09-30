---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-program-segmentationdescriptor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Program SegmentationDescriptor
<a name="aws-properties-mediatailor-program-segmentationdescriptor"></a>

The `segmentation_descriptor` message can contain advanced metadata fields, like content identifiers, to convey a wide range of information about the ad break. MediaTailor writes the ad metadata in the egress manifest as part of the `EXT-X-DATERANGE` or `EventStream` ad marker's SCTE-35 data.

`segmentation_descriptor` messages must be sent with the `time_signal` message type.

See the `segmentation_descriptor()` table of the 2022 SCTE-35 specification for more information.

## Syntax
<a name="aws-properties-mediatailor-program-segmentationdescriptor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-program-segmentationdescriptor-syntax.json"></a>

```
{
  "[SegmentationEventId](#cfn-mediatailor-program-segmentationdescriptor-segmentationeventid)" : {{Integer}},
  "[SegmentationTypeId](#cfn-mediatailor-program-segmentationdescriptor-segmentationtypeid)" : {{Integer}},
  "[SegmentationUpid](#cfn-mediatailor-program-segmentationdescriptor-segmentationupid)" : {{String}},
  "[SegmentationUpidType](#cfn-mediatailor-program-segmentationdescriptor-segmentationupidtype)" : {{Integer}},
  "[SegmentNum](#cfn-mediatailor-program-segmentationdescriptor-segmentnum)" : {{Integer}},
  "[SegmentsExpected](#cfn-mediatailor-program-segmentationdescriptor-segmentsexpected)" : {{Integer}},
  "[SubSegmentNum](#cfn-mediatailor-program-segmentationdescriptor-subsegmentnum)" : {{Integer}},
  "[SubSegmentsExpected](#cfn-mediatailor-program-segmentationdescriptor-subsegmentsexpected)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediatailor-program-segmentationdescriptor-syntax.yaml"></a>

```
  [SegmentationEventId](#cfn-mediatailor-program-segmentationdescriptor-segmentationeventid): {{Integer}}
  [SegmentationTypeId](#cfn-mediatailor-program-segmentationdescriptor-segmentationtypeid): {{Integer}}
  [SegmentationUpid](#cfn-mediatailor-program-segmentationdescriptor-segmentationupid): {{String}}
  [SegmentationUpidType](#cfn-mediatailor-program-segmentationdescriptor-segmentationupidtype): {{Integer}}
  [SegmentNum](#cfn-mediatailor-program-segmentationdescriptor-segmentnum): {{Integer}}
  [SegmentsExpected](#cfn-mediatailor-program-segmentationdescriptor-segmentsexpected): {{Integer}}
  [SubSegmentNum](#cfn-mediatailor-program-segmentationdescriptor-subsegmentnum): {{Integer}}
  [SubSegmentsExpected](#cfn-mediatailor-program-segmentationdescriptor-subsegmentsexpected): {{Integer}}
```

## Properties
<a name="aws-properties-mediatailor-program-segmentationdescriptor-properties"></a>

`SegmentationEventId`  <a name="cfn-mediatailor-program-segmentationdescriptor-segmentationeventid"></a>
The Event Identifier to assign to the `segmentation_descriptor.segmentation_event_id` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. The default value is 1.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentationTypeId`  <a name="cfn-mediatailor-program-segmentationdescriptor-segmentationtypeid"></a>
The Type Identifier to assign to the `segmentation_descriptor.segmentation_type_id` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is 48.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentationUpid`  <a name="cfn-mediatailor-program-segmentationdescriptor-segmentationupid"></a>
The Upid to assign to the `segmentation_descriptor.segmentation_upid` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. The value must be a hexadecimal string containing only the characters 0 though 9 and A through F. The default value is "" (an empty string).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentationUpidType`  <a name="cfn-mediatailor-program-segmentationdescriptor-segmentationupidtype"></a>
The Upid Type to assign to the `segmentation_descriptor.segmentation_upid_type` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is 14.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentNum`  <a name="cfn-mediatailor-program-segmentationdescriptor-segmentnum"></a>
The segment number to assign to the `segmentation_descriptor.segment_num` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification Values must be between 0 and 256, inclusive. The default value is 0.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentsExpected`  <a name="cfn-mediatailor-program-segmentationdescriptor-segmentsexpected"></a>
The number of segments expected, which is assigned to the `segmentation_descriptor.segments_expectedS` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification Values must be between 0 and 256, inclusive. The default value is 0.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubSegmentNum`  <a name="cfn-mediatailor-program-segmentationdescriptor-subsegmentnum"></a>
The sub-segment number to assign to the `segmentation_descriptor.sub_segment_num` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The defualt value is null.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubSegmentsExpected`  <a name="cfn-mediatailor-program-segmentationdescriptor-subsegmentsexpected"></a>
The number of sub-segments expected, which is assigned to the `segmentation_descriptor.sub_segments_expected` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is null.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
