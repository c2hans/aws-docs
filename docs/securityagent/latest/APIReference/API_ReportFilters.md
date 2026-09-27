---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ReportFilters.html
---

# ReportFilters
<a name="API_ReportFilters"></a>

The report-generation filters applied when a pentest or code review report is exported.

## Contents
<a name="API_ReportFilters_Contents"></a>

 ** annotationNotes **   <a name="securityagent-Type-ReportFilters-annotationNotes"></a>
Whether to include reviewer annotation notes under each finding.
Type: Boolean
Required: No

 ** complianceReport **   <a name="securityagent-Type-ReportFilters-complianceReport"></a>
Whether to include the compliance-ready report additions.
Type: Boolean
Required: No

 ** confidenceLevels **   <a name="securityagent-Type-ReportFilters-confidenceLevels"></a>
The confidence levels to include in the report.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Valid Values: `FALSE_POSITIVE | UNCONFIRMED | LOW | MEDIUM | HIGH`
Required: No

 ** findingTypes **   <a name="securityagent-Type-ReportFilters-findingTypes"></a>
The finding types to include in the report.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** riskLevels **   <a name="securityagent-Type-ReportFilters-riskLevels"></a>
The severity levels to include in the report.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Valid Values: `UNKNOWN | INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL`
Required: No

 ** riskTypes **   <a name="securityagent-Type-ReportFilters-riskTypes"></a>
The risk types to include in the report.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Valid Values: `CROSS_SITE_SCRIPTING | DEFAULT_CREDENTIALS | INSECURE_DIRECT_OBJECT_REFERENCE | PRIVILEGE_ESCALATION | SERVER_SIDE_TEMPLATE_INJECTION | COMMAND_INJECTION | CODE_INJECTION | SQL_INJECTION | ARBITRARY_FILE_UPLOAD | INSECURE_DESERIALIZATION | LOCAL_FILE_INCLUSION | INFORMATION_DISCLOSURE | PATH_TRAVERSAL | SERVER_SIDE_REQUEST_FORGERY | JSON_WEB_TOKEN_VULNERABILITIES | XML_EXTERNAL_ENTITY | FILE_DELETION | OTHER | GRAPHQL_VULNERABILITIES | BUSINESS_LOGIC_VULNERABILITIES | CRYPTOGRAPHIC_VULNERABILITIES | DENIAL_OF_SERVICE | FILE_ACCESS | FILE_CREATION | DATABASE_MODIFICATION | DATABASE_ACCESS | OUTBOUND_SERVICE_REQUEST | UNKNOWN`
Required: No

 ** statuses **   <a name="securityagent-Type-ReportFilters-statuses"></a>
The finding statuses to include in the report.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Valid Values: `ACTIVE | RESOLVED | ACCEPTED | FALSE_POSITIVE`
Required: No

 ** taskStatuses **   <a name="securityagent-Type-ReportFilters-taskStatuses"></a>
The task execution statuses to include in the report's task table.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Valid Values: `IN_PROGRESS | ABORTED | COMPLETED | INTERNAL_ERROR | FAILED`
Required: No

## See Also
<a name="API_ReportFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ReportFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ReportFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ReportFilters)
