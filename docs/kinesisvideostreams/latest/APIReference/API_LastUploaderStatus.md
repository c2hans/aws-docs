---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_LastUploaderStatus.html
---

# LastUploaderStatus
<a name="API_LastUploaderStatus"></a>

The latest status of a stream’s edge to cloud uploader job.

## Contents
<a name="API_LastUploaderStatus_Contents"></a>

 ** JobStatusDetails **   <a name="KinesisVideo-Type-LastUploaderStatus-JobStatusDetails"></a>
A description of an uploader job’s latest status.
Type: String
Required: No

 ** LastCollectedTime **   <a name="KinesisVideo-Type-LastUploaderStatus-LastCollectedTime"></a>
The timestamp at which the uploader job was last executed and media collected to the cloud.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="KinesisVideo-Type-LastUploaderStatus-LastUpdatedTime"></a>
The timestamp at which the uploader status was last updated.
Type: Timestamp
Required: No

 ** UploaderStatus **   <a name="KinesisVideo-Type-LastUploaderStatus-UploaderStatus"></a>
The status of the latest uploader job.
Type: String
Valid Values: `SUCCESS | USER_ERROR | SYSTEM_ERROR`
Required: No

## See Also
<a name="API_LastUploaderStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/LastUploaderStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/LastUploaderStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/LastUploaderStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
