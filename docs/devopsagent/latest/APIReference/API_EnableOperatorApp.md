---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_EnableOperatorApp.html
---

# EnableOperatorApp
<a name="API_EnableOperatorApp"></a>

Enable the Operator App to access the given AgentSpace

## Request Syntax
<a name="API_EnableOperatorApp_RequestSyntax"></a>

```
POST /v1/agentspaces/{{agentSpaceId}}/operator HTTP/1.1
Content-type: application/json

{
   "authFlow": "{{string}}",
   "idcInstanceArn": "{{string}}",
   "idpClientId": "{{string}}",
   "idpClientSecret": "{{string}}",
   "issuerUrl": "{{string}}",
   "operatorAppRoleArn": "{{string}}",
   "provider": "{{string}}"
}
```

## URI Request Parameters
<a name="API_EnableOperatorApp_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentSpaceId](#API_EnableOperatorApp_RequestSyntax) **   <a name="devopsagent-EnableOperatorApp-request-uri-agentSpaceId"></a>
Unique identifier for an agent space (allows alphanumeric characters and hyphens; 1-64 characters)
Pattern: `[a-zA-Z0-9-]{1,64}`
Required: Yes

## Request Body
<a name="API_EnableOperatorApp_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authFlow](#API_EnableOperatorApp_RequestSyntax) **   <a name="devopsagent-EnableOperatorApp-request-authFlow"></a>
The authentication flow configured for the operator App. e.g. iam or idc
Type: String
Valid Values: `iam | idc | idp`
Required: Yes

 ** [idcInstanceArn](#API_EnableOperatorApp_RequestSyntax) **   <a name="devopsagent-EnableOperatorApp-request-idcInstanceArn"></a>
The IdC instance Arn used to create an IdC auth application
Type: String
Required: No

 ** [idpClientId](#API_EnableOperatorApp_RequestSyntax) **   <a name="devopsagent-EnableOperatorApp-request-idpClientId"></a>
The OIDC client ID for the IdP application
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [idpClientSecret](#API_EnableOperatorApp_RequestSyntax) **   <a name="devopsagent-EnableOperatorApp-request-idpClientSecret"></a>
The OIDC client secret for the IdP application
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [issuerUrl](#API_EnableOperatorApp_RequestSyntax) **   <a name="devopsagent-EnableOperatorApp-request-issuerUrl"></a>
The OIDC issuer URL of the external Identity Provider
Type: String
Required: No

 ** [operatorAppRoleArn](#API_EnableOperatorApp_RequestSyntax) **   <a name="devopsagent-EnableOperatorApp-request-operatorAppRoleArn"></a>
The IAM role end users assume to access AIDevOps APIs
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: Yes

 ** [provider](#API_EnableOperatorApp_RequestSyntax) **   <a name="devopsagent-EnableOperatorApp-request-provider"></a>
The Identity Provider name (e.g., Entra, Okta, Google)
Type: String
Required: No

## Response Syntax
<a name="API_EnableOperatorApp_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentSpaceId": "string",
   "iam": {
      "createdAt": "string",
      "operatorAppRoleArn": "string",
      "updatedAt": "string"
   },
   "idc": {
      "createdAt": "string",
      "idcApplicationArn": "string",
      "idcInstanceArn": "string",
      "operatorAppRoleArn": "string",
      "updatedAt": "string"
   },
   "idp": {
      "clientId": "string",
      "createdAt": "string",
      "issuerUrl": "string",
      "operatorAppRoleArn": "string",
      "provider": "string",
      "updatedAt": "string"
   },
   "operatorAppUrl": "string"
}
```

## Response Elements
<a name="API_EnableOperatorApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentSpaceId](#API_EnableOperatorApp_ResponseSyntax) **   <a name="devopsagent-EnableOperatorApp-response-agentSpaceId"></a>
The unique identifier of the AgentSpace
Type: String
Pattern: `[a-zA-Z0-9-]{1,64}`

 ** [iam](#API_EnableOperatorApp_ResponseSyntax) **   <a name="devopsagent-EnableOperatorApp-response-iam"></a>
Configuration for IAM-based authentication flow for the Operator App.
Type: [IamAuthConfiguration](API_IamAuthConfiguration.md) object

 ** [idc](#API_EnableOperatorApp_ResponseSyntax) **   <a name="devopsagent-EnableOperatorApp-response-idc"></a>
Configuration for AWS Identity Center (IdC) authentication flow for the Operator App.
Type: [IdcAuthConfiguration](API_IdcAuthConfiguration.md) object

 ** [idp](#API_EnableOperatorApp_ResponseSyntax) **   <a name="devopsagent-EnableOperatorApp-response-idp"></a>
Configuration for external Identity Provider OIDC authentication flow for the Operator App.
Type: [IdpAuthConfiguration](API_IdpAuthConfiguration.md) object

 ** [operatorAppUrl](#API_EnableOperatorApp_ResponseSyntax) **   <a name="devopsagent-EnableOperatorApp-response-operatorAppUrl"></a>
The URL for operators to access the Operator App
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https://[a-zA-Z0-9.-]+(/.*)?`

## Errors
<a name="API_EnableOperatorApp_Errors"></a>

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

 ** IdentityCenterServiceException **
Calls to the customer Identity Center have failed
 ** message **
Detailed error message describing why the call fails
 ** underlyingErrorCode **
The Idc error code
HTTP Status Code: 400

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
<a name="API_EnableOperatorApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/EnableOperatorApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/EnableOperatorApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/EnableOperatorApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/EnableOperatorApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/EnableOperatorApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/EnableOperatorApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/EnableOperatorApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/EnableOperatorApp)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/EnableOperatorApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/EnableOperatorApp)
