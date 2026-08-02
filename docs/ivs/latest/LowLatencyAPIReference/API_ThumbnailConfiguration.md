---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ThumbnailConfiguration.html
---

# ThumbnailConfiguration
<a name="API_ThumbnailConfiguration"></a>

An object representing a configuration of thumbnails for recorded video.

## Contents
<a name="API_ThumbnailConfiguration_Contents"></a>

 ** recordingMode **   <a name="ivs-Type-ThumbnailConfiguration-recordingMode"></a>
Thumbnail recording mode. Default: `INTERVAL`.
Type: String
Valid Values: `DISABLED | INTERVAL`
Required: No

 ** resolution **   <a name="ivs-Type-ThumbnailConfiguration-resolution"></a>
Indicates the desired resolution of recorded thumbnails. Thumbnails are recorded at the selected resolution if the corresponding rendition is available during the stream; otherwise, they are recorded at source resolution. For more information about resolution values and their corresponding height and width dimensions, see [Auto-Record to Amazon S3](https://docs.aws.amazon.com/ivs/latest/userguide/record-to-s3.html). Default: Null (source resolution is returned).
Type: String
Valid Values: `SD | HD | FULL_HD | LOWEST_RESOLUTION`
Required: No

 ** storage **   <a name="ivs-Type-ThumbnailConfiguration-storage"></a>
Indicates the format in which thumbnails are recorded. `SEQUENTIAL` records all generated thumbnails in a serial manner, to the media/thumbnails directory. `LATEST` saves the latest thumbnail in media/latest\_thumbnail/thumb.jpg and overwrites it at the interval specified by `targetIntervalSeconds`. You can enable both `SEQUENTIAL` and `LATEST`. Default: `SEQUENTIAL`.
Type: Array of strings
Valid Values: `SEQUENTIAL | LATEST`
Required: No

 ** targetIntervalSeconds **   <a name="ivs-Type-ThumbnailConfiguration-targetIntervalSeconds"></a>
The targeted thumbnail-generation interval in seconds. This is configurable (and required) only if `recordingMode` is `INTERVAL`. Default: 60.
 **Important:** For the `BASIC` channel type, or the `STANDARD` channel type with multitrack input, setting a value for `targetIntervalSeconds` does not guarantee that thumbnails are generated at the specified interval. For thumbnails to be generated at the `targetIntervalSeconds` interval, the `IDR/Keyframe` value for the input video must be less than the `targetIntervalSeconds` value. See [ Amazon IVS Streaming Configuration](https://docs.aws.amazon.com/ivs/latest/userguide/streaming-config.html) for information on setting `IDR/Keyframe` to the recommended value in video-encoder settings.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 60.
Required: No

## See Also
<a name="API_ThumbnailConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/ThumbnailConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/ThumbnailConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/ThumbnailConfiguration)
