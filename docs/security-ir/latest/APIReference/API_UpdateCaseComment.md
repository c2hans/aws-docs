---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UpdateCaseComment.html
---

# UpdateCaseComment
<a name="API_UpdateCaseComment"></a>

Updates an existing case comment.

## Request Syntax
<a name="API_UpdateCaseComment_RequestSyntax"></a>

```
PUT /v1/cases/{{caseId}}/update-case-comment/{{commentId}} HTTP/1.1
Content-type: application/json

{
   "body": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateCaseComment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_UpdateCaseComment_RequestSyntax) **   <a name="securityir-UpdateCaseComment-request-uri-caseId"></a>
Required element for UpdateCaseComment to identify the case ID containing the comment to be updated.
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `\d{10,32}.*`
Required: Yes

 ** [commentId](#API_UpdateCaseComment_RequestSyntax) **   <a name="securityir-UpdateCaseComment-request-uri-commentId"></a>
Required element for UpdateCaseComment to identify the case ID to be updated.
Length Constraints: Fixed length of 6.
Pattern: `\d{6}`
Required: Yes

## Request Body
<a name="API_UpdateCaseComment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [body](#API_UpdateCaseComment_RequestSyntax) **   <a name="securityir-UpdateCaseComment-request-body"></a>
Required element for UpdateCaseComment to identify the content for the comment to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12000.
Required: Yes

## Response Syntax
<a name="API_UpdateCaseComment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "body": "string",
   "commentId": "string"
}
```

## Response Elements
<a name="API_UpdateCaseComment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [body](#API_UpdateCaseComment_ResponseSyntax) **   <a name="securityir-UpdateCaseComment-response-body"></a>
Response element for UpdateCaseComment providing the updated comment content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12000.

 ** [commentId](#API_UpdateCaseComment_ResponseSyntax) **   <a name="securityir-UpdateCaseComment-response-commentId"></a>
Response element for UpdateCaseComment providing the updated comment ID.
Type: String
Length Constraints: Fixed length of 6.
Pattern: `\d{6}`

## Errors
<a name="API_UpdateCaseComment_Errors"></a>

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
<a name="API_UpdateCaseComment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/UpdateCaseComment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/UpdateCaseComment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/UpdateCaseComment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/UpdateCaseComment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/UpdateCaseComment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/UpdateCaseComment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/UpdateCaseComment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/UpdateCaseComment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/UpdateCaseComment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/UpdateCaseComment)
