---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateMaintenanceWindow.html
---

# UpdateMaintenanceWindow
<a name="API_UpdateMaintenanceWindow"></a>

Updates an existing maintenance window. Only specified parameters are modified.

**Note**
The value you specify for `Duration` determines the specific end time for the maintenance window based on the time it begins. No maintenance window tasks are permitted to start after the resulting endtime minus the number of hours you specify for `Cutoff`. For example, if the maintenance window starts at 3 PM, the duration is three hours, and the value you specify for `Cutoff` is one hour, no maintenance window tasks can start after 5 PM.

## Request Syntax
<a name="API_UpdateMaintenanceWindow_RequestSyntax"></a>

```
{
   "AllowUnassociatedTargets": {{boolean}},
   "Cutoff": {{number}},
   "Description": "{{string}}",
   "Duration": {{number}},
   "Enabled": {{boolean}},
   "EndDate": "{{string}}",
   "Name": "{{string}}",
   "Replace": {{boolean}},
   "Schedule": "{{string}}",
   "ScheduleOffset": {{number}},
   "ScheduleTimezone": "{{string}}",
   "StartDate": "{{string}}",
   "WindowId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateMaintenanceWindow_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AllowUnassociatedTargets](#API_UpdateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-request-AllowUnassociatedTargets"></a>
Whether targets must be registered with the maintenance window before tasks can be defined for those targets.
Type: Boolean
Required: No

 ** [Cutoff](#API_UpdateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-request-Cutoff"></a>
The number of hours before the end of the maintenance window that AWS Systems Manager stops scheduling new tasks for execution.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 23.
Required: No

 ** [Description](#API_UpdateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-request-Description"></a>
An optional description for the update request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Duration](#API_UpdateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-request-Duration"></a>
The duration of the maintenance window in hours.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 24.
Required: No

 ** [Enabled](#API_UpdateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-request-Enabled"></a>
Whether the maintenance window is enabled.
Type: Boolean
Required: No

 ** [EndDate](#API_UpdateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-request-EndDate"></a>
The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become inactive. `EndDate` allows you to set a date and time in the future when the maintenance window will no longer run.
Type: String
Required: No

 ** [Name](#API_UpdateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-request-Name"></a>
The name of the maintenance window.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** [Replace](#API_UpdateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-request-Replace"></a>
If `True`, then all fields that are required by the [CreateMaintenanceWindow](API_CreateMaintenanceWindow.md) operation are also required for this API request. Optional fields that aren't specified are set to null.
Type: Boolean
Required: No

 ** [Schedule](#API_UpdateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-request-Schedule"></a>
The schedule of the maintenance window in the form of a cron or rate expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [ScheduleOffset](#API_UpdateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-request-ScheduleOffset"></a>
The number of days to wait after the date and time specified by a cron expression before running the maintenance window.
For example, the following cron expression schedules a maintenance window to run the third Tuesday of every month at 11:30 PM.
 `cron(30 23 ? * TUE#3 *)`
If the schedule offset is `2`, the maintenance window won't run until two days later.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 6.
Required: No

 ** [ScheduleTimezone](#API_UpdateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-request-ScheduleTimezone"></a>
The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los\_Angeles", "UTC", or "Asia/Seoul". For more information, see the [Time Zone Database](https://www.iana.org/time-zones) on the IANA website.
Type: String
Required: No

 ** [StartDate](#API_UpdateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-request-StartDate"></a>
The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become active. `StartDate` allows you to delay activation of the maintenance window until the specified future date.
When using a rate schedule, if you provide a start date that occurs in the past, the current date and time are used as the start date.
Type: String
Required: No

 ** [WindowId](#API_UpdateMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-request-WindowId"></a>
The ID of the maintenance window to update.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: Yes

## Response Syntax
<a name="API_UpdateMaintenanceWindow_ResponseSyntax"></a>

```
{
   "AllowUnassociatedTargets": boolean,
   "Cutoff": number,
   "Description": "string",
   "Duration": number,
   "Enabled": boolean,
   "EndDate": "string",
   "Name": "string",
   "Schedule": "string",
   "ScheduleOffset": number,
   "ScheduleTimezone": "string",
   "StartDate": "string",
   "WindowId": "string"
}
```

## Response Elements
<a name="API_UpdateMaintenanceWindow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AllowUnassociatedTargets](#API_UpdateMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-response-AllowUnassociatedTargets"></a>
Whether targets must be registered with the maintenance window before tasks can be defined for those targets.
Type: Boolean

 ** [Cutoff](#API_UpdateMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-response-Cutoff"></a>
The number of hours before the end of the maintenance window that AWS Systems Manager stops scheduling new tasks for execution.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 23.

 ** [Description](#API_UpdateMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-response-Description"></a>
An optional description of the update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [Duration](#API_UpdateMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-response-Duration"></a>
The duration of the maintenance window in hours.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 24.

 ** [Enabled](#API_UpdateMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-response-Enabled"></a>
Whether the maintenance window is enabled.
Type: Boolean

 ** [EndDate](#API_UpdateMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-response-EndDate"></a>
The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive. The maintenance window won't run after this specified time.
Type: String

 ** [Name](#API_UpdateMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-response-Name"></a>
The name of the maintenance window.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`

 ** [Schedule](#API_UpdateMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-response-Schedule"></a>
The schedule of the maintenance window in the form of a cron or rate expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ScheduleOffset](#API_UpdateMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-response-ScheduleOffset"></a>
The number of days to wait to run a maintenance window after the scheduled cron expression date and time.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 6.

 ** [ScheduleTimezone](#API_UpdateMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-response-ScheduleTimezone"></a>
The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los\_Angeles", "UTC", or "Asia/Seoul". For more information, see the [Time Zone Database](https://www.iana.org/time-zones) on the IANA website.
Type: String

 ** [StartDate](#API_UpdateMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-response-StartDate"></a>
The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active. The maintenance window won't run before this specified time.
Type: String

 ** [WindowId](#API_UpdateMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindow-response-WindowId"></a>
The ID of the created maintenance window.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`

## Errors
<a name="API_UpdateMaintenanceWindow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_UpdateMaintenanceWindow_Examples"></a>

### Example
<a name="API_UpdateMaintenanceWindow_Example_1"></a>

This example illustrates one usage of UpdateMaintenanceWindow.

#### Sample Request
<a name="API_UpdateMaintenanceWindow_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 160
X-Amz-Target: AmazonSSM.UpdateMaintenanceWindow
X-Amz-Date: 20240312T203703Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240312/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "Duration": 10,
    "WindowId": "mw-0c50858d01EXAMPLE",
    "Name": "Default-Maintenance-Window",
    "Description": "Standard maintenance windows for production servers"
}
```

#### Sample Response
<a name="API_UpdateMaintenanceWindow_Example_1_Response"></a>

```
{
    "AllowUnassociatedTargets": true,
    "Cutoff": 4,
    "Description": "Standard maintenance windows for production servers",
    "Duration": 10,
    "Enabled": true,
    "Name": "Default-Maintenance-Window",
    "Schedule": "rate(3 minutes)",
    "WindowId": "mw-0c50858d01EXAMPLE"
}
```

## See Also
<a name="API_UpdateMaintenanceWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/UpdateMaintenanceWindow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/UpdateMaintenanceWindow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/UpdateMaintenanceWindow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/UpdateMaintenanceWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UpdateMaintenanceWindow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/UpdateMaintenanceWindow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/UpdateMaintenanceWindow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/UpdateMaintenanceWindow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UpdateMaintenanceWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/UpdateMaintenanceWindow)
