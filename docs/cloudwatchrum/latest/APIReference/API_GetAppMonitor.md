---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetAppMonitor.html
---

# GetAppMonitor
<a name="API_GetAppMonitor"></a>

Retrieves the complete configuration information for one app monitor.

## Request Syntax
<a name="API_GetAppMonitor_RequestSyntax"></a>

```
GET /appmonitor/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAppMonitor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_GetAppMonitor_RequestSyntax) **   <a name="cloudwatchrum-GetAppMonitor-request-uri-Name"></a>
The app monitor to retrieve information for.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!\.)[\.\-_#A-Za-z0-9]+`
Required: Yes

## Request Body
<a name="API_GetAppMonitor_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAppMonitor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AppMonitor": {
      "AppMonitorConfiguration": {
         "AllowCookies": boolean,
         "EnableXRay": boolean,
         "ExcludedPages": [ "string" ],
         "FavoritePages": [ "string" ],
         "GuestRoleArn": "string",
         "IdentityPoolId": "string",
         "IncludedPages": [ "string" ],
         "SessionSampleRate": number,
         "Telemetries": [ "string" ]
      },
      "Created": "string",
      "CustomEvents": {
         "Status": "string"
      },
      "DataStorage": {
         "CwLog": {
            "CwLogEnabled": boolean,
            "CwLogGroup": "string"
         }
      },
      "DeobfuscationConfiguration": {
         "JavaScriptSourceMaps": {
            "S3Uri": "string",
            "Status": "string"
         }
      },
      "Domain": "string",
      "DomainList": [ "string" ],
      "Id": "string",
      "LastModified": "string",
      "Name": "string",
      "State": "string",
      "Tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_GetAppMonitor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppMonitor](#API_GetAppMonitor_ResponseSyntax) **   <a name="cloudwatchrum-GetAppMonitor-response-AppMonitor"></a>
A structure containing all the configuration information for the app monitor.
Type: [AppMonitor](API_AppMonitor.md) object

## Errors
<a name="API_GetAppMonitor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

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
<a name="API_GetAppMonitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rum-2018-05-10/GetAppMonitor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rum-2018-05-10/GetAppMonitor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/GetAppMonitor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rum-2018-05-10/GetAppMonitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/GetAppMonitor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rum-2018-05-10/GetAppMonitor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rum-2018-05-10/GetAppMonitor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rum-2018-05-10/GetAppMonitor)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rum-2018-05-10/GetAppMonitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/GetAppMonitor)
