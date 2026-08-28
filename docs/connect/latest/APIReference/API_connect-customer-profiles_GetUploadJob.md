---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetUploadJob.html
---

# GetUploadJob
<a name="API_connect-customer-profiles_GetUploadJob"></a>

This API retrieves the details of a specific upload job.

## Request Syntax
<a name="API_connect-customer-profiles_GetUploadJob_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/upload-jobs/{{JobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetUploadJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetUploadJob_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJob-request-uri-DomainName"></a>
The unique name of the domain containing the upload job.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [JobId](#API_connect-customer-profiles_GetUploadJob_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJob-request-uri-JobId"></a>
The unique identifier of the upload job to retrieve.
Pattern: `[a-f0-9]{32}`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetUploadJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetUploadJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CompletedAt": number,
   "CreatedAt": number,
   "DataExpiry": number,
   "DisplayName": "string",
   "Fields": {
      "string" : {
         "ContentType": "string",
         "Source": "string",
         "Target": "string"
      }
   },
   "JobId": "string",
   "ResultsSummary": {
      "CreatedRecords": number,
      "FailedRecords": number,
      "UpdatedRecords": number
   },
   "Status": "string",
   "StatusReason": "string",
   "UniqueKey": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetUploadJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CompletedAt](#API_connect-customer-profiles_GetUploadJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJob-response-CompletedAt"></a>
The timestamp when the upload job was completed.
Type: Timestamp

 ** [CreatedAt](#API_connect-customer-profiles_GetUploadJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJob-response-CreatedAt"></a>
The timestamp when the upload job was created.
Type: Timestamp

 ** [DataExpiry](#API_connect-customer-profiles_GetUploadJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJob-response-DataExpiry"></a>
The expiry duration for the profiles ingested with the upload job.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1098.

 ** [DisplayName](#API_connect-customer-profiles_GetUploadJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJob-response-DisplayName"></a>
The unique name of the upload job. Could be a file name to identify the upload job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Fields](#API_connect-customer-profiles_GetUploadJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJob-response-Fields"></a>
The mapping between CSV Columns and Profile Object attributes for the upload job.
Type: String to [ObjectTypeField](API_connect-customer-profiles_ObjectTypeField.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_.-]+$`

 ** [JobId](#API_connect-customer-profiles_GetUploadJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJob-response-JobId"></a>
The unique identifier of the upload job.
Type: String
Pattern: `[a-f0-9]{32}`

 ** [ResultsSummary](#API_connect-customer-profiles_GetUploadJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJob-response-ResultsSummary"></a>
The summary of results for the upload job, including the number of updated, created, and failed records.
Type: [ResultsSummary](API_connect-customer-profiles_ResultsSummary.md) object

 ** [Status](#API_connect-customer-profiles_GetUploadJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJob-response-Status"></a>
The status describing the status for the upload job. The following are Valid Values:
+  **CREATED**: The upload job has been created, but has not started processing yet.
+  **IN\_PROGRESS**: The upload job is currently in progress, ingesting and processing the profile data.
+  **PARTIALLY\_SUCCEEDED**: The upload job has successfully completed the ingestion and processing of all profile data.
+  **SUCCEEDED**: The upload job has successfully completed the ingestion and processing of all profile data.
+  **FAILED**: The upload job has failed to complete.
+  **STOPPED**: The upload job has been manually stopped or terminated before completion.
Type: String
Valid Values: `CREATED | IN_PROGRESS | PARTIALLY_SUCCEEDED | SUCCEEDED | FAILED | STOPPED`

 ** [StatusReason](#API_connect-customer-profiles_GetUploadJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJob-response-StatusReason"></a>
The reason for the current status of the upload job. Possible reasons:
+  **VALIDATION\_FAILURE**: The upload job has encountered an error or issue and was unable to complete the profile data ingestion.
+  **INTERNAL\_FAILURE**: Failure caused from service side
Type: String
Valid Values: `VALIDATION_FAILURE | INTERNAL_FAILURE`

 ** [UniqueKey](#API_connect-customer-profiles_GetUploadJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetUploadJob-response-UniqueKey"></a>
The unique key columns used for de-duping the keys in the upload job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

## Errors
<a name="API_connect-customer-profiles_GetUploadJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_GetUploadJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetUploadJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetUploadJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetUploadJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetUploadJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetUploadJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetUploadJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetUploadJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetUploadJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetUploadJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetUploadJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
