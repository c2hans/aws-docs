---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ExportInfo.html
---

# ExportInfo
<a name="API_ExportInfo"></a>

Information regarding the export status of discovered data. The value is an array of objects.

## Contents
<a name="API_ExportInfo_Contents"></a>

 ** exportId **   <a name="DiscServ-Type-ExportInfo-exportId"></a>
A unique identifier used to query an export.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: Yes

 ** exportRequestTime **   <a name="DiscServ-Type-ExportInfo-exportRequestTime"></a>
The time that the data export was initiated.
Type: Timestamp
Required: Yes

 ** exportStatus **   <a name="DiscServ-Type-ExportInfo-exportStatus"></a>
The status of the data export job.
Type: String
Valid Values: `FAILED | SUCCEEDED | IN_PROGRESS`
Required: Yes

 ** statusMessage **   <a name="DiscServ-Type-ExportInfo-statusMessage"></a>
A status message provided for API callers.
Type: String
Required: Yes

 ** configurationsDownloadUrl **   <a name="DiscServ-Type-ExportInfo-configurationsDownloadUrl"></a>
A URL for an Amazon S3 bucket where you can review the exported data. The URL is displayed only if the export succeeded.
Type: String
Required: No

 ** isTruncated **   <a name="DiscServ-Type-ExportInfo-isTruncated"></a>
If true, the export of agent information exceeded the size limit for a single export and the exported data is incomplete for the requested time range. To address this, select a smaller time range for the export by using `startDate` and `endDate`.
Type: Boolean
Required: No

 ** requestedEndTime **   <a name="DiscServ-Type-ExportInfo-requestedEndTime"></a>
The `endTime` used in the `StartExportTask` request. If no `endTime` was requested, this result does not appear in `ExportInfo`.
Type: Timestamp
Required: No

 ** requestedStartTime **   <a name="DiscServ-Type-ExportInfo-requestedStartTime"></a>
The value of `startTime` parameter in the `StartExportTask` request. If no `startTime` was requested, this result does not appear in `ExportInfo`.
Type: Timestamp
Required: No

## See Also
<a name="API_ExportInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/ExportInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/ExportInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/ExportInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
