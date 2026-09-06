---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_RecorderConfig.html
---

# RecorderConfig
<a name="API_RecorderConfig"></a>

The recorder configuration consists of the local `MediaSourceConfig` details that are used as credentials to access the local media files streamed on the camera.

## Contents
<a name="API_RecorderConfig_Contents"></a>

 ** MediaSourceConfig **   <a name="KinesisVideo-Type-RecorderConfig-MediaSourceConfig"></a>
The configuration details that consist of the credentials required (`MediaUriSecretArn` and `MediaUriType`) to access the media files streamed to the camera.
Type: [MediaSourceConfig](API_MediaSourceConfig.md) object
Required: Yes

 ** ScheduleConfig **   <a name="KinesisVideo-Type-RecorderConfig-ScheduleConfig"></a>
The configuration that consists of the `ScheduleExpression` and the `DurationInMinutes` details that specify the scheduling to record from a camera, or local media file, onto the Edge Agent. If the `ScheduleExpression` attribute is not provided, then the Edge Agent will always be set to recording mode.
Type: [ScheduleConfig](API_ScheduleConfig.md) object
Required: No

## See Also
<a name="API_RecorderConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/RecorderConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/RecorderConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/RecorderConfig)
