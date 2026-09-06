---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-config-apis.html
---

# Using APIs to create call analytics configurations for the Amazon Chime SDK
<a name="create-config-apis"></a>

You can programmatically create Voice Connectors and call analytics configurations, and then associate them in order to start a call analytics workflow. This guide assumes that you know how to write the code.

The APIs that you use vary, depending on the type of workflow. For example, to record audio, you first call the [CreateMediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipelineConfiguration.html) API to create a call analytics configuration. You then call the [CreateVoiceConnector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnector.html) to create a Voice Connector. Finally, you associate the configuration with a Voice Connector by using the [PutVoiceConnectorStreamingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorStreamingConfiguration.html) API.

In contrast, to record audio with a Kinesis video stream producer, you call [CreateMediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipelineConfiguration.html), and then call the [CreateMediaInsightsPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipeline.html) API.

For more information about using call analytics configurations to enable different workflows, refer to the workflows in [Using call analytics configurations for the Amazon Chime SDK](using-call-analytics-configurations.md), later in this section.
