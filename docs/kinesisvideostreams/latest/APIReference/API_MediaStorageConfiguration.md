---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_MediaStorageConfiguration.html
---

# MediaStorageConfiguration
<a name="API_MediaStorageConfiguration"></a>

A structure that encapsulates, or contains, the media storage configuration properties.
+ If `StorageStatus` is enabled, the data will be stored in the `StreamARN` provided. In order for WebRTC Ingestion to work, the stream must have data retention enabled.
+ If `StorageStatus` is disabled, no data will be stored, and the `StreamARN` parameter will not be needed.

## Contents
<a name="API_MediaStorageConfiguration_Contents"></a>

 ** Status **   <a name="KinesisVideo-Type-MediaStorageConfiguration-Status"></a>
The status of the media storage configuration.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** StreamARN **   <a name="KinesisVideo-Type-MediaStorageConfiguration-StreamARN"></a>
The Amazon Resource Name (ARN) of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
Required: No

## See Also
<a name="API_MediaStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/MediaStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/MediaStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/MediaStorageConfiguration)
