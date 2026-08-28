---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_GetMedicalScribeListeningSession.html
---

# GetMedicalScribeListeningSession
<a name="API_GetMedicalScribeListeningSession"></a>

Retrieves details about an existing Medical Scribe listening session

## Request Syntax
<a name="API_GetMedicalScribeListeningSession_RequestSyntax"></a>

```
GET /medical-scribe-stream/domain/{{domainId}}/subscription/{{subscriptionId}}/session/{{sessionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMedicalScribeListeningSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_GetMedicalScribeListeningSession_RequestSyntax) **   <a name="connecthealth-GetMedicalScribeListeningSession-request-uri-domainId"></a>
The Domain identifier
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

 ** [sessionId](#API_GetMedicalScribeListeningSession_RequestSyntax) **   <a name="connecthealth-GetMedicalScribeListeningSession-request-uri-sessionId"></a>
The Session identifier
Length Constraints: Fixed length of 36.
Pattern: `.*[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}.*`
Required: Yes

 ** [subscriptionId](#API_GetMedicalScribeListeningSession_RequestSyntax) **   <a name="connecthealth-GetMedicalScribeListeningSession-request-uri-subscriptionId"></a>
The Subscription identifier
Length Constraints: Fixed length of 25.
Pattern: `sub-[a-zA-Z0-9]{21}`
Required: Yes

## Request Body
<a name="API_GetMedicalScribeListeningSession_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMedicalScribeListeningSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "medicalScribeListeningSessionDetails": {
      "channelDefinitions": [
         {
            "channelId": number,
            "participantRole": "string"
         }
      ],
      "domainId": "string",
      "encounterContextProvided": boolean,
      "languageCode": "string",
      "mediaEncoding": "string",
      "mediaSampleRateHertz": number,
      "postStreamActionResult": {
         "clinicalNoteGenerationResult": {
            "afterVisitSummaryResult": {
               "failureReason": "string",
               "outputLocation": "string",
               "status": "string"
            },
            "noteResult": {
               "failureReason": "string",
               "outputLocation": "string",
               "status": "string"
            },
            "transcriptResult": {
               "failureReason": "string",
               "outputLocation": "string",
               "status": "string"
            }
         }
      },
      "postStreamActionSettings": {
         "clinicalNoteGenerationSettings": {
            "noteTemplateSettings": { ... }
         },
         "outputS3Uri": "string"
      },
      "sessionId": "string",
      "streamCreationTime": number,
      "streamEndTime": number,
      "streamStatus": "string",
      "subscriptionId": "string"
   }
}
```

## Response Elements
<a name="API_GetMedicalScribeListeningSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [medicalScribeListeningSessionDetails](#API_GetMedicalScribeListeningSession_ResponseSyntax) **   <a name="connecthealth-GetMedicalScribeListeningSession-response-medicalScribeListeningSessionDetails"></a>
Details about the Medical Scribe listening session
Type: [MedicalScribeListeningSessionDetails](API_MedicalScribeListeningSessionDetails.md) object

## Errors
<a name="API_GetMedicalScribeListeningSession_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
This error is thrown when the client exceeds the allowed request rate.
HTTP Status Code: 429

## See Also
<a name="API_GetMedicalScribeListeningSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/GetMedicalScribeListeningSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/GetMedicalScribeListeningSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/GetMedicalScribeListeningSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/GetMedicalScribeListeningSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/GetMedicalScribeListeningSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/GetMedicalScribeListeningSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/GetMedicalScribeListeningSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/GetMedicalScribeListeningSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/GetMedicalScribeListeningSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/GetMedicalScribeListeningSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
