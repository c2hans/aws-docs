---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_GetSchedule.html
---

# GetSchedule
<a name="API_GetSchedule"></a>

Retrieves the specified schedule.

## Request Syntax
<a name="API_GetSchedule_RequestSyntax"></a>

```
GET /schedules/{{Name}}?groupName={{GroupName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSchedule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [GroupName](#API_GetSchedule_RequestSyntax) **   <a name="scheduler-GetSchedule-request-uri-GroupName"></a>
The name of the schedule group associated with this schedule. If you omit this, EventBridge Scheduler assumes that the schedule is associated with the default group.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`

 ** [Name](#API_GetSchedule_RequestSyntax) **   <a name="scheduler-GetSchedule-request-uri-Name"></a>
The name of the schedule to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`
Required: Yes

## Request Body
<a name="API_GetSchedule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSchedule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ActionAfterCompletion": "string",
   "Arn": "string",
   "CreationDate": number,
   "Description": "string",
   "EndDate": number,
   "FlexibleTimeWindow": {
      "MaximumWindowInMinutes": number,
      "Mode": "string"
   },
   "GroupName": "string",
   "KmsKeyArn": "string",
   "LastModificationDate": number,
   "Name": "string",
   "ScheduleExpression": "string",
   "ScheduleExpressionTimezone": "string",
   "StartDate": number,
   "State": "string",
   "Target": {
      "Arn": "string",
      "DeadLetterConfig": {
         "Arn": "string"
      },
      "EcsParameters": {
         "CapacityProviderStrategy": [
            {
               "base": number,
               "capacityProvider": "string",
               "weight": number
            }
         ],
         "EnableECSManagedTags": boolean,
         "EnableExecuteCommand": boolean,
         "Group": "string",
         "LaunchType": "string",
         "NetworkConfiguration": {
            "awsvpcConfiguration": {
               "AssignPublicIp": "string",
               "SecurityGroups": [ "string" ],
               "Subnets": [ "string" ]
            }
         },
         "PlacementConstraints": [
            {
               "expression": "string",
               "type": "string"
            }
         ],
         "PlacementStrategy": [
            {
               "field": "string",
               "type": "string"
            }
         ],
         "PlatformVersion": "string",
         "PropagateTags": "string",
         "ReferenceId": "string",
         "Tags": [
            {
               "string" : "string"
            }
         ],
         "TaskCount": number,
         "TaskDefinitionArn": "string"
      },
      "EventBridgeParameters": {
         "DetailType": "string",
         "Source": "string"
      },
      "Input": "string",
      "KinesisParameters": {
         "PartitionKey": "string"
      },
      "RetryPolicy": {
         "MaximumEventAgeInSeconds": number,
         "MaximumRetryAttempts": number
      },
      "RoleArn": "string",
      "SageMakerPipelineParameters": {
         "PipelineParameterList": [
            {
               "Name": "string",
               "Value": "string"
            }
         ]
      },
      "SqsParameters": {
         "MessageGroupId": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActionAfterCompletion](#API_GetSchedule_ResponseSyntax) **   <a name="scheduler-GetSchedule-response-ActionAfterCompletion"></a>
Indicates the action that EventBridge Scheduler applies to the schedule after the schedule completes invoking the target.
Type: String
Valid Values: `NONE | DELETE`

 ** [Arn](#API_GetSchedule_ResponseSyntax) **   <a name="scheduler-GetSchedule-response-Arn"></a>
The Amazon Resource Name (ARN) of the schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]+)?:scheduler:[a-z0-9\-]+:\d{12}:schedule\/[0-9a-zA-Z-_.]+\/[0-9a-zA-Z-_.]+`

 ** [CreationDate](#API_GetSchedule_ResponseSyntax) **   <a name="scheduler-GetSchedule-response-CreationDate"></a>
The time at which the schedule was created.
Type: Timestamp

 ** [Description](#API_GetSchedule_ResponseSyntax) **   <a name="scheduler-GetSchedule-response-Description"></a>
The description of the schedule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.

 ** [EndDate](#API_GetSchedule_ResponseSyntax) **   <a name="scheduler-GetSchedule-response-EndDate"></a>
The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the `EndDate` you specify. EventBridge Scheduler ignores `EndDate` for one-time schedules.
Type: Timestamp

 ** [FlexibleTimeWindow](#API_GetSchedule_ResponseSyntax) **   <a name="scheduler-GetSchedule-response-FlexibleTimeWindow"></a>
Allows you to configure a time window during which EventBridge Scheduler invokes the schedule.
Type: [FlexibleTimeWindow](API_FlexibleTimeWindow.md) object

 ** [GroupName](#API_GetSchedule_ResponseSyntax) **   <a name="scheduler-GetSchedule-response-GroupName"></a>
The name of the schedule group associated with this schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`

 ** [KmsKeyArn](#API_GetSchedule_ResponseSyntax) **   <a name="scheduler-GetSchedule-response-KmsKeyArn"></a>
The ARN for a customer managed KMS Key that is be used to encrypt and decrypt your data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]+)?:kms:[a-z0-9\-]+:\d{12}:(key|alias)\/[0-9a-zA-Z-_]*`

 ** [LastModificationDate](#API_GetSchedule_ResponseSyntax) **   <a name="scheduler-GetSchedule-response-LastModificationDate"></a>
The time at which the schedule was last modified.
Type: Timestamp

 ** [Name](#API_GetSchedule_ResponseSyntax) **   <a name="scheduler-GetSchedule-response-Name"></a>
The name of the schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-_.]+`

 ** [ScheduleExpression](#API_GetSchedule_ResponseSyntax) **   <a name="scheduler-GetSchedule-response-ScheduleExpression"></a>
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

 ** [ScheduleExpressionTimezone](#API_GetSchedule_ResponseSyntax) **   <a name="scheduler-GetSchedule-response-ScheduleExpressionTimezone"></a>
The timezone in which the scheduling expression is evaluated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.

 ** [StartDate](#API_GetSchedule_ResponseSyntax) **   <a name="scheduler-GetSchedule-response-StartDate"></a>
The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the `StartDate` you specify. EventBridge Scheduler ignores `StartDate` for one-time schedules.
Type: Timestamp

 ** [State](#API_GetSchedule_ResponseSyntax) **   <a name="scheduler-GetSchedule-response-State"></a>
Specifies whether the schedule is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [Target](#API_GetSchedule_ResponseSyntax) **   <a name="scheduler-GetSchedule-response-Target"></a>
The schedule target.
Type: [Target](API_Target.md) object

## Errors
<a name="API_GetSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Unexpected error encountered while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource which does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/scheduler-2021-06-30/GetSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/scheduler-2021-06-30/GetSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/GetSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/scheduler-2021-06-30/GetSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/GetSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/scheduler-2021-06-30/GetSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/scheduler-2021-06-30/GetSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/scheduler-2021-06-30/GetSchedule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/scheduler-2021-06-30/GetSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/GetSchedule)
