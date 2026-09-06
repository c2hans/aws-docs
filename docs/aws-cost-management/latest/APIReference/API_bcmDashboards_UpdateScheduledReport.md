---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_UpdateScheduledReport.html
---

# UpdateScheduledReport
<a name="API_bcmDashboards_UpdateScheduledReport"></a>

Updates an existing scheduled report's properties, including its name, description, schedule configuration, and widget settings. Only the parameters included in the request are updated; all other properties remain unchanged.

## Request Syntax
<a name="API_bcmDashboards_UpdateScheduledReport_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "clearWidgetDateRangeOverride": {{boolean}},
   "clearWidgetIds": {{boolean}},
   "dashboardArn": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "scheduleConfig": {
      "scheduleExpression": "{{string}}",
      "scheduleExpressionTimeZone": "{{string}}",
      "schedulePeriod": {
         "endTime": {{number}},
         "startTime": {{number}}
      },
      "state": "{{string}}"
   },
   "scheduledReportExecutionRoleArn": "{{string}}",
   "widgetDateRangeOverride": {
      "endTime": {
         "type": "{{string}}",
         "value": "{{string}}"
      },
      "startTime": {
         "type": "{{string}}",
         "value": "{{string}}"
      }
   },
   "widgetIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_bcmDashboards_UpdateScheduledReport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_bcmDashboards_UpdateScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateScheduledReport-request-arn"></a>
The ARN of the scheduled report to update.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:scheduled-report/(\*|[-a-z0-9]+)`
Required: Yes

 ** [clearWidgetDateRangeOverride](#API_bcmDashboards_UpdateScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateScheduledReport-request-clearWidgetDateRangeOverride"></a>
Set to `true` to clear the existing date range override from the scheduled report.
Type: Boolean
Required: No

 ** [clearWidgetIds](#API_bcmDashboards_UpdateScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateScheduledReport-request-clearWidgetIds"></a>
Set to `true` to clear existing widget IDs from the scheduled report.
Type: Boolean
Required: No

 ** [dashboardArn](#API_bcmDashboards_UpdateScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateScheduledReport-request-dashboardArn"></a>
The ARN of the dashboard to associate with the scheduled report.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:dashboard/(\*|[-a-z0-9]+)`
Required: No

 ** [description](#API_bcmDashboards_UpdateScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateScheduledReport-request-description"></a>
The new description for the scheduled report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!.* {2})[ a-zA-Z0-9.,!?;:@#$%&\-_/\\]*`
Required: No

 ** [name](#API_bcmDashboards_UpdateScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateScheduledReport-request-name"></a>
The new name for the scheduled report.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `(?!.* {2})[a-zA-Z][a-zA-Z0-9 _-]{0,48}[a-zA-Z0-9_-]`
Required: No

 ** [scheduleConfig](#API_bcmDashboards_UpdateScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateScheduledReport-request-scheduleConfig"></a>
The updated schedule configuration for the report.
Type: [ScheduleConfig](API_bcmDashboards_ScheduleConfig.md) object
Required: No

 ** [scheduledReportExecutionRoleArn](#API_bcmDashboards_UpdateScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateScheduledReport-request-scheduledReportExecutionRoleArn"></a>
The ARN of the IAM role that the scheduled report uses to execute. AWS Billing and Cost Management Dashboards will assume this IAM role while executing the scheduled report.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:iam::[0-9]{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: No

 ** [widgetDateRangeOverride](#API_bcmDashboards_UpdateScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateScheduledReport-request-widgetDateRangeOverride"></a>
The date range override to apply to widgets in the scheduled report.
Type: [DateTimeRange](API_bcmDashboards_DateTimeRange.md) object
Required: No

 ** [widgetIds](#API_bcmDashboards_UpdateScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateScheduledReport-request-widgetIds"></a>
The list of widget identifiers to include in the scheduled report. If not specified, all widgets in the dashboard are included.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## Response Syntax
<a name="API_bcmDashboards_UpdateScheduledReport_ResponseSyntax"></a>

```
{
   "arn": "string"
}
```

## Response Elements
<a name="API_bcmDashboards_UpdateScheduledReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_bcmDashboards_UpdateScheduledReport_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateScheduledReport-response-arn"></a>
The ARN of the updated scheduled report.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:scheduled-report/(\*|[-a-z0-9]+)`

## Errors
<a name="API_bcmDashboards_UpdateScheduledReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action. Verify your IAM permissions and any resource policies.
HTTP Status Code: 400

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource. For example, attempting to create a resource that already exists or is being created.
HTTP Status Code: 400

 ** InternalServerException **
An internal error occurred while processing the request. Retry your request. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource (dashboard, policy, or widget) was not found. Verify the ARN and try again.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling. Reduce the frequency of requests and use exponential backoff.
HTTP Status Code: 400

 ** ValidationException **
The input parameters do not satisfy the requirements. Check the error message for specific validation details.
HTTP Status Code: 400

## Examples
<a name="API_bcmDashboards_UpdateScheduledReport_Examples"></a>

### To update a scheduled report
<a name="API_bcmDashboards_UpdateScheduledReport_Example_1"></a>

The following example updates the name and schedule of a scheduled report.

```
{
    "arn": "arn:aws:bcm-dashboards::123456789012:scheduled-report/report-1",
    "name": "daily-cost-report",
    "scheduleConfig": {
        "scheduleExpression": "cron(0 8 * * ? *)",
        "scheduleExpressionTimeZone": "America/Los_Angeles",
        "schedulePeriod": {
            "startTime": "2026-04-01T00:00:00Z"
        },
        "state": "ENABLED"
    }
}
```

## See Also
<a name="API_bcmDashboards_UpdateScheduledReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-dashboards-2025-08-18/UpdateScheduledReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-dashboards-2025-08-18/UpdateScheduledReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/UpdateScheduledReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-dashboards-2025-08-18/UpdateScheduledReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/UpdateScheduledReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-dashboards-2025-08-18/UpdateScheduledReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-dashboards-2025-08-18/UpdateScheduledReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-dashboards-2025-08-18/UpdateScheduledReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-dashboards-2025-08-18/UpdateScheduledReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/UpdateScheduledReport)
