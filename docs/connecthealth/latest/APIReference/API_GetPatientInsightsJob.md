---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_GetPatientInsightsJob.html
---

# GetPatientInsightsJob
<a name="API_GetPatientInsightsJob"></a>

Get details of a started patient insights job.

## Request Syntax
<a name="API_GetPatientInsightsJob_RequestSyntax"></a>

```
GET /domain/{{domainId}}/patient-insights-job/{{jobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPatientInsightsJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_GetPatientInsightsJob_RequestSyntax) **   <a name="connecthealth-GetPatientInsightsJob-request-uri-domainId"></a>

Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

 ** [jobId](#API_GetPatientInsightsJob_RequestSyntax) **   <a name="connecthealth-GetPatientInsightsJob-request-uri-jobId"></a>

Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

## Request Body
<a name="API_GetPatientInsightsJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPatientInsightsJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "encounterContext": {
      "encounterReason": "string"
   },
   "inputDataConfig": {
      "fhirServer": {
         "fhirEndpoint": "string",
         "oauthToken": "string"
      },
      "s3Sources": [
         {
            "uri": "string"
         }
      ]
   },
   "insightsContext": {
      "insightsType": "string"
   },
   "insightsOutput": {
      "uri": "string"
   },
   "jobArn": "string",
   "jobId": "string",
   "jobStatus": "string",
   "outputDataConfig": {
      "s3OutputPath": "string"
   },
   "patientContext": {
      "dateOfBirth": "string",
      "patientId": "string",
      "pronouns": "string"
   },
   "statusDetails": "string",
   "updatedTime": "string",
   "userContext": {
      "role": "string",
      "specialty": "string",
      "userId": "string"
   }
}
```

## Response Elements
<a name="API_GetPatientInsightsJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-GetPatientInsightsJob-response-creationTime"></a>
Date and time the patient insights job was submitted.
Type: Timestamp

 ** [encounterContext](#API_GetPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-GetPatientInsightsJob-response-encounterContext"></a>

Type: [PatientInsightsEncounterContext](API_PatientInsightsEncounterContext.md) object

 ** [inputDataConfig](#API_GetPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-GetPatientInsightsJob-response-inputDataConfig"></a>

Type: [InputDataConfig](API_InputDataConfig.md) object

 ** [insightsContext](#API_GetPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-GetPatientInsightsJob-response-insightsContext"></a>

Type: [InsightsContext](API_InsightsContext.md) object

 ** [insightsOutput](#API_GetPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-GetPatientInsightsJob-response-insightsOutput"></a>

Type: [InsightsOutput](API_InsightsOutput.md) object

 ** [jobArn](#API_GetPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-GetPatientInsightsJob-response-jobArn"></a>

Type: String
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn:aws[-a-z]*:health-agent:[-a-z0-9]+:[0-9]{12}:domain/[-a-zA-Z0-9-]+/patient-insights-job/[-a-zA-Z0-9_/.]+`

 ** [jobId](#API_GetPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-GetPatientInsightsJob-response-jobId"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.

 ** [jobStatus](#API_GetPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-GetPatientInsightsJob-response-jobStatus"></a>

Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | FAILED | SUCCEEDED`

 ** [outputDataConfig](#API_GetPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-GetPatientInsightsJob-response-outputDataConfig"></a>

Type: [OutputDataConfig](API_OutputDataConfig.md) object

 ** [patientContext](#API_GetPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-GetPatientInsightsJob-response-patientContext"></a>

Type: [PatientInsightsPatientContext](API_PatientInsightsPatientContext.md) object

 ** [statusDetails](#API_GetPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-GetPatientInsightsJob-response-statusDetails"></a>
Contains information about the status of a job.
Type: String
Pattern: `.*[\s\S]*\S[\s\S]*.*`

 ** [updatedTime](#API_GetPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-GetPatientInsightsJob-response-updatedTime"></a>
Date and time the patient insights job was last updated.
Type: Timestamp

 ** [userContext](#API_GetPatientInsightsJob_ResponseSyntax) **   <a name="connecthealth-GetPatientInsightsJob-response-userContext"></a>

Type: [UserContext](API_UserContext.md) object

## Errors
<a name="API_GetPatientInsightsJob_Errors"></a>

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
<a name="API_GetPatientInsightsJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/GetPatientInsightsJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/GetPatientInsightsJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/GetPatientInsightsJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/GetPatientInsightsJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/GetPatientInsightsJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/GetPatientInsightsJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/GetPatientInsightsJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/GetPatientInsightsJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/GetPatientInsightsJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/GetPatientInsightsJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
