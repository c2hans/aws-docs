---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-scheduling_GetTimeOff.html
---

# GetTimeOff
<a name="API_connect-scheduling_GetTimeOff"></a>

Returns a time off request, including its current status and validation results.

## Request Syntax
<a name="API_connect-scheduling_GetTimeOff_RequestSyntax"></a>

```
GET /scheduling/instances/{{InstanceId}}/users/{{UserId}}/timeoffs/{{TimeOffId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-scheduling_GetTimeOff_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_connect-scheduling_GetTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_GetTimeOff-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `(arn:(aws|aws-us-gov):connect:[a-z]{2}(-[a-z]+){1,2}-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [TimeOffId](#API_connect-scheduling_GetTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_GetTimeOff-request-uri-TimeOffId"></a>
The identifier of the time off request. If the time off request doesn't belong to `UserId`, the operation returns `ResourceNotFoundException`.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** [UserId](#API_connect-scheduling_GetTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_GetTimeOff-request-uri-UserId"></a>
The identifier of the user who the time off request belongs to. This can be the ID or the ARN of the user.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_connect-scheduling_GetTimeOff_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-scheduling_GetTimeOff_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedAt": number,
   "CreatedBy": { ... },
   "Description": "string",
   "EndAt": number,
   "ShiftActivityId": "string",
   "StartAt": number,
   "Status": "string",
   "TimeOffId": "string",
   "UpdatedAt": number,
   "UpdatedBy": { ... },
   "UserId": "string",
   "ValidationResults": [
      {
         "Code": "string",
         "Severity": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-scheduling_GetTimeOff_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_connect-scheduling_GetTimeOff_ResponseSyntax) **   <a name="connect-connect-scheduling_GetTimeOff-response-CreatedAt"></a>
The timestamp when the time off request was created.
Type: Timestamp

 ** [CreatedBy](#API_connect-scheduling_GetTimeOff_ResponseSyntax) **   <a name="connect-connect-scheduling_GetTimeOff-response-CreatedBy"></a>
The identity that created the request. Immutable for the life of the request.
Type: [ActorInfo](API_connect-scheduling_ActorInfo.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [Description](#API_connect-scheduling_GetTimeOff_ResponseSyntax) **   <a name="connect-connect-scheduling_GetTimeOff-response-Description"></a>
The description of the time off request. `CreateTimeOff` sets it, and `CancelTimeOff` replaces or removes it. An edit in the Connect Customer admin website can also change it. `GetTimeOff` doesn't return descriptions sent with `ApproveTimeOff` or `RejectTimeOff`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [EndAt](#API_connect-scheduling_GetTimeOff_ResponseSyntax) **   <a name="connect-connect-scheduling_GetTimeOff-response-EndAt"></a>
The end of the time off window, exclusive, as sent to `CreateTimeOff`.
Type: Timestamp

 ** [ShiftActivityId](#API_connect-scheduling_GetTimeOff_ResponseSyntax) **   <a name="connect-connect-scheduling_GetTimeOff-response-ShiftActivityId"></a>
The identifier of the shift activity for the time off request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [StartAt](#API_connect-scheduling_GetTimeOff_ResponseSyntax) **   <a name="connect-connect-scheduling_GetTimeOff-response-StartAt"></a>
The start of the time off window, inclusive, as sent to `CreateTimeOff`.
Type: Timestamp

 ** [Status](#API_connect-scheduling_GetTimeOff_ResponseSyntax) **   <a name="connect-connect-scheduling_GetTimeOff-response-Status"></a>
The status of the time off request.
+  `PENDING`: Connect Customer is processing a change to the request, which then changes to another status. An edit in the Connect Customer admin website can also make a request `PENDING`, so an `APPROVED` request can become `PENDING` and then end `APPROVED` or `REJECTED`.
+  `AWAITING_APPROVAL`: the request is waiting for an `ApproveTimeOff` or `RejectTimeOff` call.
Type: String
Valid Values: `PENDING | APPROVED | REJECTED | CANCELLED | AWAITING_APPROVAL`

 ** [TimeOffId](#API_connect-scheduling_GetTimeOff_ResponseSyntax) **   <a name="connect-connect-scheduling_GetTimeOff-response-TimeOffId"></a>
The identifier of the time off request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`

 ** [UpdatedAt](#API_connect-scheduling_GetTimeOff_ResponseSyntax) **   <a name="connect-connect-scheduling_GetTimeOff-response-UpdatedAt"></a>
The timestamp when the time off request was last modified.
Type: Timestamp

 ** [UpdatedBy](#API_connect-scheduling_GetTimeOff_ResponseSyntax) **   <a name="connect-connect-scheduling_GetTimeOff-response-UpdatedBy"></a>
The identity that made the most recent `ApproveTimeOff`, `RejectTimeOff`, or `CancelTimeOff` call on the request, or took the same action in the Connect Customer admin website. Absent until one of those actions is taken, including after Connect Customer decides an `AUTOMATIC` request. `UpdatedAt` also changes when a `PENDING` request changes to another status and for other edits, which don't set `UpdatedBy`.
Type: [ActorInfo](API_connect-scheduling_ActorInfo.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [UserId](#API_connect-scheduling_GetTimeOff_ResponseSyntax) **   <a name="connect-connect-scheduling_GetTimeOff-response-UserId"></a>
The identifier of the user the time off is for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [ValidationResults](#API_connect-scheduling_GetTimeOff_ResponseSyntax) **   <a name="connect-connect-scheduling_GetTimeOff-response-ValidationResults"></a>
Warnings or failures produced while processing the time off request.
Type: Array of [TimeOffValidationResult](API_connect-scheduling_TimeOffValidationResult.md) objects

## Errors
<a name="API_connect-scheduling_GetTimeOff_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

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
<a name="API_connect-scheduling_GetTimeOff_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectscheduling-2026-07-16/GetTimeOff)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectscheduling-2026-07-16/GetTimeOff)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectscheduling-2026-07-16/GetTimeOff)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectscheduling-2026-07-16/GetTimeOff)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectscheduling-2026-07-16/GetTimeOff)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectscheduling-2026-07-16/GetTimeOff)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectscheduling-2026-07-16/GetTimeOff)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectscheduling-2026-07-16/GetTimeOff)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectscheduling-2026-07-16/GetTimeOff)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectscheduling-2026-07-16/GetTimeOff)
