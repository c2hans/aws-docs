---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetScope.html
---

# GetScope
<a name="API_GetScope"></a>

Gets information about a scope, including the name, status, tags, and target details. The scope in Network Flow Monitor is an account.

## Request Syntax
<a name="API_GetScope_RequestSyntax"></a>

```
GET /scopes/{{scopeId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetScope_RequestParameters"></a>

The request uses the following URI parameters.

 ** [scopeId](#API_GetScope_RequestSyntax) **   <a name="networkflowmonitor-GetScope-request-uri-scopeId"></a>
The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account. A scope ID is returned from a `CreateScope` API call.
Length Constraints: Minimum length of 1.
Required: Yes

## Request Body
<a name="API_GetScope_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetScope_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "scopeArn": "string",
   "scopeId": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "targets": [
      {
         "region": "string",
         "targetIdentifier": {
            "targetId": { ... },
            "targetType": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetScope_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [scopeArn](#API_GetScope_ResponseSyntax) **   <a name="networkflowmonitor-GetScope-response-scopeArn"></a>
The Amazon Resource Name (ARN) of the scope.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`

 ** [scopeId](#API_GetScope_ResponseSyntax) **   <a name="networkflowmonitor-GetScope-response-scopeId"></a>
The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account. A scope ID is returned from a `CreateScope` API call.
Type: String

 ** [status](#API_GetScope_ResponseSyntax) **   <a name="networkflowmonitor-GetScope-response-status"></a>
The status for a scope. The status can be one of the following: `SUCCEEDED`, `IN_PROGRESS`, `FAILED`, `DEACTIVATING`, or `DEACTIVATED`.
A status of `DEACTIVATING` means that you've requested a scope to be deactivated and Network Flow Monitor is in the process of deactivating the scope. A status of `DEACTIVATED` means that the deactivating process is complete.
Type: String
Valid Values: `SUCCEEDED | IN_PROGRESS | FAILED | DEACTIVATING | DEACTIVATED`

 ** [tags](#API_GetScope_ResponseSyntax) **   <a name="networkflowmonitor-GetScope-response-tags"></a>
The tags for a scope.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [targets](#API_GetScope_ResponseSyntax) **   <a name="networkflowmonitor-GetScope-response-targets"></a>
The targets to define the scope to be monitored. A target is an array of targetResources, which are currently Region-account pairs, defined by targetResource constructs.
Type: Array of [TargetResource](API_TargetResource.md) objects

## Errors
<a name="API_GetScope_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

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
<a name="API_GetScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/GetScope)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/GetScope)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/GetScope)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/GetScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/GetScope)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/GetScope)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/GetScope)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/GetScope)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/GetScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/GetScope)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Network Flow Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkflowmonitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
