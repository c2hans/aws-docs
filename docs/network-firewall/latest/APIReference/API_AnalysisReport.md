---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_AnalysisReport.html
---

# AnalysisReport
<a name="API_AnalysisReport"></a>

A report that captures key activity from the last 30 days of network traffic monitored by your firewall.

You can generate up to one report per traffic type, per 30 day period. For example, when you successfully create an HTTP traffic report, you cannot create another HTTP traffic report until 30 days pass. Alternatively, if you generate a report that combines metrics on both HTTP and HTTPS traffic, you cannot create another report for either traffic type until 30 days pass.

## Contents
<a name="API_AnalysisReport_Contents"></a>

 ** AnalysisReportId **   <a name="networkfirewall-Type-AnalysisReport-AnalysisReportId"></a>
The unique ID of the query that ran when you requested an analysis report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\S+`
Required: No

 ** AnalysisType **   <a name="networkfirewall-Type-AnalysisReport-AnalysisType"></a>
The type of traffic that will be used to generate a report.
Type: String
Valid Values: `TLS_SNI | HTTP_HOST`
Required: No

 ** ReportTime **   <a name="networkfirewall-Type-AnalysisReport-ReportTime"></a>
The date and time the analysis report was ran.
Type: Timestamp
Required: No

 ** Status **   <a name="networkfirewall-Type-AnalysisReport-Status"></a>
The status of the analysis report you specify. Statuses include `RUNNING`, `COMPLETED`, or `FAILED`.
Type: String
Required: No

## See Also
<a name="API_AnalysisReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/AnalysisReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/AnalysisReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/AnalysisReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
