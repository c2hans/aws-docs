---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-building-data-lake-for-games/data-ingestion.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data ingestion
<a name="data-ingestion"></a>

 Game developers collect and process different type of events from various sources. Typical examples include marketing data from the game and third-party services (clicks, installs, impressions) and in-game events. Before you can transform and analyze this data in the data lake, it needs to be ingested into a raw region of the data lake. This chapter discusses different data ingestion mechanisms and design choices.

## Data collection — third-party service or self-made
<a name="data-collection---third-party-service-or-self-made"></a>

 Sometimes game developers develop their own solutions to generate and ingest events. For example, they can develop their own mobile tracker and own the code that generates and ingest events. In this case, they can use the technology stack and data ingestion methods of their choice. However, sometimes game developers rely on partner services to collect data. Examples include mobile attribution services such as AppsFlyer, or third-party mobile trackers such as Amplitude or Google Analytics. An ingest solution depends on data export options that such third-party service provides. The most common is a batch export to an S3 bucket, where you can pick up files from there with a batch extract, transfer, and load (ETL) process.

## Streaming or batch
<a name="streaming-or-batch"></a>

 You can stream events or load them in batches. Streaming means that a game or a partner service ingests events as they are generated. A streaming storage service such as [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) or Apache Kafka stores these events, and consumers can read them in the order of arrival.

 However, ingesting every single event is inefficient - it generates excessive network traffic and might lead to high cost depending on the streaming storage and service used. That’s why some degree of batching is often used with streaming to improve performance. For example, events are sent to a stream after every battle in the game, or once in five minutes.

 Batch ingest means that a pack of events is accumulated on a server, or in a partner service, and then is uploaded as a single file containing multiple events. You can upload directly into a raw region of your data lake, or upload to a separate bucket and apply some kind of transformation when copying to the data lake. The latter is usually used when importing data from third-party services.

 Streaming is a good choice in most cases. Advantages of streaming include:
+  Lower risk of losing events if the client crashes, if there is a network outage (which is normal for mobile games), and so on.
+  Shorter time to report, you don’t need to wait hours for the next batch to have fresh events available in the data lake.
+  Real-time analytics capabilities with a streaming framework such as Apache Flink or Spark Streaming.
+  Support of multiple independent consumers in parallel. For example, you can save data in the data lake and write it to a time-series database at the same time.
+  Cost becomes a factor when we are dealing with large volumes of data (stream or batch). Refer to the pricing page for the respective AWS service to understand the costs associated with per stream, data ingested, data retrievals, and data stored.

 Sometimes batch processing is the option. Advantages of batch include:
+  The ability to stitch together data from multiple data sources with various data formats.
+  The ability to process large or small datasets. Scale cluster size based on dynamic requirements (for example, serverless capability with [AWS Glue](https://aws.amazon.com/glue/features/), [Amazon EMR Serverless](https://aws.amazon.com/emr/serverless/), and [AWS Batch](https://aws.amazon.com/batch/features/) with [AWS Fargate](https://aws.amazon.com/fargate/)).
+  Bound data processing time and resources by a business service-level agreement (SLA) for a cost-efficient workload.

## Client or server
<a name="client-or-server"></a>

Depending on the architecture, you might choose to ingest game events from a game client (such as a mobile device), from a game server, or both. Both methods are popular, and often used together serving different use cases. Events such as users’ interactions with the game can be streamed from a mobile device, and events such as battle results can be streamed from the server.

When streaming from a mobile device, you can use a ready software development kit (SDK) such as Amazon Pinpoint, or develop your own, that can be re-used between games. Such an SDK would have three main responsibilities:
+  Batching events for performance, and providing temporary on-device storage and retries so events are not lost when the device is not connected.
+  Ingesting to a stream in cloud or on-premises, including authentication.
+  Automatically populating demographics data (operating system family, device model) and automatically collecting basic events (such as session start, session stop, and so on).

 Another popular option is to stream from a client is using a third-party SDK that is not connected to a stream, but to a backend provided by a third-party (such as Amplitude or Google Firebase), and export events in batches from their backend. Advantages of such approach include ready-to-use dashboards in the backend service, and easy setup of the SDK and backend. Disadvantages include losing streaming and real-time capabilities.

## REST API or ingesting directly to a stream
<a name="rest-api-or-ingesting-directly-to-a-stream"></a>

 If you choose to build a custom backend for streaming events, you can integrate your game directly with a streaming storage such as Amazon Kinesis or Apache Kafka using a client SDK, or implement a generic REST API in front of the stream.

 Benefits of the REST API include:
+  Decoupling of particular streaming storage technology from an interface. You don’t need to integrate your client or server with a stream and you don’t need AWS SDK on the client for Amazon Kinesis, which might be important for mobile games or platforms such as game consoles.
+  Ease of support for existing games that don’t support direct streaming - you can build an API for them to mimic a legacy data ingestion solution.
+  More authentication and authorization options.

 However, such API requires extra development effort and can be more costly than ingesting directly. Often games developers use a hybrid approach - they ingest directly to a stream (Amazon Kinesis Data Streams or [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/)) from newer games, and implement a REST API layer for legacy games.

## Other sources
<a name="other-sources"></a>

 Sometimes you might need data from other sources, such as operational databases. You can query them directly through services such as [Amazon Athena Federated Queries](https://docs.aws.amazon.com/athena/latest/ug/connect-to-a-data-source.html), or extract data and store it in your data lake using the [AWS Database Migration Service](https://aws.amazon.com/dms/) (AWS DMS). AWS DMS can be configured many ways. One is to offload data from your databases into your data lake on Amazon S3. This can be done in a number of ways that include full load, full load \+ change data capture (CDC), and CDC only. Refer to the [AWS Database Migration Service Documentation](https://docs.aws.amazon.com/dms/) for further details.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
