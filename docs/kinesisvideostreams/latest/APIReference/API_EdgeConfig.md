---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_EdgeConfig.html
---

# EdgeConfig
<a name="API_EdgeConfig"></a>

A description of the stream's edge configuration that will be used to sync with the Edge Agent IoT Greengrass component. The Edge Agent component will run on an IoT Hub Device setup at your premise.

## Contents
<a name="API_EdgeConfig_Contents"></a>

 ** HubDeviceArn **   <a name="KinesisVideo-Type-EdgeConfig-HubDeviceArn"></a>
The "**Internet of Things (IoT) Thing**" Arn of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\d-]+:iot:[a-z0-9-]+:[0-9]+:thing/[a-zA-Z0-9_.-]+`
Required: Yes

 ** RecorderConfig **   <a name="KinesisVideo-Type-EdgeConfig-RecorderConfig"></a>
The recorder configuration consists of the local `MediaSourceConfig` details, that are used as credentials to access the local media files streamed on the camera.
Type: [RecorderConfig](API_RecorderConfig.md) object
Required: Yes

 ** DeletionConfig **   <a name="KinesisVideo-Type-EdgeConfig-DeletionConfig"></a>
The deletion configuration is made up of the retention time (`EdgeRetentionInHours`) and local size configuration (`LocalSizeConfig`) details that are used to make the deletion.
Type: [DeletionConfig](API_DeletionConfig.md) object
Required: No

 ** UploaderConfig **   <a name="KinesisVideo-Type-EdgeConfig-UploaderConfig"></a>
The uploader configuration contains the `ScheduleExpression` details that are used to schedule upload jobs for the recorded media files from the Edge Agent to a Kinesis Video Stream.
Type: [UploaderConfig](API_UploaderConfig.md) object
Required: No

## See Also
<a name="API_EdgeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/EdgeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/EdgeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/EdgeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
