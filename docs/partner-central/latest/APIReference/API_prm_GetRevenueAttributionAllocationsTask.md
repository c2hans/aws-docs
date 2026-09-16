---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_GetRevenueAttributionAllocationsTask.html
---

# GetRevenueAttributionAllocationsTask
<a name="API_prm_GetRevenueAttributionAllocationsTask"></a>

Retrieves the current status of a previously submitted allocations task. When COMPLETE, includes the latest revision. When FAILED, includes error details.

## Request Parameters
<a name="API_prm_GetRevenueAttributionAllocationsTask_RequestParameters"></a>

 ** Catalog **
The catalog that contains the resource.
Type: String
Valid Values: `AWS | Sandbox`
Required: Yes

 ** RevenueAttributionIdentifier **
The revenue attribution identifier.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 1011.
Pattern: `(arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[a-zA-Z]+/revenue-attribution/ra-[a-z0-9]{13}|ra-[a-z0-9]{13})`
Required: Yes

## Response Elements
<a name="API_prm_GetRevenueAttributionAllocationsTask_ResponseElements"></a>

The following elements are returned by the service.

 ** Catalog **
The catalog used for this task.
Type: String
Valid Values: `AWS | Sandbox`

 ** RevenueAttributionArn **
ARN of the revenue attribution resource.
Type: String

 ** StartedAt **
When processing started.
Type: Timestamp

 ** Status **
Current task status.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | FAILED`

 ** TaskId **
The unique identifier for the asynchronous task.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `raatask-[a-z0-9]{13}`

 ** TotalRevenueAttributionAllocationRecords **
Total revenue attribution allocation records in the batch.
Type: Integer

 ** Description **
Human-readable description, if provided at creation.
Type: String

 ** EndedAt **
When processing ended. Only present when COMPLETE or FAILED.
Type: Timestamp

 ** ErrorDetailList **
All errors discovered during async processing. Only present when FAILED.
Type: Array of [RevenueAttributionAllocationErrorDetail](API_prm_RevenueAttributionAllocationErrorDetail.md) objects

 ** RevenueAttributionLatestRevision **
The revision number assigned to this batch. Only present when COMPLETE.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[1-9][0-9]*`

## Errors
<a name="API_prm_GetRevenueAttributionAllocationsTask_Errors"></a>

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
<a name="API_prm_GetRevenueAttributionAllocationsTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocationsTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocationsTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocationsTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocationsTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocationsTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocationsTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocationsTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocationsTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocationsTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/GetRevenueAttributionAllocationsTask)
