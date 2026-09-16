---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateUserJourney.html
---

# CreateUserJourney
<a name="API_CreateUserJourney"></a>

Creates a user journey within a system.

## Request Syntax
<a name="API_CreateUserJourney_RequestSyntax"></a>

```
POST /v2/create-user-journey HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "policyArn": "{{string}}",
   "systemArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateUserJourney_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateUserJourney_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateUserJourney_RequestSyntax) **   <a name="ngresiliencehub-CreateUserJourney-request-clientToken"></a>
Idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [description](#API_CreateUserJourney_RequestSyntax) **   <a name="ngresiliencehub-CreateUserJourney-request-description"></a>
Resource description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [name](#API_CreateUserJourney_RequestSyntax) **   <a name="ngresiliencehub-CreateUserJourney-request-name"></a>
Entity label (not part of ARN — spaces allowed).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9 _\-]{1,59}`
Required: Yes

 ** [policyArn](#API_CreateUserJourney_RequestSyntax) **   <a name="ngresiliencehub-CreateUserJourney-request-policyArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** [systemArn](#API_CreateUserJourney_RequestSyntax) **   <a name="ngresiliencehub-CreateUserJourney-request-systemArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

## Response Syntax
<a name="API_CreateUserJourney_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "userJourney": {
      "createdAt": number,
      "description": "string",
      "name": "string",
      "policyArn": "string",
      "updatedAt": number,
      "userJourneyId": "string"
   }
}
```

## Response Elements
<a name="API_CreateUserJourney_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [userJourney](#API_CreateUserJourney_ResponseSyntax) **   <a name="ngresiliencehub-CreateUserJourney-response-userJourney"></a>
The created user journey.
Type: [UserJourney](API_UserJourney.md) object

## Errors
<a name="API_CreateUserJourney_Errors"></a>

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
<a name="API_CreateUserJourney_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/CreateUserJourney)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/CreateUserJourney)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/CreateUserJourney)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/CreateUserJourney)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/CreateUserJourney)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/CreateUserJourney)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/CreateUserJourney)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/CreateUserJourney)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/CreateUserJourney)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/CreateUserJourney)
