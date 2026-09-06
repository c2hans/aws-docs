---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_SlackChannelConfiguration.html
---

# SlackChannelConfiguration
<a name="API_SlackChannelConfiguration"></a>

An Amazon Q Developer configuration for Slack.

## Contents
<a name="API_SlackChannelConfiguration_Contents"></a>

 ** ChatConfigurationArn **   <a name="qdevinchatapps-Type-SlackChannelConfiguration-ChatConfigurationArn"></a>
The Amazon Resource Name (ARN) of the SlackChannelConfiguration.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 1169.
Pattern: `arn:aws:(wheatley|chatbot):[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** IamRoleArn **   <a name="qdevinchatapps-Type-SlackChannelConfiguration-IamRoleArn"></a>
A user-defined role that Amazon Q Developer assumes. This is not the service-linked role.
For more information, see [IAM policies for Amazon Q Developer](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** SlackChannelId **   <a name="qdevinchatapps-Type-SlackChannelConfiguration-SlackChannelId"></a>
The ID of the Slack channel.
To get this ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ABCBBLZZZ.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9]+`
Required: Yes

 ** SlackChannelName **   <a name="qdevinchatapps-Type-SlackChannelConfiguration-SlackChannelName"></a>
The name of the Slack channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** SlackTeamId **   <a name="qdevinchatapps-Type-SlackChannelConfiguration-SlackTeamId"></a>
The ID of the Slack workspace authorized with Amazon Chime.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9A-Z]{1,255}`
Required: Yes

 ** SlackTeamName **   <a name="qdevinchatapps-Type-SlackChannelConfiguration-SlackTeamName"></a>
Name of the Slack workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** SnsTopicArns **   <a name="qdevinchatapps-Type-SlackChannelConfiguration-SnsTopicArns"></a>
The ARNs of the SNS topics that deliver notifications to Amazon Q Developer.
Type: Array of strings
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** ConfigurationName **   <a name="qdevinchatapps-Type-SlackChannelConfiguration-ConfigurationName"></a>
The name of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_]+`
Required: No

 ** GuardrailPolicyArns **   <a name="qdevinchatapps-Type-SlackChannelConfiguration-GuardrailPolicyArns"></a>
The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed `AdministratorAccess` policy is applied by default if this is not set.
Type: Array of strings
Length Constraints: Minimum length of 11. Maximum length of 1163.
Pattern: `(^$|(?!.*\/aws-service-role\/.*)arn:aws:iam:[A-Za-z0-9_\/.-]{0,63}:[A-Za-z0-9_\/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_\/+=,@.-]{0,1023})`
Required: No

 ** LoggingLevel **   <a name="qdevinchatapps-Type-SlackChannelConfiguration-LoggingLevel"></a>
Logging levels include `ERROR`, `INFO`, or `NONE`.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 5.
Pattern: `(ERROR|INFO|NONE)`
Required: No

 ** State **   <a name="qdevinchatapps-Type-SlackChannelConfiguration-State"></a>
Either `ENABLED` or `DISABLED`. The resource returns `DISABLED` if the organization's Amazon Q Developer policy has explicitly denied that configuration. For example, if Amazon Chime is disabled.
Type: String
Pattern: `(ENABLED|DISABLED)`
Required: No

 ** StateReason **   <a name="qdevinchatapps-Type-SlackChannelConfiguration-StateReason"></a>
Provided if State is `DISABLED`. Provides context as to why the resource is disabled.
Type: String
Required: No

 ** Tags **   <a name="qdevinchatapps-Type-SlackChannelConfiguration-Tags"></a>
A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** UserAuthorizationRequired **   <a name="qdevinchatapps-Type-SlackChannelConfiguration-UserAuthorizationRequired"></a>
Enables use of a user role requirement in your chat configuration.
Type: Boolean
Required: No

## See Also
<a name="API_SlackChannelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/SlackChannelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/SlackChannelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/SlackChannelConfiguration)
