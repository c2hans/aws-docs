---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_SegmentationDescriptor.html
---

# SegmentationDescriptor
<a name="API_SegmentationDescriptor"></a>

The `segmentation_descriptor` message can contain advanced metadata fields, like content identifiers, to convey a wide range of information about the ad break. MediaTailor writes the ad metadata in the egress manifest as part of the `EXT-X-DATERANGE` or `EventStream` ad marker's SCTE-35 data.

 `segmentation_descriptor` messages must be sent with the `time_signal` message type.

See the `segmentation_descriptor()` table of the 2022 SCTE-35 specification for more information.

## Contents
<a name="API_SegmentationDescriptor_Contents"></a>

 ** SegmentationEventId **   <a name="mediatailor-Type-SegmentationDescriptor-SegmentationEventId"></a>
The Event Identifier to assign to the `segmentation_descriptor.segmentation_event_id` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. The default value is 1.
Type: Integer
Required: No

 ** SegmentationTypeId **   <a name="mediatailor-Type-SegmentationDescriptor-SegmentationTypeId"></a>
The Type Identifier to assign to the `segmentation_descriptor.segmentation_type_id` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is 48.
Type: Integer
Required: No

 ** SegmentationUpid **   <a name="mediatailor-Type-SegmentationDescriptor-SegmentationUpid"></a>
The Upid to assign to the `segmentation_descriptor.segmentation_upid` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. The value must be a hexadecimal string containing only the characters 0 though 9 and A through F. The default value is "" (an empty string).
Type: String
Required: No

 ** SegmentationUpidType **   <a name="mediatailor-Type-SegmentationDescriptor-SegmentationUpidType"></a>
The Upid Type to assign to the `segmentation_descriptor.segmentation_upid_type` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is 14.
Type: Integer
Required: No

 ** SegmentNum **   <a name="mediatailor-Type-SegmentationDescriptor-SegmentNum"></a>
The segment number to assign to the `segmentation_descriptor.segment_num` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification Values must be between 0 and 256, inclusive. The default value is 0.
Type: Integer
Required: No

 ** SegmentsExpected **   <a name="mediatailor-Type-SegmentationDescriptor-SegmentsExpected"></a>
The number of segments expected, which is assigned to the `segmentation_descriptor.segments_expectedS` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification Values must be between 0 and 256, inclusive. The default value is 0.
Type: Integer
Required: No

 ** SubSegmentNum **   <a name="mediatailor-Type-SegmentationDescriptor-SubSegmentNum"></a>
The sub-segment number to assign to the `segmentation_descriptor.sub_segment_num` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The defualt value is null.
Type: Integer
Required: No

 ** SubSegmentsExpected **   <a name="mediatailor-Type-SegmentationDescriptor-SubSegmentsExpected"></a>
The number of sub-segments expected, which is assigned to the `segmentation_descriptor.sub_segments_expected` message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is null.
Type: Integer
Required: No

## See Also
<a name="API_SegmentationDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/SegmentationDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/SegmentationDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/SegmentationDescriptor)
