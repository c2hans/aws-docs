---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_TestSetDiscrepancyReportBotAliasTarget.html
---

# TestSetDiscrepancyReportBotAliasTarget
<a name="API_TestSetDiscrepancyReportBotAliasTarget"></a>

Contains information about the bot alias used for the test set discrepancy report.

## Contents
<a name="API_TestSetDiscrepancyReportBotAliasTarget_Contents"></a>

 ** botAliasId **   <a name="lexv2-Type-TestSetDiscrepancyReportBotAliasTarget-botAliasId"></a>
The unique identifier for the bot associated with the bot alias.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^(\bTSTALIASID\b|[0-9a-zA-Z]+)$`
Required: Yes

 ** botId **   <a name="lexv2-Type-TestSetDiscrepancyReportBotAliasTarget-botId"></a>
The unique identifier for the bot alias.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** localeId **   <a name="lexv2-Type-TestSetDiscrepancyReportBotAliasTarget-localeId"></a>
The unique identifier of the locale associated with the bot alias.
Type: String
Required: Yes

## See Also
<a name="API_TestSetDiscrepancyReportBotAliasTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/TestSetDiscrepancyReportBotAliasTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/TestSetDiscrepancyReportBotAliasTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/TestSetDiscrepancyReportBotAliasTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
