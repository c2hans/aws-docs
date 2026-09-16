---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UpdateAppMonitor.html
---

# UpdateAppMonitor
<a name="API_UpdateAppMonitor"></a>

Updates the configuration of an existing app monitor. When you use this operation, only the parts of the app monitor configuration that you specify in this operation are changed. For any parameters that you omit, the existing values are kept.

You can't use this operation to change the tags of an existing app monitor. To change the tags of an existing app monitor, use [TagResource](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_TagResource.html).

To create a new app monitor, use [CreateAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_CreateAppMonitor.html).

After you update an app monitor, sign in to the CloudWatch RUM console to get the updated JavaScript code snippet to add to your web application. For more information, see [How do I find a code snippet that I've already generated?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-find-code-snippet.html)

## Request Syntax
<a name="API_UpdateAppMonitor_RequestSyntax"></a>

```
PATCH /appmonitor/{{Name}} HTTP/1.1
Content-type: application/json

{
   "AppMonitorConfiguration": {
      "AllowCookies": {{boolean}},
      "EnableXRay": {{boolean}},
      "ExcludedPages": [ "{{string}}" ],
      "FavoritePages": [ "{{string}}" ],
      "GuestRoleArn": "{{string}}",
      "IdentityPoolId": "{{string}}",
      "IncludedPages": [ "{{string}}" ],
      "SessionSampleRate": {{number}},
      "Telemetries": [ "{{string}}" ]
   },
   "CustomEvents": {
      "Status": "{{string}}"
   },
   "CwLogEnabled": {{boolean}},
   "DeobfuscationConfiguration": {
      "JavaScriptSourceMaps": {
         "S3Uri": "{{string}}",
         "Status": "{{string}}"
      }
   },
   "Domain": "{{string}}",
   "DomainList": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateAppMonitor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_UpdateAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-UpdateAppMonitor-request-uri-Name"></a>
The name of the app monitor to update.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!\.)[\.\-_#A-Za-z0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateAppMonitor_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AppMonitorConfiguration](#API_UpdateAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-UpdateAppMonitor-request-AppMonitorConfiguration"></a>
A structure that contains much of the configuration data for the app monitor. If you are using Amazon Cognito for authorization, you must include this structure in your request, and it must include the ID of the Amazon Cognito identity pool to use for authorization. If you don't include `AppMonitorConfiguration`, you must set up your own authorization method. For more information, see [Authorize your application to send data to AWS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-authorization.html).
Type: [AppMonitorConfiguration](API_AppMonitorConfiguration.md) object
Required: No

 ** [CustomEvents](#API_UpdateAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-UpdateAppMonitor-request-CustomEvents"></a>
Specifies whether this app monitor allows the web client to define and send custom events. The default is for custom events to be `DISABLED`.
For more information about custom events, see [Send custom events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-custom-events.html).
Type: [CustomEvents](API_CustomEvents.md) object
Required: No

 ** [CwLogEnabled](#API_UpdateAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-UpdateAppMonitor-request-CwLogEnabled"></a>
Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges.
Type: Boolean
Required: No

 ** [DeobfuscationConfiguration](#API_UpdateAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-UpdateAppMonitor-request-DeobfuscationConfiguration"></a>
 A structure that contains the configuration for how an app monitor can deobfuscate stack traces.
Type: [DeobfuscationConfiguration](API_DeobfuscationConfiguration.md) object
Required: No

 ** [Domain](#API_UpdateAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-UpdateAppMonitor-request-Domain"></a>
The top-level internet domain name for which your application has administrative authority.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(localhost)$|^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|(?=^[a-zA-Z0-9\.\*-]{4,253}$)(?!.*\.-)(?!.*-\.)(?!.*\.\.)(?!.*[^\.]{64,})^(\*\.)?(?![-\.\*])[^\*]{1,}\.(\*|(?!.*--)(?=.*[a-zA-Z])[^\*]{1,}[^\*-])`
Required: No

 ** [DomainList](#API_UpdateAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-UpdateAppMonitor-request-DomainList"></a>
 List the domain names for which your application has administrative authority. The `UpdateAppMonitor` allows either the domain or the domain list.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(localhost)$|^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|(?=^[a-zA-Z0-9\.\*-]{4,253}$)(?!.*\.-)(?!.*-\.)(?!.*\.\.)(?!.*[^\.]{64,})^(\*\.)?(?![-\.\*])[^\*]{1,}\.(\*|(?!.*--)(?=.*[a-zA-Z])[^\*]{1,}[^\*-])`
Required: No

## Response Syntax
<a name="API_UpdateAppMonitor_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateAppMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateAppMonitor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
This operation attempted to create a resource that already exists.
 ** resourceName **
The name of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 409

 ** InternalServerException **
Internal service exception.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource not found.
 ** resourceName **
The name of the resource that is associated with the error.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because of quota limits.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
One of the arguments for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAppMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rum-2018-05-10/UpdateAppMonitor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rum-2018-05-10/UpdateAppMonitor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/UpdateAppMonitor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rum-2018-05-10/UpdateAppMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/UpdateAppMonitor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rum-2018-05-10/UpdateAppMonitor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rum-2018-05-10/UpdateAppMonitor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rum-2018-05-10/UpdateAppMonitor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rum-2018-05-10/UpdateAppMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/UpdateAppMonitor)
