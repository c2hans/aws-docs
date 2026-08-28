---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_AssociateService.html
---

# AssociateService
<a name="API_AssociateService"></a>

Adds a specific service association to an AgentSpace. It overwrites the existing association of the same service. Returns 201 Created on success.

## Request Syntax
<a name="API_AssociateService_RequestSyntax"></a>

```
POST /v1/agentspaces/{{agentSpaceId}}/associations HTTP/1.1
Content-type: application/json

{
   "capabilities": {
      "{{string}}" : {
         "enabled": {{boolean}},
         "triggerFilterGroups": [
            {
               "events": [ "{{string}}" ],
               "targetBranches": {
                  "patterns": [ "{{string}}" ]
               }
            }
         ]
      }
   },
   "configuration": { ... },
   "serviceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateService_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentSpaceId](#API_AssociateService_RequestSyntax) **   <a name="devopsagent-AssociateService-request-uri-agentSpaceId"></a>
Unique identifier for an agent space (allows alphanumeric characters and hyphens; 1-64 characters)
Pattern: `[a-zA-Z0-9-]{1,64}`
Required: Yes

## Request Body
<a name="API_AssociateService_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [capabilities](#API_AssociateService_RequestSyntax) **   <a name="devopsagent-AssociateService-request-capabilities"></a>
Enabled capabilities for this association.
Type: String to [CapabilityConfiguration](API_CapabilityConfiguration.md) object map
Valid Keys: `RELEASE_READINESS_REVIEW | RELEASE_READINESS_REVIEW_AUTOMATED_TESTING`
Required: No

 ** [configuration](#API_AssociateService_RequestSyntax) **   <a name="devopsagent-AssociateService-request-configuration"></a>
The configuration that directs how AgentSpace interacts with the given service.
Type: [ServiceConfiguration](API_ServiceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [serviceId](#API_AssociateService_RequestSyntax) **   <a name="devopsagent-AssociateService-request-serviceId"></a>
The unique identifier of the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Response Syntax
<a name="API_AssociateService_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "association": {
      "agentSpaceId": "string",
      "associationId": "string",
      "capabilities": {
         "string" : {
            "enabled": boolean,
            "triggerFilterGroups": [
               {
                  "events": [ "string" ],
                  "targetBranches": {
                     "patterns": [ "string" ]
                  }
               }
            ]
         }
      },
      "configuration": { ... },
      "createdAt": "string",
      "serviceId": "string",
      "status": "string",
      "updatedAt": "string"
   },
   "webhook": {
      "apiKey": "string",
      "webhookId": "string",
      "webhookSecret": "string",
      "webhookType": "string",
      "webhookUrl": "string"
   }
}
```

## Response Elements
<a name="API_AssociateService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [association](#API_AssociateService_ResponseSyntax) **   <a name="devopsagent-AssociateService-response-association"></a>
Represents a service association within an AgentSpace, defining how the agent interacts with external services.
Type: [Association](API_Association.md) object

 ** [webhook](#API_AssociateService_ResponseSyntax) **   <a name="devopsagent-AssociateService-response-webhook"></a>
Generic webhook configuration
Type: [GenericWebhook](API_GenericWebhook.md) object

## Errors
<a name="API_AssociateService_Errors"></a>

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
<a name="API_AssociateService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/AssociateService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/AssociateService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/AssociateService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/AssociateService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/AssociateService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/AssociateService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/AssociateService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/AssociateService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/AssociateService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/AssociateService)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
