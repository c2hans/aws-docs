---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BotAnalyzerRecommendation.html
---

# BotAnalyzerRecommendation
<a name="API_BotAnalyzerRecommendation"></a>

Contains a recommendation for bot optimization identified by the Bot Analyzer.

## Contents
<a name="API_BotAnalyzerRecommendation_Contents"></a>

 ** issueDescription **   <a name="lexv2-Type-BotAnalyzerRecommendation-issueDescription"></a>
A detailed description of the identified configuration issue.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: Yes

 ** issueLocation **   <a name="lexv2-Type-BotAnalyzerRecommendation-issueLocation"></a>
The location information for the identified issue within the bot configuration.
Type: [IssueLocation](API_IssueLocation.md) object
Required: Yes

 ** priority **   <a name="lexv2-Type-BotAnalyzerRecommendation-priority"></a>
The priority level of the recommendation.
Valid Values: `High | Medium | Low`
Type: String
Valid Values: `High | Medium | Low`
Required: Yes

 ** proposedFix **   <a name="lexv2-Type-BotAnalyzerRecommendation-proposedFix"></a>
The recommended solution to address the identified issue.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: Yes

## See Also
<a name="API_BotAnalyzerRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BotAnalyzerRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BotAnalyzerRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BotAnalyzerRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
