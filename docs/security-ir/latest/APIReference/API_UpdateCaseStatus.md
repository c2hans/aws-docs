---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UpdateCaseStatus.html
---

# UpdateCaseStatus
<a name="API_UpdateCaseStatus"></a>

Updates the state transitions for a designated cases.

 **Self-managed**: the following states are available for self-managed cases.
+ Submitted → Detection and Analysis
+ Submitted → Post-incident Activities
+ Submitted → Containment, Eradication, and Recovery
+ Detection and Analysis → Containment, Eradication, and Recovery
+ Detection and Analysis → Post-incident Activities
+ Containment, Eradication, and Recovery → Detection and Analysis
+ Containment, Eradication, and Recovery → Post-incident Activities
+ Post-incident Activities → Containment, Eradication, and Recovery
+ Post-incident Activities → Detection and Analysis
+ Any → Closed

 **AWS supported**: You must use the `CloseCase` API to close.

## Request Syntax
<a name="API_UpdateCaseStatus_RequestSyntax"></a>

```
POST /v1/cases/{{caseId}}/update-case-status HTTP/1.1
Content-type: application/json

{
   "caseStatus": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateCaseStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_UpdateCaseStatus_RequestSyntax) **   <a name="securityir-UpdateCaseStatus-request-uri-caseId"></a>
Required element for UpdateCaseStatus to identify the case to update.
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `\d{10,32}.*`
Required: Yes

## Request Body
<a name="API_UpdateCaseStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [caseStatus](#API_UpdateCaseStatus_RequestSyntax) **   <a name="securityir-UpdateCaseStatus-request-caseStatus"></a>
Required element for UpdateCaseStatus to identify the status for a case. Options include `Submitted | Detection and Analysis | Containment, Eradication and Recovery | Post-incident Activities`.
Type: String
Valid Values: `Submitted | Detection and Analysis | Containment, Eradication and Recovery | Post-incident Activities`
Required: Yes

## Response Syntax
<a name="API_UpdateCaseStatus_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "caseStatus": "string"
}
```

## Response Elements
<a name="API_UpdateCaseStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [caseStatus](#API_UpdateCaseStatus_ResponseSyntax) **   <a name="securityir-UpdateCaseStatus-response-caseStatus"></a>
Response element for UpdateCaseStatus showing the newly configured status.
Type: String
Valid Values: `Submitted | Detection and Analysis | Containment, Eradication and Recovery | Post-incident Activities`

## Errors
<a name="API_UpdateCaseStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** message **
The ID of the resource which lead to the access denial.
HTTP Status Code: 403

 ** ConflictException **
Returned when there is a conflict with the current state of the resource.
For UpdateResolverType, this error may occur when attempting to change an AWS-supported case to Self-managed, which is not supported.
 ** message **
The exception message.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **

 ** message **
The exception message.
 ** retryAfterSeconds **
The number of seconds after which to retry the request.
HTTP Status Code: 500

 ** InvalidTokenException **

 ** message **
The exception message.
HTTP Status Code: 423

 ** ResourceNotFoundException **

 ** message **
The exception message.
HTTP Status Code: 404

 ** SecurityIncidentResponseNotActiveException **

 ** message **
The exception message.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **

 ** message **
The exception message.
 ** quotaCode **
The code of the quota.
 ** resourceId **
The ID of the requested resource which lead to the service quota exception.
 ** resourceType **
The type of the requested resource which lead to the service quota exception.
 ** serviceCode **
The service code of the quota.
HTTP Status Code: 402

 ** ThrottlingException **

 ** message **
The exception message.
 ** quotaCode **
The quota code of the exception.
 ** retryAfterSeconds **
The number of seconds after which to retry the request.
 ** serviceCode **
The service code of the exception.
HTTP Status Code: 429

 ** ValidationException **
Returned when the request contains invalid parameters.
For UpdateResolverType, this error may occur when attempting an unsupported resolver type transition.
 ** fieldList **
The fields which lead to the exception.
 ** message **
The exception message.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateCaseStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/UpdateCaseStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/UpdateCaseStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/UpdateCaseStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/UpdateCaseStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/UpdateCaseStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/UpdateCaseStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/UpdateCaseStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/UpdateCaseStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/UpdateCaseStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/UpdateCaseStatus)
