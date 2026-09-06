---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Video.html
---

# Video
<a name="API_Video"></a>

Settings for video.

## Contents
<a name="API_Video_Contents"></a>

 ** bitrate **   <a name="ivsrealtimeeapireference-Type-Video-bitrate"></a>
Bitrate for generated output, in bps. Default: 2500000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 8500000.
Required: No

 ** framerate **   <a name="ivsrealtimeeapireference-Type-Video-framerate"></a>
Video frame rate, in fps. Default: 30.
Type: Float
Valid Range: Minimum value of 1. Maximum value of 60.
Required: No

 ** height **   <a name="ivsrealtimeeapireference-Type-Video-height"></a>
Video-resolution height. This must be an even number. Note that the maximum value is determined by `width` times `height`, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 720.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 1920.
Required: No

 ** width **   <a name="ivsrealtimeeapireference-Type-Video-width"></a>
Video-resolution width. This must be an even number. Note that the maximum value is determined by `width` times `height`, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 1280.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 1920.
Required: No

## See Also
<a name="API_Video_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/Video)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/Video)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/Video)
