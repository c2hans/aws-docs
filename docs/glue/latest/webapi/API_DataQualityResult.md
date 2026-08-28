---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityResult.html
---

# DataQualityResult
<a name="API_DataQualityResult"></a>

Describes a data quality result.

## Contents
<a name="API_DataQualityResult_Contents"></a>

 ** AggregatedMetrics **   <a name="Glue-Type-DataQualityResult-AggregatedMetrics"></a>
 A summary of `DataQualityAggregatedMetrics` objects showing the total counts of processed rows and rules, including their pass/fail statistics based on row-level results.
Type: [DataQualityAggregatedMetrics](API_DataQualityAggregatedMetrics.md) object
Required: No

 ** AnalyzerResults **   <a name="Glue-Type-DataQualityResult-AnalyzerResults"></a>
A list of `DataQualityAnalyzerResult` objects representing the results for each analyzer.
Type: Array of [DataQualityAnalyzerResult](API_DataQualityAnalyzerResult.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2000 items.
Required: No

 ** CompletedOn **   <a name="Glue-Type-DataQualityResult-CompletedOn"></a>
The date and time when this data quality run completed.
Type: Timestamp
Required: No

 ** DataSource **   <a name="Glue-Type-DataQualityResult-DataSource"></a>
The table associated with the data quality result, if any.
Type: [DataSource](API_DataSource.md) object
Required: No

 ** EvaluationContext **   <a name="Glue-Type-DataQualityResult-EvaluationContext"></a>
In the context of a job in AWS Glue Studio, each node in the canvas is typically assigned some sort of name and data quality nodes will have names. In the case of multiple nodes, the `evaluationContext` can differentiate the nodes.
Type: String
Required: No

 ** JobName **   <a name="Glue-Type-DataQualityResult-JobName"></a>
The job name associated with the data quality result, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** JobRunId **   <a name="Glue-Type-DataQualityResult-JobRunId"></a>
The job run ID associated with the data quality result, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Observations **   <a name="Glue-Type-DataQualityResult-Observations"></a>
A list of `DataQualityObservation` objects representing the observations generated after evaluating the rules and analyzers.
Type: Array of [DataQualityObservation](API_DataQualityObservation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** ProfileId **   <a name="Glue-Type-DataQualityResult-ProfileId"></a>
The Profile ID for the data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ResultId **   <a name="Glue-Type-DataQualityResult-ResultId"></a>
A unique result ID for the data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** RuleResults **   <a name="Glue-Type-DataQualityResult-RuleResults"></a>
A list of `DataQualityRuleResult` objects representing the results for each rule.
Type: Array of [DataQualityRuleResult](API_DataQualityRuleResult.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2000 items.
Required: No

 ** RulesetEvaluationRunId **   <a name="Glue-Type-DataQualityResult-RulesetEvaluationRunId"></a>
The unique run ID for the ruleset evaluation for this data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** RulesetName **   <a name="Glue-Type-DataQualityResult-RulesetName"></a>
The name of the ruleset associated with the data quality result.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Score **   <a name="Glue-Type-DataQualityResult-Score"></a>
An aggregate data quality score. Represents the ratio of rules that passed to the total number of rules.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

 ** StartedOn **   <a name="Glue-Type-DataQualityResult-StartedOn"></a>
The date and time when this data quality run started.
Type: Timestamp
Required: No

## See Also
<a name="API_DataQualityResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
