---
source_url: https://docs.aws.amazon.com/abuse-signal/latest/APIReference/API_ReportStatusListItem.html
---

# ReportStatusListItem

Status information for an individual abuse report. The ListAbuseReportStatuses operation returns this structure in its reports list.

## Contents
<a name="API_ReportStatusListItem_Contents"></a>

 ** description **   <a name="abusesignal-Type-ReportStatusListItem-description"></a>
A human-readable description of the status.
Type: String
Required: Yes

 ** reportId **   <a name="abusesignal-Type-ReportStatusListItem-reportId"></a>
The unique identifier of the abuse report.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `[a-zA-Z0-9]{20,64}`
Required: Yes

 ** status **   <a name="abusesignal-Type-ReportStatusListItem-status"></a>
The current processing status of the abuse report. Valid values are `QUEUED` (the report has been received and queued for processing), `PROCESSING` (the report has been received and is being processed), and `COMPLETED` (the report has been processed).
Type: String
Valid Values: `QUEUED | PROCESSING | COMPLETED`
Required: Yes

 ** correlationId **   <a name="abusesignal-Type-ReportStatusListItem-correlationId"></a>
The reporter-provided correlation ID for cross-referencing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-_]{1,256}`
Required: No

 ** reasonCode **   <a name="abusesignal-Type-ReportStatusListItem-reasonCode"></a>
A code that explains the resolution outcome. This value is present only after the report reaches the terminal `COMPLETED` status; it is absent while the report is `QUEUED` or `PROCESSING`.
Type: String
Valid Values: `ACTIONED | NOT_RESOLVABLE_TO_AWS | REVIEWED_NO_AWS_ACTION | CONTENT_DOWN_OR_INACCESSIBLE | NEED_MORE_INFORMATION`
Required: No

## See Also
<a name="API_ReportStatusListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/abuse-signal-2026-01-12/ReportStatusListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/abuse-signal-2026-01-12/ReportStatusListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/abuse-signal-2026-01-12/ReportStatusListItem)
