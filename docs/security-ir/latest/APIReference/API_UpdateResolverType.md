---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UpdateResolverType.html
---

# UpdateResolverType
<a name="API_UpdateResolverType"></a>

Updates the resolver type for a case.

**Important**
This operation only supports changing a case from Self-managed to AWS-supported resolution. Once a case is changed to AWS-supported, it cannot be changed back to Self-managed.

## Request Syntax
<a name="API_UpdateResolverType_RequestSyntax"></a>

```
POST /v1/cases/{{caseId}}/update-resolver-type HTTP/1.1
Content-type: application/json

{
   "resolverType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateResolverType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_UpdateResolverType_RequestSyntax) **   <a name="securityir-UpdateResolverType-request-uri-caseId"></a>
Required element for UpdateResolverType to identify the case to update.
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `\d{10,32}.*`
Required: Yes

## Request Body
<a name="API_UpdateResolverType_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resolverType](#API_UpdateResolverType_RequestSyntax) **   <a name="securityir-UpdateResolverType-request-resolverType"></a>
Required element for UpdateResolverType to identify the new resolver.
Valid values are `AWS` (for AWS-supported) or `Self` (for Self-managed). Note that you can only transition from Self-managed to AWS-supported. Attempting to change an AWS-supported case to Self-managed will result in an error.
Type: String
Valid Values: `AWS | Self`
Required: Yes

## Response Syntax
<a name="API_UpdateResolverType_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "caseId": "string",
   "caseStatus": "string",
   "resolverType": "string"
}
```

## Response Elements
<a name="API_UpdateResolverType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [caseId](#API_UpdateResolverType_ResponseSyntax) **   <a name="securityir-UpdateResolverType-response-caseId"></a>
Response element for UpdateResolver identifying the case ID being updated.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `\d{10,32}.*`

 ** [caseStatus](#API_UpdateResolverType_ResponseSyntax) **   <a name="securityir-UpdateResolverType-response-caseStatus"></a>
Response element for UpdateResolver identifying the current status of the case.
Type: String
Valid Values: `Submitted | Acknowledged | Detection and Analysis | Containment, Eradication and Recovery | Post-incident Activities | Ready to Close | Closed`

 ** [resolverType](#API_UpdateResolverType_ResponseSyntax) **   <a name="securityir-UpdateResolverType-response-resolverType"></a>
Response element for UpdateResolver identifying the current resolver of the case.
This value will be `AWS` after a successful transition from Self-managed to AWS-supported.
Type: String
Valid Values: `AWS | Self`

## Errors
<a name="API_UpdateResolverType_Errors"></a>

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
<a name="API_UpdateResolverType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/UpdateResolverType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/UpdateResolverType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/UpdateResolverType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/UpdateResolverType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/UpdateResolverType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/UpdateResolverType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/UpdateResolverType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/UpdateResolverType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/UpdateResolverType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/UpdateResolverType)
