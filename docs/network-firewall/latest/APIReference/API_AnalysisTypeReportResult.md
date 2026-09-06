---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_AnalysisTypeReportResult.html
---

# AnalysisTypeReportResult
<a name="API_AnalysisTypeReportResult"></a>

The results of a `COMPLETED` analysis report generated with [StartAnalysisReport](API_StartAnalysisReport.md).

For an example of traffic analysis report results, see the response syntax of [GetAnalysisReportResults](API_GetAnalysisReportResults.md).

## Contents
<a name="API_AnalysisTypeReportResult_Contents"></a>

 ** Domain **   <a name="networkfirewall-Type-AnalysisTypeReportResult-Domain"></a>
The most frequently accessed domains.
Type: String
Required: No

 ** FirstAccessed **   <a name="networkfirewall-Type-AnalysisTypeReportResult-FirstAccessed"></a>
The date and time any domain was first accessed (within the last 30 day period).
Type: Timestamp
Required: No

 ** Hits **   <a name="networkfirewall-Type-AnalysisTypeReportResult-Hits"></a>
The number of attempts made to access a observed domain.
Type: [Hits](API_Hits.md) object
Required: No

 ** LastAccessed **   <a name="networkfirewall-Type-AnalysisTypeReportResult-LastAccessed"></a>
The date and time any domain was last accessed (within the last 30 day period).
Type: Timestamp
Required: No

 ** Protocol **   <a name="networkfirewall-Type-AnalysisTypeReportResult-Protocol"></a>
The type of traffic captured by the analysis report.
Type: String
Required: No

 ** UniqueSources **   <a name="networkfirewall-Type-AnalysisTypeReportResult-UniqueSources"></a>
The number of unique source IP addresses that connected to a domain.
Type: [UniqueSources](API_UniqueSources.md) object
Required: No

## See Also
<a name="API_AnalysisTypeReportResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/AnalysisTypeReportResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/AnalysisTypeReportResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/AnalysisTypeReportResult)
