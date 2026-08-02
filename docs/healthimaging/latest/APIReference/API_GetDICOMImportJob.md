---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_GetDICOMImportJob.html
---

# GetDICOMImportJob
<a name="API_GetDICOMImportJob"></a>

Get the import job properties to learn more about the job or job progress.

**Note**
The `jobStatus` refers to the execution of the import job. Therefore, an import job can return a `jobStatus` as `COMPLETED` even if validation issues are discovered during the import process. If a `jobStatus` returns as `COMPLETED`, we still recommend you review the output manifests written to S3, as they provide details on the success or failure of individual P10 object imports.

## Request Syntax
<a name="API_GetDICOMImportJob_RequestSyntax"></a>

```
GET /getDICOMImportJob/datastore/{{datastoreId}}/job/{{jobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDICOMImportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datastoreId](#API_GetDICOMImportJob_RequestSyntax) **   <a name="healthimaging-GetDICOMImportJob-request-uri-datastoreId"></a>
The data store identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** [jobId](#API_GetDICOMImportJob_RequestSyntax) **   <a name="healthimaging-GetDICOMImportJob-request-uri-jobId"></a>
The import job identifier.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_GetDICOMImportJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDICOMImportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobProperties": {
      "dataAccessRoleArn": "string",
      "datastoreId": "string",
      "endedAt": number,
      "importConfiguration": { ... },
      "inputS3Uri": "string",
      "jobId": "string",
      "jobName": "string",
      "jobStatus": "string",
      "message": "string",
      "outputS3Uri": "string",
      "submittedAt": number
   }
}
```

## Response Elements
<a name="API_GetDICOMImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobProperties](#API_GetDICOMImportJob_ResponseSyntax) **   <a name="healthimaging-GetDICOMImportJob-response-jobProperties"></a>
The properties of the import job.
Type: [DICOMImportJobProperties](API_DICOMImportJobProperties.md) object

## Errors
<a name="API_GetDICOMImportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during processing of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource which does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints set by the service.
HTTP Status Code: 400

## See Also
<a name="API_GetDICOMImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/medical-imaging-2023-07-19/GetDICOMImportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/medical-imaging-2023-07-19/GetDICOMImportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/GetDICOMImportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/medical-imaging-2023-07-19/GetDICOMImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/GetDICOMImportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/medical-imaging-2023-07-19/GetDICOMImportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/medical-imaging-2023-07-19/GetDICOMImportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/medical-imaging-2023-07-19/GetDICOMImportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/medical-imaging-2023-07-19/GetDICOMImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/GetDICOMImportJob)
