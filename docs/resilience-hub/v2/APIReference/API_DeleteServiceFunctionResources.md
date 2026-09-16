---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DeleteServiceFunctionResources.html
---

# DeleteServiceFunctionResources
<a name="API_DeleteServiceFunctionResources"></a>

Removes resources from a service function.

## Request Syntax
<a name="API_DeleteServiceFunctionResources_RequestSyntax"></a>

```
POST /v2/delete-service-function-resources HTTP/1.1
Content-type: application/json

{
   "resources": [ "{{string}}" ],
   "serviceArn": "{{string}}",
   "serviceFunctionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteServiceFunctionResources_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteServiceFunctionResources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resources](#API_DeleteServiceFunctionResources_RequestSyntax) **   <a name="ngresiliencehub-DeleteServiceFunctionResources-request-resources"></a>
The list of resources to remove from the service function.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** [serviceArn](#API_DeleteServiceFunctionResources_RequestSyntax) **   <a name="ngresiliencehub-DeleteServiceFunctionResources-request-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [serviceFunctionId](#API_DeleteServiceFunctionResources_RequestSyntax) **   <a name="ngresiliencehub-DeleteServiceFunctionResources-request-serviceFunctionId"></a>
The identifier of the service function to remove resources from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\S{1,255}`
Required: Yes

## Response Syntax
<a name="API_DeleteServiceFunctionResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "resources": [ "string" ],
   "serviceArn": "string",
   "serviceFunctionId": "string"
}
```

## Response Elements
<a name="API_DeleteServiceFunctionResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resources](#API_DeleteServiceFunctionResources_ResponseSyntax) **   <a name="ngresiliencehub-DeleteServiceFunctionResources-response-resources"></a>
The list of resources that were removed.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [serviceArn](#API_DeleteServiceFunctionResources_ResponseSyntax) **   <a name="ngresiliencehub-DeleteServiceFunctionResources-response-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [serviceFunctionId](#API_DeleteServiceFunctionResources_ResponseSyntax) **   <a name="ngresiliencehub-DeleteServiceFunctionResources-response-serviceFunctionId"></a>
The identifier of the service function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\S{1,255}`

## Errors
<a name="API_DeleteServiceFunctionResources_Errors"></a>

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
<a name="API_DeleteServiceFunctionResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/DeleteServiceFunctionResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/DeleteServiceFunctionResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/DeleteServiceFunctionResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/DeleteServiceFunctionResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/DeleteServiceFunctionResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/DeleteServiceFunctionResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/DeleteServiceFunctionResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/DeleteServiceFunctionResources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/DeleteServiceFunctionResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/DeleteServiceFunctionResources)
