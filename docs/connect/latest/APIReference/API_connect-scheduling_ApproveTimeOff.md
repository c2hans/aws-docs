---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-scheduling_ApproveTimeOff.html
---

# ApproveTimeOff
<a name="API_connect-scheduling_ApproveTimeOff"></a>

Approves a time off request. Evaluates agent time off balances and group time off allowances before approving. `RuleFailureAction` controls what happens when these evaluations fail. The request is rejected with `CONFLICTING_TIME_OFF_REQUEST` if it overlaps another time off request for the user that is `APPROVED` or being approved.

The time off request is processed asynchronously, so a successful call doesn't indicate the final status. Read the resulting status with `GetTimeOff` or from the time off state-change events.

Approving an `APPROVED` request succeeds without a change. Approving a `REJECTED` request evaluates the rules again, so it can end `APPROVED` or `REJECTED`, and repeating the call can give a different result. Check the status with `GetTimeOff` before you retry.

Returns `ConflictException` if the request is `PENDING` or `CANCELLED`. `PENDING` means Connect Customer is still processing the request asynchronously. Wait until `GetTimeOff` returns a status other than `PENDING`, and then retry.

**Important**
When the approval succeeds, Connect Customer cancels any overtime or voluntary time off activity that overlaps the approved window.

**Note**
Connect Customer doesn't check whether the principal that calls this operation supervises the user. The staffing group's approval settings also don't apply. IAM permissions are the only control. If you allow a principal to call this operation, that principal can send `RuleFailureAction` `OVERRIDE` and approve a request past failed rules. Grant permission for this operation only to principals that you trust to override time off rules.

## Request Syntax
<a name="API_connect-scheduling_ApproveTimeOff_RequestSyntax"></a>

```
POST /scheduling/instances/{{InstanceId}}/users/{{UserId}}/timeoffs/{{TimeOffId}}/approve HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "RuleFailureAction": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-scheduling_ApproveTimeOff_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_connect-scheduling_ApproveTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_ApproveTimeOff-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `(arn:(aws|aws-us-gov):connect:[a-z]{2}(-[a-z]+){1,2}-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [TimeOffId](#API_connect-scheduling_ApproveTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_ApproveTimeOff-request-uri-TimeOffId"></a>
The unique identifier of the time off request to approve. If the time off request doesn't belong to `UserId`, the operation returns `ResourceNotFoundException`.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** [UserId](#API_connect-scheduling_ApproveTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_ApproveTimeOff-request-uri-UserId"></a>
The identifier of the user who the time off request belongs to. This can be the ID or the ARN of the user.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_connect-scheduling_ApproveTimeOff_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_connect-scheduling_ApproveTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_ApproveTimeOff-request-Description"></a>
A description recorded with the approval. `GetTimeOff` doesn't return it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** [RuleFailureAction](#API_connect-scheduling_ApproveTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_ApproveTimeOff-request-RuleFailureAction"></a>
Controls what happens when a configured rule fails. `REJECT`, the default, records an `ERROR` and leaves the request `REJECTED`. `OVERRIDE` records a `WARNING` and approves the request, like the *Override time off rules* option in the Connect Customer admin website. `OVERRIDE` never waives `CONFLICTING_TIME_OFF_REQUEST`.
Type: String
Valid Values: `REJECT | OVERRIDE`
Required: No

## Response Syntax
<a name="API_connect-scheduling_ApproveTimeOff_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-scheduling_ApproveTimeOff_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-scheduling_ApproveTimeOff_Errors"></a>

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
<a name="API_connect-scheduling_ApproveTimeOff_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectscheduling-2026-07-16/ApproveTimeOff)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectscheduling-2026-07-16/ApproveTimeOff)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectscheduling-2026-07-16/ApproveTimeOff)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectscheduling-2026-07-16/ApproveTimeOff)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectscheduling-2026-07-16/ApproveTimeOff)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectscheduling-2026-07-16/ApproveTimeOff)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectscheduling-2026-07-16/ApproveTimeOff)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectscheduling-2026-07-16/ApproveTimeOff)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectscheduling-2026-07-16/ApproveTimeOff)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectscheduling-2026-07-16/ApproveTimeOff)
