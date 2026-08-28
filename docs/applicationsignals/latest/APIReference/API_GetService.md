---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_GetService.html
---

# GetService
<a name="API_GetService"></a>

Returns information about a service discovered by Application Signals.

## Request Syntax
<a name="API_GetService_RequestSyntax"></a>

```
POST /service?EndTime={{EndTime}}&StartTime={{StartTime}} HTTP/1.1
Content-type: application/json

{
   "KeyAttributes": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_GetService_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EndTime](#API_GetService_RequestSyntax) **   <a name="applicationsignals-GetService-request-uri-EndTime"></a>
The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`
Your requested start time will be rounded to the nearest hour.
Required: Yes

 ** [StartTime](#API_GetService_RequestSyntax) **   <a name="applicationsignals-GetService-request-uri-StartTime"></a>
The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`
Your requested start time will be rounded to the nearest hour.
Required: Yes

## Request Body
<a name="API_GetService_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [KeyAttributes](#API_GetService_RequestSyntax) **   <a name="applicationsignals-GetService-request-KeyAttributes"></a>
Use this field to specify which service you want to retrieve information for. You must specify at least the `Type`, `Name`, and `Environment` attributes.
This is a string-to-string map. It can include the following fields.
+  `Type` designates the type of object this is.
+  `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource`.
+  `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service`, `RemoteService`, or `AWS::Service`.
+  `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource`.
+  `Environment` specifies the location where this object is hosted, or what it belongs to.
Type: String to string map
Map Entries: Maximum number of 4 items.
Key Pattern: `[a-zA-Z]{1,50}`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `[ -~]*[!-~]+[ -~]*`
Required: Yes

## Response Syntax
<a name="API_GetService_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EndTime": number,
   "LogGroupReferences": [
      {
         "string" : "string"
      }
   ],
   "Service": {
      "AttributeMaps": [
         {
            "string" : "string"
         }
      ],
      "KeyAttributes": {
         "string" : "string"
      },
      "LogGroupReferences": [
         {
            "string" : "string"
         }
      ],
      "MetricReferences": [
         {
            "AccountId": "string",
            "Dimensions": [
               {
                  "Name": "string",
                  "Value": "string"
               }
            ],
            "MetricName": "string",
            "MetricType": "string",
            "Namespace": "string"
         }
      ],
      "ServiceGroups": [
         {
            "GroupIdentifier": "string",
            "GroupName": "string",
            "GroupSource": "string",
            "GroupValue": "string"
         }
      ]
   },
   "StartTime": number
}
```

## Response Elements
<a name="API_GetService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndTime](#API_GetService_ResponseSyntax) **   <a name="applicationsignals-GetService-response-EndTime"></a>
The end time of the data included in the response. In a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`.
This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.
Type: Timestamp

 ** [LogGroupReferences](#API_GetService_ResponseSyntax) **   <a name="applicationsignals-GetService-response-LogGroupReferences"></a>
An array of string-to-string maps that each contain information about one log group associated with this service. Each string-to-string map includes the following fields:
+  `"Type": "AWS::Resource"`
+  `"ResourceType": "AWS::Logs::LogGroup"`
+  `"Identifier": "name-of-log-group"`
Type: Array of string to string maps
Map Entries: Maximum number of 4 items.
Key Pattern: `[a-zA-Z]{1,50}`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `[ -~]*[!-~]+[ -~]*`

 ** [Service](#API_GetService_ResponseSyntax) **   <a name="applicationsignals-GetService-response-Service"></a>
A structure containing information about the service.
Type: [Service](API_Service.md) object

 ** [StartTime](#API_GetService_ResponseSyntax) **   <a name="applicationsignals-GetService-response-StartTime"></a>
The start time of the data included in the response. In a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`.
This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.
Type: Timestamp

## Errors
<a name="API_GetService_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_GetService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/GetService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/GetService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/GetService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/GetService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/GetService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/GetService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/GetService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/GetService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/GetService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/GetService)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
