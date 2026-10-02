---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentContext.html
---

# UpdateAgentContext
<a name="API_UpdateAgentContext"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

Updates an existing context associated with a profile.

## Request Syntax
<a name="API_UpdateAgentContext_RequestSyntax"></a>

```
PUT /api/v1/agent-profiles/{{profileArn}}/contexts/{{id}} HTTP/1.1
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
   "title": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAgentContext_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateAgentContext_RequestSyntax) **   <a name="wellarchitected-UpdateAgentContext-request-uri-id"></a>
The unique identifier of the context to update.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [profileArn](#API_UpdateAgentContext_RequestSyntax) **   <a name="wellarchitected-UpdateAgentContext-request-uri-profileArn"></a>
The Amazon Resource Name (ARN) of the profile containing the context.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:\d{12}:agent-profile/([a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_UpdateAgentContext_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateAgentContext_RequestSyntax) **   <a name="wellarchitected-UpdateAgentContext-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [content](#API_UpdateAgentContext_RequestSyntax) **   <a name="wellarchitected-UpdateAgentContext-request-content"></a>
The updated typed content of the context. The structure contains application-specific fields such as account IDs, Regions, services, and resource types.
Type: [ContextContent](API_ContextContent.md) object
Required: No

 ** [title](#API_UpdateAgentContext_RequestSyntax) **   <a name="wellarchitected-UpdateAgentContext-request-title"></a>
The updated title of the context.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+`
Required: No

## Response Syntax
<a name="API_UpdateAgentContext_ResponseSyntax"></a>

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
<a name="API_UpdateAgentContext_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [context](#API_UpdateAgentContext_ResponseSyntax) **   <a name="wellarchitected-UpdateAgentContext-response-context"></a>
The updated context summary.
Type: [ContextSummary](API_ContextSummary.md) object

## Errors
<a name="API_UpdateAgentContext_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

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
<a name="API_UpdateAgentContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/UpdateAgentContext)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/UpdateAgentContext)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/UpdateAgentContext)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/UpdateAgentContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/UpdateAgentContext)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/UpdateAgentContext)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/UpdateAgentContext)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/UpdateAgentContext)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/UpdateAgentContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/UpdateAgentContext)
