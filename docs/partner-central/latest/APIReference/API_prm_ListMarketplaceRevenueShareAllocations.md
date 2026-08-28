---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_ListMarketplaceRevenueShareAllocations.html
---

# ListMarketplaceRevenueShareAllocations
<a name="API_prm_ListMarketplaceRevenueShareAllocations"></a>

Returns a paginated list of allocations under a marketplace revenue share, with optional filtering by status and effective date range. Supports historical reads at a specific share revision.

## Request Parameters
<a name="API_prm_ListMarketplaceRevenueShareAllocations_RequestParameters"></a>

 ** Catalog **
The catalog containing the allocations.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** ProductId **
The AWS Marketplace product identifier for the parent revenue share.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `prod-[a-z0-9]{13}`
Required: Yes

 ** AfterEffectiveFrom **
Inclusive lower bound for EffectiveFrom date filter.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: No

 ** BeforeEffectiveFrom **
Exclusive upper bound for EffectiveFrom date filter (half-open range).
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: No

 ** MarketplaceRevenueShareRevision **
Optional share revision for historical list. Returns allocations as they existed at this revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`
Required: No

 ** MaxResults **
Maximum number of results per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** NextToken **
Pagination token from a previous response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** SortBy **
The field to sort marketplace revenue share allocations by.
Type: String
Valid Values: `EffectiveFrom`
Required: No

 ** SortOrder **
The direction to sort results. Defaults to DESCENDING.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

 ** Status **
Filter by allocation status.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## Response Elements
<a name="API_prm_ListMarketplaceRevenueShareAllocations_ResponseElements"></a>

The following elements are returned by the service.

 ** MarketplaceRevenueShareAllocationSummaries **
The list of allocation summaries for the current page.
Type: Array of [MarketplaceRevenueShareAllocationSummary](API_prm_MarketplaceRevenueShareAllocationSummary.md) objects

 ** NextToken **
Pagination token for the next page. Absent if no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\S]+`

## Errors
<a name="API_prm_ListMarketplaceRevenueShareAllocations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions.
 ** Reason **
The reason for the access denial.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Reason **
The reason the resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled due to too many requests. Retry your request.
 ** QuotaCode **
The quota code associated with the throttling error.
 ** ServiceCode **
The service code associated with the throttling error.
HTTP Status Code: 429

 ** ValidationException **
The request failed validation due to invalid input parameters.
 ** FieldList **
A list of fields that failed validation.
 ** Reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_prm_ListMarketplaceRevenueShareAllocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShareAllocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShareAllocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShareAllocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShareAllocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShareAllocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShareAllocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShareAllocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShareAllocations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShareAllocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShareAllocations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
