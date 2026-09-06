---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_InstanceStorageConfig.html
---

# InstanceStorageConfig
<a name="API_InstanceStorageConfig"></a>

The storage configuration for the instance.

## Contents
<a name="API_InstanceStorageConfig_Contents"></a>

 ** StorageType **   <a name="connect-Type-InstanceStorageConfig-StorageType"></a>
A valid storage type.
Type: String
Valid Values: `S3 | KINESIS_VIDEO_STREAM | KINESIS_STREAM | KINESIS_FIREHOSE`
Required: Yes

 ** AssociationId **   <a name="connect-Type-InstanceStorageConfig-AssociationId"></a>
The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** KinesisFirehoseConfig **   <a name="connect-Type-InstanceStorageConfig-KinesisFirehoseConfig"></a>
The configuration of the Kinesis Firehose delivery stream.
Type: [KinesisFirehoseConfig](API_KinesisFirehoseConfig.md) object
Required: No

 ** KinesisStreamConfig **   <a name="connect-Type-InstanceStorageConfig-KinesisStreamConfig"></a>
The configuration of the Kinesis data stream.
Type: [KinesisStreamConfig](API_KinesisStreamConfig.md) object
Required: No

 ** KinesisVideoStreamConfig **   <a name="connect-Type-InstanceStorageConfig-KinesisVideoStreamConfig"></a>
The configuration of the Kinesis video stream.
Type: [KinesisVideoStreamConfig](API_KinesisVideoStreamConfig.md) object
Required: No

 ** S3Config **   <a name="connect-Type-InstanceStorageConfig-S3Config"></a>
The S3 bucket configuration.
Type: [S3Config](API_S3Config.md) object
Required: No

## See Also
<a name="API_InstanceStorageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/InstanceStorageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/InstanceStorageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/InstanceStorageConfig)
