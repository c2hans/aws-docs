---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_TeamsUserIdentity.html
---

# TeamsUserIdentity
<a name="API_TeamsUserIdentity"></a>

Identifes a user level permission for a channel configuration.

## Contents
<a name="API_TeamsUserIdentity_Contents"></a>

 ** ChatConfigurationArn **   <a name="qdevinchatapps-Type-TeamsUserIdentity-ChatConfigurationArn"></a>
The Amazon Resource Name (ARN) of the MicrosoftTeamsChannelConfiguration associated with the user identity to delete.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 1169.
Pattern: `arn:aws:(wheatley|chatbot):[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** IamRoleArn **   <a name="qdevinchatapps-Type-TeamsUserIdentity-IamRoleArn"></a>
A user-defined role that Amazon Q Developer assumes. This is not the service-linked role.
For more information, see [IAM policies for Amazon Q Developer](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** TeamId **   <a name="qdevinchatapps-Type-TeamsUserIdentity-TeamId"></a>
 The ID of the Microsoft Teams authorized with Amazon Q Developer.
To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the Amazon Q Developer console. Then you can copy and paste the team ID from the console. For more information, see [Step 1: Configure a Microsoft Teams client](https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}`
Required: Yes

 ** AwsUserIdentity **   <a name="qdevinchatapps-Type-TeamsUserIdentity-AwsUserIdentity"></a>
The AWS user identity ARN used to associate a Microsoft Teams user Identity with an IAM Role.
Type: String
Length Constraints: Minimum length of 15. Maximum length of 1101.
Pattern: `arn:aws:(iam|sts)::[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: No

 ** TeamsChannelId **   <a name="qdevinchatapps-Type-TeamsUserIdentity-TeamsChannelId"></a>
The ID of the Microsoft Teams channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9-_=+\/.,])*%3[aA]([a-zA-Z0-9-_=+\/.,])*%40([a-zA-Z0-9-_=+\/.,])*`
Required: No

 ** TeamsTenantId **   <a name="qdevinchatapps-Type-TeamsUserIdentity-TeamsTenantId"></a>
The ID of the Microsoft Teams tenant.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}`
Required: No

 ** UserId **   <a name="qdevinchatapps-Type-TeamsUserIdentity-UserId"></a>
The Microsoft Teams user ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}`
Required: No

## See Also
<a name="API_TeamsUserIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/TeamsUserIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/TeamsUserIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/TeamsUserIdentity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
