---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisScanResultsAggregatedByChecksFilterCriteria.html
---

# CisScanResultsAggregatedByChecksFilterCriteria
<a name="API_CisScanResultsAggregatedByChecksFilterCriteria"></a>

The scan results aggregated by checks filter criteria.

## Contents
<a name="API_CisScanResultsAggregatedByChecksFilterCriteria_Contents"></a>

 ** accountIdFilters **   <a name="inspector2-Type-CisScanResultsAggregatedByChecksFilterCriteria-accountIdFilters"></a>
The criteria's account ID filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** checkIdFilters **   <a name="inspector2-Type-CisScanResultsAggregatedByChecksFilterCriteria-checkIdFilters"></a>
The criteria's check ID filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** failedResourcesFilters **   <a name="inspector2-Type-CisScanResultsAggregatedByChecksFilterCriteria-failedResourcesFilters"></a>
The criteria's failed resources filters.
Type: Array of [CisNumberFilter](API_CisNumberFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** platformFilters **   <a name="inspector2-Type-CisScanResultsAggregatedByChecksFilterCriteria-platformFilters"></a>
The criteria's platform filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** securityLevelFilters **   <a name="inspector2-Type-CisScanResultsAggregatedByChecksFilterCriteria-securityLevelFilters"></a>
The criteria's security level filters.
Type: Array of [CisSecurityLevelFilter](API_CisSecurityLevelFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** titleFilters **   <a name="inspector2-Type-CisScanResultsAggregatedByChecksFilterCriteria-titleFilters"></a>
The criteria's title filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_CisScanResultsAggregatedByChecksFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CisScanResultsAggregatedByChecksFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CisScanResultsAggregatedByChecksFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CisScanResultsAggregatedByChecksFilterCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
