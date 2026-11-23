---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetCustomerAccountBulkJobReportUrl.html
---

# GetCustomerAccountBulkJobReportUrl

Use `GetCustomerAccountBulkJobReportUrl` to get a temporary URL for downloading the report of a bulk job, such as the list of records that failed. A report is available only after the job is `COMPLETED` or `FAILED`. For a job that is still running, the request fails with a `ConflictException`.

The report is generated on request. If `ReportStatus` is not `AVAILABLE`, call the operation again later.

## Request Syntax
<a name="API_GetCustomerAccountBulkJobReportUrl_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Identifier": "{{string}}",
   "ReportType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCustomerAccountBulkJobReportUrl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_GetCustomerAccountBulkJobReportUrl_RequestSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJobReportUrl-request-Catalog"></a>
Specifies the catalog for the request. Valid values:
+  `AWS`: Production.
+  `Sandbox`: Testing environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [Identifier](#API_GetCustomerAccountBulkJobReportUrl_RequestSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJobReportUrl-request-Identifier"></a>
Specifies the ARN or the identifier of the bulk job.
Type: String
Pattern: `(arn:.*|bulkjob-[0-9a-z]{13})`
Required: Yes

 ** [ReportType](#API_GetCustomerAccountBulkJobReportUrl_RequestSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJobReportUrl-request-ReportType"></a>
Specifies which records the report covers. If you omit this field, the report covers the records that failed.
Type: String
Valid Values: `FAILED_RECORDS | ALL_RECORDS`
Required: No

## Response Syntax
<a name="API_GetCustomerAccountBulkJobReportUrl_ResponseSyntax"></a>

```
{
   "ExpiresAt": "string",
   "FailureReason": "string",
   "ReportStatus": "string",
   "ReportType": "string",
   "Url": "string"
}
```

## Response Elements
<a name="API_GetCustomerAccountBulkJobReportUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReportStatus](#API_GetCustomerAccountBulkJobReportUrl_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJobReportUrl-response-ReportStatus"></a>
The status of the report. The `Url` is returned only when the status is `AVAILABLE`.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | AVAILABLE | FAILED | EXPIRED`

 ** [ReportType](#API_GetCustomerAccountBulkJobReportUrl_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJobReportUrl-response-ReportType"></a>
The records that the report covers.
Type: String
Valid Values: `FAILED_RECORDS | ALL_RECORDS`

 ** [ExpiresAt](#API_GetCustomerAccountBulkJobReportUrl_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJobReportUrl-response-ExpiresAt"></a>
The date and time when the URL expires. Present only when `ReportStatus` is `AVAILABLE`.
Type: Timestamp

 ** [FailureReason](#API_GetCustomerAccountBulkJobReportUrl_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJobReportUrl-response-FailureReason"></a>
The reason that the report couldn't be generated. Present only when `ReportStatus` is `FAILED`.
Type: String

 ** [Url](#API_GetCustomerAccountBulkJobReportUrl_ResponseSyntax) **   <a name="AWSPartnerCentral-GetCustomerAccountBulkJobReportUrl-response-Url"></a>
A temporary URL for downloading the report. Present only when `ReportStatus` is `AVAILABLE`.
Type: String

## Errors
<a name="API_GetCustomerAccountBulkJobReportUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error occurs when you don't have permission to perform the requested action.
You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.
 ** Message **
A message that describes why access was denied.
 ** Reason **
The reason why access was denied for the requested operation.
HTTP Status Code: 400

 ** ConflictException **
This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.
Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.
 ** Message **
A message that describes the conflict.
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
<a name="API_GetCustomerAccountBulkJobReportUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJobReportUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJobReportUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJobReportUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJobReportUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJobReportUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJobReportUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJobReportUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJobReportUrl)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJobReportUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/GetCustomerAccountBulkJobReportUrl)
