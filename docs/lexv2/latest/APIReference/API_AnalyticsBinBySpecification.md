---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsBinBySpecification.html
---

# AnalyticsBinBySpecification
<a name="API_AnalyticsBinBySpecification"></a>

Contains the time metric, interval, and method by which to bin the analytics data.

## Contents
<a name="API_AnalyticsBinBySpecification_Contents"></a>

 ** interval **   <a name="lexv2-Type-AnalyticsBinBySpecification-interval"></a>
Specifies the interval of time by which to bin the analytics data.
Type: String
Valid Values: `OneHour | OneDay`
Required: Yes

 ** name **   <a name="lexv2-Type-AnalyticsBinBySpecification-name"></a>
Specifies the time metric by which to bin the analytics data.
Type: String
Valid Values: `ConversationStartTime | UtteranceTimestamp`
Required: Yes

 ** order **   <a name="lexv2-Type-AnalyticsBinBySpecification-order"></a>
Specifies whether to bin the analytics data in ascending or descending order. If this field is left blank, the default order is by the key of the bin in descending order.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## See Also
<a name="API_AnalyticsBinBySpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AnalyticsBinBySpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AnalyticsBinBySpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AnalyticsBinBySpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
