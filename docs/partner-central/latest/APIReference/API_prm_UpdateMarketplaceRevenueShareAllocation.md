---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_UpdateMarketplaceRevenueShareAllocation.html
---

# UpdateMarketplaceRevenueShareAllocation
<a name="API_prm_UpdateMarketplaceRevenueShareAllocation"></a>

Updates an existing marketplace revenue share allocation. Supports modifying effective dates, revenue share percentage, and status with time-based mutability rules.

## Request Parameters
<a name="API_prm_UpdateMarketplaceRevenueShareAllocation_RequestParameters"></a>

 ** Catalog **
The catalog containing the allocation.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** MarketplaceRevenueShareAllocationId **
The identifier of the allocation to update.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `mrsa-[A-Za-z0-9]{13}`
Required: Yes

 ** MarketplaceRevenueShareRevision **
The current revision of the parent share. Must match for optimistic concurrency control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`
Required: Yes

 ** ProductId **
The AWS Marketplace product identifier for the parent revenue share.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `prod-[a-z0-9]{13}`
Required: Yes

 ** ClientToken **
A unique token to ensure idempotency of the update request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]{1,64}`
Required: No

 ** EffectiveFrom **
The new effective start date. Must be the first day of a month. Only modifiable on future-dated allocations.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: No

 ** EffectiveUntil **
The new effective end date. Must be the last day of a month and on or after today.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: No

 ** RevenueSharePercent **
The new revenue share percentage. Only modifiable on future-dated allocations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `\d{1,3}(\.\d{1,2})?`
Required: No

 ** Status **
The new status. Set to INACTIVE for soft-delete. Only modifiable on future-dated allocations.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## Response Elements
<a name="API_prm_UpdateMarketplaceRevenueShareAllocation_ResponseElements"></a>

The following elements are returned by the service.

 ** Arn **
The Amazon Resource Name (ARN) of the parent marketplace revenue share.
Type: String

 ** EffectiveFrom **
The effective start date of the allocation.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`

 ** MarketplaceRevenueShareAllocationId **
The unique identifier of the updated allocation.
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
The latest revision of the parent marketplace revenue share after the update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`

 ** ProductName **
The display name of the AWS Marketplace product.
Type: String

## Errors
<a name="API_prm_UpdateMarketplaceRevenueShareAllocation_Errors"></a>

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
<a name="API_prm_UpdateMarketplaceRevenueShareAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShareAllocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShareAllocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShareAllocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShareAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShareAllocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShareAllocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShareAllocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShareAllocation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShareAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/UpdateMarketplaceRevenueShareAllocation)
