---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-channel-flow.html
---

# Creating a channel flow for Amazon Chime SDK messaging
<a name="create-channel-flow"></a>

Once you have processor(s) setup, you use the Amazon Chime SDK Messaging APIs to create a channel flow. You can use a `Fallback` action to define whether to stop or continue processing if the channel flow can't connect to the processor Lambda function. If a processor has a fallback action of `ABORT`, the processor sets the message status to `FAILED`, and it doesn't send the message. Note that if the last processor in the channel flow sequence has a fallback action of `CONTINUE`, the message is considered processed and sent to recipients in the channel. Once you create a channel flow, you can associate it with individual channels. For more information, refer to the [CreateChannelFlow](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelFlow.html) API documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
