---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_AnalysisReport.html
---

# AnalysisReport
<a name="API_AnalysisReport"></a>

Retrieves the summary of the performance analysis report created for a time period.

## Contents
<a name="API_AnalysisReport_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AnalysisReportId **   <a name="performanceinsights-Type-AnalysisReport-AnalysisReportId"></a>
The name of the analysis report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `report-[0-9a-f]{17}`
Required: Yes

 ** CreateTime **   <a name="performanceinsights-Type-AnalysisReport-CreateTime"></a>
The time you created the analysis report.
Type: Timestamp
Required: No

 ** EndTime **   <a name="performanceinsights-Type-AnalysisReport-EndTime"></a>
The analysis end time in the report.
Type: Timestamp
Required: No

 ** Identifier **   <a name="performanceinsights-Type-AnalysisReport-Identifier"></a>
The unique identifier of the analysis report.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** Insights **   <a name="performanceinsights-Type-AnalysisReport-Insights"></a>
The list of identified insights in the analysis report.
Type: Array of [Insight](API_Insight.md) objects
Required: No

 ** ServiceType **   <a name="performanceinsights-Type-AnalysisReport-ServiceType"></a>
List the tags for the AWS service for which Performance Insights returns metrics. Valid values are as follows:
+  `RDS`
+  `DOCDB`
Type: String
Valid Values: `RDS | DOCDB`
Required: No

 ** StartTime **   <a name="performanceinsights-Type-AnalysisReport-StartTime"></a>
The analysis start time in the report.
Type: Timestamp
Required: No

 ** Status **   <a name="performanceinsights-Type-AnalysisReport-Status"></a>
The status of the created analysis report.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED`
Required: No

## See Also
<a name="API_AnalysisReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/AnalysisReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/AnalysisReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/AnalysisReport)
