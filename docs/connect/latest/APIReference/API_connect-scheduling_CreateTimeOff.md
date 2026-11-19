---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-scheduling_CreateTimeOff.html
---

# CreateTimeOff

Creates a time off request for a user. You don't provide a status, because Connect Customer owns the request lifecycle. To get the decided status, call `GetTimeOff` or use the time off state-change events.

 `ApprovalType` controls who approves the request. You can specify one of the following values:
+  `AWAIT_APPROVAL`: the request waits in `AWAITING_APPROVAL` until you call `ApproveTimeOff` or `RejectTimeOff`. Rule evaluation and the overlap check run at approval, not at creation. A waiting request doesn't reserve its window, so another request for the same window can be approved first.
+  `AUTOMATIC`: Connect Customer evaluates the rules (time off balances and group allowances) and decides the request. The request can be `PENDING` while Connect Customer decides, and then ends `APPROVED` or `REJECTED`. If it overlaps another time off request for the user, the requested time off ends `REJECTED` with `CONFLICTING_TIME_OFF_REQUEST`. It also ends `REJECTED` if it overlaps overtime or voluntary time off. If the whole window is in the past, Connect Customer records failed rules as `WARNING` and doesn't reject the request, whatever the `RuleFailureAction`.

The staffing group's *Supervisor approval needed* setting doesn't apply to this operation. `ApprovalType` alone decides whether the request waits for approval. The operation fails with `ValidationException` on `UserId` in the following cases:
+ The user isn't in a staffing group, or the staffing group isn't associated with a forecast group.
+ Time off isn't [enabled](https://docs.aws.amazon.com/connect/latest/adminguide/enable-to.html) for the user's staffing group, or the user's staff rules don't allow time off.

To change the dates of a request, cancel it with `CancelTimeOff` and create a new request. The new request has a new `TimeOffId`.

**Note**
Connect Customer doesn't check whether the principal that calls this operation supervises the user. The staffing group's approval settings also don't apply. IAM permissions are the only control. If you allow a principal to call this operation, that principal can send `ApprovalType` `AUTOMATIC` with `RuleFailureAction` `OVERRIDE` and approve a request past failed rules. Grant permission for this operation only to principals that you trust to override time off rules.

