---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_UpdateMarketplaceRevenueShare.html
---

# UpdateMarketplaceRevenueShare

Replaces the AWS Marketplace products in a marketplace revenue share. The request must include the complete set of AWS Marketplace products, which should be products that run on the same backend AWS infrastructure, and their typed AWS account lists. Any AWS Marketplace product not included is removed, along with its AWS account lists. An empty Products list closes the marketplace revenue share. A closed marketplace revenue share cannot be reopened.

## Request Parameters
<a name="API_prm_UpdateMarketplaceRevenueShare_RequestParameters"></a>

 ** Catalog **
The catalog that the marketplace revenue share belongs to.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** Identifier **
The identifier of the marketplace revenue share to update, as an ID (for example, mrs-0a1b2c3d4e5f6) or ARN.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/marketplace-revenue-share/mrs-[a-z0-9]{13}|mrs-[a-z0-9]{13})`
Required: Yes

 ** Products **
The complete set of AWS Marketplace products for the marketplace revenue share, each with its typed AWS account lists. Include AWS Marketplace products that run on the same backend AWS infrastructure. Specify 0 to 25 AWS Marketplace products. An empty list closes the marketplace revenue share.
Type: Array of [MarketplaceRevenueShareProductEntry](API_prm_MarketplaceRevenueShareProductEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: Yes

 ** Revision **
The current revision of the marketplace revenue share, used for optimistic concurrency control. If the revision is out of date, the request fails with a ConflictException and the reason REVISION\_MISMATCH.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`
Required: Yes

 ** ClientToken **
A unique token to ensure idempotency of the update request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]{1,64}`
Required: No

## Response Elements
<a name="API_prm_UpdateMarketplaceRevenueShare_ResponseElements"></a>

The following elements are returned by the service.

 ** Arn **
The Amazon Resource Name (ARN) of the updated marketplace revenue share.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/marketplace-revenue-share/mrs-[a-z0-9]{13}`

 ** Id **
The unique identifier of the updated marketplace revenue share, in short ID form (for example, mrs-0a1b2c3d4e5f6).
Type: String
Length Constraints: Fixed length of 17.
Pattern: `mrs-[a-z0-9]{13}`

 ** LastModifiedDate **
The date when the marketplace revenue share was last modified.
Type: Timestamp

 ** LatestRevision **
The latest revision of the marketplace revenue share after the update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`

 ** Products **
The AWS Marketplace products in the marketplace revenue share after the update, each with per-type AWS account counts. Empty when the marketplace revenue share is closed.
Type: Array of [MarketplaceRevenueShareProductSummary](API_prm_MarketplaceRevenueShareProductSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

## Errors
<a name="API_prm_UpdateMarketplaceRevenueShare_Errors"></a>

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
<a name="API_prm_UpdateMarketplaceRevenueShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShare)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShare)
