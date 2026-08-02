---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateAssertion.html
---

# CreateAssertion
<a name="API_CreateAssertion"></a>

Creates a resilience assertion for a service.

## Request Syntax
<a name="API_CreateAssertion_RequestSyntax"></a>

```
POST /v2/create-assertion HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "serviceArn": "{{string}}",
   "text": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAssertion_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAssertion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateAssertion_RequestSyntax) **   <a name="ngresiliencehub-CreateAssertion-request-clientToken"></a>
Idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [serviceArn](#API_CreateAssertion_RequestSyntax) **   <a name="ngresiliencehub-CreateAssertion-request-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [text](#API_CreateAssertion_RequestSyntax) **   <a name="ngresiliencehub-CreateAssertion-request-text"></a>
The text content of the assertion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## Response Syntax
<a name="API_CreateAssertion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assertion": {
      "assertionId": "string",
      "createdAt": number,
      "serviceArn": "string",
      "source": "string",
      "text": "string",
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_CreateAssertion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assertion](#API_CreateAssertion_ResponseSyntax) **   <a name="ngresiliencehub-CreateAssertion-response-assertion"></a>
The created assertion.
Type: [Assertion](API_Assertion.md) object

## Errors
<a name="API_CreateAssertion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied — caller lacks required permissions.
HTTP Status Code: 403

 ** ConflictException **
Conflict — resource already exists.
HTTP Status Code: 409

 ** InternalServerException **
Internal service error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource not found.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Service quota exceeded.
HTTP Status Code: 402

 ** ValidationException **
Validation error — invalid input parameters.
 ** fieldList **
The list of fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_CreateAssertion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/CreateAssertion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/CreateAssertion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/CreateAssertion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/CreateAssertion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/CreateAssertion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/CreateAssertion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/CreateAssertion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/CreateAssertion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/CreateAssertion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/CreateAssertion)
