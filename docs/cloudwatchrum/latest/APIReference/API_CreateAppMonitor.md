---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_CreateAppMonitor.html
---

# CreateAppMonitor
<a name="API_CreateAppMonitor"></a>

Creates a Amazon CloudWatch RUM app monitor, which collects telemetry data from your application and sends that data to RUM. The data includes performance and reliability information such as page load time, client-side errors, and user behavior.

You use this operation only to create a new app monitor. To update an existing app monitor, use [UpdateAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UpdateAppMonitor.html) instead.

After you create an app monitor, sign in to the CloudWatch RUM console to get the JavaScript code snippet to add to your web application. For more information, see [How do I find a code snippet that I've already generated?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-find-code-snippet.html)

## Request Syntax
<a name="API_CreateAppMonitor_RequestSyntax"></a>

```
POST /appmonitor HTTP/1.1
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
   "DomainList": [ "{{string}}" ],
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAppMonitor_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAppMonitor_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AppMonitorConfiguration](#API_CreateAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-CreateAppMonitor-request-AppMonitorConfiguration"></a>
A structure that contains much of the configuration data for the app monitor. If you are using Amazon Cognito for authorization, you must include this structure in your request, and it must include the ID of the Amazon Cognito identity pool to use for authorization. If you don't include `AppMonitorConfiguration`, you must set up your own authorization method. For more information, see [Authorize your application to send data to AWS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-authorization.html).
If you omit this argument, the sample rate used for RUM is set to 10% of the user sessions.
Type: [AppMonitorConfiguration](API_AppMonitorConfiguration.md) object
Required: No

 ** [CustomEvents](#API_CreateAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-CreateAppMonitor-request-CustomEvents"></a>
Specifies whether this app monitor allows the web client to define and send custom events. If you omit this parameter, custom events are `DISABLED`.
For more information about custom events, see [Send custom events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-custom-events.html).
Type: [CustomEvents](API_CustomEvents.md) object
Required: No

 ** [CwLogEnabled](#API_CreateAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-CreateAppMonitor-request-CwLogEnabled"></a>
Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges.
If you omit this parameter, the default is `false`.
Type: Boolean
Required: No

 ** [DeobfuscationConfiguration](#API_CreateAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-CreateAppMonitor-request-DeobfuscationConfiguration"></a>
 A structure that contains the configuration for how an app monitor can deobfuscate stack traces.
Type: [DeobfuscationConfiguration](API_DeobfuscationConfiguration.md) object
Required: No

 ** [Domain](#API_CreateAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-CreateAppMonitor-request-Domain"></a>
The top-level internet domain name for which your application has administrative authority.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(localhost)$|^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|(?=^[a-zA-Z0-9\.\*-]{4,253}$)(?!.*\.-)(?!.*-\.)(?!.*\.\.)(?!.*[^\.]{64,})^(\*\.)?(?![-\.\*])[^\*]{1,}\.(\*|(?!.*--)(?=.*[a-zA-Z])[^\*]{1,}[^\*-])`
Required: No

 ** [DomainList](#API_CreateAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-CreateAppMonitor-request-DomainList"></a>
 List the domain names for which your application has administrative authority. The `CreateAppMonitor` requires either the domain or the domain list.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(localhost)$|^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|(?=^[a-zA-Z0-9\.\*-]{4,253}$)(?!.*\.-)(?!.*-\.)(?!.*\.\.)(?!.*[^\.]{64,})^(\*\.)?(?![-\.\*])[^\*]{1,}\.(\*|(?!.*--)(?=.*[a-zA-Z])[^\*]{1,}[^\*-])`
Required: No

 ** [Name](#API_CreateAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-CreateAppMonitor-request-Name"></a>
A name for the app monitor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!\.)[\.\-_#A-Za-z0-9]+`
Required: Yes

 ** [Tags](#API_CreateAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-CreateAppMonitor-request-Tags"></a>
Assigns one or more tags (key-value pairs) to the app monitor.
Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.
Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.
You can associate as many as 50 tags with an app monitor.
For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateAppMonitor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Id": "string"
}
```

## Response Elements
<a name="API_CreateAppMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Id](#API_CreateAppMonitor_ResponseSyntax) **   <a name="cloudwatchrum-CreateAppMonitor-response-Id"></a>
The unique ID of the new app monitor.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`

## Errors
<a name="API_CreateAppMonitor_Errors"></a>

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

 ** ServiceQuotaExceededException **
This request exceeds a service quota.
HTTP Status Code: 402

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

## Examples
<a name="API_CreateAppMonitor_Examples"></a>

### Example
<a name="API_CreateAppMonitor_Example_1"></a>

The following example creates an app monitor.

#### Sample Request
<a name="API_CreateAppMonitor_Example_1_Request"></a>

```
{
    "AppMonitorConfiguration": {
        "AllowCookies": true,
        "EnableXRay": true,
        "ExcludedPages": [
            "https://www.example.com/pageB"
        ],
        "GuestRoleArn": "arn:aws:iam::123456789012:role/RUM-EXAMPLE-us-west-2-[account]-0000000000000-Unauth",
        "IdentityPoolId": "us-west-2: EXAMPLE-4811-4e5a-8a94-EXAMPLEec1",
        "SessionSampleRate": 0.1,
        "Telemetries": [
            "performance"
        ]
    },
    "CwLogEnabled": true,
    "Domain": "example.com",
    "Name": "appMonitor",
    "Tags": {
        "KeyName": "tagValue"
     }
}
```

#### Sample Response
<a name="API_CreateAppMonitor_Example_1_Response"></a>

```
{
    "Id": “a0abf0c2-a736-4819-8371-4d90108265df”
}
```

## See Also
<a name="API_CreateAppMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rum-2018-05-10/CreateAppMonitor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rum-2018-05-10/CreateAppMonitor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/CreateAppMonitor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rum-2018-05-10/CreateAppMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/CreateAppMonitor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rum-2018-05-10/CreateAppMonitor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rum-2018-05-10/CreateAppMonitor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rum-2018-05-10/CreateAppMonitor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rum-2018-05-10/CreateAppMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/CreateAppMonitor)
