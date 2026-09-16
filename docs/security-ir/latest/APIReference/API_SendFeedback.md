---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_SendFeedback.html
---

# SendFeedback
<a name="API_SendFeedback"></a>

Submits feedback about an investigation action or result. This operation allows users to provide usefulness ratings and comments to help improve the quality of investigation recommendations and actions.

## Request Syntax
<a name="API_SendFeedback_RequestSyntax"></a>

```
POST /v1/cases/{{caseId}}/feedback/{{resultId}}/send-feedback HTTP/1.1
Content-type: application/json

{
   "comment": "{{string}}",
   "usefulness": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendFeedback_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_SendFeedback_RequestSyntax) **   <a name="securityir-SendFeedback-request-uri-caseId"></a>
Required element that specifies the unique identifier of the case for which to submit feedback.
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `\d{10,32}.*`
Required: Yes

 ** [resultId](#API_SendFeedback_RequestSyntax) **   <a name="securityir-SendFeedback-request-uri-resultId"></a>
The unique identifier of the investigation result or action for which feedback is being provided.
Pattern: `inv-[a-z0-9]{10,32}`
Required: Yes

## Request Body
<a name="API_SendFeedback_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [comment](#API_SendFeedback_RequestSyntax) **   <a name="securityir-SendFeedback-request-comment"></a>
Optional text feedback providing additional context or details about the usefulness rating. This can include specific suggestions for improvement or explanations of the rating.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** [usefulness](#API_SendFeedback_RequestSyntax) **   <a name="securityir-SendFeedback-request-usefulness"></a>
A rating indicating how useful the investigation result or action was. This helps improve future recommendations and investigation quality.
Type: String
Valid Values: `USEFUL | NOT_USEFUL`
Required: Yes

## Response Syntax
<a name="API_SendFeedback_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_SendFeedback_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SendFeedback_Errors"></a>

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
<a name="API_SendFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/SendFeedback)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/SendFeedback)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/SendFeedback)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/SendFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/SendFeedback)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/SendFeedback)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/SendFeedback)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/SendFeedback)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/SendFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/SendFeedback)
