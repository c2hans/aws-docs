---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_GetMedicalCodingJob.html
---

# GetMedicalCodingJob

Retrieves information about a medical coding job, including its status and, when it succeeds, the location of its results.

Medical coding jobs are in preview release and are subject to change.

## Request Syntax
<a name="API_GetMedicalCodingJob_RequestSyntax"></a>

```
GET /domain/{{domainId}}/medical-coding-job/{{jobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMedicalCodingJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_GetMedicalCodingJob_RequestSyntax) **   <a name="connecthealth-GetMedicalCodingJob-request-uri-domainId"></a>
The unique identifier of the parent Domain.
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

 ** [jobId](#API_GetMedicalCodingJob_RequestSyntax) **   <a name="connecthealth-GetMedicalCodingJob-request-uri-jobId"></a>
The unique identifier of the medical coding job.
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

## Request Body
<a name="API_GetMedicalCodingJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMedicalCodingJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "datasetId": "string",
   "encounterContext": {
      "afterHours": boolean,
      "encounterDate": "string",
      "encounterDurationMinutes": number,
      "encounterReason": "string",
      "encounterType": "string"
   },
   "jobArn": "string",
   "jobId": "string",
   "jobStatus": "string",
   "medicalCodingOutput": {
      "uri": "string"
   },
   "outputDataConfig": {
      "s3OutputPath": "string"
   },
   "patientContext": {
      "dateOfBirth": "string",
      "insurance": "string",
      "sex": "string",
      "status": "string"
   },
   "statusDetails": "string",
   "text": "string",
   "updatedTime": "string"
}
```

## Response Elements
<a name="API_GetMedicalCodingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetMedicalCodingJob_ResponseSyntax) **   <a name="connecthealth-GetMedicalCodingJob-response-creationTime"></a>
The date and time that the medical coding job was created.
Type: Timestamp

 ** [datasetId](#API_GetMedicalCodingJob_ResponseSyntax) **   <a name="connecthealth-GetMedicalCodingJob-response-datasetId"></a>
The unique identifier of the dataset that the job codes against. Not returned if the job uses the general medical coding knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`

 ** [encounterContext](#API_GetMedicalCodingJob_ResponseSyntax) **   <a name="connecthealth-GetMedicalCodingJob-response-encounterContext"></a>
The encounter context that you provided for the job.
Type: [MedicalCodesEncounterContext](API_MedicalCodesEncounterContext.md) object

 ** [jobArn](#API_GetMedicalCodingJob_ResponseSyntax) **   <a name="connecthealth-GetMedicalCodingJob-response-jobArn"></a>
The Amazon Resource Name (ARN) of the medical coding job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn:aws[-a-z]*:health-agent:[-a-z0-9]+:[0-9]{12}:domain/[-a-zA-Z0-9-]+/medical-coding-job/[-a-zA-Z0-9_/.]+`

 ** [jobId](#API_GetMedicalCodingJob_ResponseSyntax) **   <a name="connecthealth-GetMedicalCodingJob-response-jobId"></a>
The unique identifier of the medical coding job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.

 ** [jobStatus](#API_GetMedicalCodingJob_ResponseSyntax) **   <a name="connecthealth-GetMedicalCodingJob-response-jobStatus"></a>
The status of the medical coding job.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | FAILED | SUCCEEDED`

 ** [medicalCodingOutput](#API_GetMedicalCodingJob_ResponseSyntax) **   <a name="connecthealth-GetMedicalCodingJob-response-medicalCodingOutput"></a>
The location of the job results. Returned when the job succeeds.
Type: [MedicalCodingOutput](API_MedicalCodingOutput.md) object

 ** [outputDataConfig](#API_GetMedicalCodingJob_ResponseSyntax) **   <a name="connecthealth-GetMedicalCodingJob-response-outputDataConfig"></a>
The output configuration that you provided for the job.
Type: [MedicalCodingOutputDataConfig](API_MedicalCodingOutputDataConfig.md) object

 ** [patientContext](#API_GetMedicalCodingJob_ResponseSyntax) **   <a name="connecthealth-GetMedicalCodingJob-response-patientContext"></a>
The patient context that you provided for the job.
Type: [MedicalCodesPatientContext](API_MedicalCodesPatientContext.md) object

 ** [statusDetails](#API_GetMedicalCodingJob_ResponseSyntax) **   <a name="connecthealth-GetMedicalCodingJob-response-statusDetails"></a>
Details about the status of the job, such as the reason that it failed.
Type: String
Pattern: `.*[\s\S]*\S[\s\S]*.*`

 ** [text](#API_GetMedicalCodingJob_ResponseSyntax) **   <a name="connecthealth-GetMedicalCodingJob-response-text"></a>
The clinical text that the medical coding job codes.
Type: String
Pattern: `.*[\s\S]*\S[\s\S]*.*`

 ** [updatedTime](#API_GetMedicalCodingJob_ResponseSyntax) **   <a name="connecthealth-GetMedicalCodingJob-response-updatedTime"></a>
The date and time that the medical coding job was last updated.
Type: Timestamp

## Errors
<a name="API_GetMedicalCodingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error is thrown when the client does not supply proper credentials to the API.
HTTP Status Code: 401

 ** InternalServerException **
This error is thrown when a transient error causes our API to fail.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This error is thrown when the requested resource is not found.
HTTP Status Code: 404

 ** ThrottlingException **
This error is thrown when the client exceeds the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
This error is thrown when the client supplies invalid input to the API.
HTTP Status Code: 400

## See Also
<a name="API_GetMedicalCodingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/GetMedicalCodingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/GetMedicalCodingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/GetMedicalCodingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/GetMedicalCodingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/GetMedicalCodingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/GetMedicalCodingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/GetMedicalCodingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/GetMedicalCodingJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/GetMedicalCodingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/GetMedicalCodingJob)
