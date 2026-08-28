---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_FindingsReportSummary.html
---

# FindingsReportSummary
<a name="API_FindingsReportSummary"></a>

 Information about potential recommendations that might be created from the analysis of profiling data.

## Contents
<a name="API_FindingsReportSummary_Contents"></a>

 ** id **   <a name="profiler-Type-FindingsReportSummary-id"></a>
The universally unique identifier (UUID) of the recommendation report.
Type: String
Pattern: `.*[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}.*`
Required: No

 ** profileEndTime **   <a name="profiler-Type-FindingsReportSummary-profileEndTime"></a>
 The end time of the period during which the metric is flagged as anomalous. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp
Required: No

 ** profileStartTime **   <a name="profiler-Type-FindingsReportSummary-profileStartTime"></a>
The start time of the profile the analysis data is about. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp
Required: No

 ** profilingGroupName **   <a name="profiler-Type-FindingsReportSummary-profilingGroupName"></a>
The name of the profiling group that is associated with the analysis data.
Type: String
Required: No

 ** totalNumberOfFindings **   <a name="profiler-Type-FindingsReportSummary-totalNumberOfFindings"></a>
The total number of different recommendations that were found by the analysis.
Type: Integer
Required: No

## See Also
<a name="API_FindingsReportSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/FindingsReportSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/FindingsReportSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/FindingsReportSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Profiler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
