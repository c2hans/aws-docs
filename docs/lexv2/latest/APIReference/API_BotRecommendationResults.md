---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BotRecommendationResults.html
---

# BotRecommendationResults
<a name="API_BotRecommendationResults"></a>

The object representing the URL of the bot definition, the URL of the associated transcript, and a statistical summary of the bot recommendation results.

## Contents
<a name="API_BotRecommendationResults_Contents"></a>

 ** associatedTranscriptsUrl **   <a name="lexv2-Type-BotRecommendationResults-associatedTranscriptsUrl"></a>
The presigned url link of the associated transcript.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** botLocaleExportUrl **   <a name="lexv2-Type-BotRecommendationResults-botLocaleExportUrl"></a>
The presigned URL link of the recommended bot definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** statistics **   <a name="lexv2-Type-BotRecommendationResults-statistics"></a>
The statistical summary of the bot recommendation results.
Type: [BotRecommendationResultStatistics](API_BotRecommendationResultStatistics.md) object
Required: No

## See Also
<a name="API_BotRecommendationResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BotRecommendationResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BotRecommendationResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BotRecommendationResults)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
