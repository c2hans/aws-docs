---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_CreateMonitor.html
---

# CreateMonitor
<a name="API_CreateMonitor"></a>

Create a monitor for specific network flows between local and remote resources, so that you can monitor network performance for one or several of your workloads. For each monitor, Network Flow Monitor publishes detailed end-to-end performance metrics and a network health indicator (NHI) that informs you whether there were AWS network issues for one or more of the network flows tracked by a monitor, during a time period that you choose.

## Request Syntax
<a name="API_CreateMonitor_RequestSyntax"></a>

```
POST /monitors HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "localResources": [
      {
         "identifier": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "monitorName": "{{string}}",
   "remoteResources": [
      {
         "identifier": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "scopeArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateMonitor_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMonitor_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateMonitor_RequestSyntax) **   <a name="networkflowmonitor-CreateMonitor-request-clientToken"></a>
A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Don't reuse the same client token for other API requests.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [localResources](#API_CreateMonitor_RequestSyntax) **   <a name="networkflowmonitor-CreateMonitor-request-localResources"></a>
The local resources to monitor. A local resource in a workload is the location of the host, or hosts, where the Network Flow Monitor agent is installed. For example, if a workload consists of an interaction between a web service and a backend database (for example, Amazon Dynamo DB), the subnet with the EC2 instance that hosts the web service, which also runs the agent, is the local resource.
Be aware that all local resources must belong to the current Region.
Type: Array of [MonitorLocalResource](API_MonitorLocalResource.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [monitorName](#API_CreateMonitor_RequestSyntax) **   <a name="networkflowmonitor-CreateMonitor-request-monitorName"></a>
The name of the monitor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [remoteResources](#API_CreateMonitor_RequestSyntax) **   <a name="networkflowmonitor-CreateMonitor-request-remoteResources"></a>
The remote resources to monitor. A remote resource is the other endpoint in the bi-directional flow of a workload, with a local resource. For example, Amazon Dynamo DB can be a remote resource.
When you specify remote resources, be aware that specific combinations of resources are allowed and others are not, including the following constraints:
+ All remote resources that you specify must all belong to a single Region.
+ If you specify AWS services as remote resources, any other remote resources that you specify must be in the current Region.
+ When you specify a remote resource for another Region, you can only specify the `Region` resource type. You cannot specify a subnet, VPC, or Availability Zone in another Region.
+ If you leave the `RemoteResources` parameter empty, the monitor will include all network flows that terminate in the current Region.
Type: Array of [MonitorRemoteResource](API_MonitorRemoteResource.md) objects
Required: No

 ** [scopeArn](#API_CreateMonitor_RequestSyntax) **   <a name="networkflowmonitor-CreateMonitor-request-scopeArn"></a>
The Amazon Resource Name (ARN) of the scope for the monitor.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** [tags](#API_CreateMonitor_RequestSyntax) **   <a name="networkflowmonitor-CreateMonitor-request-tags"></a>
The tags for a monitor. You can add a maximum of 200 tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateMonitor_ResponseSyntax"></a>

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
<a name="API_CreateMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-CreateMonitor-response-createdAt"></a>
The date and time when the monitor was created.
Type: Timestamp

 ** [localResources](#API_CreateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-CreateMonitor-response-localResources"></a>
The local resources to monitor. A local resource in a workload is the location of hosts where the Network Flow Monitor agent is installed.
Type: Array of [MonitorLocalResource](API_MonitorLocalResource.md) objects

 ** [modifiedAt](#API_CreateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-CreateMonitor-response-modifiedAt"></a>
The last date and time that the monitor was modified.
Type: Timestamp

 ** [monitorArn](#API_CreateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-CreateMonitor-response-monitorArn"></a>
The Amazon Resource Name (ARN) of the monitor.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 512.
Pattern: `arn:.*`

 ** [monitorName](#API_CreateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-CreateMonitor-response-monitorName"></a>
The name of the monitor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [monitorStatus](#API_CreateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-CreateMonitor-response-monitorStatus"></a>
The status of a monitor. The status can be one of the following
+  `PENDING`: The monitor is in the process of being created.
+  `ACTIVE`: The monitor is active.
+  `INACTIVE`: The monitor is inactive.
+  `ERROR`: Monitor creation failed due to an error.
+  `DELETING`: The monitor is in the process of being deleted.
Type: String
Valid Values: `PENDING | ACTIVE | INACTIVE | ERROR | DELETING`

 ** [remoteResources](#API_CreateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-CreateMonitor-response-remoteResources"></a>
The remote resources to monitor. A remote resource is the other endpoint specified for the network flow of a workload, with a local resource. For example, Amazon Dynamo DB can be a remote resource.
Type: Array of [MonitorRemoteResource](API_MonitorRemoteResource.md) objects

 ** [tags](#API_CreateMonitor_ResponseSyntax) **   <a name="networkflowmonitor-CreateMonitor-response-tags"></a>
The tags for a monitor.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateMonitor_Errors"></a>

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
<a name="API_CreateMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/CreateMonitor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/CreateMonitor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/CreateMonitor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/CreateMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/CreateMonitor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/CreateMonitor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/CreateMonitor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/CreateMonitor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/CreateMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/CreateMonitor)
