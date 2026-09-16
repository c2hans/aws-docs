---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetReadSetImportJob.html
---

# GetReadSetImportJob
<a name="API_GetReadSetImportJob"></a>

Gets detailed and status information about a read set import job and returns the data in JSON format.

## Request Syntax
<a name="API_GetReadSetImportJob_RequestSyntax"></a>

```
GET /sequencestore/{{sequenceStoreId}}/importjob/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetReadSetImportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetReadSetImportJob_RequestSyntax) **   <a name="omics-GetReadSetImportJob-request-uri-id"></a>
The job's ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** [sequenceStoreId](#API_GetReadSetImportJob_RequestSyntax) **   <a name="omics-GetReadSetImportJob-request-uri-sequenceStoreId"></a>
The job's sequence store ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_GetReadSetImportJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetReadSetImportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "completionTime": "string",
   "creationTime": "string",
   "id": "string",
   "roleArn": "string",
   "sequenceStoreId": "string",
   "sources": [
      {
         "description": "string",
         "generatedFrom": "string",
         "name": "string",
         "readSetId": "string",
         "referenceArn": "string",
         "sampleId": "string",
         "sourceFiles": {
            "source1": "string",
            "source2": "string"
         },
         "sourceFileType": "string",
         "status": "string",
         "statusMessage": "string",
         "subjectId": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "status": "string",
   "statusMessage": "string"
}
```

## Response Elements
<a name="API_GetReadSetImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [completionTime](#API_GetReadSetImportJob_ResponseSyntax) **   <a name="omics-GetReadSetImportJob-response-completionTime"></a>
When the job completed.
Type: Timestamp

 ** [creationTime](#API_GetReadSetImportJob_ResponseSyntax) **   <a name="omics-GetReadSetImportJob-response-creationTime"></a>
When the job was created.
Type: Timestamp

 ** [id](#API_GetReadSetImportJob_ResponseSyntax) **   <a name="omics-GetReadSetImportJob-response-id"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [roleArn](#API_GetReadSetImportJob_ResponseSyntax) **   <a name="omics-GetReadSetImportJob-response-roleArn"></a>
The job's service role ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`

 ** [sequenceStoreId](#API_GetReadSetImportJob_ResponseSyntax) **   <a name="omics-GetReadSetImportJob-response-sequenceStoreId"></a>
The job's sequence store ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [sources](#API_GetReadSetImportJob_ResponseSyntax) **   <a name="omics-GetReadSetImportJob-response-sources"></a>
The job's source files.
Type: Array of [ImportReadSetSourceItem](API_ImportReadSetSourceItem.md) objects

 ** [status](#API_GetReadSetImportJob_ResponseSyntax) **   <a name="omics-GetReadSetImportJob-response-status"></a>
The job's status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | CANCELLING | CANCELLED | FAILED | COMPLETED | COMPLETED_WITH_FAILURES`

 ** [statusMessage](#API_GetReadSetImportJob_ResponseSyntax) **   <a name="omics-GetReadSetImportJob-response-statusMessage"></a>
The job's status message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_GetReadSetImportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetReadSetImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetReadSetImportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetReadSetImportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetReadSetImportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetReadSetImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetReadSetImportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetReadSetImportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetReadSetImportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetReadSetImportJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetReadSetImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetReadSetImportJob)
