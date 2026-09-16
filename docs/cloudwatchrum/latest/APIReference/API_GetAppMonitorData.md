---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetAppMonitorData.html
---

# GetAppMonitorData
<a name="API_GetAppMonitorData"></a>

Retrieves the raw performance events that RUM has collected from your web application, so that you can do your own processing or analysis of this data.

## Request Syntax
<a name="API_GetAppMonitorData_RequestSyntax"></a>

```
POST /appmonitor/{{Name}}/data HTTP/1.1
Content-type: application/json

{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TimeRange": {
      "After": {{number}},
      "Before": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_GetAppMonitorData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_GetAppMonitorData_RequestSyntax) **   <a name="cloudwatchrum-GetAppMonitorData-request-uri-Name"></a>
The name of the app monitor that collected the data that you want to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!\.)[\.\-_#A-Za-z0-9]+`
Required: Yes

## Request Body
<a name="API_GetAppMonitorData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_GetAppMonitorData_RequestSyntax) **   <a name="cloudwatchrum-GetAppMonitorData-request-Filters"></a>
An array of structures that you can use to filter the results to those that match one or more sets of key-value pairs that you specify.
Type: Array of [QueryFilter](API_QueryFilter.md) objects
Required: No

 ** [MaxResults](#API_GetAppMonitorData_RequestSyntax) **   <a name="cloudwatchrum-GetAppMonitorData-request-MaxResults"></a>
The maximum number of results to return in one operation.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetAppMonitorData_RequestSyntax) **   <a name="cloudwatchrum-GetAppMonitorData-request-NextToken"></a>
Use the token returned by the previous operation to request the next page of results.
Type: String
Required: No

 ** [TimeRange](#API_GetAppMonitorData_RequestSyntax) **   <a name="cloudwatchrum-GetAppMonitorData-request-TimeRange"></a>
A structure that defines the time range that you want to retrieve results from.
Type: [TimeRange](API_TimeRange.md) object
Required: Yes

## Response Syntax
<a name="API_GetAppMonitorData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Events": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetAppMonitorData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Events](#API_GetAppMonitorData_ResponseSyntax) **   <a name="cloudwatchrum-GetAppMonitorData-response-Events"></a>
The events that RUM collected that match your request.
Type: Array of strings

 ** [NextToken](#API_GetAppMonitorData_ResponseSyntax) **   <a name="cloudwatchrum-GetAppMonitorData-response-NextToken"></a>
A token that you can use in a subsequent operation to retrieve the next set of results.
Type: String

## Errors
<a name="API_GetAppMonitorData_Errors"></a>

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
<a name="API_GetAppMonitorData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rum-2018-05-10/GetAppMonitorData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rum-2018-05-10/GetAppMonitorData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/GetAppMonitorData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rum-2018-05-10/GetAppMonitorData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/GetAppMonitorData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rum-2018-05-10/GetAppMonitorData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rum-2018-05-10/GetAppMonitorData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rum-2018-05-10/GetAppMonitorData)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rum-2018-05-10/GetAppMonitorData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/GetAppMonitorData)
