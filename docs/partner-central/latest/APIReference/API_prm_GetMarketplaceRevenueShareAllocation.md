---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_GetMarketplaceRevenueShareAllocation.html
---

# GetMarketplaceRevenueShareAllocation
<a name="API_prm_GetMarketplaceRevenueShareAllocation"></a>

Retrieves the details of a specific marketplace revenue share allocation.

## Request Parameters
<a name="API_prm_GetMarketplaceRevenueShareAllocation_RequestParameters"></a>

 ** Catalog **
The catalog that the allocation belongs to.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** MarketplaceRevenueShareAllocationId **
The unique identifier of the allocation to retrieve.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `mrsa-[A-Za-z0-9]{13}`
Required: Yes

 ** ProductId **
The AWS Marketplace product identifier of the parent revenue share.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `prod-[a-z0-9]{13}`
Required: Yes

 ** MarketplaceRevenueShareRevision **
The revision of the parent marketplace revenue share at which to retrieve the allocation. Omit to return the latest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`
Required: No

## Response Elements
<a name="API_prm_GetMarketplaceRevenueShareAllocation_ResponseElements"></a>

The following elements are returned by the service.

 ** Arn **
The Amazon Resource Name (ARN) of the allocation.
Type: String

 ** EffectiveFrom **
The effective start date of the allocation.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`

 ** MarketplaceRevenueShareAllocationId **
The unique identifier of the allocation.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `mrsa-[A-Za-z0-9]{13}`

 ** ProductId **
The AWS Marketplace product identifier.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `prod-[a-z0-9]{13}`

 ** RevenueSharePercent **
The revenue share percentage.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `\d{1,3}(\.\d{1,2})?`

 ** Status **
The status of the allocation.
Type: String
Valid Values: `ACTIVE | INACTIVE`

 ** CreatedDate **
The date when the allocation was created.
Type: Timestamp

 ** EffectiveUntil **
The effective end date of the allocation, or null if open-ended.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`

 ** LastModifiedDate **
The date when the allocation was last modified.
Type: Timestamp

 ** LatestMarketplaceRevenueShareRevision **
The latest revision of the parent marketplace revenue share.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`

 ** ProductName **
The display name of the AWS Marketplace product.
Type: String

## Errors
<a name="API_prm_GetMarketplaceRevenueShareAllocation_Errors"></a>

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
<a name="API_prm_GetMarketplaceRevenueShareAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShareAllocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShareAllocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShareAllocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShareAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShareAllocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShareAllocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShareAllocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShareAllocation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShareAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShareAllocation)
