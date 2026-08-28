---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_GetRevenueAttribution.html
---

# GetRevenueAttribution
<a name="API_prm_GetRevenueAttribution"></a>

Retrieves the details of a specific revenue attribution.

## Request Parameters
<a name="API_prm_GetRevenueAttribution_RequestParameters"></a>

 ** Catalog **
The catalog that the revenue attribution belongs to.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** Identifier **
The unique identifier of the revenue attribution to retrieve. Accepts a direct ID or ARN.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/revenue-attribution/ra-[a-z0-9]{13}|ra-[a-z0-9]{13})`
Required: Yes

 ** Revision **
The revision of the attribution to retrieve. Omit to return the latest revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`
Required: No

## Response Elements
<a name="API_prm_GetRevenueAttribution_ResponseElements"></a>

The following elements are returned by the service.

 ** Arn **
The Amazon Resource Name (ARN) of the revenue attribution.
Type: String

 ** Catalog **
The catalog that the revenue attribution belongs to.
Type: String
Valid Values: `AWS | Sandbox`

 ** Id **
The unique identifier of the revenue attribution.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/revenue-attribution/ra-[a-z0-9]{13}|ra-[a-z0-9]{13})`

 ** TenancyModel **
The tenancy model for this revenue attribution.
Type: String
Valid Values: `MULTI_TENANT | SINGLE_TENANT`

 ** CreatedDate **
The date when the revenue attribution was created.
Type: Timestamp

 ** Description **
A description of the revenue attribution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** EffectiveFrom **
The date from which this revenue attribution is effective, derived from the earliest allocation start date (YYYY-MM-DD).
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`

 ** EffectiveUntil **
The date until which this revenue attribution is effective, derived from the latest allocation end date (YYYY-MM-DD).
Type: String
Length Constraints: Fixed length of 10.
Pattern: `\d{4}-\d{2}-\d{2}`

 ** LastModifiedDate **
The date when the revenue attribution was last modified.
Type: Timestamp

 ** LatestRevision **
The latest revision of the attribution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`

 ** MarketplaceProduct **
The associated AWS Marketplace product listing, if set.
Type: [MarketplaceProductSummary](API_prm_MarketplaceProductSummary.md) object

 ** Name **
The display name of the revenue attribution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** Revision **
The revision of the retrieved attribution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`

 ** TotalActiveRevenueAttributionAllocationCount **
The total number of allocations under this revenue attribution whose Status is ACTIVE.
Type: Integer
Valid Range: Minimum value of 0.

 ** TotalRevenueAttributionAllocationCount **
The total number of allocations under this revenue attribution, counting both ACTIVE and INACTIVE.
Type: Integer
Valid Range: Minimum value of 0.

## Errors
<a name="API_prm_GetRevenueAttribution_Errors"></a>

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
<a name="API_prm_GetRevenueAttribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttribution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttribution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttribution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttribution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttribution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttribution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttribution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttribution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
