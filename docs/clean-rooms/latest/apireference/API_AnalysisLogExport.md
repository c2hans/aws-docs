---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AnalysisLogExport.html
---

# AnalysisLogExport
<a name="API_AnalysisLogExport"></a>

An export of the redacted Apache Spark logs for a protected query.

## Contents
<a name="API_AnalysisLogExport_Contents"></a>

 ** analysisId **   <a name="API-Type-AnalysisLogExport-analysisId"></a>
The unique identifier of the protected query that the analysis logs were exported for.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** analysisLogExportId **   <a name="API-Type-AnalysisLogExport-analysisLogExportId"></a>
The unique identifier of the analysis log export.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** analysisType **   <a name="API-Type-AnalysisLogExport-analysisType"></a>
The type of analysis that the logs were exported for. Currently, only `PROTECTED_QUERY` is supported.
Type: String
Valid Values: `PROTECTED_QUERY`
Required: Yes

 ** createTime **   <a name="API-Type-AnalysisLogExport-createTime"></a>
The time the analysis log export was created.
Type: Timestamp
Required: Yes

 ** membershipId **   <a name="API-Type-AnalysisLogExport-membershipId"></a>
The unique identifier of the membership that the analysis log export belongs to.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** resultConfiguration **   <a name="API-Type-AnalysisLogExport-resultConfiguration"></a>
Contains the details needed to write the exported analysis logs.
Type: [AnalysisLogExportResultConfiguration](API_AnalysisLogExportResultConfiguration.md) object
Required: Yes

 ** status **   <a name="API-Type-AnalysisLogExport-status"></a>
The status of the analysis log export. Possible values are:
+  `IN_PROGRESS` – The export is currently running.
+  `SUCCESS` – The export completed successfully.
+  `FAILED` – The export failed. See the `error` field for details.
Type: String
Valid Values: `IN_PROGRESS | SUCCESS | FAILED`
Required: Yes

 ** updateTime **   <a name="API-Type-AnalysisLogExport-updateTime"></a>
The time the analysis log export was last updated.
Type: Timestamp
Required: Yes

 ** error **   <a name="API-Type-AnalysisLogExport-error"></a>
The analysis log export error. This is present only when the export `status` is `FAILED`.
Type: [AnalysisLogExportError](API_AnalysisLogExportError.md) object
Required: No

## See Also
<a name="API_AnalysisLogExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AnalysisLogExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AnalysisLogExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AnalysisLogExport)
