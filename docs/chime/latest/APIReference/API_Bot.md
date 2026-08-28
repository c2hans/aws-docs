---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_Bot.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# Bot
<a name="API_Bot"></a>

A resource that allows Enterprise account administrators to configure an interface to receive events from Amazon Chime.

## Contents
<a name="API_Bot_Contents"></a>

 ** BotEmail **   <a name="chime-Type-Bot-BotEmail"></a>
The bot email address.
Type: String
Required: No

 ** BotId **   <a name="chime-Type-Bot-BotId"></a>
The bot ID.
Type: String
Required: No

 ** BotType **   <a name="chime-Type-Bot-BotType"></a>
The bot type.
Type: String
Valid Values: `ChatBot`
Required: No

 ** CreatedTimestamp **   <a name="chime-Type-Bot-CreatedTimestamp"></a>
The bot creation timestamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** Disabled **   <a name="chime-Type-Bot-Disabled"></a>
When true, the bot is stopped from running in your account.
Type: Boolean
Required: No

 ** DisplayName **   <a name="chime-Type-Bot-DisplayName"></a>
The bot display name.
Type: String
Required: No

 ** SecurityToken **   <a name="chime-Type-Bot-SecurityToken"></a>
The security token used to authenticate Amazon Chime with the outgoing event endpoint.
Type: String
Required: No

 ** UpdatedTimestamp **   <a name="chime-Type-Bot-UpdatedTimestamp"></a>
The updated bot timestamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** UserId **   <a name="chime-Type-Bot-UserId"></a>
The unique ID for the bot user.
Type: String
Required: No

## See Also
<a name="API_Bot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/Bot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/Bot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/Bot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
