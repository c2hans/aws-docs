---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/creating-ca-configuration.html
---

# Creating call analytics configurations for the Amazon Chime SDK
<a name="creating-ca-configuration"></a>

To use call analytics, you start by creating a *configuration*, a static structure that holds the information needed to create a call analytics pipeline. You can use the Amazon Chime SDK console to create a configuration, or call the [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipelineConfiguration.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipelineConfiguration.html) API.

A call analytics configuration includes details about audio processors, such as recording, voice analytics, or Amazon Transcribe. It also includes insight destinations and alert event configurations. Optionally, you can save your call data to an Amazon S3 bucket for further analysis.

However, *configurations do not include specific audio sources*. That allows you reuse the configuration across multiple call analytics workflows. For example, you can use the same call analytics configuration with different Voice Connectors or across different Amazon Kinesis Video Stream (KVS) sources.

You use the configurations to create pipelines when SIP calls occur through a Voice Connector, or when new media is sent to an Amazon Kinesis Video Stream (KVS). The pipelines, in turn, process the media according to the specifications in the configuration.

You can stop a pipeline programmatically at any time. Pipelines also stop processing media when a Voice Connector call ends. In addition, you can pause a pipeline. Doing so disables calls to the underlying Amazon machine learning services and resumes them when desired. However, call recording runs while you pause a pipeline.

The following sections explain the prerequisites for creating a call analytics configuration, and how to create one.

**Topics**
+ [Understanding the Amazon Chime SDK call analytics prerequisites](ca-prerequisites.md)
+ [Using the Amazon Chime SDK console to create call analytics configurations](create-config-console.md)
+ [Using APIs to create call analytics configurations for the Amazon Chime SDK](create-config-apis.md)
+ [Associating a configuration with a Voice Connector for the Amazon Chime SDK](ca-associate-vc-steps.md)

For more information about call analytics configurations, refer to [Managing call analytics](https://docs.aws.amazon.com/chime-sdk/latest/ag/ag-call-analytics.html) in the *Amazon Chime SDK Administrator Guide*.

For more information about using call analytics configurations to enable different workflows, refer to [Using call analytics configurations for the Amazon Chime SDK](using-call-analytics-configurations.md), later in this section.
