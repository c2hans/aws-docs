---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsIntentNodeSummary.html
---

# AnalyticsIntentNodeSummary
<a name="API_AnalyticsIntentNodeSummary"></a>

An object containing information about the requested path.

## Contents
<a name="API_AnalyticsIntentNodeSummary_Contents"></a>

 ** intentCount **   <a name="lexv2-Type-AnalyticsIntentNodeSummary-intentCount"></a>
The total number of sessions that follow the given path to the given intent.
Type: Integer
Required: No

 ** intentLevel **   <a name="lexv2-Type-AnalyticsIntentNodeSummary-intentLevel"></a>
The number of intents up to and including the requested path.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** intentName **   <a name="lexv2-Type-AnalyticsIntentNodeSummary-intentName"></a>
The name of the intent at the end of the requested path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

 ** intentPath **   <a name="lexv2-Type-AnalyticsIntentNodeSummary-intentPath"></a>
The path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** nodeType **   <a name="lexv2-Type-AnalyticsIntentNodeSummary-nodeType"></a>
Specifies whether the node is the end of a path (`Exit`) or not (`Inner`).
Type: String
Valid Values: `Inner | Exit`
Required: No

## See Also
<a name="API_AnalyticsIntentNodeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AnalyticsIntentNodeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AnalyticsIntentNodeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AnalyticsIntentNodeSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
