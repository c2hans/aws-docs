---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-scheduling_RejectTimeOff.html
---

# RejectTimeOff

Rejects a time off request.

Rejecting a `REJECTED` request succeeds without a change. Returns `ConflictException` if the request is `PENDING` or `CANCELLED`. `PENDING` means Connect Customer is still processing the request asynchronously. Wait until `GetTimeOff` returns a status other than `PENDING`, and then retry.

## Request Syntax
<a name="API_connect-scheduling_RejectTimeOff_RequestSyntax"></a>

```
POST /scheduling/instances/{{InstanceId}}/users/{{UserId}}/timeoffs/{{TimeOffId}}/reject HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-scheduling_RejectTimeOff_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_connect-scheduling_RejectTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_RejectTimeOff-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `(arn:(aws|aws-us-gov):connect:[a-z]{2}(-[a-z]+){1,2}-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [TimeOffId](#API_connect-scheduling_RejectTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_RejectTimeOff-request-uri-TimeOffId"></a>
The unique identifier of the time off request to reject. If the time off request doesn't belong to `UserId`, the operation returns `ResourceNotFoundException`.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** [UserId](#API_connect-scheduling_RejectTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_RejectTimeOff-request-uri-UserId"></a>
The identifier of the user who the time off request belongs to. This can be the ID or the ARN of the user.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_connect-scheduling_RejectTimeOff_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_connect-scheduling_RejectTimeOff_RequestSyntax) **   <a name="connect-connect-scheduling_RejectTimeOff-request-Description"></a>
A description recorded with the rejection, such as the reason. `GetTimeOff` doesn't return it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## Response Syntax
<a name="API_connect-scheduling_RejectTimeOff_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-scheduling_RejectTimeOff_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-scheduling_RejectTimeOff_Errors"></a>

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
<a name="API_connect-scheduling_RejectTimeOff_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectscheduling-2026-07-16/RejectTimeOff)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectscheduling-2026-07-16/RejectTimeOff)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectscheduling-2026-07-16/RejectTimeOff)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectscheduling-2026-07-16/RejectTimeOff)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectscheduling-2026-07-16/RejectTimeOff)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectscheduling-2026-07-16/RejectTimeOff)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectscheduling-2026-07-16/RejectTimeOff)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectscheduling-2026-07-16/RejectTimeOff)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectscheduling-2026-07-16/RejectTimeOff)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectscheduling-2026-07-16/RejectTimeOff)
