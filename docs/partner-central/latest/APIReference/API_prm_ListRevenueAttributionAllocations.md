---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_ListRevenueAttributionAllocations.html
---

# ListRevenueAttributionAllocations
<a name="API_prm_ListRevenueAttributionAllocations"></a>

Returns a paginated list of committed allocations with support for filtering by entity, customer, status, or date range.

## Request Parameters
<a name="API_prm_ListRevenueAttributionAllocations_RequestParameters"></a>

 ** Catalog **
The catalog that contains the resource.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** RevenueAttributionIdentifier **
The revenue attribution identifier to query.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/revenue-attribution/ra-[a-z0-9]{13}|ra-[a-z0-9]{13})`
Required: Yes

 ** AfterEffectiveFrom **
Inclusive lower bound for EffectiveFrom date filter.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: No

 ** AfterEffectiveUntil **
Inclusive lower bound for EffectiveUntil date filter.
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

 ** BeforeEffectiveUntil **
Exclusive upper bound for EffectiveUntil date filter (half-open range).
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: No

 ** CustomerAwsAccountIdFilters **
Filter by customer AWS account IDs for associated deal entities.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** EntityIdentifierFilters **
Filter by deal entity identifiers.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-:/.]+`
Required: No

 ** EntityTypeFilters **
Filter by deal entity types.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `OFFER | OPPORTUNITY`
Required: No

 ** MaxResults **
Maximum results per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** NextToken **
Pagination token from previous response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** RevenueAttributionRevision **
Point-in-time revision number to query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`
Required: No

 ** SortBy **
Field to sort by.
Type: String
Valid Values: `EffectiveFrom`
Required: No

 ** SortOrder **
Sort direction. Defaults to ASCENDING.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

 ** StatusFilter **
Filter by allocation status.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## Response Elements
<a name="API_prm_ListRevenueAttributionAllocations_ResponseElements"></a>

The following elements are returned by the service.

 ** RevenueAttributionAllocationSummaries **
Paginated list of allocations matching filters.
Type: Array of [RevenueAttributionAllocationSummary](API_prm_RevenueAttributionAllocationSummary.md) objects

 ** NextToken **
Token for next page. Absent if no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\S]+`

## Errors
<a name="API_prm_ListRevenueAttributionAllocations_Errors"></a>

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
<a name="API_prm_ListRevenueAttributionAllocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/ListRevenueAttributionAllocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/ListRevenueAttributionAllocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/ListRevenueAttributionAllocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/ListRevenueAttributionAllocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/ListRevenueAttributionAllocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/ListRevenueAttributionAllocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/ListRevenueAttributionAllocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/ListRevenueAttributionAllocations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/ListRevenueAttributionAllocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/ListRevenueAttributionAllocations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
