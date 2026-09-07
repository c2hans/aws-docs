---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/what-is-amazon-chime-sdk-call-analytics.html
---

# What is Amazon Chime SDK call analytics
<a name="what-is-amazon-chime-sdk-call-analytics"></a>

Amazon Chime SDK call analytics is a low-code solution for generating cost-effective insights from real-time audio, including capabilities for audio ingestion, recording, voice analytics, alerting, and a data lake. You can generate machine learning powered insights using call analytics by creating a reusable call analytics configuration that determines which AWS machine learning integrations and audio processing features to enable for a workflow. You then use the call analytics configuration with various media sources such as Voice Connectors or Amazon Kinesis Video Streams. Call analytics generates insights through integrations with Amazon Transcribe and Transcribe call analytics (TCA), and natively through [Amazon Chime SDK voice analytics](voice-analytics.md), a service that runs under call analytics.

You follow these steps to use call analytics:

![Image showing the process of setting up Amazon Chime SDK call analytics.](https://docs.aws.amazon.com/chime-sdk/latest/dg/images/CallAnalyticsOverview.png)

In the diagram:

1. You start by creating a call analytics configuration.

1. You set your output destinations and an optional data lake.

1. You create workflows that associate your configuration with a Voice Connector and Amazon Kinesis Video Streams.

1. You analyze and optionally visualize your insights.

You can use the Amazon Chime SDK console to create a call analytics configuration and enable call analytics to start automatically. If you need to control the configurations that apply to a given type of call, you use APIs to create a configuration. Either way, the configuration contains details about the AWS machine learning services to invoke for the call audio, enable call recording, and the destinations for the insights, metadata, and recordings. Call analytics provides the following destinations:
+ An Amazon Kinesis Data Stream (KDS). You can use KDS to receive live call insights that you can then integrate into your application. For instance, you can integrate the live insights to help a sales or customer-support agent during a customer call, or use the insights to augment generative AI prompts and summaries.
+ An Amazon S3 bucket configured as a data warehouse. The bucket stores data in Parquet format. Parquet is an open-source file format designed to compress and store large volumes of data. You can then use Amazon Athena to query that data using simple query language (SQL), or move the data to your existing data warehouse to pair up with your business data. For example, you can perform post-call aggregate analytics to understand effectiveness of the customer calls, problems areas of a product, or opportunities to train employees to achieve better customer outcomes.

In addition to those destinations, call analytics also supports real-time alerts that you can preconfigure, based on the insights. The alerts are sent to Amazon EventBridge.

**Note**
When you create a call analytics configuration, you don't select a specific audio source. That allows you to reuse configurations across multiple audio sources. For example, a configuration can enable call recording and provide call transcription. You can then use the configuration with a Chime SDK Voice Connector and an audio stream via a Kinesis Video Stream. You can also share the configuration among multiple Voice Connectors. Each call analytics configuration is unique and identified by an ARN.
