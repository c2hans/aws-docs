---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_StartOpportunityBulkJob.html
---

# StartOpportunityBulkJob

The `StartOpportunityBulkJob` operation creates or updates many opportunities in AWS Partner Central (Partner Central) from a single CSV file. The column headers in the file determine whether the job creates or updates opportunities.

Returns a `JobId` for the job. Use `ListOpportunityBulkJobs` to track the job, `ListOpportunityBulkJobResults` to review each record, and `GetOpportunityBulkJobReportUrl` to download a report of the failed records.

## Request Syntax
<a name="API_StartOpportunityBulkJob_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "FileFormat": "{{string}}",
   "FileURI": "{{string}}"
}
```

## Request Parameters
<a name="API_StartOpportunityBulkJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_StartOpportunityBulkJob_RequestSyntax) **   <a name="AWSPartnerCentral-StartOpportunityBulkJob-request-Catalog"></a>
Specifies the catalog for the request. Valid values:
+  `AWS`: Production.
+  `Sandbox`: Testing environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ClientToken](#API_StartOpportunityBulkJob_RequestSyntax) **   <a name="AWSPartnerCentral-StartOpportunityBulkJob-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the operation completes no more than one time. If this token matches a previous request with the same parameters, the operation returns the `JobId` of the original job. If you reuse the token with different parameters, the request fails with a `ConflictException`.
Type: String
Pattern: `.{1,255}`
Required: Yes

 ** [FileFormat](#API_StartOpportunityBulkJob_RequestSyntax) **   <a name="AWSPartnerCentral-StartOpportunityBulkJob-request-FileFormat"></a>
Specifies the format of the input file. The only supported value is `CSV`.
Type: String
Valid Values: `CSV`
Required: Yes

 ** [FileURI](#API_StartOpportunityBulkJob_RequestSyntax) **   <a name="AWSPartnerCentral-StartOpportunityBulkJob-request-FileURI"></a>
Specifies the location of the CSV file that contains the opportunities to create or update. Use one of the following:
+ An `s3://` URI of a file that you uploaded to Partner Central for your account. You can add only the `versionId` query parameter.
+ An `https://` presigned Amazon S3 URL
The file must be a plain-text CSV file no larger than 100 MB.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `(s3://|https://).*`
Required: Yes

## Response Syntax
<a name="API_StartOpportunityBulkJob_ResponseSyntax"></a>

```
{
   "JobId": "string"
}
```

## Response Elements
<a name="API_StartOpportunityBulkJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_StartOpportunityBulkJob_ResponseSyntax) **   <a name="AWSPartnerCentral-StartOpportunityBulkJob-response-JobId"></a>
The unique identifier of the bulk job. Use it with the other opportunity bulk job operations.
Type: String
Pattern: `bulkjob-[0-9a-z]{13}`

## Errors
<a name="API_StartOpportunityBulkJob_Errors"></a>

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

 ** ServiceQuotaExceededException **
This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.
Suggested action: Review the [Quotas](https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html) for the resource, and either reduce usage or request a quota increase.
 ** Message **
A message that describes which quota the request exceeded.
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
<a name="API_StartOpportunityBulkJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/StartOpportunityBulkJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/StartOpportunityBulkJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/StartOpportunityBulkJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/StartOpportunityBulkJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/StartOpportunityBulkJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/StartOpportunityBulkJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/StartOpportunityBulkJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/StartOpportunityBulkJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/StartOpportunityBulkJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/StartOpportunityBulkJob)
