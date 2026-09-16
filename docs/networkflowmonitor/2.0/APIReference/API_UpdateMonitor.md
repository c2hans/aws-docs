---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_UpdateMonitor.html
---

# UpdateMonitor
<a name="API_UpdateMonitor"></a>

Update a monitor to add or remove local or remote resources.

## Request Syntax
<a name="API_UpdateMonitor_RequestSyntax"></a>

```
PATCH /monitors/{{monitorName}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "localResourcesToAdd": [
      {
         "identifier": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "localResourcesToRemove": [
      {
         "identifier": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "remoteResourcesToAdd": [
      {
         "identifier": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "remoteResourcesToRemove": [
      {
         "identifier": "{{string}}",
         "type": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateMonitor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [monitorName](#API_UpdateMonitor_RequestSyntax) **   <a name="networkflowmonitor-UpdateMonitor-request-uri-monitorName"></a>
The name of the monitor.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Request Body
<a name="API_UpdateMonitor_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateMonitor_RequestSyntax) **   <a name="networkflowmonitor-UpdateMonitor-request-clientToken"></a>
A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Don't reuse the same client token for other API requests.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [localResourcesToAdd](#API_UpdateMonitor_RequestSyntax) **   <a name="networkflowmonitor-UpdateMonitor-request-localResourcesToAdd"></a>
Additional local resources to specify network flows for a monitor, as an array of resources with identifiers and types. A local resource in a workload is the location of hosts where the Network Flow Monitor agent is installed.
Type: Array of [MonitorLocalResource](API_MonitorLocalResource.md) objects
Required: No

 ** [localResourcesToRemove](#API_UpdateMonitor_RequestSyntax) **   <a name="networkflowmonitor-UpdateMonitor-request-localResourcesToRemove"></a>
The local resources to remove, as an array of resources with identifiers and types.
Type: Array of [MonitorLocalResource](API_MonitorLocalResource.md) objects
Required: No

 ** [remoteResourcesToAdd](#API_UpdateMonitor_RequestSyntax) **   <a name="networkflowmonitor-UpdateMonitor-request-remoteResourcesToAdd"></a>
The remote resources to add, as an array of resources with identifiers and types.
A remote resource is the other endpoint in the flow of a workload, with a local resource. For example, Amazon Dynamo DB can be a remote resource.
Type: Array of [MonitorRemoteResource](API_MonitorRemoteResource.md) objects
Required: No

 ** [remoteResourcesToRemove](#API_UpdateMonitor_RequestSyntax) **   <a name="networkflowmonitor-UpdateMonitor-request-remoteResourcesToRemove"></a>
The remote resources to remove, as an array of resources with identifiers and types.
A remote resource is the other endpoint specified for the network flow of a workload, with a local resource. For example, Amazon Dynamo DB can be a remote resource.
Type: Array of [MonitorRemoteResource](API_MonitorRemoteResource.md) objects
Required: No

## Response Syntax
<a name="API_UpdateMonitor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "localResources": [
      {
         "identifier": "string",
         "type": "string"
      }
   ],
   "modifiedAt": number,
   "monitorArn": "string",
   "monitorName": "string",
   "monitorStatus": "string",
   "remoteResources": [
      {
         "identifier": "string",
         "type": "string"
      }
   ],
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_UpdateMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_UpdateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-UpdateMonitor-response-createdAt"></a>
The date and time when the monitor was created.
Type: Timestamp

 ** [localResources](#API_UpdateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-UpdateMonitor-response-localResources"></a>
The local resources to monitor. A local resource in a workload is the location of hosts where the Network Flow Monitor agent is installed.
Type: Array of [MonitorLocalResource](API_MonitorLocalResource.md) objects

 ** [modifiedAt](#API_UpdateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-UpdateMonitor-response-modifiedAt"></a>
The last date and time that the monitor was modified.
Type: Timestamp

 ** [monitorArn](#API_UpdateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-UpdateMonitor-response-monitorArn"></a>
The Amazon Resource Name (ARN) of the monitor.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 512.
Pattern: `arn:.*`

 ** [monitorName](#API_UpdateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-UpdateMonitor-response-monitorName"></a>
The name of the monitor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [monitorStatus](#API_UpdateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-UpdateMonitor-response-monitorStatus"></a>
The status of a monitor. The status can be one of the following
+  `PENDING`: The monitor is in the process of being created.
+  `ACTIVE`: The monitor is active.
+  `INACTIVE`: The monitor is inactive.
+  `ERROR`: Monitor creation failed due to an error.
+  `DELETING`: The monitor is in the process of being deleted.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR | DELETING`

 ** [remoteResources](#API_UpdateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-UpdateMonitor-response-remoteResources"></a>
The remote resources updated for a monitor, as an array of resources with identifiers and types.
A remote resource is the other endpoint specified for the network flow of a workload, with a local resource. For example, Amazon Dynamo DB can be a remote resource.
Type: Array of [MonitorRemoteResource](API_MonitorRemoteResource.md) objects

 ** [tags](#API_UpdateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-UpdateMonitor-response-tags"></a>
The tags for a monitor.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_UpdateMonitor_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
Invalid request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/UpdateMonitor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/UpdateMonitor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/UpdateMonitor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/UpdateMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/UpdateMonitor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/UpdateMonitor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/UpdateMonitor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/UpdateMonitor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/UpdateMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/UpdateMonitor)
