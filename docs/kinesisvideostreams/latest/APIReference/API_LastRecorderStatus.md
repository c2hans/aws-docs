---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_LastRecorderStatus.html
---

# LastRecorderStatus
<a name="API_LastRecorderStatus"></a>

The latest status of a stream's edge recording job.

## Contents
<a name="API_LastRecorderStatus_Contents"></a>

 ** JobStatusDetails **   <a name="KinesisVideo-Type-LastRecorderStatus-JobStatusDetails"></a>
A description of a recorder job’s latest status.
Type: String
Required: No

 ** LastCollectedTime **   <a name="KinesisVideo-Type-LastRecorderStatus-LastCollectedTime"></a>
The timestamp at which the recorder job was last executed and media stored to local disk.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="KinesisVideo-Type-LastRecorderStatus-LastUpdatedTime"></a>
The timestamp at which the recorder status was last updated.
Type: Timestamp
Required: No

 ** RecorderStatus **   <a name="KinesisVideo-Type-LastRecorderStatus-RecorderStatus"></a>
The status of the latest recorder job.
Type: String
Valid Values: `SUCCESS | USER_ERROR | SYSTEM_ERROR`
Required: No

## See Also
<a name="API_LastRecorderStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/LastRecorderStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/LastRecorderStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/LastRecorderStatus)
