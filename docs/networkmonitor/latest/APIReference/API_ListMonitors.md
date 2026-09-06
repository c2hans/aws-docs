---
source_url: https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_ListMonitors.html
---

# ListMonitors
<a name="API_ListMonitors"></a>

Returns a list of all of your monitors.

## Request Syntax
<a name="API_ListMonitors_RequestSyntax"></a>

```
GET /monitors?maxResults={{maxResults}}&nextToken={{nextToken}}&state={{state}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMonitors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListMonitors_RequestSyntax) **   <a name="networksyntheticmonitor-ListMonitors-request-uri-maxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
If `MaxResults` is given a value larger than 100, only 100 results are returned.
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [nextToken](#API_ListMonitors_RequestSyntax) **   <a name="networksyntheticmonitor-ListMonitors-request-uri-nextToken"></a>
The token for the next page of results.
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [state](#API_ListMonitors_RequestSyntax) **   <a name="networksyntheticmonitor-ListMonitors-request-uri-state"></a>
The list of all monitors and their states.

## Request Body
<a name="API_ListMonitors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMonitors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "monitors": [
      {
         "aggregationPeriod": number,
         "monitorArn": "string",
         "monitorName": "string",
         "state": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMonitors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [monitors](#API_ListMonitors_ResponseSyntax) **   <a name="networksyntheticmonitor-ListMonitors-response-monitors"></a>
Lists individual details about each of your monitors.
Type: Array of [MonitorSummary](API_MonitorSummary.md) objects

 ** [nextToken](#API_ListMonitors_ResponseSyntax) **   <a name="networksyntheticmonitor-ListMonitors-response-nextToken"></a>
The token for the next page of results.
Type: String

## Errors
<a name="API_ListMonitors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling
HTTP Status Code: 429

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListMonitors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmonitor-2023-08-01/ListMonitors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmonitor-2023-08-01/ListMonitors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmonitor-2023-08-01/ListMonitors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmonitor-2023-08-01/ListMonitors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmonitor-2023-08-01/ListMonitors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmonitor-2023-08-01/ListMonitors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmonitor-2023-08-01/ListMonitors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmonitor-2023-08-01/ListMonitors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmonitor-2023-08-01/ListMonitors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmonitor-2023-08-01/ListMonitors)
