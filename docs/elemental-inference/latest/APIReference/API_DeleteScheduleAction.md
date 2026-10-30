---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_DeleteScheduleAction.html
---

# DeleteScheduleAction
<a name="API_DeleteScheduleAction"></a>

Deletes a schedule action from a feed. A deleted action never runs.

You can delete only an action whose status is PENDING. Deleting an action doesn't reverse changes that the action already made to the feed. When you delete or archive a feed, Elemental Inference deletes all the schedule actions on that feed.

## Request Syntax
<a name="API_DeleteScheduleAction_RequestSyntax"></a>

```
DELETE /v1/feed/{{id}}/schedule-actions?actionName={{actionName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteScheduleAction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actionName](#API_DeleteScheduleAction_RequestSyntax) **   <a name="elementalinference-DeleteScheduleAction-request-uri-actionName"></a>
The name of the schedule action that you want to delete.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`
Required: Yes

 ** [id](#API_DeleteScheduleAction_RequestSyntax) **   <a name="elementalinference-DeleteScheduleAction-request-uri-id"></a>
The ID of the feed that holds the schedule action.
Pattern: `[a-z0-9]{19}`
Required: Yes

## Request Body
<a name="API_DeleteScheduleAction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteScheduleAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionName": "string"
}
```

## Response Elements
<a name="API_DeleteScheduleAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionName](#API_DeleteScheduleAction_ResponseSyntax) **   <a name="elementalinference-DeleteScheduleAction-response-actionName"></a>
The name of the schedule action that Elemental Inference deleted.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`

## Errors
<a name="API_DeleteScheduleAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict.
HTTP Status Code: 409

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
<a name="API_DeleteScheduleAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/DeleteScheduleAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/DeleteScheduleAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/DeleteScheduleAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/DeleteScheduleAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/DeleteScheduleAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/DeleteScheduleAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/DeleteScheduleAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/DeleteScheduleAction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/DeleteScheduleAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/DeleteScheduleAction)
