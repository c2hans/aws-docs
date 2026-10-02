---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateAgentContext.html
---

# CreateAgentContext
<a name="API_CreateAgentContext"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Creates a context associated with an optimization profile. Contexts provide application and environment information used during recommendation generation.

## Request Syntax
<a name="API_CreateAgentContext_RequestSyntax"></a>

```
POST /api/v1/agent-profiles/{{profileArn}}/contexts HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "content": {
      "accountIds": [ "{{string}}" ],
      "additionalContext": "{{string}}",
      "applicationOverview": "{{string}}",
      "applicationType": "{{string}}",
      "architectureOverview": "{{string}}",
      "awsServices": [ "{{string}}" ],
      "criticality": "{{string}}",
      "industry": "{{string}}",
      "organizationalUnitIds": [ "{{string}}" ],
      "regions": [ "{{string}}" ],
      "resourceTags": [
         {
            "key": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "resourceTypes": [ "{{string}}" ]
   },
   "contextType": "{{string}}",
   "title": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAgentContext_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileArn](#API_CreateAgentContext_RequestSyntax) **   <a name="wellarchitected-CreateAgentContext-request-uri-profileArn"></a>
The Amazon Resource Name (ARN) of the profile to associate the context with.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_CreateAgentContext_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateAgentContext_RequestSyntax) **   <a name="wellarchitected-CreateAgentContext-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [content](#API_CreateAgentContext_RequestSyntax) **   <a name="wellarchitected-CreateAgentContext-request-content"></a>
The typed content of the context. The structure contains application-specific fields such as account IDs, Regions, services, and resource types.
Type: [ContextContent](API_ContextContent.md) object
Required: Yes

 ** [contextType](#API_CreateAgentContext_RequestSyntax) **   <a name="wellarchitected-CreateAgentContext-request-contextType"></a>
The type of the context.
Type: String
Valid Values: `APPLICATION`
Required: Yes

 ** [title](#API_CreateAgentContext_RequestSyntax) **   <a name="wellarchitected-CreateAgentContext-request-title"></a>
The title of the context.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`
Required: Yes

## Response Syntax
<a name="API_CreateAgentContext_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "context": {
      "applicationType": "string",
      "content": {
         "accountIds": [ "string" ],
         "additionalContext": "string",
         "applicationOverview": "string",
         "applicationType": "string",
         "architectureOverview": "string",
         "awsServices": [ "string" ],
         "criticality": "string",
         "industry": "string",
         "organizationalUnitIds": [ "string" ],
         "regions": [ "string" ],
         "resourceTags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "resourceTypes": [ "string" ]
      },
      "contextType": "string",
      "createdAt": "string",
      "createdBy": "string",
      "criticality": "string",
      "id": "string",
      "lastModifiedAt": "string",
      "lastModifiedBy": "string",
      "profileArn": "string",
      "title": "string"
   }
}
```

## Response Elements
<a name="API_CreateAgentContext_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [context](#API_CreateAgentContext_ResponseSyntax) **   <a name="wellarchitected-CreateAgentContext-response-context"></a>
The created context summary.
Type: [ContextSummary](API_ContextSummary.md) object

## Errors
<a name="API_CreateAgentContext_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The user has reached their resource quota.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateAgentContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/CreateAgentContext)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/CreateAgentContext)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/CreateAgentContext)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/CreateAgentContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/CreateAgentContext)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/CreateAgentContext)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/CreateAgentContext)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/CreateAgentContext)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/CreateAgentContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/CreateAgentContext)
