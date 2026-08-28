---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BotVersionSummary.html
---

# BotVersionSummary
<a name="API_BotVersionSummary"></a>

Summary information about a bot version returned by the [ListBotVersions](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotVersions.html) operation.

## Contents
<a name="API_BotVersionSummary_Contents"></a>

 ** botName **   <a name="lexv2-Type-BotVersionSummary-botName"></a>
The name of the bot associated with the version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

 ** botStatus **   <a name="lexv2-Type-BotVersionSummary-botStatus"></a>
The status of the bot. When the status is available, the version of the bot is ready for use.
Type: String
Valid Values: `Creating | Available | Inactive | Deleting | Failed | Versioning | Importing | Updating`
Required: No

 ** botVersion **   <a name="lexv2-Type-BotVersionSummary-botVersion"></a>
The numeric version of the bot, or `DRAFT` to indicate that this is the version of the bot that can be updated..
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: No

 ** creationDateTime **   <a name="lexv2-Type-BotVersionSummary-creationDateTime"></a>
A timestamp of the date and time that the version was created.
Type: Timestamp
Required: No

 ** description **   <a name="lexv2-Type-BotVersionSummary-description"></a>
The description of the version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

## See Also
<a name="API_BotVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BotVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BotVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BotVersionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
