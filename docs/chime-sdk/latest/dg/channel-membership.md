---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/channel-membership.html
---

# Creating a channel membership for an AppInstanceBot for Amazon Chime SDK messaging
<a name="channel-membership"></a>

Once you create the AppInstanceBot, you add it as a member to a new or existing channel. For more information see [CreateChannel](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannel.html) and [ CreateChannelMembership](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelMembership.html) in the *Amazon Chime SDK messaging API* documentation.

The following example shows how to use the AWS CLI to create a channel and add an `AppInstanceBot` as a member.

```
aws chime-sdk-messaging create-channel \
--chime-bearer {{caller_app_instance_user_arn}} \
--app-instance-arn {{app_instance_arn}} \
--name {{channel_name}} \
--member-arns '[
   "{{app_instance_bot_arn}}"
]'
```

The following example shows how to use the AWS CLI to add an `AppInstanceBot` to an existing channel.

```
aws chime-sdk-messaging create-channel-membership \
--chime-bearer {{caller_app_instance_user_arn}} \
--channel-arn {{channel_arn}} \
--member-arn {{app_instance_bot_arn}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
