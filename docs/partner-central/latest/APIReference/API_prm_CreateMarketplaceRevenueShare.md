---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_CreateMarketplaceRevenueShare.html
---

# CreateMarketplaceRevenueShare

Creates a marketplace revenue share in the specified catalog. A marketplace revenue share is the portion of revenue that AWS Marketplace drives as a sales channel for one or more AWS Marketplace products, provided as a monthly percentage through marketplace revenue share allocations. Group AWS Marketplace products that run on the same backend AWS infrastructure in one marketplace revenue share so that they share the same monthly allocations.

## Request Parameters
<a name="API_prm_CreateMarketplaceRevenueShare_RequestParameters"></a>

 ** Catalog **
The catalog in which to create the marketplace revenue share.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** Products **
The AWS Marketplace products to include in the marketplace revenue share. Include AWS Marketplace products that run on the same backend AWS infrastructure; they share the same monthly marketplace revenue share allocations. For each AWS Marketplace product, you can optionally specify its AWS deployed accounts. Specify 1 to 25 AWS Marketplace products.
Type: Array of [MarketplaceRevenueShareProductEntry](API_prm_MarketplaceRevenueShareProductEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

 ** ClientToken **
A unique token to ensure idempotency of the create request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]{1,64}`
Required: No

 ** Tags **
Tags to associate with the marketplace revenue share upon creation.
Type: Array of [Tag](API_prm_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Elements
<a name="API_prm_CreateMarketplaceRevenueShare_ResponseElements"></a>

The following elements are returned by the service.

 ** Arn **
The Amazon Resource Name (ARN) of the newly created marketplace revenue share.
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
The unique identifier of the newly created marketplace revenue share, in short ID form (for example, mrs-0a1b2c3d4e5f6).
Type: String
Length Constraints: Fixed length of 17.
Pattern: `mrs-[a-z0-9]{13}`

 ** LastModifiedDate **
The date when the marketplace revenue share was last modified.
Type: Timestamp

 ** Products **
The AWS Marketplace products in the newly created marketplace revenue share, each with per-type AWS account counts.
Type: Array of [MarketplaceRevenueShareProductSummary](API_prm_MarketplaceRevenueShareProductSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** Revision **
The revision of the newly created marketplace revenue share.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`

## Errors
<a name="API_prm_CreateMarketplaceRevenueShare_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would exceed a service quota limit.
 ** Message **
A message that describes which service quota would be exceeded.
 ** Reason **
The reason the service quota was exceeded.
HTTP Status Code: 402

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
<a name="API_prm_CreateMarketplaceRevenueShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShare)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShare)
