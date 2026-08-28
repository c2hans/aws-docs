---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_UpdateScope.html
---

# UpdateScope
<a name="API_UpdateScope"></a>

Update a scope to add or remove resources that you want to be available for Network Flow Monitor to generate metrics for, when you have active agents on those resources sending metrics reports to the Network Flow Monitor backend.

## Request Syntax
<a name="API_UpdateScope_RequestSyntax"></a>

```
PATCH /scopes/{{scopeId}} HTTP/1.1
Content-type: application/json

{
   "resourcesToAdd": [
      {
         "region": "{{string}}",
         "targetIdentifier": {
            "targetId": { ... },
            "targetType": "{{string}}"
         }
      }
   ],
   "resourcesToDelete": [
      {
         "region": "{{string}}",
         "targetIdentifier": {
            "targetId": { ... },
            "targetType": "{{string}}"
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateScope_RequestParameters"></a>

The request uses the following URI parameters.

 ** [scopeId](#API_UpdateScope_RequestSyntax) **   <a name="networkflowmonitor-UpdateScope-request-uri-scopeId"></a>
The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.
Required: Yes

## Request Body
<a name="API_UpdateScope_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourcesToAdd](#API_UpdateScope_RequestSyntax) **   <a name="networkflowmonitor-UpdateScope-request-resourcesToAdd"></a>
A list of resources to add to a scope.
Type: Array of [TargetResource](API_TargetResource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 99 items.
Required: No

 ** [resourcesToDelete](#API_UpdateScope_RequestSyntax) **   <a name="networkflowmonitor-UpdateScope-request-resourcesToDelete"></a>
A list of resources to delete from a scope.
Type: Array of [TargetResource](API_TargetResource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 99 items.
Required: No

## Response Syntax
<a name="API_UpdateScope_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "scopeArn": "string",
   "scopeId": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_UpdateScope_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [scopeArn](#API_UpdateScope_ResponseSyntax) **   <a name="networkflowmonitor-UpdateScope-response-scopeArn"></a>
The Amazon Resource Name (ARN) of the scope.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`

 ** [scopeId](#API_UpdateScope_ResponseSyntax) **   <a name="networkflowmonitor-UpdateScope-response-scopeId"></a>
The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.
Type: String

 ** [status](#API_UpdateScope_ResponseSyntax) **   <a name="networkflowmonitor-UpdateScope-response-status"></a>
The status for a scope. The status can be one of the following: `SUCCEEDED`, `IN_PROGRESS`, `FAILED`, `DEACTIVATING`, or `DEACTIVATED`.
A status of `DEACTIVATING` means that you've requested a scope to be deactivated and Network Flow Monitor is in the process of deactivating the scope. A status of `DEACTIVATED` means that the deactivating process is complete.
Type: String
Valid Values: `SUCCEEDED | IN_PROGRESS | FAILED | DEACTIVATING | DEACTIVATED`

 ** [tags](#API_UpdateScope_ResponseSyntax) **   <a name="networkflowmonitor-UpdateScope-response-tags"></a>
The tags for a scope.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_UpdateScope_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The requested resource is in use.
HTTP Status Code: 409

 ** InternalServerException **
An internal error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request specifies a resource that doesn't exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeded a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
Invalid request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/UpdateScope)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/UpdateScope)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/UpdateScope)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/UpdateScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/UpdateScope)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/UpdateScope)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/UpdateScope)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/UpdateScope)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/UpdateScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/UpdateScope)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Network Flow Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkflowmonitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
