---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_Insight.html
---

# Insight
<a name="API_Insight"></a>

Retrieves the list of performance issues which are identified.

## Contents
<a name="API_Insight_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InsightId **   <a name="performanceinsights-Type-Insight-InsightId"></a>
The unique identifier for the insight. For example, `insight-12345678901234567`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** BaselineData **   <a name="performanceinsights-Type-Insight-BaselineData"></a>
 Metric names and values from the timeframe used as baseline to generate the insight.
Type: Array of [Data](API_Data.md) objects
Required: No

 ** Context **   <a name="performanceinsights-Type-Insight-Context"></a>
Indicates if the insight is causal or correlated insight.
Type: String
Valid Values: `CAUSAL | CONTEXTUAL`
Required: No

 ** Description **   <a name="performanceinsights-Type-Insight-Description"></a>
Description of the insight. For example: `A high severity Insight found between 02:00 to 02:30, where there was an unusually high DB load 600x above baseline. Likely performance impact`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8000.
Pattern: `(.|\n)*`
Required: No

 ** EndTime **   <a name="performanceinsights-Type-Insight-EndTime"></a>
The end time of the insight. For example, `2018-10-30T00:00:00Z`.
Type: Timestamp
Required: No

 ** InsightData **   <a name="performanceinsights-Type-Insight-InsightData"></a>
List of data objects containing metrics and references from the time range while generating the insight.
Type: Array of [Data](API_Data.md) objects
Required: No

 ** InsightType **   <a name="performanceinsights-Type-Insight-InsightType"></a>
The type of insight. For example, `HighDBLoad`, `HighCPU`, or `DominatingSQLs`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** Recommendations **   <a name="performanceinsights-Type-Insight-Recommendations"></a>
List of recommendations for the insight. For example, `Investigate the following SQLs that contributed to 100% of the total DBLoad during that time period: sql-id`.
Type: Array of [Recommendation](API_Recommendation.md) objects
Required: No

 ** Severity **   <a name="performanceinsights-Type-Insight-Severity"></a>
The severity of the insight. The values are: `Low`, `Medium`, or `High`.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** StartTime **   <a name="performanceinsights-Type-Insight-StartTime"></a>
The start time of the insight. For example, `2018-10-30T00:00:00Z`.
Type: Timestamp
Required: No

 ** SupportingInsights **   <a name="performanceinsights-Type-Insight-SupportingInsights"></a>
List of supporting insights that provide additional factors for the insight.
Type: Array of [Insight](#API_Insight) objects
Required: No

## See Also
<a name="API_Insight_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/Insight)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/Insight)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/Insight)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS Performance Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query performance-insights` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
