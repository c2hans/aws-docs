---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BotAliasTestExecutionTarget.html
---

# BotAliasTestExecutionTarget
<a name="API_BotAliasTestExecutionTarget"></a>

The target Amazon S3 location for the test set execution using a bot alias.

## Contents
<a name="API_BotAliasTestExecutionTarget_Contents"></a>

 ** botAliasId **   <a name="lexv2-Type-BotAliasTestExecutionTarget-botAliasId"></a>
The bot alias Id of the bot alias used in the test set execution.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^(\bTSTALIASID\b|[0-9a-zA-Z]+)$`
Required: Yes

 ** botId **   <a name="lexv2-Type-BotAliasTestExecutionTarget-botId"></a>
The bot Id of the bot alias used in the test set execution.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** localeId **   <a name="lexv2-Type-BotAliasTestExecutionTarget-localeId"></a>
The locale Id of the bot alias used in the test set execution.
Type: String
Required: Yes

## See Also
<a name="API_BotAliasTestExecutionTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BotAliasTestExecutionTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BotAliasTestExecutionTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BotAliasTestExecutionTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
