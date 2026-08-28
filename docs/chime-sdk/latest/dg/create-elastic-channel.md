---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-elastic-channel.html
---

# Creating elastic channels for Amazon Chime SDK meetings
<a name="create-elastic-channel"></a>

You use the `ElasticChannelConfiguration` field in the [CreateChannel](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannel.html) API to create an elastic channel. Once you create an elastic channel, you create channel memberships.

**Note**
For non-elastic channels, the `AppInstanceUser` that creates the channel is automatically added to that channel as a member and moderator. For elastic channels, the channel creator is only added as a moderator.
You can't update an `ElasticChannelConfiguration` once set.
You can't update a channel from elastic to non-elastic and vice-versa.
You can't include a list of member ARNs in a [CreateChannel](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannel.html) API request. However, you can include a list of moderator ARNs.
You can't create an `UNRESTRICTED` type elastic channel.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
