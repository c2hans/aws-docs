---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AnalysisLogExportSummary.html
---

# AnalysisLogExportSummary
<a name="API_AnalysisLogExportSummary"></a>

A summary of an analysis log export, including its identifier, status, analysis type, and creation time. Returned by `ListAnalysisLogExports`.

## Contents
<a name="API_AnalysisLogExportSummary_Contents"></a>

 ** analysisId **   <a name="API-Type-AnalysisLogExportSummary-analysisId"></a>
The unique identifier of the protected query that the analysis logs were exported for.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** analysisLogExportId **   <a name="API-Type-AnalysisLogExportSummary-analysisLogExportId"></a>
The unique identifier of the analysis log export.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** analysisType **   <a name="API-Type-AnalysisLogExportSummary-analysisType"></a>
The type of analysis that the logs were exported for. Currently, only `PROTECTED_QUERY` is supported.
Type: String
Valid Values: `PROTECTED_QUERY`
Required: Yes

 ** createTime **   <a name="API-Type-AnalysisLogExportSummary-createTime"></a>
The time the analysis log export was created.
Type: Timestamp
Required: Yes

 ** status **   <a name="API-Type-AnalysisLogExportSummary-status"></a>
The status of the analysis log export. Possible values are:
+  `IN_PROGRESS` – The export is currently running.
+  `SUCCESS` – The export completed successfully.
+  `FAILED` – The export failed.
Type: String
Valid Values: `IN_PROGRESS | SUCCESS | FAILED`
Required: Yes

## See Also
<a name="API_AnalysisLogExportSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AnalysisLogExportSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AnalysisLogExportSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AnalysisLogExportSummary)
