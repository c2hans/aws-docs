---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_TimeSignalMessage.html
---

# TimeSignalMessage
<a name="API_TimeSignalMessage"></a>

The SCTE-35 `time_signal` message can be sent with one or more `segmentation_descriptor` messages. A `time_signal` message can be sent only if a single `segmentation_descriptor` message is sent.

The `time_signal` message contains only the `splice_time` field which is constructed using a given presentation timestamp. When sending a `time_signal` message, the `splice_command_type` field in the `splice_info_section` message is set to 6 (0x06).

See the `time_signal()` table of the 2022 SCTE-35 specification for more information.

## Contents
<a name="API_TimeSignalMessage_Contents"></a>

 ** SegmentationDescriptors **   <a name="mediatailor-Type-TimeSignalMessage-SegmentationDescriptors"></a>
The configurations for the SCTE-35 `segmentation_descriptor` message(s) sent with the `time_signal` message.
Type: Array of [SegmentationDescriptor](API_SegmentationDescriptor.md) objects
Required: No

## See Also
<a name="API_TimeSignalMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/TimeSignalMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/TimeSignalMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/TimeSignalMessage)
