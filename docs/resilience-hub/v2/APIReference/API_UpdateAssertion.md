---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_UpdateAssertion.html
---

# UpdateAssertion
<a name="API_UpdateAssertion"></a>

Updates a resilience assertion.

## Request Syntax
<a name="API_UpdateAssertion_RequestSyntax"></a>

```
POST /v2/update-assertion HTTP/1.1
Content-type: application/json

{
   "assertionId": "{{string}}",
   "serviceArn": "{{string}}",
   "text": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAssertion_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateAssertion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assertionId](#API_UpdateAssertion_RequestSyntax) **   <a name="ngresiliencehub-UpdateAssertion-request-assertionId"></a>
The unique identifier of the assertion to update.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}`
Required: Yes

 ** [serviceArn](#API_UpdateAssertion_RequestSyntax) **   <a name="ngresiliencehub-UpdateAssertion-request-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [text](#API_UpdateAssertion_RequestSyntax) **   <a name="ngresiliencehub-UpdateAssertion-request-text"></a>
The updated text content of the assertion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

## Response Syntax
<a name="API_UpdateAssertion_ResponseSyntax"></a>

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
<a name="API_UpdateAssertion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assertion](#API_UpdateAssertion_ResponseSyntax) **   <a name="ngresiliencehub-UpdateAssertion-response-assertion"></a>
The updated assertion.
Type: [Assertion](API_Assertion.md) object

## Errors
<a name="API_UpdateAssertion_Errors"></a>

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

 ** ValidationException **
Validation error — invalid input parameters.
 ** fieldList **
The list of fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAssertion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/UpdateAssertion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/UpdateAssertion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/UpdateAssertion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/UpdateAssertion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/UpdateAssertion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/UpdateAssertion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/UpdateAssertion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/UpdateAssertion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/UpdateAssertion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/UpdateAssertion)
