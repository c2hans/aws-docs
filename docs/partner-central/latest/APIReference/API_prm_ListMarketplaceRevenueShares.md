---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_ListMarketplaceRevenueShares.html
---

# ListMarketplaceRevenueShares
<a name="API_prm_ListMarketplaceRevenueShares"></a>

Returns a paginated list of marketplace revenue shares with optional filters.

## Request Parameters
<a name="API_prm_ListMarketplaceRevenueShares_RequestParameters"></a>

 ** Catalog **
The catalog to list marketplace revenue shares from.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** CreatedAfter **
Filter results to only include marketplace revenue shares created after this timestamp.
Type: Timestamp
Required: No

 ** CreatedBefore **
Filter results to only include marketplace revenue shares created before this timestamp.
Type: Timestamp
Required: No

 ** MaxResults **
The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** NextToken **
Token for pagination. Use the value returned in the previous response to retrieve the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** ProductCodes **
Filter results to only include shares with these product codes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ProductIds **
Filter results to only include shares with these product identifiers.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Fixed length of 18.
Pattern: `prod-[a-z0-9]{13}`
Required: No

 ** SortBy **
The field to sort marketplace revenue shares by.
Type: String
Valid Values: `LastModifiedDate`
Required: No

 ** SortOrder **
The direction to sort results.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Elements
<a name="API_prm_ListMarketplaceRevenueShares_ResponseElements"></a>

The following elements are returned by the service.

 ** MarketplaceRevenueShareSummaries **
The list of marketplace revenue share summaries.
Type: Array of [MarketplaceRevenueShareSummary](API_prm_MarketplaceRevenueShareSummary.md) objects

 ** NextToken **
Token for pagination. Present if there are more results available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\S]+`

## Errors
<a name="API_prm_ListMarketplaceRevenueShares_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions.
 ** Reason **
The reason for the access denial.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

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
<a name="API_prm_ListMarketplaceRevenueShares_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShares)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShares)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShares)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShares)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShares)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShares)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShares)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShares)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShares)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShares)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
