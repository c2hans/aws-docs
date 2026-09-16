---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateMaintenanceWindow.html
---

# CreateMaintenanceWindow
<a name="API_CreateMaintenanceWindow"></a>

Creates a new maintenance window.

**Note**
The value you specify for `Duration` determines the specific end time for the maintenance window based on the time it begins. No maintenance window tasks are permitted to start after the resulting endtime minus the number of hours you specify for `Cutoff`. For example, if the maintenance window starts at 3 PM, the duration is three hours, and the value you specify for `Cutoff` is one hour, no maintenance window tasks can start after 5 PM.

## Request Syntax
<a name="API_CreateMaintenanceWindow_RequestSyntax"></a>

```
{
   "AllowUnassociatedTargets": {{boolean}},
   "ClientToken": "{{string}}",
   "Cutoff": {{number}},
   "Description": "{{string}}",
   "Duration": {{number}},
   "EndDate": "{{string}}",
   "Name": "{{string}}",
   "Schedule": "{{string}}",
   "ScheduleOffset": {{number}},
   "ScheduleTimezone": "{{string}}",
   "StartDate": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateMaintenanceWindow_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AllowUnassociatedTargets](#API_CreateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-CreateMaintenanceWindow-request-AllowUnassociatedTargets"></a>
Enables a maintenance window task to run on managed nodes, even if you haven't registered those nodes as targets. If enabled, then you must specify the unregistered managed nodes (by node ID) when you register a task with the maintenance window.
If you don't enable this option, then you must specify previously-registered targets when you register a task with the maintenance window.
Type: Boolean
Required: Yes

 ** [ClientToken](#API_CreateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-CreateMaintenanceWindow-request-ClientToken"></a>
User-provided idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [Cutoff](#API_CreateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-CreateMaintenanceWindow-request-Cutoff"></a>
The number of hours before the end of the maintenance window that AWS Systems Manager stops scheduling new tasks for execution.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 23.
Required: Yes

 ** [Description](#API_CreateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-CreateMaintenanceWindow-request-Description"></a>
An optional description for the maintenance window. We recommend specifying a description to help you organize your maintenance windows.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Duration](#API_CreateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-CreateMaintenanceWindow-request-Duration"></a>
The duration of the maintenance window in hours.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 24.
Required: Yes

 ** [EndDate](#API_CreateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-CreateMaintenanceWindow-request-EndDate"></a>
The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become inactive. `EndDate` allows you to set a date and time in the future when the maintenance window will no longer run.
Type: String
Required: No

 ** [Name](#API_CreateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-CreateMaintenanceWindow-request-Name"></a>
The name of the maintenance window.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: Yes

 ** [Schedule](#API_CreateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-CreateMaintenanceWindow-request-Schedule"></a>
The schedule of the maintenance window in the form of a cron or rate expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [ScheduleOffset](#API_CreateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-CreateMaintenanceWindow-request-ScheduleOffset"></a>
The number of days to wait after the date and time specified by a cron expression before running the maintenance window.
For example, the following cron expression schedules a maintenance window to run on the third Tuesday of every month at 11:30 PM.
 `cron(30 23 ? * TUE#3 *)`
If the schedule offset is `2`, the maintenance window won't run until two days later.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 6.
Required: No

 ** [ScheduleTimezone](#API_CreateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-CreateMaintenanceWindow-request-ScheduleTimezone"></a>
The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los\_Angeles", "UTC", or "Asia/Seoul". For more information, see the [Time Zone Database](https://www.iana.org/time-zones) on the IANA website.
Type: String
Required: No

 ** [StartDate](#API_CreateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-CreateMaintenanceWindow-request-StartDate"></a>
The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become active. `StartDate` allows you to delay activation of the maintenance window until the specified future date.
When using a rate schedule, if you provide a start date that occurs in the past, the current date and time are used as the start date.
Type: String
Required: No

 ** [Tags](#API_CreateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-CreateMaintenanceWindow-request-Tags"></a>
Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a maintenance window to identify the type of tasks it will run, the types of targets, and the environment it will run in. In this case, you could specify the following key-value pairs:
+  `Key=TaskType,Value=AgentUpdate`
+  `Key=OS,Value=Windows`
+  `Key=Environment,Value=Production`
To add tags to an existing maintenance window, use the [AddTagsToResource](API_AddTagsToResource.md) operation.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: No

## Response Syntax
<a name="API_CreateMaintenanceWindow_ResponseSyntax"></a>

```
{
   "WindowId": "string"
}
```

## Response Elements
<a name="API_CreateMaintenanceWindow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WindowId](#API_CreateMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-CreateMaintenanceWindow-response-WindowId"></a>
The ID of the created maintenance window.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`

## Errors
<a name="API_CreateMaintenanceWindow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IdempotentParameterMismatch **
Error returned when an idempotent operation is retried and the parameters don't match the original call to the API with the same idempotency token.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceLimitExceededException **
Error returned when the caller has exceeded the default resource quotas. For example, too many maintenance windows or patch baselines have been created.
For information about resource quotas in Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

## Examples
<a name="API_CreateMaintenanceWindow_Examples"></a>

### Example
<a name="API_CreateMaintenanceWindow_Example_1"></a>

This example illustrates one usage of CreateMaintenanceWindow.

#### Sample Request
<a name="API_CreateMaintenanceWindow_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 186
X-Amz-Target: AmazonSSM.CreateMaintenanceWindow
X-Amz-Date: 20240312T201809Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240312/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "Name": "My-Development-Maintenance-Window",
    "Cutoff": 2,
    "Schedule": "cron(0 12 ? * WED *)",
    "AllowUnassociatedTargets": true,
    "Duration": 6,
    "Tags": [
        {
            "Key": "Environment",
            "Value": "Development"
        }
    ],
    "ClientToken": "aa1b2cde-27e3-42ff-9cac-99380EXAMPLE"
}
```

#### Sample Response
<a name="API_CreateMaintenanceWindow_Example_1_Response"></a>

```
{
    "WindowId": "mw-0c50858d01EXAMPLE"
}
```

## See Also
<a name="API_CreateMaintenanceWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/CreateMaintenanceWindow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/CreateMaintenanceWindow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CreateMaintenanceWindow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/CreateMaintenanceWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CreateMaintenanceWindow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/CreateMaintenanceWindow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/CreateMaintenanceWindow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/CreateMaintenanceWindow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/CreateMaintenanceWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CreateMaintenanceWindow)
