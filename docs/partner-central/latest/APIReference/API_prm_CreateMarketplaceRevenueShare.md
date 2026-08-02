---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_CreateMarketplaceRevenueShare.html
---

# CreateMarketplaceRevenueShare
<a name="API_prm_CreateMarketplaceRevenueShare"></a>

Creates a new marketplace revenue share resource in the specified catalog.

## Request Parameters
<a name="API_prm_CreateMarketplaceRevenueShare_RequestParameters"></a>

 ** Catalog **
The catalog in which to create the marketplace revenue share.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** ProductId **
The AWS Marketplace product identifier for this revenue share.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `prod-[a-z0-9]{13}`
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
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Elements
<a name="API_prm_CreateMarketplaceRevenueShare_ResponseElements"></a>

The following elements are returned by the service.

 ** Arn **
The Amazon Resource Name (ARN) of the newly created marketplace revenue share.
Type: String

 ** ProductId **
The AWS Marketplace product identifier of the newly created revenue share.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `prod-[a-z0-9]{13}`

 ** Catalog **
The catalog that the marketplace revenue share belongs to.
Type: String
Valid Values: `AWS | Sandbox`

 ** CreatedDate **
The date when the marketplace revenue share was created.
Type: Timestamp

 ** LastModifiedDate **
The date when the marketplace revenue share was last modified.
Type: Timestamp

 ** ProductCode **
The AWS Marketplace product code.
Type: String

 ** ProductName **
The display name of the AWS Marketplace product.
Type: String

 ** Revision **
The revision number of the newly created marketplace revenue share.
Type: Integer
Valid Range: Minimum value of 1.

## Errors
<a name="API_prm_CreateMarketplaceRevenueShare_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions.
 ** Reason **
The reason for the access denial.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
 ** Reason **
The reason for the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Reason **
The reason the resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would exceed a service quota limit.
 ** Reason **
The reason the service quota was exceeded.
HTTP Status Code: 402

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
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShare)
