---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_MediaSourceConfig.html
---

# MediaSourceConfig
<a name="API_MediaSourceConfig"></a>

The configuration details that consist of the credentials required (`MediaUriSecretArn` and `MediaUriType`) to access the media files that are streamed to the camera.

## Contents
<a name="API_MediaSourceConfig_Contents"></a>

 ** MediaUriSecretArn **   <a name="KinesisVideo-Type-MediaSourceConfig-MediaUriSecretArn"></a>
The AWS Secrets Manager ARN for the username and password of the camera, or a local media file location.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z\d-]+:secretsmanager:[a-z0-9-]+:[0-9]+:secret:[a-zA-Z0-9_.-]+`
Required: Yes

 ** MediaUriType **   <a name="KinesisVideo-Type-MediaSourceConfig-MediaUriType"></a>
The Uniform Resource Identifier (URI) type. The `FILE_URI` value can be used to stream local media files.
Preview only supports the `RTSP_URI` media source URI format .
Type: String
Valid Values: `RTSP_URI | FILE_URI`
Required: Yes

## See Also
<a name="API_MediaSourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/MediaSourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/MediaSourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/MediaSourceConfig)
