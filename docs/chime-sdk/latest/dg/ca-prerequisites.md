---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-prerequisites.html
---

# Understanding the Amazon Chime SDK call analytics prerequisites
<a name="ca-prerequisites"></a>

Before you create a call analytics configuration, you must have the following items. You can use the AWS console to create them:
+ An Amazon Chime SDK Voice Connector. If not, refer to [Creating Amazon Chime SDK Voice Connectors](https://docs.aws.amazon.com/chime-sdk/latest/ag/ca-prerequisites.html). You must also:
  + Enable streaming for the Voice Connector. For more information, refer to [Automating the Amazon Chime SDK with EventBridge](https://docs.aws.amazon.com/chime-sdk/latest/ag/automating-chime-with-cloudwatch-events.html), in the *Amazon Chime SDK Administrator Guide*
  + Configure the Voice Connector to use call analytics. For more information, refer to [Configuring Voice Connectors to use call analytics](https://docs.aws.amazon.com/chime-sdk/latest/ag/configure-voicecon.html), in the *Amazon Chime SDK Administrator Guide*.
+ Amazon EventBridge targets. If not, see [Monitoring the Amazon Chime SDK with EventBridge](https://docs.aws.amazon.com/chime-sdk/latest/ag/automating-chime-with-cloudwatch-events.html), *Amazon Chime SDK Administrator Guide*.
+ A service-linked role that allows the Voice Connector to access actions on the EventBridge targets. For more information, refer to [Using the Amazon Chime SDK Voice Connector service linked role policy](https://docs.aws.amazon.com/chime-sdk/latest/ag/using-service-linked-roles-stream.html), in the *Amazon Chime SDK Administrator Guide*.
+ An Amazon Kinesis Data Stream. If not, refer to [ Creating and Managing Streams](https://docs.aws.amazon.com/streams/latest/dev/working-with-streams.html), in the *Amazon Kinesis Streams Developer Guide*. Voice analytics and transcription require a Kinesis Data Stream.
+ To analyze calls offline, you must create an Amazon Chime SDK data lake. To do that, refer to [Creating an Amazon Chime SDK data lake](ca-data-lake.md), later in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
