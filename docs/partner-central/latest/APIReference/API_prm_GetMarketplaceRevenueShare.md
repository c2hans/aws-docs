---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_GetMarketplaceRevenueShare.html
---

# GetMarketplaceRevenueShare
<a name="API_prm_GetMarketplaceRevenueShare"></a>

Retrieves the details of a specific marketplace revenue share.

## Request Parameters
<a name="API_prm_GetMarketplaceRevenueShare_RequestParameters"></a>

 ** Catalog **
The catalog that the marketplace revenue share belongs to.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** ProductId **
The AWS Marketplace product identifier of the revenue share to retrieve.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `prod-[a-z0-9]{13}`
Required: Yes

 ** Revision **
The revision of the marketplace revenue share to retrieve. Omit to return the latest revision.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## Response Elements
<a name="API_prm_GetMarketplaceRevenueShare_ResponseElements"></a>

The following elements are returned by the service.

 ** Arn **
The Amazon Resource Name (ARN) of the marketplace revenue share.
Type: String

 ** Catalog **
The catalog that the marketplace revenue share belongs to.
Type: String
Valid Values: `AWS | Sandbox`

 ** ProductId **
The AWS Marketplace product identifier of the revenue share.
Type: String
Length Constraints: Fixed length of 18.
Pattern: `prod-[a-z0-9]{13}`

 ** CreatedDate **
The date when the marketplace revenue share was created.
Type: Timestamp

 ** LastModifiedDate **
The date when the marketplace revenue share was last modified.
Type: Timestamp

 ** LatestRevision **
The latest revision number of the marketplace revenue share.
Type: Integer
Valid Range: Minimum value of 1.

 ** ProductCode **
The AWS Marketplace product code.
Type: String

 ** ProductName **
The display name of the AWS Marketplace product.
Type: String

 ** Revision **
The revision number of the retrieved marketplace revenue share.
Type: Integer
Valid Range: Minimum value of 1.

 ** TotalActiveMarketplaceRevenueShareAllocationCount **
The number of active allocations under this marketplace revenue share.
Type: Integer

 ** TotalMarketplaceRevenueShareAllocationCount **
The total number of allocations under this marketplace revenue share.
Type: Integer

## Errors
<a name="API_prm_GetMarketplaceRevenueShare_Errors"></a>

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
<a name="API_prm_GetMarketplaceRevenueShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/GetMarketplaceRevenueShare)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
