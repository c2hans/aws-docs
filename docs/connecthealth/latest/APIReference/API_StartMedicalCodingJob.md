---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_StartMedicalCodingJob.html
---

# StartMedicalCodingJob
<a name="API_StartMedicalCodingJob"></a>

Starts an asynchronous job that generates medical codes (ICD-10 and CPT) for clinical text. Call GetMedicalCodingJob to check the status of the job. When the job succeeds, Amazon Connect Health writes the results to the output Amazon S3 location.

To tailor the codes to your organization, specify an ACTIVE medical coding dataset in the Domain. If you don't specify a dataset, the job uses the general medical coding knowledge base.

Medical coding jobs are in preview release and are subject to change.

## Request Syntax
<a name="API_StartMedicalCodingJob_RequestSyntax"></a>

```
POST /domain/{{domainId}}/medical-coding-job HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "datasetId": "{{string}}",
   "encounterContext": {
      "afterHours": {{boolean}},
      "encounterDate": "{{string}}",
      "encounterDurationMinutes": {{number}},
      "encounterReason": "{{string}}",
      "encounterType": "{{string}}"
   },
   "outputDataConfig": {
      "s3OutputPath": "{{string}}"
   },
   "patientContext": {
      "dateOfBirth": "{{string}}",
      "insurance": "{{string}}",
      "sex": "{{string}}",
      "status": "{{string}}"
   },
   "text": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartMedicalCodingJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_StartMedicalCodingJob_RequestSyntax) **   <a name="connecthealth-StartMedicalCodingJob-request-uri-domainId"></a>
The unique identifier of the parent Domain.
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_StartMedicalCodingJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartMedicalCodingJob_RequestSyntax) **   <a name="connecthealth-StartMedicalCodingJob-request-clientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Pattern: `.*[\s\S]*\S[\s\S]*.*`
Required: No

 ** [datasetId](#API_StartMedicalCodingJob_RequestSyntax) **   <a name="connecthealth-StartMedicalCodingJob-request-datasetId"></a>
The unique identifier of an ACTIVE medical coding dataset in the Domain to code against. If you don't specify a dataset, the job uses the general medical coding knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`
Required: No

 ** [encounterContext](#API_StartMedicalCodingJob_RequestSyntax) **   <a name="connecthealth-StartMedicalCodingJob-request-encounterContext"></a>
Encounter context for the job. Providing this information can improve the accuracy of the medical codes.
Type: [MedicalCodesEncounterContext](API_MedicalCodesEncounterContext.md) object
Required: No

 ** [outputDataConfig](#API_StartMedicalCodingJob_RequestSyntax) **   <a name="connecthealth-StartMedicalCodingJob-request-outputDataConfig"></a>
The output configuration for the job.
Type: [MedicalCodingOutputDataConfig](API_MedicalCodingOutputDataConfig.md) object
Required: Yes

 ** [patientContext](#API_StartMedicalCodingJob_RequestSyntax) **   <a name="connecthealth-StartMedicalCodingJob-request-patientContext"></a>
Patient context for the job. Providing this information can improve the accuracy of the medical codes.
Type: [MedicalCodesPatientContext](API_MedicalCodesPatientContext.md) object
Required: No

 ** [text](#API_StartMedicalCodingJob_RequestSyntax) **   <a name="connecthealth-StartMedicalCodingJob-request-text"></a>
The clinical text to generate medical codes for, such as a clinical note.
Type: String
Pattern: `.*[\s\S]*\S[\s\S]*.*`
Required: Yes

## Response Syntax
<a name="API_StartMedicalCodingJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "jobArn": "string",
   "jobId": "string"
}
```

## Response Elements
<a name="API_StartMedicalCodingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_StartMedicalCodingJob_ResponseSyntax) **   <a name="connecthealth-StartMedicalCodingJob-response-creationTime"></a>
The date and time that the medical coding job was created.
Type: Timestamp

 ** [jobArn](#API_StartMedicalCodingJob_ResponseSyntax) **   <a name="connecthealth-StartMedicalCodingJob-response-jobArn"></a>
The Amazon Resource Name (ARN) of the medical coding job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn:aws[-a-z]*:health-agent:[-a-z0-9]+:[0-9]{12}:domain/[-a-zA-Z0-9-]+/medical-coding-job/[-a-zA-Z0-9_/.]+`

 ** [jobId](#API_StartMedicalCodingJob_ResponseSyntax) **   <a name="connecthealth-StartMedicalCodingJob-response-jobId"></a>
The unique identifier of the medical coding job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.

## Errors
<a name="API_StartMedicalCodingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error is thrown when the client does not supply proper credentials to the API.
HTTP Status Code: 401

 ** ConflictException **
This error is thrown when a resource update is no longer valid due to assumptions about initial state changing.
HTTP Status Code: 409

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
<a name="API_StartMedicalCodingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/StartMedicalCodingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/StartMedicalCodingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/StartMedicalCodingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/StartMedicalCodingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/StartMedicalCodingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/StartMedicalCodingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/StartMedicalCodingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/StartMedicalCodingJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/StartMedicalCodingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/StartMedicalCodingJob)
