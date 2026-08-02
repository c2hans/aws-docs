---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_GetRevenueAttributionAllocation.html
---

# GetRevenueAttributionAllocation
<a name="API_prm_GetRevenueAttributionAllocation"></a>

Retrieves a single allocation by its RevenueAttributionAllocationId. Supports optional point-in-time version queries.

## Request Parameters
<a name="API_prm_GetRevenueAttributionAllocation_RequestParameters"></a>

 ** Catalog **
The catalog that contains the resource.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** RevenueAttributionAllocationId **
The allocation identifier.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `alloc-[a-z0-9]{13}`
Required: Yes

 ** RevenueAttributionIdentifier **
The revenue attribution identifier.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/revenue-attribution/ra-[a-z0-9]{13}|ra-[a-z0-9]{13})`
Required: Yes

 ** RevenueAttributionRevision **
Point-in-time revision number to query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`
Required: No

## Response Elements
<a name="API_prm_GetRevenueAttributionAllocation_ResponseElements"></a>

The following elements are returned by the service.

 ** CreatedDate **
When the allocation was first created.
Type: Timestamp

 ** CustomerAwsAccountId **
The customer AWS account ID for this associated deal entity.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** EffectiveFrom **
First day of the effective month.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`

 ** EffectiveUntil **
Last day of the effective month.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`

 ** EntityIdentifier **
The unique identifier of the associated deal entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-:/.]+`

 ** EntityType **
The type of the associated deal entity.
Type: String
Valid Values: `OFFER | OPPORTUNITY`

 ** LastModifiedDate **
When the allocation was last modified.
Type: Timestamp

 ** RevenueAttributionAllocationId **
Unique allocation identifier.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `alloc-[a-z0-9]{13}`

 ** RevenueAttributionIdentifier **
The revenue attribution identifier.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/revenue-attribution/ra-[a-z0-9]{13}|ra-[a-z0-9]{13})`

 ** RevenueAttributionLatestRevision **
The latest committed revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`

 ** RevenueAttributionRevision **
The revision of this allocation version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`

 ** RevenueSharePercent **
Revenue share percentage.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `\d{1,3}(\.\d{1,2})?`

 ** Status **
Current allocation status.
Type: String
Valid Values: `ACTIVE | INACTIVE`

 ** EntityName **
The display name of the associated deal entity.
Type: String

## Errors
<a name="API_prm_GetRevenueAttributionAllocation_Errors"></a>

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
<a name="API_prm_GetRevenueAttributionAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocation)
