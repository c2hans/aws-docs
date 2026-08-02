---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_Fmtp.html
---

# Fmtp
<a name="API_Fmtp"></a>

 A set of parameters that define the media stream.

## Contents
<a name="API_Fmtp_Contents"></a>

 ** channelOrder **   <a name="mediaconnect-Type-Fmtp-channelOrder"></a>
 The format of the audio channel.
Type: String
Required: No

 ** colorimetry **   <a name="mediaconnect-Type-Fmtp-colorimetry"></a>
The format used for the representation of color.
Type: String
Valid Values: `BT601 | BT709 | BT2020 | BT2100 | ST2065-1 | ST2065-3 | XYZ`
Required: No

 ** exactFramerate **   <a name="mediaconnect-Type-Fmtp-exactFramerate"></a>
The frame rate for the video stream, in frames/second. For example: 60000/1001.
Type: String
Required: No

 ** par **   <a name="mediaconnect-Type-Fmtp-par"></a>
The pixel aspect ratio (PAR) of the video.
Type: String
Required: No

 ** range **   <a name="mediaconnect-Type-Fmtp-range"></a>
The encoding range of the video.
Type: String
Valid Values: `NARROW | FULL | FULLPROTECT`
Required: No

 ** scanMode **   <a name="mediaconnect-Type-Fmtp-scanMode"></a>
The type of compression that was used to smooth the video’s appearance.
Type: String
Valid Values: `progressive | interlace | progressive-segmented-frame`
Required: No

 ** tcs **   <a name="mediaconnect-Type-Fmtp-tcs"></a>
The transfer characteristic system (TCS) that is used in the video.
Type: String
Valid Values: `SDR | PQ | HLG | LINEAR | BT2100LINPQ | BT2100LINHLG | ST2065-1 | ST428-1 | DENSITY`
Required: No

## See Also
<a name="API_Fmtp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/Fmtp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/Fmtp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/Fmtp)
