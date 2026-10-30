---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_CreateScheduleAction.html
---

# CreateScheduleAction
<a name="API_CreateScheduleAction"></a>

Creates a schedule action on a feed. A schedule action applies configuration changes to the feed at a time that you specify, in the same way as an UpdateFeed request.

Elemental Inference validates the targets of the action when you create it.

## Request Syntax
<a name="API_CreateScheduleAction_RequestSyntax"></a>

```
POST /v1/feed/{{id}}/schedule-actions HTTP/1.1
Content-type: application/json

{
   "actionName": "{{string}}",
   "operations": [
      { ... }
   ],
   "startConfiguration": { ... }
}
```

## URI Request Parameters
<a name="API_CreateScheduleAction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_CreateScheduleAction_RequestSyntax) **   <a name="elementalinference-CreateScheduleAction-request-uri-id"></a>
Specifies the ID of the feed that you want to add the schedule action to.
Pattern: `[a-z0-9]{19}`
Required: Yes

## Request Body
<a name="API_CreateScheduleAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actionName](#API_CreateScheduleAction_RequestSyntax) **   <a name="elementalinference-CreateScheduleAction-request-actionName"></a>
A name for the schedule action. The name must be unique within the feed. You can reuse the name of an action that you deleted.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`
Required: Yes

 ** [operations](#API_CreateScheduleAction_RequestSyntax) **   <a name="elementalinference-CreateScheduleAction-request-operations"></a>
Specifies the list of configuration changes that you want to make to the feed. Elemental Inference applies all the operations in an action together, in the order that you specify them. If any operation fails, Elemental Inference doesn't apply any of them.
Type: Array of [ScheduleActionOperation](API_ScheduleActionOperation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [startConfiguration](#API_CreateScheduleAction_RequestSyntax) **   <a name="elementalinference-CreateScheduleAction-request-startConfiguration"></a>
Specifies when the action runs.
Type: [ScheduleActionStartConfiguration](API_ScheduleActionStartConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_CreateScheduleAction_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

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
```

## Response Elements
<a name="API_CreateScheduleAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [actionName](#API_CreateScheduleAction_ResponseSyntax) **   <a name="elementalinference-CreateScheduleAction-response-actionName"></a>
The name that you specified.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`

 ** [error](#API_CreateScheduleAction_ResponseSyntax) **   <a name="elementalinference-CreateScheduleAction-response-error"></a>
A description of why the action failed. Elemental Inference returns this property only when the status is FAILED.
Type: [ScheduleActionError](API_ScheduleActionError.md) object

 ** [operations](#API_CreateScheduleAction_ResponseSyntax) **   <a name="elementalinference-CreateScheduleAction-response-operations"></a>
The configuration changes that the action makes to the feed.
Type: Array of [ScheduleActionOperation](API_ScheduleActionOperation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [startConfiguration](#API_CreateScheduleAction_ResponseSyntax) **   <a name="elementalinference-CreateScheduleAction-response-startConfiguration"></a>
Specifies when the action runs.
Type: [ScheduleActionStartConfiguration](API_ScheduleActionStartConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_CreateScheduleAction_ResponseSyntax) **   <a name="elementalinference-CreateScheduleAction-response-status"></a>
The status of the action. After you create the action successfully, Elemental Inference sets the status to PENDING.
Type: String
Valid Values: `PENDING | COMPLETED | FAILED`

## Errors
<a name="API_CreateScheduleAction_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request was rejected because it would exceed one or more service quotas for your account. Review your service quotas and either delete unused resources or request a quota increase.
HTTP Status Code: 402

 ** TooManyRequestException **
The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying.
HTTP Status Code: 400

## See Also
<a name="API_CreateScheduleAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/CreateScheduleAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/CreateScheduleAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/CreateScheduleAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/CreateScheduleAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/CreateScheduleAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/CreateScheduleAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/CreateScheduleAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/CreateScheduleAction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/CreateScheduleAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/CreateScheduleAction)
