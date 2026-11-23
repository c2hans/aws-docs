---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_ListMarketplaceRevenueShares.html
---

# ListMarketplaceRevenueShares

Returns a paginated list of marketplace revenue shares with optional filters.

## Request Parameters
<a name="API_prm_ListMarketplaceRevenueShares_RequestParameters"></a>

 ** Catalog **
The catalog to list marketplace revenue shares from.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** CreatedAfter **
Filters results to marketplace revenue shares created at or after this timestamp (inclusive).
Type: Timestamp
Required: No

 ** CreatedBefore **
Filters results to marketplace revenue shares created before this timestamp (exclusive).
Type: Timestamp
Required: No

 ** Identifiers **
Filters results to the specified marketplace revenue shares, by ID or ARN. Specify 1 to 100 identifiers. When you specify multiple filters, a marketplace revenue share must match all of them.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 17. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/marketplace-revenue-share/mrs-[a-z0-9]{13}|mrs-[a-z0-9]{13})`
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
Filters results to marketplace revenue shares that contain an AWS Marketplace product with any of the specified product codes. Specify 1 to 10 product codes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9]+`
Required: No

 ** ProductIds **
Filters results to marketplace revenue shares that contain any of the specified AWS Marketplace products. Specify 1 to 10 AWS Marketplace product IDs or product ARNs. Only marketplace revenue shares that you own are returned.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-:/.]+`
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
 ** Message **
A message that describes why access was denied.
 ** Reason **
The reason for the access denial.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry your request.
 ** Message **
A message that describes the internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
A message that describes which resource was not found.
 ** Reason **
The reason the resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled due to too many requests. Retry your request.
 ** Message **
A message that indicates the request rate limit was exceeded.
 ** QuotaCode **
The quota code associated with the throttling error.
 ** ServiceCode **
The service code associated with the throttling error.
HTTP Status Code: 429

 ** ValidationException **
The request failed validation due to invalid input parameters.
 ** FieldList **
A list of fields that failed validation.
 ** Message **
A message that describes the validation failure.
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
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShares)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/ListMarketplaceRevenueShares)
