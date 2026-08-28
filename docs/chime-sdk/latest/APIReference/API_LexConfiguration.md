---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_LexConfiguration.html
---

# LexConfiguration
<a name="API_LexConfiguration"></a>

The configuration for an Amazon Lex V2 bot.

## Contents
<a name="API_LexConfiguration_Contents"></a>

 ** LexBotAliasArn **   <a name="chimesdk-Type-LexConfiguration-LexBotAliasArn"></a>
The ARN of the Amazon Lex V2 bot's alias. The ARN uses this format: `arn:aws:lex:REGION:ACCOUNT:bot-alias/MYBOTID/MYBOTALIAS`
Type: String
Length Constraints: Minimum length of 15. Maximum length of 2048.
Pattern: `arn:aws:lex:[a-z]{2}-[a-z]+-\d{1}:\d{12}:bot-alias/[A-Z0-9]{10}/[A-Z0-9]{10}`
Required: Yes

 ** LocaleId **   <a name="chimesdk-Type-LexConfiguration-LocaleId"></a>
Identifies the Amazon Lex V2 bot's language and locale. The string must match one of the supported locales in Amazon Lex V2. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html) in the *Amazon Lex V2 Developer Guide*.
Type: String
Required: Yes

 ** InvokedBy **   <a name="chimesdk-Type-LexConfiguration-InvokedBy"></a>
Specifies the type of message that triggers a bot.
Type: [InvokedBy](API_InvokedBy.md) object
Required: No

 ** RespondsTo **   <a name="chimesdk-Type-LexConfiguration-RespondsTo"></a>
 **Deprecated**. Use `InvokedBy` instead.
Determines whether the Amazon Lex V2 bot responds to all standard messages. Control messages are not supported.
Type: String
Valid Values: `STANDARD_MESSAGES`
Required: No

 ** WelcomeIntent **   <a name="chimesdk-Type-LexConfiguration-WelcomeIntent"></a>
The name of the welcome intent configured in the Amazon Lex V2 bot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([A-Za-z]_?)+$`
Required: No

## See Also
<a name="API_LexConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/LexConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/LexConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/LexConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
