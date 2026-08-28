---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityAggregatedMetrics.html
---

# DataQualityAggregatedMetrics
<a name="API_DataQualityAggregatedMetrics"></a>

A summary of metrics showing the total counts of processed rows and rules, including their pass/fail statistics based on row-level results.

## Contents
<a name="API_DataQualityAggregatedMetrics_Contents"></a>

 ** TotalRowsFailed **   <a name="Glue-Type-DataQualityAggregatedMetrics-TotalRowsFailed"></a>
The total number of rows that failed one or more data quality rules.
Type: Double
Required: No

 ** TotalRowsPassed **   <a name="Glue-Type-DataQualityAggregatedMetrics-TotalRowsPassed"></a>
The total number of rows that passed all applicable data quality rules.
Type: Double
Required: No

 ** TotalRowsProcessed **   <a name="Glue-Type-DataQualityAggregatedMetrics-TotalRowsProcessed"></a>
The total number of rows that were processed during the data quality evaluation.
Type: Double
Required: No

 ** TotalRulesFailed **   <a name="Glue-Type-DataQualityAggregatedMetrics-TotalRulesFailed"></a>
The total number of data quality rules that failed their evaluation criteria.
Type: Double
Required: No

 ** TotalRulesPassed **   <a name="Glue-Type-DataQualityAggregatedMetrics-TotalRulesPassed"></a>
The total number of data quality rules that passed their evaluation criteria.
Type: Double
Required: No

 ** TotalRulesProcessed **   <a name="Glue-Type-DataQualityAggregatedMetrics-TotalRulesProcessed"></a>
The total number of data quality rules that were evaluated.
Type: Double
Required: No

## See Also
<a name="API_DataQualityAggregatedMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityAggregatedMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityAggregatedMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityAggregatedMetrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
