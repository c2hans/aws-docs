---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_EdgeAgentStatus.html
---

# EdgeAgentStatus
<a name="API_EdgeAgentStatus"></a>

An object that contains the latest status details for an edge agent's recorder and uploader jobs. Use this information to determine the current health of an edge agent.

## Contents
<a name="API_EdgeAgentStatus_Contents"></a>

 ** LastRecorderStatus **   <a name="KinesisVideo-Type-EdgeAgentStatus-LastRecorderStatus"></a>
The latest status of a stream’s edge recording job.
Type: [LastRecorderStatus](API_LastRecorderStatus.md) object
Required: No

 ** LastUploaderStatus **   <a name="KinesisVideo-Type-EdgeAgentStatus-LastUploaderStatus"></a>
The latest status of a stream’s edge to cloud uploader job.
Type: [LastUploaderStatus](API_LastUploaderStatus.md) object
Required: No

## See Also
<a name="API_EdgeAgentStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/EdgeAgentStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/EdgeAgentStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/EdgeAgentStatus)
