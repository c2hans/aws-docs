---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServiceDependencies.html
---

# ListServiceDependencies
<a name="API_ListServiceDependencies"></a>

Returns a list of service dependencies of the service that you specify. A dependency is an infrastructure component that an operation of this service connects with. Dependencies can include AWS services, AWS resources, and third-party services.

## Request Syntax
<a name="API_ListServiceDependencies_RequestSyntax"></a>

```
POST /service-dependencies?EndTime={{EndTime}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&StartTime={{StartTime}} HTTP/1.1
Content-type: application/json

{
   "KeyAttributes": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListServiceDependencies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EndTime](#API_ListServiceDependencies_RequestSyntax) **   <a name="applicationsignals-ListServiceDependencies-request-uri-EndTime"></a>
The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`
Your requested end time will be rounded to the nearest hour.
Required: Yes

 ** [MaxResults](#API_ListServiceDependencies_RequestSyntax) **   <a name="applicationsignals-ListServiceDependencies-request-uri-MaxResults"></a>
The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListServiceDependencies_RequestSyntax) **   <a name="applicationsignals-ListServiceDependencies-request-uri-NextToken"></a>
Include this value, if it was returned by the previous operation, to get the next set of service dependencies.

 ** [StartTime](#API_ListServiceDependencies_RequestSyntax) **   <a name="applicationsignals-ListServiceDependencies-request-uri-StartTime"></a>
The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`
Your requested start time will be rounded to the nearest hour.
Required: Yes

## Request Body
<a name="API_ListServiceDependencies_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [KeyAttributes](#API_ListServiceDependencies_RequestSyntax) **   <a name="applicationsignals-ListServiceDependencies-request-KeyAttributes"></a>
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
<a name="API_ListServiceDependencies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EndTime": number,
   "NextToken": "string",
   "ServiceDependencies": [
      {
         "DependencyKeyAttributes": {
            "string" : "string"
         },
         "DependencyOperationName": "string",
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
         "OperationName": "string"
      }
   ],
   "StartTime": number
}
```

## Response Elements
<a name="API_ListServiceDependencies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndTime](#API_ListServiceDependencies_ResponseSyntax) **   <a name="applicationsignals-ListServiceDependencies-response-EndTime"></a>
The end of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`
This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.
Type: Timestamp

 ** [NextToken](#API_ListServiceDependencies_ResponseSyntax) **   <a name="applicationsignals-ListServiceDependencies-response-NextToken"></a>
Include this value in your next use of this API to get next set of service dependencies.
Type: String

 ** [ServiceDependencies](#API_ListServiceDependencies_ResponseSyntax) **   <a name="applicationsignals-ListServiceDependencies-response-ServiceDependencies"></a>
An array, where each object in the array contains information about one of the dependencies of this service.
Type: Array of [ServiceDependency](API_ServiceDependency.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [StartTime](#API_ListServiceDependencies_ResponseSyntax) **   <a name="applicationsignals-ListServiceDependencies-response-StartTime"></a>
The start of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`
This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.
Type: Timestamp

## Errors
<a name="API_ListServiceDependencies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListServiceDependencies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/ListServiceDependencies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/ListServiceDependencies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ListServiceDependencies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/ListServiceDependencies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ListServiceDependencies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/ListServiceDependencies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/ListServiceDependencies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/ListServiceDependencies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/ListServiceDependencies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ListServiceDependencies)
