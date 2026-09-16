---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetMonitor.html
---

# GetMonitor
<a name="API_GetMonitor"></a>

Gets information about a monitor in Network Flow Monitor based on a monitor name. The information returned includes the Amazon Resource Name (ARN), create time, modified time, resources included in the monitor, and status information.

## Request Syntax
<a name="API_GetMonitor_RequestSyntax"></a>

```
GET /monitors/{{monitorName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMonitor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [monitorName](#API_GetMonitor_RequestSyntax) **   <a name="networkflowmonitor-GetMonitor-request-uri-monitorName"></a>
The name of the monitor.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Request Body
<a name="API_GetMonitor_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMonitor_ResponseSyntax"></a>

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
<a name="API_GetMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetMonitor_ResponseSyntax) **   <a name="networkflowmonitor-GetMonitor-response-createdAt"></a>
The date and time when the monitor was created.
Type: Timestamp

 ** [localResources](#API_GetMonitor_ResponseSyntax) **   <a name="networkflowmonitor-GetMonitor-response-localResources"></a>
The local resources to monitor. A local resource in a workload is the location of the hosts where the Network Flow Monitor agent is installed.
Type: Array of [MonitorLocalResource](API_MonitorLocalResource.md) objects

 ** [modifiedAt](#API_GetMonitor_ResponseSyntax) **   <a name="networkflowmonitor-GetMonitor-response-modifiedAt"></a>
The date and time when the monitor was last modified.
Type: Timestamp

 ** [monitorArn](#API_GetMonitor_ResponseSyntax) **   <a name="networkflowmonitor-GetMonitor-response-monitorArn"></a>
The Amazon Resource Name (ARN) of the monitor.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 512.
Pattern: `arn:.*`

 ** [monitorName](#API_GetMonitor_ResponseSyntax) **   <a name="networkflowmonitor-GetMonitor-response-monitorName"></a>
The name of the monitor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [monitorStatus](#API_GetMonitor_ResponseSyntax) **   <a name="networkflowmonitor-GetMonitor-response-monitorStatus"></a>
The status of a monitor. The status can be one of the following
+  `PENDING`: The monitor is in the process of being created.
+  `ACTIVE`: The monitor is active.
+  `INACTIVE`: The monitor is inactive.
+  `ERROR`: Monitor creation failed due to an error.
+  `DELETING`: The monitor is in the process of being deleted.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR | DELETING`

 ** [remoteResources](#API_GetMonitor_ResponseSyntax) **   <a name="networkflowmonitor-GetMonitor-response-remoteResources"></a>
The remote resources to monitor. A remote resource is the other endpoint specified for the network flow of a workload, with a local resource. For example, Amazon Dynamo DB can be a remote resource.
Type: Array of [MonitorRemoteResource](API_MonitorRemoteResource.md) objects

 ** [tags](#API_GetMonitor_ResponseSyntax) **   <a name="networkflowmonitor-GetMonitor-response-tags"></a>
The tags for a monitor.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_GetMonitor_Errors"></a>

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
<a name="API_GetMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/GetMonitor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/GetMonitor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/GetMonitor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/GetMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/GetMonitor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/GetMonitor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/GetMonitor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/GetMonitor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/GetMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/GetMonitor)
