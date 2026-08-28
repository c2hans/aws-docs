---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_StartDICOMImportJob.html
---

# StartDICOMImportJob
<a name="API_StartDICOMImportJob"></a>

Start importing bulk data into an `ACTIVE` data store. The import job imports DICOM P10 files or enhances existing DICOM files with JSON metadata. The `importConfiguration` parameter specifies the import type. The data is found in the S3 prefix specified by the `inputS3Uri` parameter. The import job stores processing results in the file specified by the `outputS3Uri` parameter.

## Request Syntax
<a name="API_StartDICOMImportJob_RequestSyntax"></a>

```
POST /startDICOMImportJob/datastore/{{datastoreId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "dataAccessRoleArn": "{{string}}",
   "importConfiguration": { ... },
   "inputOwnerAccountId": "{{string}}",
   "inputS3Uri": "{{string}}",
   "jobName": "{{string}}",
   "outputS3Uri": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartDICOMImportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datastoreId](#API_StartDICOMImportJob_RequestSyntax) **   <a name="healthimaging-StartDICOMImportJob-request-uri-datastoreId"></a>
The data store identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

## Request Body
<a name="API_StartDICOMImportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartDICOMImportJob_RequestSyntax) **   <a name="healthimaging-StartDICOMImportJob-request-clientToken"></a>
A unique identifier for API idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._-]+`
Required: Yes

 ** [dataAccessRoleArn](#API_StartDICOMImportJob_RequestSyntax) **   <a name="healthimaging-StartDICOMImportJob-request-dataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants permission to access medical imaging resources.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: Yes

 ** [importConfiguration](#API_StartDICOMImportJob_RequestSyntax) **   <a name="healthimaging-StartDICOMImportJob-request-importConfiguration"></a>
The import configuration for the import job.
Type: [ImportConfiguration](API_ImportConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [inputOwnerAccountId](#API_StartDICOMImportJob_RequestSyntax) **   <a name="healthimaging-StartDICOMImportJob-request-inputOwnerAccountId"></a>
The account ID of the source S3 bucket owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** [inputS3Uri](#API_StartDICOMImportJob_RequestSyntax) **   <a name="healthimaging-StartDICOMImportJob-request-inputS3Uri"></a>
The input prefix path for the S3 bucket that contains the DICOM files to be imported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: Yes

 ** [jobName](#API_StartDICOMImportJob_RequestSyntax) **   <a name="healthimaging-StartDICOMImportJob-request-jobName"></a>
The import job name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/#-]+`
Required: No

 ** [outputS3Uri](#API_StartDICOMImportJob_RequestSyntax) **   <a name="healthimaging-StartDICOMImportJob-request-outputS3Uri"></a>
The output prefix of the S3 bucket to upload the results of the DICOM import job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: Yes

## Response Syntax
<a name="API_StartDICOMImportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datastoreId": "string",
   "jobId": "string",
   "jobStatus": "string",
   "submittedAt": number
}
```

## Response Elements
<a name="API_StartDICOMImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datastoreId](#API_StartDICOMImportJob_ResponseSyntax) **   <a name="healthimaging-StartDICOMImportJob-response-datastoreId"></a>
The data store identifier.
Type: String
Pattern: `[0-9a-z]{32}`

 ** [jobId](#API_StartDICOMImportJob_ResponseSyntax) **   <a name="healthimaging-StartDICOMImportJob-response-jobId"></a>
The import job identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[0-9a-z]+`

 ** [jobStatus](#API_StartDICOMImportJob_ResponseSyntax) **   <a name="healthimaging-StartDICOMImportJob-response-jobStatus"></a>
The import job status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | FAILED`

 ** [submittedAt](#API_StartDICOMImportJob_ResponseSyntax) **   <a name="healthimaging-StartDICOMImportJob-response-submittedAt"></a>
The timestamp when the import job was submitted.
Type: Timestamp

## Errors
<a name="API_StartDICOMImportJob_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request caused a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints set by the service.
HTTP Status Code: 400

## See Also
<a name="API_StartDICOMImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/medical-imaging-2023-07-19/StartDICOMImportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/medical-imaging-2023-07-19/StartDICOMImportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/StartDICOMImportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/medical-imaging-2023-07-19/StartDICOMImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/StartDICOMImportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/medical-imaging-2023-07-19/StartDICOMImportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/medical-imaging-2023-07-19/StartDICOMImportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/medical-imaging-2023-07-19/StartDICOMImportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/medical-imaging-2023-07-19/StartDICOMImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/StartDICOMImportJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
