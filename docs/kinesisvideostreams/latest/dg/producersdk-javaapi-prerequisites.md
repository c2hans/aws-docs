---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-javaapi-prerequisites.html
---

# Prerequisites
<a name="producersdk-javaapi-prerequisites"></a>

Before you set up the Java producer SDK, ensure that you have the following prerequisites:
+ In the sample code, you provide credentials by specifying a profile that you set up in your AWS credentials profile file. If you haven't already done so, first set up your credentials profile. For more information, see [ Set up AWS Credentials and Region for Development](http://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html) in the *AWS SDK for Java*.
**Note**
The Java example uses a `SystemPropertiesCredentialsProvider` object to obtain your credentials. The provider retrieves these credentials from the `aws.accessKeyId` and `aws.secretKey` Java system properties. You set these system properties in your Java development environment. For information about how to set Java system properties, see the documentation for your particular integrated development environment (IDE).
+ Your `NativeLibraryPath` must contain your `KinesisVideoProducerJNI` file, available at [https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp). The file name extension for this file depends on your operating system:
  + **KinesisVideoProducerJNI.so** for Linux
  + **KinesisVideoProducerJNI.dylib** for macOS
  + **KinesisVideoProducerJNI.dll** for Windows
**Note**
Pre-built libraries for macOS, Ubuntu, Windows, and Raspbian are available in `src/main/resources/lib` at [https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java.git](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java). For other environments, compile the [C\+\+](producer-sdk-cpp.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
