---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_GetMarketplaceRevenueShare.html
---

# GetMarketplaceRevenueShare

Retrieves the details of a specific marketplace revenue share.

## Request Parameters
<a name="API_prm_GetMarketplaceRevenueShare_RequestParameters"></a>

 ** Catalog **
The catalog that the marketplace revenue share belongs to.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** Identifier **
The identifier of the marketplace revenue share to retrieve, as an ID (for example, mrs-0a1b2c3d4e5f6) or ARN.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/marketplace-revenue-share/mrs-[a-z0-9]{13}|mrs-[a-z0-9]{13})`
Required: Yes

 ** Revision **
The revision of the marketplace revenue share to retrieve. Omit to return the latest revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`
Required: No

## Response Elements
<a name="API_prm_GetMarketplaceRevenueShare_ResponseElements"></a>

The following elements are returned by the service.

 ** Arn **
The Amazon Resource Name (ARN) of the marketplace revenue share.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/marketplace-revenue-share/mrs-[a-z0-9]{13}`

 ** Catalog **
The catalog that the marketplace revenue share belongs to.
Type: String
Valid Values: `AWS | Sandbox`

 ** CreatedDate **
The date when the marketplace revenue share was created.
Type: Timestamp

 ** Id **
The unique identifier of the marketplace revenue share, in short ID form (for example, mrs-0a1b2c3d4e5f6).
Type: String
Length Constraints: Fixed length of 17.
Pattern: `mrs-[a-z0-9]{13}`

 ** LastModifiedDate **
The date when the marketplace revenue share was last modified.
Type: Timestamp

 ** LatestRevision **
The latest revision of the marketplace revenue share.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`

 ** Products **
The AWS Marketplace products in the marketplace revenue share, each with its typed AWS account lists and full AWS account IDs. Empty when the marketplace revenue share is closed.
Type: Array of [MarketplaceRevenueShareProductDetail](API_prm_MarketplaceRevenueShareProductDetail.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** Revision **
The revision of the retrieved marketplace revenue share.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`

 ** TotalActiveMarketplaceRevenueShareAllocationCount **
The number of active allocations under this marketplace revenue share.
Type: Integer
Valid Range: Minimum value of 0.

 ** TotalMarketplaceRevenueShareAllocationCount **
The total number of allocations under this marketplace revenue share.
Type: Integer
Valid Range: Minimum value of 0.

 ** EffectiveFrom **
The date from which the marketplace revenue share is effective, derived from the earliest start date among its ACTIVE marketplace revenue share allocations (YYYY-MM-DD). Not returned when the marketplace revenue share has no ACTIVE marketplace revenue share allocations.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`

 ** EffectiveUntil **
The date until which the marketplace revenue share is effective, derived from the latest end date among its ACTIVE marketplace revenue share allocations (YYYY-MM-DD). Not returned when the marketplace revenue share has no ACTIVE marketplace revenue share allocations.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`

## Errors
<a name="API_prm_GetMarketplaceRevenueShare_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions.
 ** Message **
A message that describes why access was denied.
 ** Reason **
The reason for the access denial.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
 ** Message **
A message that describes the conflict.
 ** Reason **
The reason for the conflict.
HTTP Status Code: 409

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
<a name="API_prm_GetMarketplaceRevenueShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
