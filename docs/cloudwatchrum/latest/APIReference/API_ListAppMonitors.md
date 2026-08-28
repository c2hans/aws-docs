---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListAppMonitors.html
---

# ListAppMonitors
<a name="API_ListAppMonitors"></a>

Returns a list of the Amazon CloudWatch RUM app monitors in the account.

## Request Syntax
<a name="API_ListAppMonitors_RequestSyntax"></a>

```
POST /appmonitors?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAppMonitors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListAppMonitors_RequestSyntax) **   <a name="cloudwatchrum-ListAppMonitors-request-uri-MaxResults"></a>
The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListAppMonitors_RequestSyntax) **   <a name="cloudwatchrum-ListAppMonitors-request-uri-NextToken"></a>
Use the token returned by the previous operation to request the next page of results.

## Request Body
<a name="API_ListAppMonitors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAppMonitors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AppMonitorSummaries": [
      {
         "Created": "string",
         "Id": "string",
         "LastModified": "string",
         "Name": "string",
         "State": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAppMonitors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppMonitorSummaries](#API_ListAppMonitors_ResponseSyntax) **   <a name="cloudwatchrum-ListAppMonitors-response-AppMonitorSummaries"></a>
An array of structures that contain information about the returned app monitors.
Type: Array of [AppMonitorSummary](API_AppMonitorSummary.md) objects

 ** [NextToken](#API_ListAppMonitors_ResponseSyntax) **   <a name="cloudwatchrum-ListAppMonitors-response-NextToken"></a>
A token that you can use in a subsequent operation to retrieve the next set of results.
Type: String

## Errors
<a name="API_ListAppMonitors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Internal service exception.
 ** retryAfterSeconds **
The value of a parameter in the request caused an error.
HTTP Status Code: 500

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
<a name="API_ListAppMonitors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rum-2018-05-10/ListAppMonitors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rum-2018-05-10/ListAppMonitors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/ListAppMonitors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rum-2018-05-10/ListAppMonitors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/ListAppMonitors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rum-2018-05-10/ListAppMonitors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rum-2018-05-10/ListAppMonitors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rum-2018-05-10/ListAppMonitors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rum-2018-05-10/ListAppMonitors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/ListAppMonitors)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch RUM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchrum` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
