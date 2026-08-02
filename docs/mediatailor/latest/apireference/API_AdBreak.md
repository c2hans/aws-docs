---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AdBreak.html
---

# AdBreak
<a name="API_AdBreak"></a>

Ad break configuration parameters.

## Contents
<a name="API_AdBreak_Contents"></a>

 ** OffsetMillis **   <a name="mediatailor-Type-AdBreak-OffsetMillis"></a>
How long (in milliseconds) after the beginning of the program that an ad starts. This value must fall within 100ms of a segment boundary, otherwise the ad break will be skipped.
Type: Long
Required: Yes

 ** AdBreakMetadata **   <a name="mediatailor-Type-AdBreak-AdBreakMetadata"></a>
Defines a list of key/value pairs that MediaTailor generates within the `EXT-X-ASSET`tag for `SCTE35_ENHANCED` output.
Type: Array of [KeyValuePair](API_KeyValuePair.md) objects
Required: No

 ** MessageType **   <a name="mediatailor-Type-AdBreak-MessageType"></a>
The SCTE-35 ad insertion type. Accepted value: `SPLICE_INSERT`, `TIME_SIGNAL`.
Type: String
Valid Values: `SPLICE_INSERT | TIME_SIGNAL`
Required: No

 ** Slate **   <a name="mediatailor-Type-AdBreak-Slate"></a>
Ad break slate configuration.
Type: [SlateSource](API_SlateSource.md) object
Required: No

 ** SpliceInsertMessage **   <a name="mediatailor-Type-AdBreak-SpliceInsertMessage"></a>
This defines the SCTE-35 `splice_insert()` message inserted around the ad. For information about using `splice_insert()`, see the SCTE-35 specficiaiton, section 9.7.3.1.
Type: [SpliceInsertMessage](API_SpliceInsertMessage.md) object
Required: No

 ** TimeSignalMessage **   <a name="mediatailor-Type-AdBreak-TimeSignalMessage"></a>
Defines the SCTE-35 `time_signal` message inserted around the ad.
Programs on a channel's schedule can be configured with one or more ad breaks. You can attach a `splice_insert` SCTE-35 message to the ad break. This message provides basic metadata about the ad break.
See section 9.7.4 of the 2022 SCTE-35 specification for more information.
Type: [TimeSignalMessage](API_TimeSignalMessage.md) object
Required: No

## See Also
<a name="API_AdBreak_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/AdBreak)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/AdBreak)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/AdBreak)
