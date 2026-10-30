---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ListScheduleActions.html
---

# ListScheduleActions
<a name="API_ListScheduleActions"></a>

Displays a list of the schedule actions on a feed, including the status of each action and, for a failed action, information about why it failed.

Elemental Inference keeps an action whose status is COMPLETED or FAILED for about 48 hours after its scheduled time, and then deletes it automatically.

## Request Syntax
<a name="API_ListScheduleActions_RequestSyntax"></a>

```
GET /v1/feed/{{id}}/schedule-actions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListScheduleActions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_ListScheduleActions_RequestSyntax) **   <a name="elementalinference-ListScheduleActions-request-uri-id"></a>
The ID of the feed that you want to query.
Pattern: `[a-z0-9]{19}`
Required: Yes

 ** [maxResults](#API_ListScheduleActions_RequestSyntax) **   <a name="elementalinference-ListScheduleActions-request-uri-maxResults"></a>
The maximum number of results to return for each API request. If you don't specify MaxResults, Elemental Inference returns a maximum of 10 results for each page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListScheduleActions_RequestSyntax) **   <a name="elementalinference-ListScheduleActions-request-uri-nextToken"></a>
The token that identifies the batch of results that you want to see. To see the next batch, submit the request a second time and specify the NextToken value that Elemental Inference returned.

## Request Body
<a name="API_ListScheduleActions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListScheduleActions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "scheduleActions": [
      {
         "actionName": "string",
         "error": {
            "errorCode": "string",
            "errorMessage": "string"
         },
         "operations": [
            { ... }
         ],
         "startConfiguration": { ... },
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListScheduleActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListScheduleActions_ResponseSyntax) **   <a name="elementalinference-ListScheduleActions-response-nextToken"></a>
The token that identifies the next batch of results. Elemental Inference returns it only when more results are available.
Type: String

 ** [scheduleActions](#API_ListScheduleActions_ResponseSyntax) **   <a name="elementalinference-ListScheduleActions-response-scheduleActions"></a>
A list of the schedule actions on the feed.
Type: Array of [ScheduleAction](API_ScheduleAction.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListScheduleActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource specified in the action doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestException **
The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying.
HTTP Status Code: 400

## See Also
<a name="API_ListScheduleActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/ListScheduleActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/ListScheduleActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/ListScheduleActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/ListScheduleActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/ListScheduleActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/ListScheduleActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/ListScheduleActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/ListScheduleActions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/ListScheduleActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/ListScheduleActions)
