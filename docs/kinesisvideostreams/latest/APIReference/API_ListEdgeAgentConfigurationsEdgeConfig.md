---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_ListEdgeAgentConfigurationsEdgeConfig.html
---

# ListEdgeAgentConfigurationsEdgeConfig
<a name="API_ListEdgeAgentConfigurationsEdgeConfig"></a>

A description of a single stream's edge configuration.

## Contents
<a name="API_ListEdgeAgentConfigurationsEdgeConfig_Contents"></a>

 ** CreationTime **   <a name="KinesisVideo-Type-ListEdgeAgentConfigurationsEdgeConfig-CreationTime"></a>
The timestamp when the stream first created the edge config.
Type: Timestamp
Required: No

 ** EdgeConfig **   <a name="KinesisVideo-Type-ListEdgeAgentConfigurationsEdgeConfig-EdgeConfig"></a>
A description of the stream's edge configuration that will be used to sync with the Edge Agent IoT Greengrass component. The Edge Agent component will run on an IoT Hub Device setup at your premise.
Type: [EdgeConfig](API_EdgeConfig.md) object
Required: No

 ** FailedStatusDetails **   <a name="KinesisVideo-Type-ListEdgeAgentConfigurationsEdgeConfig-FailedStatusDetails"></a>
A description of the generated failure status.
Type: String
Required: No

 ** LastUpdatedTime **   <a name="KinesisVideo-Type-ListEdgeAgentConfigurationsEdgeConfig-LastUpdatedTime"></a>
The timestamp when the stream last updated the edge config.
Type: Timestamp
Required: No

 ** StreamARN **   <a name="KinesisVideo-Type-ListEdgeAgentConfigurationsEdgeConfig-StreamARN"></a>
The Amazon Resource Name (ARN) of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`
Required: No

 ** StreamName **   <a name="KinesisVideo-Type-ListEdgeAgentConfigurationsEdgeConfig-StreamName"></a>
The name of the stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** SyncStatus **   <a name="KinesisVideo-Type-ListEdgeAgentConfigurationsEdgeConfig-SyncStatus"></a>
The current sync status of the stream's edge configuration.
Type: String
Valid Values: `SYNCING | ACKNOWLEDGED | IN_SYNC | SYNC_FAILED | DELETING | DELETE_FAILED | DELETING_ACKNOWLEDGED`
Required: No

## See Also
<a name="API_ListEdgeAgentConfigurationsEdgeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/ListEdgeAgentConfigurationsEdgeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/ListEdgeAgentConfigurationsEdgeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/ListEdgeAgentConfigurationsEdgeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
