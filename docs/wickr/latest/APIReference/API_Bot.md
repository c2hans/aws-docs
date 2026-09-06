---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_Bot.html
---

# Bot
<a name="API_Bot"></a>

Represents a bot account in a Wickr network with all its informational fields.

## Contents
<a name="API_Bot_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** botId **   <a name="wickr-Type-Bot-botId"></a>
The unique identifier of the bot.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** displayName **   <a name="wickr-Type-Bot-displayName"></a>
The display name of the bot that is visible to users.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** groupId **   <a name="wickr-Type-Bot-groupId"></a>
The ID of the security group to which the bot belongs.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** hasChallenge **   <a name="wickr-Type-Bot-hasChallenge"></a>
Indicates whether the bot has a password set.
Type: Boolean
Required: No

 ** lastLogin **   <a name="wickr-Type-Bot-lastLogin"></a>
The timestamp of the bot's last login.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** pubkey **   <a name="wickr-Type-Bot-pubkey"></a>
The public key of the bot used for encryption.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** status **   <a name="wickr-Type-Bot-status"></a>
The current status of the bot (1 for pending, 2 for active).
Type: Integer
Required: No

 ** suspended **   <a name="wickr-Type-Bot-suspended"></a>
Indicates whether the bot is currently suspended.
Type: Boolean
Required: No

 ** uname **   <a name="wickr-Type-Bot-uname"></a>
The unique username hash identifier for the bot.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** username **   <a name="wickr-Type-Bot-username"></a>
The username of the bot.
Type: String
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_Bot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/Bot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/Bot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/Bot)
