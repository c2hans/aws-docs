---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-android.html
---

# Use the Android producer library
<a name="producer-sdk-android"></a>

You can use the Amazon Kinesis Video Streams provided Android producer library to write application code, with minimal configuration, to send media data from an Android device to a Kinesis video stream.

Perform the following steps to integrate your code with Kinesis Video Streams so that your application can start streaming data to your Kinesis video stream:

1. Create an instance of the `KinesisVideoClient` object.

1. Create a `MediaSource` object by providing media source information. For example, when creating a camera media source, you provide information such as identifying the camera and specifying the encoding the camera uses.

   When you want to start streaming, you must create a custom media source.

## Procedure: Use the Android producer SDK
<a name="producer-sdk-android-using"></a>

This procedure demonstrates how to use the Kinesis Video Streams Android producer client in your Android application to send data to your Kinesis video stream.

The procedure includes the following steps:
+ [Prerequisites](producersdk-android-prerequisites.md)
+ [Download and configure the Android producer library code](producersdk-android-downloadcode.md)
+ [Examine the code](producersdk-android-writecode.md)
+ [Run and verify the code](producersdk-android-reviewcode.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
