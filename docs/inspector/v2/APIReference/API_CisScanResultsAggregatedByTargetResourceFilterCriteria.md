---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisScanResultsAggregatedByTargetResourceFilterCriteria.html
---

# CisScanResultsAggregatedByTargetResourceFilterCriteria
<a name="API_CisScanResultsAggregatedByTargetResourceFilterCriteria"></a>

The scan results aggregated by target resource filter criteria.

## Contents
<a name="API_CisScanResultsAggregatedByTargetResourceFilterCriteria_Contents"></a>

 ** accountIdFilters **   <a name="inspector2-Type-CisScanResultsAggregatedByTargetResourceFilterCriteria-accountIdFilters"></a>
The criteria's account ID filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** checkIdFilters **   <a name="inspector2-Type-CisScanResultsAggregatedByTargetResourceFilterCriteria-checkIdFilters"></a>
The criteria's check ID filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** failedChecksFilters **   <a name="inspector2-Type-CisScanResultsAggregatedByTargetResourceFilterCriteria-failedChecksFilters"></a>
The criteria's failed checks filters.
Type: Array of [CisNumberFilter](API_CisNumberFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** platformFilters **   <a name="inspector2-Type-CisScanResultsAggregatedByTargetResourceFilterCriteria-platformFilters"></a>
The criteria's platform filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** statusFilters **   <a name="inspector2-Type-CisScanResultsAggregatedByTargetResourceFilterCriteria-statusFilters"></a>
The criteria's status filter.
Type: Array of [CisResultStatusFilter](API_CisResultStatusFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** targetResourceIdFilters **   <a name="inspector2-Type-CisScanResultsAggregatedByTargetResourceFilterCriteria-targetResourceIdFilters"></a>
The criteria's target resource ID filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** targetResourceTagFilters **   <a name="inspector2-Type-CisScanResultsAggregatedByTargetResourceFilterCriteria-targetResourceTagFilters"></a>
The criteria's target resource tag filters.
Type: Array of [TagFilter](API_TagFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** targetStatusFilters **   <a name="inspector2-Type-CisScanResultsAggregatedByTargetResourceFilterCriteria-targetStatusFilters"></a>
The criteria's target status filters.
Type: Array of [CisTargetStatusFilter](API_CisTargetStatusFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** targetStatusReasonFilters **   <a name="inspector2-Type-CisScanResultsAggregatedByTargetResourceFilterCriteria-targetStatusReasonFilters"></a>
The criteria's target status reason filters.
Type: Array of [CisTargetStatusReasonFilter](API_CisTargetStatusReasonFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_CisScanResultsAggregatedByTargetResourceFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CisScanResultsAggregatedByTargetResourceFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CisScanResultsAggregatedByTargetResourceFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CisScanResultsAggregatedByTargetResourceFilterCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
