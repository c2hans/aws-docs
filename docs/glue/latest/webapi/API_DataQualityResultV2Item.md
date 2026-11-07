---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityResultV2Item.html
---

# DataQualityResultV2Item
<a name="API_DataQualityResultV2Item"></a>

Describes a data quality result returned by `BatchGetDataQualityResultV2`.

## Contents
<a name="API_DataQualityResultV2Item_Contents"></a>

 ** ResultId **   <a name="Glue-Type-DataQualityResultV2Item-ResultId"></a>
A unique result ID for the data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** AggregatedMetrics **   <a name="Glue-Type-DataQualityResultV2Item-AggregatedMetrics"></a>
A summary of `DataQualityAggregatedMetrics` objects showing the total counts of processed rows and rules, including their pass/fail statistics based on row-level results.
Type: [DataQualityAggregatedMetrics](API_DataQualityAggregatedMetrics.md) object
Required: No

 ** AnalyzerResults **   <a name="Glue-Type-DataQualityResultV2Item-AnalyzerResults"></a>
A list of `DataQualityAnalyzerResult` objects representing the results for each analyzer.
Type: Array of [DataQualityAnalyzerResult](API_DataQualityAnalyzerResult.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2000 items.
Required: No

 ** DataSource **   <a name="Glue-Type-DataQualityResultV2Item-DataSource"></a>
The table associated with the data quality result, if any.
Type: [DataSource](API_DataSource.md) object
Required: No

 ** Descriptors **   <a name="Glue-Type-DataQualityResultV2Item-Descriptors"></a>
A map of user-provided descriptors that add contextual metadata and configuration to the data quality result, such as database name, table name, team, or environment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Dimensions **   <a name="Glue-Type-DataQualityResultV2Item-Dimensions"></a>
A map of platform-specific identifiers, such as cluster, application, workgroup, or project IDs, that identify where the data quality evaluation ran.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** EvaluationContext **   <a name="Glue-Type-DataQualityResultV2Item-EvaluationContext"></a>
The evaluation context for the data quality result. This value identifies a specific data quality result, or a series of related results, within a run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ExecutionCompletedOn **   <a name="Glue-Type-DataQualityResultV2Item-ExecutionCompletedOn"></a>
The date and time when this data quality run completed.
Type: Timestamp
Required: No

 ** ExecutionStartedOn **   <a name="Glue-Type-DataQualityResultV2Item-ExecutionStartedOn"></a>
The date and time when this data quality run started.
Type: Timestamp
Required: No

 ** Observations **   <a name="Glue-Type-DataQualityResultV2Item-Observations"></a>
A list of `DataQualityObservation` objects representing the anomaly detection observations generated after evaluating the rules and analyzers.
Type: Array of [DataQualityObservation](API_DataQualityObservation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** ResultPublishedOn **   <a name="Glue-Type-DataQualityResultV2Item-ResultPublishedOn"></a>
The date and time when this data quality result was published.
Type: Timestamp
Required: No

 ** RuleResults **   <a name="Glue-Type-DataQualityResultV2Item-RuleResults"></a>
A list of `DataQualityRuleResult` objects representing the results for each rule.
Type: Array of [DataQualityRuleResult](API_DataQualityRuleResult.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2000 items.
Required: No

 ** RulesetName **   <a name="Glue-Type-DataQualityResultV2Item-RulesetName"></a>
The name of the ruleset associated with the data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Score **   <a name="Glue-Type-DataQualityResultV2Item-Score"></a>
An aggregate data quality score. Represents the ratio of rules that passed to the total number of rules.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

 ** Tags **   <a name="Glue-Type-DataQualityResultV2Item-Tags"></a>
A map of tags associated with the data quality result.
Type: String to string map
Map Entries: Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_DataQualityResultV2Item_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityResultV2Item)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityResultV2Item)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityResultV2Item)
