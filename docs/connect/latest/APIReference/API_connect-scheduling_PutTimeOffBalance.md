---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-scheduling_PutTimeOffBalance.html
---

# PutTimeOffBalance

Sets the time off balance for one user and shift activity. The value replaces the existing balance rather than adjusting it, so you can safely retry the call. This operation can't remove a balance. To remove one, upload a blank balance in the Connect Customer admin website. For more information, see [Import an agent's time off balance](https://docs.aws.amazon.com/connect/latest/adminguide/upload-timeoff-balance.html) in the *Connect Customer Administrator Guide*.

## Request Syntax
<a name="API_connect-scheduling_PutTimeOffBalance_RequestSyntax"></a>

```
PUT /scheduling/instances/{{InstanceId}}/users/{{UserId}}/timeoff-balances/{{ShiftActivityId}} HTTP/1.1
Content-type: application/json

{
   "Balance": {
      "Unit": "{{string}}",
      "Value": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_connect-scheduling_PutTimeOffBalance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_connect-scheduling_PutTimeOffBalance_RequestSyntax) **   <a name="connect-connect-scheduling_PutTimeOffBalance-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `(arn:(aws|aws-us-gov):connect:[a-z]{2}(-[a-z]+){1,2}-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [ShiftActivityId](#API_connect-scheduling_PutTimeOffBalance_RequestSyntax) **   <a name="connect-connect-scheduling_PutTimeOffBalance-request-uri-ShiftActivityId"></a>
The identifier of the shift activity that the balance applies to. This can be the ID or the ARN of the shift activity.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [UserId](#API_connect-scheduling_PutTimeOffBalance_RequestSyntax) **   <a name="connect-connect-scheduling_PutTimeOffBalance-request-uri-UserId"></a>
The identifier of the user whose balance is being updated. This can be the ID or the ARN of the user.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_connect-scheduling_PutTimeOffBalance_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Balance](#API_connect-scheduling_PutTimeOffBalance_RequestSyntax) **   <a name="connect-connect-scheduling_PutTimeOffBalance-request-Balance"></a>
The new time off balance for the user and activity. It replaces the existing balance.
Type: [Duration](API_connect-scheduling_Duration.md) object
Required: Yes

## Response Syntax
<a name="API_connect-scheduling_PutTimeOffBalance_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-scheduling_PutTimeOffBalance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-scheduling_PutTimeOffBalance_Errors"></a>

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
<a name="API_connect-scheduling_PutTimeOffBalance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectscheduling-2026-07-16/PutTimeOffBalance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectscheduling-2026-07-16/PutTimeOffBalance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectscheduling-2026-07-16/PutTimeOffBalance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectscheduling-2026-07-16/PutTimeOffBalance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectscheduling-2026-07-16/PutTimeOffBalance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectscheduling-2026-07-16/PutTimeOffBalance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectscheduling-2026-07-16/PutTimeOffBalance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectscheduling-2026-07-16/PutTimeOffBalance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectscheduling-2026-07-16/PutTimeOffBalance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectscheduling-2026-07-16/PutTimeOffBalance)
