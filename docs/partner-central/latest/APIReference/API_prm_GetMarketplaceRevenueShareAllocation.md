---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_GetMarketplaceRevenueShareAllocation.html
---

# GetMarketplaceRevenueShareAllocation

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
Pattern: `mrsa-[a-z0-9]{13}`
Required: Yes

 ** MarketplaceRevenueShareIdentifier **
The identifier of the parent marketplace revenue share, as an ID (for example, mrs-0a1b2c3d4e5f6) or ARN.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/marketplace-revenue-share/mrs-[a-z0-9]{13}|mrs-[a-z0-9]{13})`
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
The unique identifier of the allocation.
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
The revision of the parent marketplace revenue share at which the marketplace revenue share allocation was retrieved.
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
<a name="API_prm_GetMarketplaceRevenueShareAllocation_Errors"></a>

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
