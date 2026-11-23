---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetCustomerAccountBulkJob.html
---

# GetCustomerAccountBulkJob

Use `GetCustomerAccountBulkJob` to retrieve the status and record counts of a bulk job.

## Request Syntax
<a name="API_GetCustomerAccountBulkJob_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCustomerAccountBulkJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_GetCustomerAccountBulkJob_RequestSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJob-request-Catalog"></a>
Specifies the catalog for the request. Valid values:
+  `AWS`: Production.
+  `Sandbox`: Testing environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [Identifier](#API_GetCustomerAccountBulkJob_RequestSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJob-request-Identifier"></a>
Specifies the ARN or the identifier of the bulk job.
Type: String
Pattern: `(arn:.*|bulkjob-[0-9a-z]{13})`
Required: Yes

## Response Syntax
<a name="API_GetCustomerAccountBulkJob_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "CompletedAt": "string",
   "CreatedAt": "string",
   "DeletedCount": number,
   "FailureCount": number,
   "FailureReason": "string",
   "FileName": "string",
   "Id": "string",
   "ProcessedRecords": number,
   "Status": "string",
   "SuccessCount": number,
   "TotalRecords": number
}
```

## Response Elements
<a name="API_GetCustomerAccountBulkJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetCustomerAccountBulkJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJob-response-Arn"></a>
The Amazon Resource Name (ARN) of the bulk job.
Type: String
Pattern: `arn:[a-z\-]*:partnercentral:[a-z0-9\-]*:[0-9]{12}:catalog/[a-zA-Z]+/customer-account-bulk-job/bulkjob-[0-9a-z]{13}`

 ** [CreatedAt](#API_GetCustomerAccountBulkJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJob-response-CreatedAt"></a>
The date and time when the bulk job was created.
Type: Timestamp

 ** [DeletedCount](#API_GetCustomerAccountBulkJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJob-response-DeletedCount"></a>
The number of accounts imported by this job that have since been deleted. This counter only increases, so the accounts still present equal `SuccessCount` minus `DeletedCount`.
Type: Integer

 ** [FailureCount](#API_GetCustomerAccountBulkJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJob-response-FailureCount"></a>
The number of records that failed.
Type: Integer

 ** [Id](#API_GetCustomerAccountBulkJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJob-response-Id"></a>
The unique identifier of the bulk job.
Type: String
Pattern: `bulkjob-[0-9a-z]{13}`

 ** [ProcessedRecords](#API_GetCustomerAccountBulkJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJob-response-ProcessedRecords"></a>
The number of records that the job has finished processing.
Type: Integer

 ** [Status](#API_GetCustomerAccountBulkJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJob-response-Status"></a>
The current status of the bulk job.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | FAILED`

 ** [SuccessCount](#API_GetCustomerAccountBulkJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJob-response-SuccessCount"></a>
The number of records that the job processed successfully.
Type: Integer

 ** [TotalRecords](#API_GetCustomerAccountBulkJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJob-response-TotalRecords"></a>
The total number of records in the file. The value is 0 until the job reads the file.
Type: Integer

 ** [CompletedAt](#API_GetCustomerAccountBulkJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJob-response-CompletedAt"></a>
The date and time when the job finished. Absent while the job is running.
Type: Timestamp

 ** [FailureReason](#API_GetCustomerAccountBulkJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJob-response-FailureReason"></a>
The reason that the job failed. Present only when the job status is `FAILED`.
Type: String

 ** [FileName](#API_GetCustomerAccountBulkJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJob-response-FileName"></a>
The name of the file that the job processes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetCustomerAccountBulkJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error occurs when you don't have permission to perform the requested action.
You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.
 ** Message **
A message that describes why access was denied.
 ** Reason **
The reason why access was denied for the requested operation.
HTTP Status Code: 400

 ** InternalServerException **
This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.
Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.
 ** Message **
A message that describes the internal error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.
Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.
 ** Message **
A message that describes which resource the service couldn't find.
HTTP Status Code: 400

 ** ThrottlingException **
This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.
This error occurs when there are too many requests sent. Review the provided [Quotas](https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html) and retry after the provided delay.
 ** Message **
A message that describes why the service throttled the request.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the service or business validation rules.
Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.
 ** ErrorList **
A list of issues that were discovered in the submitted request or the resource state.
 ** Message **
A message that describes the validation error.
 ** Reason **
The primary reason for this validation exception to occur.
+  *REQUEST\_VALIDATION\_FAILED:* The request format is not valid.

  Fix: Verify your request payload includes all required fields, uses correct data types and string formats.
+  *BUSINESS\_VALIDATION\_FAILED:* The requested change doesn't pass the business validation rules.

  Fix: Check that your change aligns with the business rules defined by AWS Partner Central.
HTTP Status Code: 400

## See Also
<a name="API_GetCustomerAccountBulkJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJob)
