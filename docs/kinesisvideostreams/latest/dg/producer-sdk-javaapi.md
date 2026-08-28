---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-javaapi.html
---

# Use the Java producer library
<a name="producer-sdk-javaapi"></a>

You can use the Amazon Kinesis Video Streams provided Java producer library to write application code with minimal configuration, to send media data from a device to a Kinesis video stream.

Perform the following steps to integrate your code with Kinesis Video Streams so that your application can start streaming data to your Kinesis video stream:

1. Create an instance of the `KinesisVideoClient` object.

1. Create a `MediaSource` object by providing media source information. For example, when creating a camera media source, you provide information such as identifying the camera and specifying the encoding the camera uses.

   When you want to start streaming, you must create a custom media source.

1. Register the media source with `KinesisVideoClient`.

   After you register the media source with `KinesisVideoClient`, whenever the data becomes available with the media source, it calls `KinesisVideoClient` with the data.

## Procedure: Use the Java producer SDK
<a name="producer-sdk-java-using"></a>

This procedure demonstrates how to use the Kinesis Video Streams Java producer client in your Java application to send data to your Kinesis video stream.

These steps don't require you to have a media source, such as a camera or microphone. Instead, for testing purposes, the code generates sample frames that consist of a series of bytes. You can use the same coding pattern when you send media data from real sources such as cameras and microphones.

The procedure includes the following steps:
+ [Download and configure the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-javaapi-downloadcode.html)
+ [Write and examine the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-javaapi-writecode.html)
+ [Run and verify the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-javaapi-reviewcode.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
