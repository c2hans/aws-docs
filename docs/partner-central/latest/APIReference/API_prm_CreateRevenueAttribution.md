---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_CreateRevenueAttribution.html
---

# CreateRevenueAttribution
<a name="API_prm_CreateRevenueAttribution"></a>

Creates a new revenue attribution record in the specified catalog.

## Request Parameters
<a name="API_prm_CreateRevenueAttribution_RequestParameters"></a>

 ** Catalog **
The catalog in which to create the revenue attribution.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** Name **
The name of the revenue attribution. Must be unique within the catalog and the partner's account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x20-\x7E]+`
Required: Yes

 ** TenancyModel **
The tenancy model for this revenue attribution.
Type: String
Valid Values: `MULTI_TENANT | SINGLE_TENANT`
Required: Yes

 ** ClientToken **
A unique token to ensure idempotency of the create request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]{1,64}`
Required: No

 ** Description **
A description of the revenue attribution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\x20-\x7E]*`
Required: No

 ** ProductIdentifier **
The unique product identifier in AWS Marketplace. Accepts a product entity ID (e.g., prod-abc123def4567) or a product ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-:/.]+`
Required: No

 ** Tags **
Tags to associate with the revenue attribution upon creation.
Type: Array of [Tag](API_prm_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Elements
<a name="API_prm_CreateRevenueAttribution_ResponseElements"></a>

The following elements are returned by the service.

 ** Arn **
The Amazon Resource Name (ARN) of the newly created revenue attribution.
Type: String

 ** Id **
The unique identifier of the newly created revenue attribution.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/revenue-attribution/ra-[a-z0-9]{13}|ra-[a-z0-9]{13})`

 ** TenancyModel **
The tenancy model for this revenue attribution.
Type: String
Valid Values: `MULTI_TENANT | SINGLE_TENANT`

 ** Description **
The description of the revenue attribution.
Type: String

 ** MarketplaceProduct **
The associated AWS Marketplace product listing, if set at creation.
Type: [MarketplaceProductSummary](API_prm_MarketplaceProductSummary.md) object

 ** Name **
The name of the revenue attribution.
Type: String

 ** Revision **
The revision of the newly created attribution resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`

## Errors
<a name="API_prm_CreateRevenueAttribution_Errors"></a>

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
<a name="API_prm_CreateRevenueAttribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/CreateRevenueAttribution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/CreateRevenueAttribution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/CreateRevenueAttribution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/CreateRevenueAttribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/CreateRevenueAttribution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/CreateRevenueAttribution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/CreateRevenueAttribution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/CreateRevenueAttribution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/CreateRevenueAttribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/CreateRevenueAttribution)
