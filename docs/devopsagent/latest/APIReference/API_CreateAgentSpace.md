---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_CreateAgentSpace.html
---

# CreateAgentSpace
<a name="API_CreateAgentSpace"></a>

Creates a new AgentSpace with the specified name and description. Duplicate space names are allowed.

## Request Syntax
<a name="API_CreateAgentSpace_RequestSyntax"></a>

```
POST /v1/agentspaces HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "kmsKeyArn": "{{string}}",
   "locale": "{{string}}",
   "name": "{{string}}",
   "preferences": {
      "{{string}}" : {{boolean}}
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAgentSpace_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAgentSpace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateAgentSpace_RequestSyntax) **   <a name="devopsagent-CreateAgentSpace-request-clientToken"></a>
Client-provided token to ensure request idempotency. When the same token is provided in subsequent calls, the same response is returned within a 8-hour window.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [description](#API_CreateAgentSpace_RequestSyntax) **   <a name="devopsagent-CreateAgentSpace-request-description"></a>
The description of the AgentSpace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: No

 ** [kmsKeyArn](#API_CreateAgentSpace_RequestSyntax) **   <a name="devopsagent-CreateAgentSpace-request-kmsKeyArn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.
Type: String
Length Constraints: Minimum length of 20.
Pattern: `arn:aws[a-zA-Z-]*:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [locale](#API_CreateAgentSpace_RequestSyntax) **   <a name="devopsagent-CreateAgentSpace-request-locale"></a>
The locale for the AgentSpace, which determines the language used in agent responses.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Pattern: `[a-zA-Z]{2,3}(-[a-zA-Z0-9]{2,8})*`
Required: No

 ** [name](#API_CreateAgentSpace_RequestSyntax) **   <a name="devopsagent-CreateAgentSpace-request-name"></a>
The name of the AgentSpace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}\p{S}\p{Z}]+`
Required: Yes

 ** [preferences](#API_CreateAgentSpace_RequestSyntax) **   <a name="devopsagent-CreateAgentSpace-request-preferences"></a>
The preferences to configure on the agent space. Preferences not provided take their default values.
Type: String to boolean map
Map Entries: Minimum number of 0 items. Maximum number of 25 items.
Valid Keys: `elevatedActionsEnabled`
Required: No

 ** [tags](#API_CreateAgentSpace_RequestSyntax) **   <a name="devopsagent-CreateAgentSpace-request-tags"></a>
Tags to add to the AgentSpace at creation time.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Required: No

## Response Syntax
<a name="API_CreateAgentSpace_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "agentSpace": {
      "agentSpaceId": "string",
      "createdAt": "string",
      "description": "string",
      "kmsKeyArn": "string",
      "locale": "string",
      "name": "string",
      "preferences": {
         "string" : boolean
      },
      "updatedAt": "string"
   },
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateAgentSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [agentSpace](#API_CreateAgentSpace_ResponseSyntax) **   <a name="devopsagent-CreateAgentSpace-response-agentSpace"></a>
Represents a complete AgentSpace with all its properties, timestamps, encryption settings, and unique identifier.
Type: [AgentSpace](API_AgentSpace.md) object

 ** [tags](#API_CreateAgentSpace_ResponseSyntax) **   <a name="devopsagent-CreateAgentSpace-response-tags"></a>
Tags associated with the created AgentSpace.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`

## Errors
<a name="API_CreateAgentSpace_Errors"></a>

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
<a name="API_CreateAgentSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/CreateAgentSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/CreateAgentSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/CreateAgentSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/CreateAgentSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/CreateAgentSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/CreateAgentSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/CreateAgentSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/CreateAgentSpace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/CreateAgentSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/CreateAgentSpace)
