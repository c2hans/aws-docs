---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCisScansFilterCriteria.html
---

# ListCisScansFilterCriteria
<a name="API_ListCisScansFilterCriteria"></a>

A list of CIS scans filter criteria.

## Contents
<a name="API_ListCisScansFilterCriteria_Contents"></a>

 ** failedChecksFilters **   <a name="inspector2-Type-ListCisScansFilterCriteria-failedChecksFilters"></a>
The list of failed checks filters.
Type: Array of [CisNumberFilter](API_CisNumberFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** scanArnFilters **   <a name="inspector2-Type-ListCisScansFilterCriteria-scanArnFilters"></a>
The list of scan ARN filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** scanAtFilters **   <a name="inspector2-Type-ListCisScansFilterCriteria-scanAtFilters"></a>
The list of scan at filters.
Type: Array of [CisDateFilter](API_CisDateFilter.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** scanConfigurationArnFilters **   <a name="inspector2-Type-ListCisScansFilterCriteria-scanConfigurationArnFilters"></a>
The list of scan configuration ARN filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** scanNameFilters **   <a name="inspector2-Type-ListCisScansFilterCriteria-scanNameFilters"></a>
The list of scan name filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** scanStatusFilters **   <a name="inspector2-Type-ListCisScansFilterCriteria-scanStatusFilters"></a>
The list of scan status filters.
Type: Array of [CisScanStatusFilter](API_CisScanStatusFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** scheduledByFilters **   <a name="inspector2-Type-ListCisScansFilterCriteria-scheduledByFilters"></a>
The list of scheduled by filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** targetAccountIdFilters **   <a name="inspector2-Type-ListCisScansFilterCriteria-targetAccountIdFilters"></a>
The list of target account ID filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** targetResourceIdFilters **   <a name="inspector2-Type-ListCisScansFilterCriteria-targetResourceIdFilters"></a>
The list of target resource ID filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** targetResourceTagFilters **   <a name="inspector2-Type-ListCisScansFilterCriteria-targetResourceTagFilters"></a>
The list of target resource tag filters.
Type: Array of [TagFilter](API_TagFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_ListCisScansFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListCisScansFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListCisScansFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListCisScansFilterCriteria)
