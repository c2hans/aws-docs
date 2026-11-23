---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_CreateMarketplaceRevenueShareAllocation.html
---

# CreateMarketplaceRevenueShareAllocation

Creates a new marketplace revenue share allocation under the specified marketplace revenue share. A marketplace revenue share allocation sets the monthly revenue share percentage, which applies equally to every AWS Marketplace product in the marketplace revenue share.

## Request Parameters
<a name="API_prm_CreateMarketplaceRevenueShareAllocation_RequestParameters"></a>

 ** Catalog **
The catalog in which to create the allocation.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** EffectiveFrom **
The effective start date for the allocation. Must be the first day of a month.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: Yes

 ** EffectiveUntil **
The effective end date for the marketplace revenue share allocation. Must be the last day of a month (YYYY-MM-DD).
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`
Required: Yes

 ** MarketplaceRevenueShareIdentifier **
The identifier of the parent marketplace revenue share, as an ID (for example, mrs-0a1b2c3d4e5f6) or ARN.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/marketplace-revenue-share/mrs-[a-z0-9]{13}|mrs-[a-z0-9]{13})`
Required: Yes

 ** MarketplaceRevenueShareRevision **
The revision of the parent marketplace revenue share that you last retrieved, used for optimistic concurrency control. If the revision is out of date, the request fails with a ConflictException and the reason REVISION\_MISMATCH.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`
Required: Yes

 ** RevenueSharePercent **
The revenue share percentage for this allocation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `\d{1,3}(\.\d{1,2})?`
Required: Yes

 ** ClientToken **
A unique token to ensure idempotency of the create request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]{1,64}`
Required: No

## Response Elements
<a name="API_prm_CreateMarketplaceRevenueShareAllocation_ResponseElements"></a>

The following elements are returned by the service.

 ** CreatedDate **
The date when the allocation was created.
Type: Timestamp

 ** EffectiveFrom **
The effective start date of the allocation.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`

 ** EffectiveUntil **
The effective end date of the marketplace revenue share allocation.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`

 ** LastModifiedDate **
The date when the allocation was last modified.
Type: Timestamp

 ** MarketplaceRevenueShareAllocationId **
The unique identifier of the newly created allocation.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `mrsa-[a-z0-9]{13}`

 ** MarketplaceRevenueShareIdentifier **
The identifier of the parent marketplace revenue share, in short ID form (for example, mrs-0a1b2c3d4e5f6).
Type: String
Length Constraints: Fixed length of 17.
Pattern: `mrs-[a-z0-9]{13}`

 ** MarketplaceRevenueShareLatestRevision **
The latest revision of the parent marketplace revenue share.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`

 ** MarketplaceRevenueShareRevision **
The revision of the parent marketplace revenue share at which the marketplace revenue share allocation was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`

 ** RevenueSharePercent **
The revenue share percentage.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `\d{1,3}(\.\d{1,2})?`

 ** Status **
The status of the allocation.
Type: String
Valid Values: `ACTIVE | INACTIVE`

## Errors
<a name="API_prm_CreateMarketplaceRevenueShareAllocation_Errors"></a>

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
<a name="API_prm_CreateMarketplaceRevenueShareAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShareAllocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShareAllocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShareAllocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShareAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShareAllocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShareAllocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShareAllocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShareAllocation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShareAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/CreateMarketplaceRevenueShareAllocation)
