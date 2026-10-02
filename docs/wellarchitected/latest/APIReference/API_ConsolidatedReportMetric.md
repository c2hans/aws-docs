---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ConsolidatedReportMetric.html
---

# ConsolidatedReportMetric
<a name="API_ConsolidatedReportMetric"></a>

A metric that contributes to the consolidated report.

## Contents
<a name="API_ConsolidatedReportMetric_Contents"></a>

 ** Lenses **   <a name="wellarchitected-Type-ConsolidatedReportMetric-Lenses"></a>
The metrics for the lenses in the workload.
Type: Array of [LensMetric](API_LensMetric.md) objects
Required: No

 ** LensesAppliedCount **   <a name="wellarchitected-Type-ConsolidatedReportMetric-LensesAppliedCount"></a>
The total number of lenses applied to the workload.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MetricType **   <a name="wellarchitected-Type-ConsolidatedReportMetric-MetricType"></a>
The metric type of a metric in the consolidated report. Currently only WORKLOAD metric types are supported.
Type: String
Valid Values: `WORKLOAD`
Required: No

 ** RiskCounts **   <a name="wellarchitected-Type-ConsolidatedReportMetric-RiskCounts"></a>
A map from risk names to the count of how many questions have that rating.
Type: String to integer map
Valid Keys: `UNANSWERED | HIGH | MEDIUM | NONE | NOT_APPLICABLE`
Valid Range: Minimum value of 0.
Required: No

 ** UpdatedAt **   <a name="wellarchitected-Type-ConsolidatedReportMetric-UpdatedAt"></a>
The date and time when the consolidated report metric was last updated.
Type: Timestamp
Required: No

 ** WorkloadArn **   <a name="wellarchitected-Type-ConsolidatedReportMetric-WorkloadArn"></a>
The ARN for the workload.
Type: String
Required: No

 ** WorkloadId **   <a name="wellarchitected-Type-ConsolidatedReportMetric-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: No

 ** WorkloadName **   <a name="wellarchitected-Type-ConsolidatedReportMetric-WorkloadName"></a>
The name of the workload.
The name must be unique within an account within an AWS Region. Spaces and capitalization are ignored when checking for uniqueness.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

## See Also
<a name="API_ConsolidatedReportMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ConsolidatedReportMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ConsolidatedReportMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ConsolidatedReportMetric)
