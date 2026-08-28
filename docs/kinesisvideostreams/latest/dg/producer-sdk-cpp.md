---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-cpp.html
---

# Use the C\+\+ producer library
<a name="producer-sdk-cpp"></a>

You can use the Amazon Kinesis Video Streams provided C\+\+ producer library to write application code to send media data from a device to a Kinesis video stream.

## Object model
<a name="producer-sdk-cpp-objectmodel"></a>

The C\+\+ library provides the following objects to manage sending data to a Kinesis video stream:
+ **KinesisVideoProducer:** Contains information about your media source and AWS credentials, and maintains callbacks to report on Kinesis Video Streams events.
+ **KinesisVideoStream:** Represents the Kinesis video stream. Contains information about the video stream's parameters, such as name, data retention period, and media content type.

## Put media into the stream
<a name="producer-sdk-cpp-putframe"></a>

You can use the C\+\+ library provided methods (for example, `PutFrame`) to put data into the `KinesisVideoStream` object. The library then manages the internal state of the data, which can include the following tasks:
+ Performing authentication.
+ Watching for network latency. If the latency is too high, the library might choose to drop frames.
+ Tracking status of streaming in progress.

## Callback interfaces
<a name="producer-sdk-cpp-callbacks"></a>

This layer exposes a set of callback interfaces, which enable it to talk to the application layer. These callback interfaces include the following:

+ **Service callbacks interface (`CallbackProvider`): **The library invokes events obtained through this interface when it creates a stream, obtains a stream description, and deletes a stream.
+ **Client-ready state or low storage events interface (`ClientCallbackProvider`):** The library invokes events on this interface when the client is ready, or when it detects that it might run out of available storage or memory.
+ **Stream events callback interface (`StreamCallbackProvider`):** The library invokes events on this interface when stream events occur, such as the stream entering the ready state, dropped frames, or stream errors.

Kinesis Video Streams provides default implementations for these interfaces. You can also provide your own custom implementation—for example, if you need custom networking logic or you want to expose a low storage condition to the user interface.

For more information about callbacks in the producer libraries, see [Producer SDK callbacks](producer-reference-callbacks.md).

## Procedure: Use the C\+\+ producer SDK
<a name="producer-sdk-cpp-using"></a>

This procedure demonstrates how to use the Kinesis Video Streams client and media sources in a C\+\+ application to send data to your Kinesis video stream.

The procedure includes the following steps:

**Topics**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
