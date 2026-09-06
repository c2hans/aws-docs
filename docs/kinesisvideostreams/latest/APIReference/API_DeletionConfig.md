---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_DeletionConfig.html
---

# DeletionConfig
<a name="API_DeletionConfig"></a>

The configuration details required to delete the connection of the stream from the Edge Agent.

## Contents
<a name="API_DeletionConfig_Contents"></a>

 ** DeleteAfterUpload **   <a name="KinesisVideo-Type-DeletionConfig-DeleteAfterUpload"></a>
The `boolean` value used to indicate whether or not you want to mark the media for deletion, once it has been uploaded to the Kinesis Video Stream cloud. The media files can be deleted if any of the deletion configuration values are set to `true`, such as when the limit for the `EdgeRetentionInHours`, or the `MaxLocalMediaSizeInMB`, has been reached.
Since the default value is set to `true`, configure the uploader schedule such that the media files are not being deleted before they are initially uploaded to the AWS cloud.
Type: Boolean
Required: No

 ** EdgeRetentionInHours **   <a name="KinesisVideo-Type-DeletionConfig-EdgeRetentionInHours"></a>
The number of hours that you want to retain the data in the stream on the Edge Agent. The default value of the retention time is 720 hours, which translates to 30 days.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 720.
Required: No

 ** LocalSizeConfig **   <a name="KinesisVideo-Type-DeletionConfig-LocalSizeConfig"></a>
The value of the local size required in order to delete the edge configuration.
Type: [LocalSizeConfig](API_LocalSizeConfig.md) object
Required: No

## See Also
<a name="API_DeletionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/DeletionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/DeletionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/DeletionConfig)
