---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_SlackUserIdentity.html
---

# SlackUserIdentity
<a name="API_SlackUserIdentity"></a>

Identifes a user level permission for a channel configuration.

## Contents
<a name="API_SlackUserIdentity_Contents"></a>

 ** ChatConfigurationArn **   <a name="qdevinchatapps-Type-SlackUserIdentity-ChatConfigurationArn"></a>
The Amazon Resource Name (ARN) of the SlackChannelConfiguration associated with the user identity to delete.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 1169.
Pattern: `arn:aws:(wheatley|chatbot):[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** IamRoleArn **   <a name="qdevinchatapps-Type-SlackUserIdentity-IamRoleArn"></a>
A user-defined role that Amazon Q Developer assumes. This is not the service-linked role.
For more information, see [IAM policies for Amazon Q Developer](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1224.
Pattern: `arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** SlackTeamId **   <a name="qdevinchatapps-Type-SlackUserIdentity-SlackTeamId"></a>
The ID of the Slack workspace authorized with Amazon Q Developer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9A-Z]{1,255}`
Required: Yes

 ** SlackUserId **   <a name="qdevinchatapps-Type-SlackUserIdentity-SlackUserId"></a>
The ID of the user in Slack
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(.*)`
Required: Yes

 ** AwsUserIdentity **   <a name="qdevinchatapps-Type-SlackUserIdentity-AwsUserIdentity"></a>
The AWS user identity ARN used to associate a Slack user ID with an IAM Role.
Type: String
Length Constraints: Minimum length of 15. Maximum length of 1101.
Pattern: `arn:aws:(iam|sts)::[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: No

## See Also
<a name="API_SlackUserIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/SlackUserIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/SlackUserIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/SlackUserIdentity)
