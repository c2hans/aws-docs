---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_CreateSchedule.html
---

# CreateSchedule
<a name="API_CreateSchedule"></a>

Creates the specified schedule.

## Request Syntax
<a name="API_CreateSchedule_RequestSyntax"></a>

```
POST /schedules/{{Name}} HTTP/1.1
Content-type: application/json

{
   "ActionAfterCompletion": "{{string}}",
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "EndDate": {{number}},
   "FlexibleTimeWindow": {
      "MaximumWindowInMinutes": {{number}},
      "Mode": "{{string}}"
   },
   "GroupName": "{{string}}",
   "KmsKeyArn": "{{string}}",
   "ScheduleExpression": "{{string}}",
   "ScheduleExpressionTimezone": "{{string}}",
   "StartDate": {{number}},
   "State": "{{string}}",
   "Target": {
      "Arn": "{{string}}",
      "DeadLetterConfig": {
         "Arn": "{{string}}"
      },
      "EcsParameters": {
         "CapacityProviderStrategy": [
            {
               "base": {{number}},
               "capacityProvider": "{{string}}",
               "weight": {{number}}
            }
         ],
         "EnableECSManagedTags": {{boolean}},
         "EnableExecuteCommand": {{boolean}},
         "Group": "{{string}}",
         "LaunchType": "{{string}}",
         "NetworkConfiguration": {
            "awsvpcConfiguration": {
               "AssignPublicIp": "{{string}}",
               "SecurityGroups": [ "{{string}}" ],
               "Subnets": [ "{{string}}" ]
            }
         },
         "PlacementConstraints": [
            {
               "expression": "{{string}}",
               "type": "{{string}}"
            }
         ],
         "PlacementStrategy": [
            {
               "field": "{{string}}",
               "type": "{{string}}"
            }
         ],
         "PlatformVersion": "{{string}}",
         "PropagateTags": "{{string}}",
         "ReferenceId": "{{string}}",
         "Tags": [
            {
               "{{string}}" : "{{string}}"
            }
         ],
         "TaskCount": {{number}},
         "TaskDefinitionArn": "{{string}}"
      },
      "EventBridgeParameters": {
         "DetailType": "{{string}}",
         "Source": "{{string}}"
      },
      "Input": "{{string}}",
      "KinesisParameters": {
         "PartitionKey": "{{string}}"
      },
      "RetryPolicy": {
         "MaximumEventAgeInSeconds": {{number}},
         "MaximumRetryAttempts": {{number}}
      },
      "RoleArn": "{{string}}",
      "SageMakerPipelineParameters": {
         "PipelineParameterList": [
            {
               "Name": "{{string}}",
               "Value": "{{string}}"
            }
         ]
      },
      "SqsParameters": {
         "MessageGroupId": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_CreateSchedule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_CreateSchedule_RequestSyntax) **   <a name="scheduler-CreateSchedule-request-uri-Name"></a>
The name of the schedule that you are creating.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`
Required: Yes

