---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_TeamsChannelConfiguration.html
---

# TeamsChannelConfiguration
<a name="API_TeamsChannelConfiguration"></a>

An Amazon Q Developer configuration for Microsoft Teams.

## Contents
<a name="API_TeamsChannelConfiguration_Contents"></a>

 ** ChannelId **   <a name="qdevinchatapps-Type-TeamsChannelConfiguration-ChannelId"></a>
The ID of the Microsoft Teams channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9-_=+\/.,])*%3[aA]([a-zA-Z0-9-_=+\/.,])*%40([a-zA-Z0-9-_=+\/.,])*`
Required: Yes

 ** ChatConfigurationArn **   <a name="qdevinchatapps-Type-TeamsChannelConfiguration-ChatConfigurationArn"></a>
The Amazon Resource Name (ARN) of the MicrosoftTeamsChannelConfiguration associated with the user identity to delete.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 1169.
Pattern: `arn:aws:(wheatley|chatbot):[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** IamRoleArn **   <a name="qdevinchatapps-Type-TeamsChannelConfiguration-IamRoleArn"></a>
A user-defined role that Amazon Q Developer assumes. This is not the service-linked role.
For more information, see [IAM policies for Amazon Q Developer](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** SnsTopicArns **   <a name="qdevinchatapps-Type-TeamsChannelConfiguration-SnsTopicArns"></a>
The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to Amazon Q Developer.
Type: Array of strings
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** TeamId **   <a name="qdevinchatapps-Type-TeamsChannelConfiguration-TeamId"></a>
 The ID of the Microsoft Teams authorized with Amazon Q Developer.
To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the Amazon Q Developer console. Then you can copy and paste the team ID from the console. For more information, see [Step 1: Configure a Microsoft Teams client](https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}`
Required: Yes

 ** TenantId **   <a name="qdevinchatapps-Type-TeamsChannelConfiguration-TenantId"></a>
The ID of the Microsoft Teams tenant.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}`
Required: Yes

 ** ChannelName **   <a name="qdevinchatapps-Type-TeamsChannelConfiguration-ChannelName"></a>
The name of the Microsoft Teams channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(.*)`
Required: No

 ** ConfigurationName **   <a name="qdevinchatapps-Type-TeamsChannelConfiguration-ConfigurationName"></a>
The name of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_]+`
Required: No

 ** GuardrailPolicyArns **   <a name="qdevinchatapps-Type-TeamsChannelConfiguration-GuardrailPolicyArns"></a>
The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed `AdministratorAccess` policy is applied by default if this is not set.
Type: Array of strings
Length Constraints: Minimum length of 11. Maximum length of 1163.
Pattern: `(^$|(?!.*\/aws-service-role\/.*)arn:aws:iam:[A-Za-z0-9_\/.-]{0,63}:[A-Za-z0-9_\/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_\/+=,@.-]{0,1023})`
Required: No

 ** LoggingLevel **   <a name="qdevinchatapps-Type-TeamsChannelConfiguration-LoggingLevel"></a>
Logging levels include `ERROR`, `INFO`, or `NONE`.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 5.
Pattern: `(ERROR|INFO|NONE)`
Required: No

 ** State **   <a name="qdevinchatapps-Type-TeamsChannelConfiguration-State"></a>
Either `ENABLED` or `DISABLED`. The resource returns `DISABLED` if the organization's Amazon Q Developer policy has explicitly denied that configuration. For example, if Amazon Chime is disabled.
Type: String
Pattern: `(ENABLED|DISABLED)`
Required: No

 ** StateReason **   <a name="qdevinchatapps-Type-TeamsChannelConfiguration-StateReason"></a>
Provided if State is `DISABLED`. Provides context as to why the resource is disabled.
Type: String
Required: No

 ** Tags **   <a name="qdevinchatapps-Type-TeamsChannelConfiguration-Tags"></a>
A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TeamName **   <a name="qdevinchatapps-Type-TeamsChannelConfiguration-TeamName"></a>
The name of the Microsoft Teams Team.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(.*)`
Required: No

 ** UserAuthorizationRequired **   <a name="qdevinchatapps-Type-TeamsChannelConfiguration-UserAuthorizationRequired"></a>
Enables use of a user role requirement in your chat configuration.
Type: Boolean
Required: No

## See Also
<a name="API_TeamsChannelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/TeamsChannelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/TeamsChannelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/TeamsChannelConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