For information about time off in the Connect Customer admin website, see [Time off management](https://docs.aws.amazon.com/connect/latest/adminguide/scheduling-time-off.html) in the *Connect Customer Administrator Guide*.

## Request Syntax
<a name="API_connect-scheduling_CreateTimeOff_RequestSyntax"></a>

```
POST /scheduling/instances/{{InstanceId}}/users/{{UserId}}/timeoffs HTTP/1.1
Content-type: application/json

{
   "ApprovalType": "{{string}}",
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "EndAt": {{number}},
   "RuleFailureAction": "{{string}}",
   "ShiftActivityId": "{{string}}",
   "StartAt": {{number}}
}
```

## URI Request Parameters
<a name="API_connect-scheduling_CreateTimeOff_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_connect-scheduling_CreateTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_CreateTimeOff-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `(arn:(aws|aws-us-gov):connect:[a-z]{2}(-[a-z]+){1,2}-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [UserId](#API_connect-scheduling_CreateTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_CreateTimeOff-request-uri-UserId"></a>
The identifier of the user who the time off request is for. This can be the ID or the ARN of the user.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_connect-scheduling_CreateTimeOff_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApprovalType](#API_connect-scheduling_CreateTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_CreateTimeOff-request-ApprovalType"></a>
Controls who approves the request. `AWAIT_APPROVAL` waits for an `ApproveTimeOff` or `RejectTimeOff` call. `AUTOMATIC` has Connect Customer decide the request. For details, see `CreateTimeOff`.
Type: String
Valid Values: `AWAIT_APPROVAL | AUTOMATIC`
Required: Yes

 ** [ClientToken](#API_connect-scheduling_CreateTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_CreateTimeOff-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If this token matches a previous request, Connect Customer returns the result of that request and doesn't create another time off request. If you don't provide a token, the AWS SDK populates this field. If you reuse a client token with a different request body, the request fails with `ValidationException`. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** [Description](#API_connect-scheduling_CreateTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_CreateTimeOff-request-Description"></a>
A description recorded on the time off request. If you omit it, the request has no description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** [EndAt](#API_connect-scheduling_CreateTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_CreateTimeOff-request-EndAt"></a>
The end of the time off window, exclusive. It must be after `StartAt` and no later than 24 months after the current date. Connect Customer stores the value as sent, to the millisecond.
Type: Timestamp
Required: Yes

 ** [RuleFailureAction](#API_connect-scheduling_CreateTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_CreateTimeOff-request-RuleFailureAction"></a>
Controls what happens when a configured rule fails. `REJECT`, the default, records an `ERROR` and ends the request `REJECTED`, unless the whole window is in the past. `OVERRIDE` records a `WARNING` and ends the request `APPROVED`, like the *Override time off rules* option in the Connect Customer admin website. `OVERRIDE` requires `AUTOMATIC`. With `AWAIT_APPROVAL`, `OVERRIDE` fails with `ValidationException`. Set it on `ApproveTimeOff` instead. `OVERRIDE` never waives `CONFLICTING_TIME_OFF_REQUEST`.
Type: String
Valid Values: `REJECT | OVERRIDE`
Required: No

 ** [ShiftActivityId](#API_connect-scheduling_CreateTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_CreateTimeOff-request-ShiftActivityId"></a>
The identifier of the shift activity that defines the type of time off being requested. This can be the ID or the ARN of the shift activity. It must be a time off activity. Activities that aren't set as *Requestable* are accepted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [StartAt](#API_connect-scheduling_CreateTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_CreateTimeOff-request-StartAt"></a>
The start of the time off window, inclusive. It must be no earlier than one year before the current date. Connect Customer stores the value as sent, to the millisecond.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_connect-scheduling_CreateTimeOff_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "TimeOffId": "string"
}
```

## Response Elements
<a name="API_connect-scheduling_CreateTimeOff_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TimeOffId](#API_connect-scheduling_CreateTimeOff_ResponseSyntax) **   <a name="connect-connect-scheduling_CreateTimeOff-response-TimeOffId"></a>
The identifier of the time off request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`

## Errors
<a name="API_connect-scheduling_CreateTimeOff_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of a conflict with the current state of the resource.
 ** ResourceId **
The identifier or ARN of the resource that is in conflict.
 ** ResourceType **
The type of the resource that is in conflict.
HTTP Status Code: 409

 ** InternalServerException **
The request processing failed because of an error or failure with the service.
 ** RetryAfterSeconds **
The number of seconds to wait before retrying.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** ResourceId **
The identifier or ARN of the resource that was not found.
 ** ResourceType **
The type of the resource that was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** QuotaCode **
The code of the quota that would be exceeded, for use with the Service Quotas API.
 ** ResourceId **
The identifier or ARN of the resource whose quota would be exceeded.
 ** ResourceType **
The type of the resource whose quota would be exceeded.
 ** ServiceCode **
The code of the service that owns the quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
 ** QuotaCode **
The code of the quota that was throttled, for use with the Service Quotas API.
 ** RetryAfterSeconds **
The number of seconds to wait before retrying.
 ** ServiceCode **
The code of the service that owns the quota.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** FieldList **
The specific input fields that failed validation, when `Reason` is `FIELD_VALIDATION_FAILED`.
 ** Reason **
The reason the input failed validation. Branch on this value rather than on the message wording.
HTTP Status Code: 400

## See Also
<a name="API_connect-scheduling_CreateTimeOff_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectscheduling-2026-07-16/CreateTimeOff)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectscheduling-2026-07-16/CreateTimeOff)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectscheduling-2026-07-16/CreateTimeOff)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectscheduling-2026-07-16/CreateTimeOff)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectscheduling-2026-07-16/CreateTimeOff)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectscheduling-2026-07-16/CreateTimeOff)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectscheduling-2026-07-16/CreateTimeOff)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectscheduling-2026-07-16/CreateTimeOff)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectscheduling-2026-07-16/CreateTimeOff)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectscheduling-2026-07-16/CreateTimeOff)
