---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetMaintenanceWindow.html
---

# GetMaintenanceWindow
<a name="API_GetMaintenanceWindow"></a>

Retrieves a maintenance window.

## Request Syntax
<a name="API_GetMaintenanceWindow_RequestSyntax"></a>

```
{
   "WindowId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMaintenanceWindow_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WindowId](#API_GetMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-request-WindowId"></a>
The ID of the maintenance window for which you want to retrieve information.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: Yes

## Response Syntax
<a name="API_GetMaintenanceWindow_ResponseSyntax"></a>

```
{
   "AllowUnassociatedTargets": boolean,
   "CreatedDate": number,
   "Cutoff": number,
   "Description": "string",
   "Duration": number,
   "Enabled": boolean,
   "EndDate": "string",
   "ModifiedDate": number,
   "Name": "string",
   "NextExecutionTime": "string",
   "Schedule": "string",
   "ScheduleOffset": number,
   "ScheduleTimezone": "string",
   "StartDate": "string",
   "WindowId": "string"
}
```

## Response Elements
<a name="API_GetMaintenanceWindow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AllowUnassociatedTargets](#API_GetMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-response-AllowUnassociatedTargets"></a>
Whether targets must be registered with the maintenance window before tasks can be defined for those targets.
Type: Boolean

 ** [CreatedDate](#API_GetMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-response-CreatedDate"></a>
The date the maintenance window was created.
Type: Timestamp

 ** [Cutoff](#API_GetMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-response-Cutoff"></a>
The number of hours before the end of the maintenance window that AWS Systems Manager stops scheduling new tasks for execution.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 23.

 ** [Description](#API_GetMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-response-Description"></a>
The description of the maintenance window.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [Duration](#API_GetMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-response-Duration"></a>
The duration of the maintenance window in hours.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 24.

 ** [Enabled](#API_GetMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-response-Enabled"></a>
Indicates whether the maintenance window is enabled.
Type: Boolean

 ** [EndDate](#API_GetMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-response-EndDate"></a>
The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive. The maintenance window won't run after this specified time.
Type: String

 ** [ModifiedDate](#API_GetMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-response-ModifiedDate"></a>
The date the maintenance window was last modified.
Type: Timestamp

 ** [Name](#API_GetMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-response-Name"></a>
The name of the maintenance window.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`

 ** [NextExecutionTime](#API_GetMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-response-NextExecutionTime"></a>
The next time the maintenance window will actually run, taking into account any specified times for the maintenance window to become active or inactive.
Type: String

 ** [Schedule](#API_GetMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-response-Schedule"></a>
The schedule of the maintenance window in the form of a cron or rate expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ScheduleOffset](#API_GetMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-response-ScheduleOffset"></a>
The number of days to wait to run a maintenance window after the scheduled cron expression date and time.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 6.

 ** [ScheduleTimezone](#API_GetMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-response-ScheduleTimezone"></a>
The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los\_Angeles", "UTC", or "Asia/Seoul". For more information, see the [Time Zone Database](https://www.iana.org/time-zones) on the IANA website.
Type: String

 ** [StartDate](#API_GetMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-response-StartDate"></a>
The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active. The maintenance window won't run before this specified time.
Type: String

 ** [WindowId](#API_GetMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-GetMaintenanceWindow-response-WindowId"></a>
The ID of the created maintenance window.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`

## Errors
<a name="API_GetMaintenanceWindow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_GetMaintenanceWindow_Examples"></a>

### Example
<a name="API_GetMaintenanceWindow_Example_1"></a>

This example illustrates one usage of GetMaintenanceWindow.

#### Sample Request
<a name="API_GetMaintenanceWindow_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 36
X-Amz-Target: AmazonSSM.GetMaintenanceWindow
X-Amz-Date: 20240312T203140Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240312/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "WindowId": "mw-0c50858d01EXAMPLE"
}
```

#### Sample Response
<a name="API_GetMaintenanceWindow_Example_1_Response"></a>

```
{
    "AllowUnassociatedTargets": true,
    "CreatedDate": 1515006912.957,
    "Cutoff": 1,
    "Duration": 6,
    "Enabled": true,
    "ModifiedDate": "2024-01-01T10:04:04.099Z",
    "Name": "My-Maintenance-Window",
    "Schedule": "rate(3 days)",
    "WindowId": "mw-0c50858d01EXAMPLE",
    "NextExecutionTime": "2024-02-25T00:08:15.099Z"
}
```

## See Also
<a name="API_GetMaintenanceWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetMaintenanceWindow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetMaintenanceWindow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetMaintenanceWindow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetMaintenanceWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetMaintenanceWindow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetMaintenanceWindow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetMaintenanceWindow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetMaintenanceWindow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetMaintenanceWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetMaintenanceWindow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
