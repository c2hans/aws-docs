---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_OrganizationalReportSummary.html
---

# OrganizationalReportSummary
<a name="API_OrganizationalReportSummary"></a>

**Important**
This is not available during the preview release.

Summary of an Organizational Report returned in a list response. Includes the core fields of the full report and the optional label, but omits the filters and coverage summary. The filters and coverage summary are available through GetAgentOrganizationalReport. The coverage summary is populated once the report reaches COMPLETED.

## Contents
<a name="API_OrganizationalReportSummary_Contents"></a>

 ** createdAt **   <a name="wellarchitected-Type-OrganizationalReportSummary-createdAt"></a>
Timestamp at which the report was created.
Type: Timestamp
Required: Yes

 ** organizationId **   <a name="wellarchitected-Type-OrganizationalReportSummary-organizationId"></a>
Identifier of the AWS Organization the report belongs to. Derived from the caller's authorization context at creation time and not accepted as a client-supplied input.
Type: String
Required: Yes

 ** ownerAccountId **   <a name="wellarchitected-Type-OrganizationalReportSummary-ownerAccountId"></a>
AWS account ID of the caller that created the report. Only this account or a delegated administrator of the same organization may retrieve or delete the report.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** reportId **   <a name="wellarchitected-Type-OrganizationalReportSummary-reportId"></a>
Unique identifier of the Organizational Report assigned by the service at creation time.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** state **   <a name="wellarchitected-Type-OrganizationalReportSummary-state"></a>
Current lifecycle state of the report.
Type: String
Valid Values: `DISCOVERING | SNAPSHOTTING | AGGREGATING | COMPRESSING | COMPLETED | FAILED | DELETING`
Required: Yes

 ** label **   <a name="wellarchitected-Type-OrganizationalReportSummary-label"></a>
Optional human-readable label supplied by the caller at creation time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## See Also
<a name="API_OrganizationalReportSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/OrganizationalReportSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/OrganizationalReportSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/OrganizationalReportSummary)
