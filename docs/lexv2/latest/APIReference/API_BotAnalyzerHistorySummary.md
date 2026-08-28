---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BotAnalyzerHistorySummary.html
---

# BotAnalyzerHistorySummary
<a name="API_BotAnalyzerHistorySummary"></a>

Contains summary information about a historical bot analysis execution.

## Contents
<a name="API_BotAnalyzerHistorySummary_Contents"></a>

 ** botAnalyzerRequestId **   <a name="lexv2-Type-BotAnalyzerHistorySummary-botAnalyzerRequestId"></a>
The unique identifier for the analysis request.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** botAnalyzerStatus **   <a name="lexv2-Type-BotAnalyzerHistorySummary-botAnalyzerStatus"></a>
The status of the historical analysis execution.
Valid Values: `Processing | Available | Failed | Stopping | Stopped`
Type: String
Valid Values: `Processing | Available | Failed | Stopping | Stopped`
Required: Yes

 ** creationDateTime **   <a name="lexv2-Type-BotAnalyzerHistorySummary-creationDateTime"></a>
The date and time when the analysis was initiated.
Type: Timestamp
Required: No

## See Also
<a name="API_BotAnalyzerHistorySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BotAnalyzerHistorySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BotAnalyzerHistorySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BotAnalyzerHistorySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
