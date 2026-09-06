---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RegisterService.html
---

# RegisterService
<a name="API_RegisterService"></a>

This operation registers the specified service

## Request Syntax
<a name="API_RegisterService_RequestSyntax"></a>

```
POST /v1/register/{{service}} HTTP/1.1
Content-type: application/json

{
   "exchangeUrlPrivateConnectionName": "{{string}}",
   "kmsKeyArn": "{{string}}",
   "name": "{{string}}",
   "privateConnectionName": "{{string}}",
   "serviceDetails": { ... },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "targetUrlPrivateConnectionName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterService_RequestParameters"></a>

The request uses the following URI parameters.

 ** [service](#API_RegisterService_RequestSyntax) **   <a name="devopsagent-RegisterService-request-uri-service"></a>
Services that can be registered via the post-registration API (excludes OAuth 3LO services).
Valid Values: `dynatrace | servicenow | pagerduty | gitlab | eventChannel | mcpservernewrelic | mcpservergrafana | mcpserverdatadog | mcpserver | mcpserversplunk | azureidentity | mcpserversigv4 | remoteagent | remoteagentsigv4`
Required: Yes

## Request Body
<a name="API_RegisterService_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [exchangeUrlPrivateConnectionName](#API_RegisterService_RequestSyntax) **   <a name="devopsagent-RegisterService-request-exchangeUrlPrivateConnectionName"></a>
The name of the private connection to use for OAuth token exchange requests only. Cannot be specified when privateConnectionName is provided.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z0-9]([a-z0-9-]*[a-z0-9])?`
Required: No

 ** [kmsKeyArn](#API_RegisterService_RequestSyntax) **   <a name="devopsagent-RegisterService-request-kmsKeyArn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.
Type: String
Length Constraints: Minimum length of 20.
Pattern: `arn:aws[a-zA-Z-]*:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [name](#API_RegisterService_RequestSyntax) **   <a name="devopsagent-RegisterService-request-name"></a>
The display name for the service registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: No

 ** [privateConnectionName](#API_RegisterService_RequestSyntax) **   <a name="devopsagent-RegisterService-request-privateConnectionName"></a>
The name of the private connection to use for VPC connectivity.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z0-9]([a-z0-9-]*[a-z0-9])?`
Required: No

 ** [serviceDetails](#API_RegisterService_RequestSyntax) **   <a name="devopsagent-RegisterService-request-serviceDetails"></a>
Service-specific authorization configuration parameters
Type: [ServiceDetails](API_ServiceDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [tags](#API_RegisterService_RequestSyntax) **   <a name="devopsagent-RegisterService-request-tags"></a>
Tags to add to the Service at registration time.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Required: No

 ** [targetUrlPrivateConnectionName](#API_RegisterService_RequestSyntax) **   <a name="devopsagent-RegisterService-request-targetUrlPrivateConnectionName"></a>
The name of the private connection to use for API calls (target URL) only. Cannot be specified when privateConnectionName is provided.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z0-9]([a-z0-9-]*[a-z0-9])?`
Required: No

## Response Syntax
<a name="API_RegisterService_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "additionalStep": { ... },
   "kmsKeyArn": "string",
   "serviceId": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_RegisterService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [additionalStep](#API_RegisterService_ResponseSyntax) **   <a name="devopsagent-RegisterService-response-additionalStep"></a>
Indicates if additional steps are required to complete service registration (e.g., 3-legged OAuth)
Type: [AdditionalServiceRegistrationStep](API_AdditionalServiceRegistrationStep.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [kmsKeyArn](#API_RegisterService_ResponseSyntax) **   <a name="devopsagent-RegisterService-response-kmsKeyArn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.
Type: String
Length Constraints: Minimum length of 20.
Pattern: `arn:aws[a-zA-Z-]*:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [serviceId](#API_RegisterService_ResponseSyntax) **   <a name="devopsagent-RegisterService-response-serviceId"></a>
Service ID - present when registration is complete, absent when additional steps are required
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_-]+`

 ** [tags](#API_RegisterService_ResponseSyntax) **   <a name="devopsagent-RegisterService-response-tags"></a>
Tags associated with the registered Service.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`

## Errors
<a name="API_RegisterService_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the requested resource is denied due to insufficient permissions.
 ** message **
Detailed error message describing why access was denied.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** message **
Detailed error message describing the conflict.
HTTP Status Code: 409

 ** ContentSizeExceededException **
This exception is thrown when the content size exceeds the allowed limit.
HTTP Status Code: 413

 ** InternalServerException **
This exception is thrown when an unexpected error occurs in the processing of a request.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more parameters provided in the request are invalid.
 ** message **
Detailed error message describing which parameter is invalid and why.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** message **
Detailed error message describing which resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would exceed the service quota limit.
 ** message **
Detailed error message describing which quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled due to too many requests. Please slow down and try again.
 ** message **
Detailed error message describing the throttling condition.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered while validating the input. A member can appear in this list more than once if it failed to satisfy multiple constraints.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_RegisterService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/RegisterService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/RegisterService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RegisterService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/RegisterService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RegisterService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/RegisterService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/RegisterService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/RegisterService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/RegisterService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RegisterService)
