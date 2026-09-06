---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_CreateScope.html
---

# CreateScope
<a name="API_CreateScope"></a>

In Network Flow Monitor, you specify a scope for the service to generate metrics for. By using the scope, Network Flow Monitor can generate a topology of all the resources to measure performance metrics for. When you create a scope, you enable permissions for Network Flow Monitor.

A scope is a Region-account pair or multiple Region-account pairs. Network Flow Monitor uses your scope to determine all the resources (the topology) where Network Flow Monitor will gather network flow performance metrics for you. To provide performance metrics, Network Flow Monitor uses the data that is sent by the Network Flow Monitor agents you install on the resources.

To define the Region-account pairs for your scope, the Network Flow Monitor API uses the following constucts, which allow for future flexibility in defining scopes:
+  *Targets*, which are arrays of targetResources.
+  *Target resources*, which are Region-targetIdentifier pairs.
+  *Target identifiers*, made up of a targetID (currently always an account ID) and a targetType (currently always an account).

## Request Syntax
<a name="API_CreateScope_RequestSyntax"></a>

```
POST /scopes HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "targets": [
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
<a name="API_CreateScope_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateScope_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateScope_RequestSyntax) **   <a name="networkflowmonitor-CreateScope-request-clientToken"></a>
A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Don't reuse the same client token for other API requests.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [tags](#API_CreateScope_RequestSyntax) **   <a name="networkflowmonitor-CreateScope-request-tags"></a>
The tags for a scope. You can add a maximum of 200 tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [targets](#API_CreateScope_RequestSyntax) **   <a name="networkflowmonitor-CreateScope-request-targets"></a>
The targets to define the scope to be monitored. A target is an array of targetResources, which are currently Region-account pairs, defined by targetResource constructs.
Type: Array of [TargetResource](API_TargetResource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_CreateScope_ResponseSyntax"></a>

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
<a name="API_CreateScope_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [scopeArn](#API_CreateScope_ResponseSyntax) **   <a name="networkflowmonitor-CreateScope-response-scopeArn"></a>
The Amazon Resource Name (ARN) of the scope.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`

 ** [scopeId](#API_CreateScope_ResponseSyntax) **   <a name="networkflowmonitor-CreateScope-response-scopeId"></a>
The identifier for the scope that includes the resources you want to get metrics for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.
Type: String

 ** [status](#API_CreateScope_ResponseSyntax) **   <a name="networkflowmonitor-CreateScope-response-status"></a>
The status for a scope. The status can be one of the following: `SUCCEEDED`, `IN_PROGRESS`, `FAILED`, `DEACTIVATING`, or `DEACTIVATED`.
A status of `DEACTIVATING` means that you've requested a scope to be deactivated and Network Flow Monitor is in the process of deactivating the scope. A status of `DEACTIVATED` means that the deactivating process is complete.
Type: String
Valid Values: `SUCCEEDED | IN_PROGRESS | FAILED | DEACTIVATING | DEACTIVATED`

 ** [tags](#API_CreateScope_ResponseSyntax) **   <a name="networkflowmonitor-CreateScope-response-tags"></a>
The tags for a scope.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateScope_Errors"></a>

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
<a name="API_CreateScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/CreateScope)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/CreateScope)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/CreateScope)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/CreateScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/CreateScope)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/CreateScope)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/CreateScope)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/CreateScope)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/CreateScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/CreateScope)