## Request Body
<a name="API_CreateSchedule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ActionAfterCompletion](#API_CreateSchedule_RequestSyntax) **   <a name="scheduler-CreateSchedule-request-ActionAfterCompletion"></a>
Specifies the action that EventBridge Scheduler applies to the schedule after the schedule completes invoking the target.
Type: String
Valid Values: `NONE | DELETE`
Required: No

 ** [ClientToken](#API_CreateSchedule_RequestSyntax) **   <a name="scheduler-CreateSchedule-request-ClientToken"></a>
 Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** [Description](#API_CreateSchedule_RequestSyntax) **   <a name="scheduler-CreateSchedule-request-Description"></a>
The description you specify for the schedule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** [EndDate](#API_CreateSchedule_RequestSyntax) **   <a name="scheduler-CreateSchedule-request-EndDate"></a>
The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the `EndDate` you specify. EventBridge Scheduler ignores `EndDate` for one-time schedules.
Type: Timestamp
Required: No

 ** [FlexibleTimeWindow](#API_CreateSchedule_RequestSyntax) **   <a name="scheduler-CreateSchedule-request-FlexibleTimeWindow"></a>
Allows you to configure a time window during which EventBridge Scheduler invokes the schedule.
Type: [FlexibleTimeWindow](API_FlexibleTimeWindow.md) object
Required: Yes

 ** [GroupName](#API_CreateSchedule_RequestSyntax) **   <a name="scheduler-CreateSchedule-request-GroupName"></a>
The name of the schedule group to associate with this schedule. If you omit this, the default schedule group is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`
Required: No

 ** [KmsKeyArn](#API_CreateSchedule_RequestSyntax) **   <a name="scheduler-CreateSchedule-request-KmsKeyArn"></a>
The Amazon Resource Name (ARN) for the customer managed KMS key that EventBridge Scheduler will use to encrypt and decrypt your data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]+)?:kms:[a-z0-9\-]+:\d{12}:(key|alias)\/[0-9a-zA-Z-_]*`
Required: No

 ** [ScheduleExpression](#API_CreateSchedule_RequestSyntax) **   <a name="scheduler-CreateSchedule-request-ScheduleExpression"></a>
 The expression that defines when the schedule runs. The following formats are supported.
+  `at` expression - `at(yyyy-mm-ddThh:mm:ss)`
+  `rate` expression - `rate(value unit)`
+  `cron` expression - `cron(fields)`
 You can use `at` expressions to create one-time schedules that invoke a target once, at the time and in the time zone, that you specify. You can use `rate` and `cron` expressions to create recurring schedules. Rate-based schedules are useful when you want to invoke a target at regular intervals, such as every 15 minutes or every five days. Cron-based schedules are useful when you want to invoke a target periodically at a specific time, such as at 8:00 am (UTC\+0) every 1st day of the month.
 A `cron` expression consists of six fields separated by white spaces: `(minutes hours day_of_month month day_of_week year)`.
 A `rate` expression consists of a *value* as a positive integer, and a *unit* with the following options: `minute` \| `minutes` \| `hour` \| `hours` \| `day` \| `days`
 For more information and examples, see [Schedule types on EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html) in the *EventBridge Scheduler User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [ScheduleExpressionTimezone](#API_CreateSchedule_RequestSyntax) **   <a name="scheduler-CreateSchedule-request-ScheduleExpressionTimezone"></a>
The timezone in which the scheduling expression is evaluated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** [StartDate](#API_CreateSchedule_RequestSyntax) **   <a name="scheduler-CreateSchedule-request-StartDate"></a>
The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the `StartDate` you specify. EventBridge Scheduler ignores `StartDate` for one-time schedules.
Type: Timestamp
Required: No

 ** [State](#API_CreateSchedule_RequestSyntax) **   <a name="scheduler-CreateSchedule-request-State"></a>
Specifies whether the schedule is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [Target](#API_CreateSchedule_RequestSyntax) **   <a name="scheduler-CreateSchedule-request-Target"></a>
The schedule's target.
Type: [Target](API_Target.md) object
Required: Yes

## Response Syntax
<a name="API_CreateSchedule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ScheduleArn": "string"
}
```

## Response Elements
<a name="API_CreateSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ScheduleArn](#API_CreateSchedule_ResponseSyntax) **   <a name="scheduler-CreateSchedule-response-ScheduleArn"></a>
The Amazon Resource Name (ARN) of the schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]+)?:scheduler:[a-z0-9\-]+:\d{12}:schedule\/[0-9a-zA-Z-_.]+\/[0-9a-zA-Z-_.]+`

## Errors
<a name="API_CreateSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting the resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error encountered while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/scheduler-2021-06-30/CreateSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/scheduler-2021-06-30/CreateSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/CreateSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/scheduler-2021-06-30/CreateSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/CreateSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/scheduler-2021-06-30/CreateSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/scheduler-2021-06-30/CreateSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/scheduler-2021-06-30/CreateSchedule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/scheduler-2021-06-30/CreateSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/CreateSchedule)
