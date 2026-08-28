---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BotSummary.html
---

# BotSummary
<a name="API_BotSummary"></a>

Summary information about a bot returned by the [ListBots](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBots.html) operation.

## Contents
<a name="API_BotSummary_Contents"></a>

 ** botId **   <a name="lexv2-Type-BotSummary-botId"></a>
The unique identifier assigned to the bot. Use this ID to get detailed information about the bot with the [DescribeBot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBot.html) operation.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: No

 ** botName **   <a name="lexv2-Type-BotSummary-botName"></a>
The name of the bot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

 ** botStatus **   <a name="lexv2-Type-BotSummary-botStatus"></a>
The current status of the bot. When the status is `Available` the bot is ready for use.
Type: String
Valid Values: `Creating | Available | Inactive | Deleting | Failed | Versioning | Importing | Updating`
Required: No

 ** botType **   <a name="lexv2-Type-BotSummary-botType"></a>
The type of the bot.
Type: String
Valid Values: `Bot | BotNetwork`
Required: No

 ** description **   <a name="lexv2-Type-BotSummary-description"></a>
The description of the bot.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** lastUpdatedDateTime **   <a name="lexv2-Type-BotSummary-lastUpdatedDateTime"></a>
The date and time that the bot was last updated.
Type: Timestamp
Required: No

 ** latestBotVersion **   <a name="lexv2-Type-BotSummary-latestBotVersion"></a>
The latest numerical version in use for the bot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^[0-9]+$`
Required: No

## See Also
<a name="API_BotSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BotSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BotSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BotSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
