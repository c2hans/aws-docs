---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_StartPatientInsightsJob.html
---

# StartPatientInsightsJob
<a name="API_StartPatientInsightsJob"></a>

Starts a new patient insights job.

## Request Syntax
<a name="API_StartPatientInsightsJob_RequestSyntax"></a>

```
POST /domain/{{domainId}}/patient-insights-job HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "encounterContext": {
      "encounterReason": "{{string}}"
   },
   "inputDataConfig": {
      "fhirServer": {
         "fhirEndpoint": "{{string}}",
         "oauthToken": "{{string}}"
      },
      "s3Sources": [
         {
            "uri": "{{string}}"
         }
      ]
   },
   "insightsContext": {
      "insightsType": "{{string}}"
   },
   "outputDataConfig": {
      "s3OutputPath": "{{string}}"
   },
   "patientContext": {
      "dateOfBirth": "{{string}}",
      "patientId": "{{string}}",
      "pronouns": "{{string}}"
   },
   "userContext": {
      "role": "{{string}}",
      "specialty": "{{string}}",
      "userId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartPatientInsightsJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_StartPatientInsightsJob_RequestSyntax) **   <a name="connecthealth-StartPatientInsightsJob-request-uri-domainId"></a>

Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_StartPatientInsightsJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartPatientInsightsJob_RequestSyntax) **   <a name="connecthealth-StartPatientInsightsJob-request-clientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Pattern: `.*[\s\S]*\S[\s\S]*.*`
Required: No

 ** [encounterContext](#API_StartPatientInsightsJob_RequestSyntax) **   <a name="connecthealth-StartPatientInsightsJob-request-encounterContext"></a>

Type: [PatientInsightsEncounterContext](API_PatientInsightsEncounterContext.md) object
Required: Yes

 ** [inputDataConfig](#API_StartPatientInsightsJob_RequestSyntax) **   <a name="connecthealth-StartPatientInsightsJob-request-inputDataConfig"></a>

Type: [InputDataConfig](API_InputDataConfig.md) object
Required: Yes

 ** [insightsContext](#API_StartPatientInsightsJob_RequestSyntax) **   <a name="connecthealth-StartPatientInsightsJob-request-insightsContext"></a>

Type: [InsightsContext](API_InsightsContext.md) object
Required: Yes

 ** [outputDataConfig](#API_StartPatientInsightsJob_RequestSyntax) **   <a name="connecthealth-StartPatientInsightsJob-request-outputDataConfig"></a>

Type: [OutputDataConfig](API_OutputDataConfig.md) object
Required: Yes

 ** [patientContext](#API_StartPatientInsightsJob_RequestSyntax) **   <a name="connecthealth-StartPatientInsightsJob-request-patientContext"></a>

Type: [PatientInsightsPatientContext](API_PatientInsightsPatientContext.md) object
Required: Yes

 ** [userContext](#API_StartPatientInsightsJob_RequestSyntax) **   <a name="connecthealth-StartPatientInsightsJob-request-userContext"></a>

Type: [UserContext](API_UserContext.md) object
Required: Yes

## Response Syntax
<a name="API_StartPatientInsightsJob_ResponseSyntax"></a>

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
<a name="API_StartPatientInsightsJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_StartPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-StartPatientInsightsJob-response-creationTime"></a>
Date and time the patient insights job was submitted.
Type: Timestamp

 ** [jobArn](#API_StartPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-StartPatientInsightsJob-response-jobArn"></a>

Type: String
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn:aws[-a-z]*:health-agent:[-a-z0-9]+:[0-9]{12}:domain/[-a-zA-Z0-9-]+/patient-insights-job/[-a-zA-Z0-9_/.]+`

 ** [jobId](#API_StartPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-StartPatientInsightsJob-response-jobId"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.

## Errors
<a name="API_StartPatientInsightsJob_Errors"></a>

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
<a name="API_StartPatientInsightsJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/StartPatientInsightsJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/StartPatientInsightsJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/StartPatientInsightsJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/StartPatientInsightsJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/StartPatientInsightsJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/StartPatientInsightsJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/StartPatientInsightsJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/StartPatientInsightsJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/StartPatientInsightsJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/StartPatientInsightsJob)
