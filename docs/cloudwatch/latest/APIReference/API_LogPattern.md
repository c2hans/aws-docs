---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_LogPattern.html
---

# LogPattern
<a name="API_LogPattern"></a>

An object that defines the log patterns that belongs to a `LogPatternSet`.

## Contents
<a name="API_LogPattern_Contents"></a>

 ** Pattern **   <a name="appinsights-Type-LogPattern-Pattern"></a>
A regular expression that defines the log pattern. A log pattern can contain as many as 50 characters, and it cannot be empty. The pattern must be DFA compatible. Patterns that utilize forward lookahead or backreference constructions are not supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\S\s]+`
Required: No

 ** PatternName **   <a name="appinsights-Type-LogPattern-PatternName"></a>
The name of the log pattern. A log pattern name can contain as many as 50 characters, and it cannot be empty. The characters can be Unicode letters, digits, or one of the following symbols: period, dash, underscore.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: No

 ** PatternSetName **   <a name="appinsights-Type-LogPattern-PatternSetName"></a>
The name of the log pattern. A log pattern name can contain as many as 30 characters, and it cannot be empty. The characters can be Unicode letters, digits, or one of the following symbols: period, dash, underscore.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: No

 ** Rank **   <a name="appinsights-Type-LogPattern-Rank"></a>
Rank of the log pattern. Must be a value between `1` and `1,000,000`. The patterns are sorted by rank, so we recommend that you set your highest priority patterns with the lowest rank. A pattern of rank `1` will be the first to get matched to a log line. A pattern of rank `1,000,000` will be last to get matched. When you configure custom log patterns from the console, a `Low` severity pattern translates to a `750,000` rank. A `Medium` severity pattern translates to a `500,000` rank. And a `High` severity pattern translates to a `250,000` rank. Rank values less than `1` or greater than `1,000,000` are reserved for AWS provided patterns.
Type: Integer
Required: No

## See Also
<a name="API_LogPattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/LogPattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/LogPattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/LogPattern)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
