---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateScheduledAction.html
---

# UpdateScheduledAction
<a name="API_UpdateScheduledAction"></a>

Reschedules a planned domain configuration change for a later time. This change can be a scheduled [service software update](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html) or a [blue/green Auto-Tune enhancement](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html#auto-tune-types).

## Request Syntax
<a name="API_UpdateScheduledAction_RequestSyntax"></a>

```
PUT /2021-01-01/opensearch/domain/{{DomainName}}/scheduledAction/update HTTP/1.1
Content-type: application/json

{
   "ActionID": "{{string}}",
   "ActionType": "{{string}}",
   "DesiredStartTime": {{number}},
   "ScheduleAt": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateScheduledAction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_UpdateScheduledAction_RequestSyntax) **   <a name="opensearchservice-UpdateScheduledAction-request-uri-DomainName"></a>
The name of the domain to reschedule an action for.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_UpdateScheduledAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ActionID](#API_UpdateScheduledAction_RequestSyntax) **   <a name="opensearchservice-UpdateScheduledAction-request-ActionID"></a>
The unique identifier of the action to reschedule. To retrieve this ID, send a [ListScheduledActions](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListScheduledActions.html) request.
Type: String
Required: Yes

 ** [ActionType](#API_UpdateScheduledAction_RequestSyntax) **   <a name="opensearchservice-UpdateScheduledAction-request-ActionType"></a>
The type of action to reschedule. Can be one of `SERVICE_SOFTWARE_UPDATE`, `JVM_HEAP_SIZE_TUNING`, or `JVM_YOUNG_GEN_TUNING`. To retrieve this value, send a [ListScheduledActions](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListScheduledActions.html) request.
Type: String
Valid Values: `SERVICE_SOFTWARE_UPDATE | JVM_HEAP_SIZE_TUNING | JVM_YOUNG_GEN_TUNING`
Required: Yes

 ** [DesiredStartTime](#API_UpdateScheduledAction_RequestSyntax) **   <a name="opensearchservice-UpdateScheduledAction-request-DesiredStartTime"></a>
The time to implement the change, in Coordinated Universal Time (UTC). Only specify this parameter if you set `ScheduleAt` to `TIMESTAMP`.
Type: Long
Required: No

 ** [ScheduleAt](#API_UpdateScheduledAction_RequestSyntax) **   <a name="opensearchservice-UpdateScheduledAction-request-ScheduleAt"></a>
When to schedule the action.
+  `NOW` - Immediately schedules the update to happen in the current hour if there's capacity available.
+  `TIMESTAMP` - Lets you specify a custom date and time to apply the update. If you specify this value, you must also provide a value for `DesiredStartTime`.
+  `OFF_PEAK_WINDOW` - Marks the action to be picked up during an upcoming off-peak window. There's no guarantee that the change will be implemented during the next immediate window. Depending on capacity, it might happen in subsequent days.
Type: String
Valid Values: `NOW | TIMESTAMP | OFF_PEAK_WINDOW`
Required: Yes

## Response Syntax
<a name="API_UpdateScheduledAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ScheduledAction": {
      "Cancellable": boolean,
      "Description": "string",
      "Id": "string",
      "Mandatory": boolean,
      "ScheduledBy": "string",
      "ScheduledTime": number,
      "Severity": "string",
      "Status": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_UpdateScheduledAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ScheduledAction](#API_UpdateScheduledAction_ResponseSyntax) **   <a name="opensearchservice-UpdateScheduledAction-response-ScheduledAction"></a>
Information about the rescheduled action.
Type: [ScheduledAction](API_ScheduledAction.md) object

## Errors
<a name="API_UpdateScheduledAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** ConflictException **
An error occurred because the client attempts to remove a resource that is currently in use.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** LimitExceededException **
An exception for trying to create more than the allowed number of resources or sub-resources.
HTTP Status Code: 409

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** SlotNotAvailableException **
An exception for attempting to schedule a domain action during an unavailable time slot.
 ** SlotSuggestions **
Alternate time slots during which OpenSearch Service has available capacity to schedule a domain action.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_UpdateScheduledAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/UpdateScheduledAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/UpdateScheduledAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/UpdateScheduledAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/UpdateScheduledAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/UpdateScheduledAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/UpdateScheduledAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/UpdateScheduledAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/UpdateScheduledAction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/UpdateScheduledAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/UpdateScheduledAction)
