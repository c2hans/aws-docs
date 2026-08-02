---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_AnalysisReportSummary.html
---

# AnalysisReportSummary
<a name="API_AnalysisReportSummary"></a>

Retrieves the details of the performance analysis report.

## Contents
<a name="API_AnalysisReportSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AnalysisReportId **   <a name="performanceinsights-Type-AnalysisReportSummary-AnalysisReportId"></a>
The name of the analysis report.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** CreateTime **   <a name="performanceinsights-Type-AnalysisReportSummary-CreateTime"></a>
The time you created the analysis report.
Type: Timestamp
Required: No

 ** EndTime **   <a name="performanceinsights-Type-AnalysisReportSummary-EndTime"></a>
The end time of the analysis in the report.
Type: Timestamp
Required: No

 ** StartTime **   <a name="performanceinsights-Type-AnalysisReportSummary-StartTime"></a>
The start time of the analysis in the report.
Type: Timestamp
Required: No

 ** Status **   <a name="performanceinsights-Type-AnalysisReportSummary-Status"></a>
The status of the analysis report.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED`
Required: No

 ** Tags **   <a name="performanceinsights-Type-AnalysisReportSummary-Tags"></a>
List of all the tags added to the analysis report.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## See Also
<a name="API_AnalysisReportSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/AnalysisReportSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/AnalysisReportSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/AnalysisReportSummary)
