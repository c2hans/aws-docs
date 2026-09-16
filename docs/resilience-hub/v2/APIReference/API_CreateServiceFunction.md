---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateServiceFunction.html
---

# CreateServiceFunction
<a name="API_CreateServiceFunction"></a>

Creates a service function within a service.

## Request Syntax
<a name="API_CreateServiceFunction_RequestSyntax"></a>

```
POST /v2/create-service-function HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "criticality": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "serviceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateServiceFunction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateServiceFunction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateServiceFunction_RequestSyntax) **   <a name="ngresiliencehub-CreateServiceFunction-request-clientToken"></a>
Idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [criticality](#API_CreateServiceFunction_RequestSyntax) **   <a name="ngresiliencehub-CreateServiceFunction-request-criticality"></a>
The criticality level of the service function.
Type: String
Valid Values: `PRIMARY | SUPPLEMENTAL`
Required: Yes

 ** [description](#API_CreateServiceFunction_RequestSyntax) **   <a name="ngresiliencehub-CreateServiceFunction-request-description"></a>
Resource description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [name](#API_CreateServiceFunction_RequestSyntax) **   <a name="ngresiliencehub-CreateServiceFunction-request-name"></a>
Entity label (not part of ARN — spaces allowed).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9 _\-]{1,59}`
Required: Yes

 ** [serviceArn](#API_CreateServiceFunction_RequestSyntax) **   <a name="ngresiliencehub-CreateServiceFunction-request-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

## Response Syntax
<a name="API_CreateServiceFunction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "serviceFunction": {
      "createdAt": number,
      "criticality": "string",
      "description": "string",
      "name": "string",
      "resourceCount": number,
      "serviceArn": "string",
      "serviceFunctionId": "string",
      "source": "string",
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_CreateServiceFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceFunction](#API_CreateServiceFunction_ResponseSyntax) **   <a name="ngresiliencehub-CreateServiceFunction-response-serviceFunction"></a>
The created service function.
Type: [ServiceFunction](API_ServiceFunction.md) object

## Errors
<a name="API_CreateServiceFunction_Errors"></a>

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
<a name="API_CreateServiceFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/CreateServiceFunction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/CreateServiceFunction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/CreateServiceFunction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/CreateServiceFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/CreateServiceFunction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/CreateServiceFunction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/CreateServiceFunction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/CreateServiceFunction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/CreateServiceFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/CreateServiceFunction)
