---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_OrganizationalReportFilters.html
---

# OrganizationalReportFilters
<a name="API_OrganizationalReportFilters"></a>

**Important**
This is not available during the preview release.

Filters narrowing the scope of an Organizational Report. Every member is optional. An absent or empty member places no constraint on that dimension. When the entire structure is absent, the report covers every account and every recommendation in the organization.

## Contents
<a name="API_OrganizationalReportFilters_Contents"></a>

 ** accountIds **   <a name="wellarchitected-Type-OrganizationalReportFilters-accountIds"></a>
AWS account IDs to include in the report. Absent or empty means all accounts in the organization are in scope. Each supplied account is validated against AWS Organizations membership. Accounts that do not belong to the caller's organization are excluded and recorded on the report's coverage summary.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10000 items.
Pattern: `\d{12}`
Required: No

 ** createdAtRange **   <a name="wellarchitected-Type-OrganizationalReportFilters-createdAtRange"></a>
Inclusive window on recommendation creation time. Absent means no lower or upper bound on createdAt.
Type: [TimeWindow](API_TimeWindow.md) object
Required: No

 ** organizationalUnitIds **   <a name="wellarchitected-Type-OrganizationalReportFilters-organizationalUnitIds"></a>
AWS Organizational Unit IDs whose member accounts are included in the report. Absent or empty means no OU-based scoping is applied. Account and OU filters combine as a union.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10000 items.
Pattern: `ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}`
Required: No

 ** pillars **   <a name="wellarchitected-Type-OrganizationalReportFilters-pillars"></a>
Well-Architected pillars to include. Absent or empty means all pillars.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Valid Values: `COST_OPTIMIZATION | SECURITY | RESILIENCE | PERFORMANCE | OPERATIONAL_EXCELLENCE`
Required: No

 ** priorities **   <a name="wellarchitected-Type-OrganizationalReportFilters-priorities"></a>
Recommendation priorities (HIGH, MEDIUM, LOW) to include. Absent or empty means all priorities.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Valid Values: `HIGH | MEDIUM | LOW`
Required: No

 ** recommendationTypes **   <a name="wellarchitected-Type-OrganizationalReportFilters-recommendationTypes"></a>
Recommendation types (RESOURCE, ARCHITECTURE, APPLICATION) to include. Absent or empty means all types.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Valid Values: `RESOURCE | ARCHITECTURE | APPLICATION`
Required: No

 ** statuses **   <a name="wellarchitected-Type-OrganizationalReportFilters-statuses"></a>
Recommendation statuses (ACTIVE, SUPPRESSED, COMPLETED) to include. Absent or empty means all statuses.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Valid Values: `ACTIVE | SUPPRESSED | COMPLETED`
Required: No

 ** updatedAtRange **   <a name="wellarchitected-Type-OrganizationalReportFilters-updatedAtRange"></a>
Inclusive window on recommendation last-updated time. Absent means no lower or upper bound on updatedAt.
Type: [TimeWindow](API_TimeWindow.md) object
Required: No

## See Also
<a name="API_OrganizationalReportFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/OrganizationalReportFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/OrganizationalReportFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/OrganizationalReportFilters)
