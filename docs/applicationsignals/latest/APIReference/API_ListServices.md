---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListServices.html
---

# ListServices
<a name="API_ListServices"></a>

Returns a list of services that have been discovered by Application Signals. A service represents a minimum logical and transactional unit that completes a business function. Services are discovered through Application Signals instrumentation.

## Request Syntax
<a name="API_ListServices_RequestSyntax"></a>

```
GET /services?AwsAccountId={{AwsAccountId}}&EndTime={{EndTime}}&IncludeLinkedAccounts={{IncludeLinkedAccounts}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&StartTime={{StartTime}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListServices_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListServices_RequestSyntax) **   <a name="applicationsignals-ListServices-request-uri-AwsAccountId"></a>
 AWS Account ID.
Pattern: `[0-9]{12}`

 ** [EndTime](#API_ListServices_RequestSyntax) **   <a name="applicationsignals-ListServices-request-uri-EndTime"></a>
The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`
Your requested start time will be rounded to the nearest hour.
Required: Yes

 ** [IncludeLinkedAccounts](#API_ListServices_RequestSyntax) **   <a name="applicationsignals-ListServices-request-uri-IncludeLinkedAccounts"></a>
If you are using this operation in a monitoring account, specify `true` to include services from source accounts in the returned data.

 ** [MaxResults](#API_ListServices_RequestSyntax) **   <a name="applicationsignals-ListServices-request-uri-MaxResults"></a>
 The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListServices_RequestSyntax) **   <a name="applicationsignals-ListServices-request-uri-NextToken"></a>
Include this value, if it was returned by the previous operation, to get the next set of services.

 ** [StartTime](#API_ListServices_RequestSyntax) **   <a name="applicationsignals-ListServices-request-uri-StartTime"></a>
The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`
Your requested start time will be rounded to the nearest hour.
Required: Yes

## Request Body
<a name="API_ListServices_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListServices_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EndTime": number,
   "NextToken": "string",
   "ServiceSummaries": [
      {
         "AttributeMaps": [
            {
               "string" : "string"
            }
         ],
         "KeyAttributes": {
            "string" : "string"
         },
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
      }
   ],
   "StartTime": number
}
```

## Response Elements
<a name="API_ListServices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndTime](#API_ListServices_ResponseSyntax) **   <a name="applicationsignals-ListServices-response-EndTime"></a>
The end of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`
This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.
Type: Timestamp

 ** [NextToken](#API_ListServices_ResponseSyntax) **   <a name="applicationsignals-ListServices-response-NextToken"></a>
Include this value in your next use of this API to get next set of services.
Type: String

 ** [ServiceSummaries](#API_ListServices_ResponseSyntax) **   <a name="applicationsignals-ListServices-response-ServiceSummaries"></a>
An array of structures, where each structure contains some information about a service. To get complete information about a service, use [GetService](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetService.html).
Type: Array of [ServiceSummary](API_ServiceSummary.md) objects

 ** [StartTime](#API_ListServices_ResponseSyntax) **   <a name="applicationsignals-ListServices-response-StartTime"></a>
The start of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: `1698778057`
This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.
Type: Timestamp

## Errors
<a name="API_ListServices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListServices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/ListServices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/ListServices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ListServices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/ListServices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ListServices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/ListServices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/ListServices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/ListServices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/ListServices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ListServices)
