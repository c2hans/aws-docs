---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateInputSource.html
---

# CreateInputSource
<a name="API_CreateInputSource"></a>

Creates an input source for a service.

## Request Syntax
<a name="API_CreateInputSource_RequestSyntax"></a>

```
POST /v2/create-input-source HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "resourceConfiguration": { ... },
   "serviceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateInputSource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateInputSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateInputSource_RequestSyntax) **   <a name="ngresiliencehub-CreateInputSource-request-clientToken"></a>
Idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [resourceConfiguration](#API_CreateInputSource_RequestSyntax) **   <a name="ngresiliencehub-CreateInputSource-request-resourceConfiguration"></a>
Resource configuration for an input source. Provide exactly one field.
Type: [ResourceConfiguration](API_ResourceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [serviceArn](#API_CreateInputSource_RequestSyntax) **   <a name="ngresiliencehub-CreateInputSource-request-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

## Response Syntax
<a name="API_CreateInputSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "inputSourceId": "string",
   "serviceArn": "string"
}
```

## Response Elements
<a name="API_CreateInputSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [inputSourceId](#API_CreateInputSource_ResponseSyntax) **   <a name="ngresiliencehub-CreateInputSource-response-inputSourceId"></a>
The unique identifier assigned to the created input source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\S{1,255}`

 ** [serviceArn](#API_CreateInputSource_ResponseSyntax) **   <a name="ngresiliencehub-CreateInputSource-response-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

## Errors
<a name="API_CreateInputSource_Errors"></a>

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
<a name="API_CreateInputSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/CreateInputSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/CreateInputSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/CreateInputSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/CreateInputSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/CreateInputSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/CreateInputSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/CreateInputSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/CreateInputSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/CreateInputSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/CreateInputSource)
