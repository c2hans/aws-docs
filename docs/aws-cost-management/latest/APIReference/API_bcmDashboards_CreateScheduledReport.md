---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_CreateScheduledReport.html
---

# CreateScheduledReport
<a name="API_bcmDashboards_CreateScheduledReport"></a>

Creates a new scheduled report for a dashboard. A scheduled report automatically generates and delivers dashboard snapshots on a recurring schedule.

## Request Syntax
<a name="API_bcmDashboards_CreateScheduledReport_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "resourceTags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "scheduledReport": {
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
}
```

## Request Parameters
<a name="API_bcmDashboards_CreateScheduledReport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_bcmDashboards_CreateScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_CreateScheduledReport-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\u0021-\u007E]+`
Required: No

 ** [resourceTags](#API_bcmDashboards_CreateScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_CreateScheduledReport-request-resourceTags"></a>
The tags to apply to the scheduled report resource for organization and management.
Type: Array of [ResourceTag](API_bcmDashboards_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [scheduledReport](#API_bcmDashboards_CreateScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_CreateScheduledReport-request-scheduledReport"></a>
The configuration for the scheduled report, including the dashboard to report on, the schedule, and the execution role that the service will use to generate the dashboard snapshot.
Type: [ScheduledReportInput](API_bcmDashboards_ScheduledReportInput.md) object
Required: Yes

## Response Syntax
<a name="API_bcmDashboards_CreateScheduledReport_ResponseSyntax"></a>

```
{
   "arn": "string"
}
```

## Response Elements
<a name="API_bcmDashboards_CreateScheduledReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_bcmDashboards_CreateScheduledReport_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_CreateScheduledReport-response-arn"></a>
The ARN of the newly created scheduled report.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:scheduled-report/(\*|[-a-z0-9]+)`

## Errors
<a name="API_bcmDashboards_CreateScheduledReport_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would exceed a service quota. Review the service quotas for AWS Billing and Cost Management Dashboards and retry your request.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling. Reduce the frequency of requests and use exponential backoff.
HTTP Status Code: 400

 ** ValidationException **
The input parameters do not satisfy the requirements. Check the error message for specific validation details.
HTTP Status Code: 400

## Examples
<a name="API_bcmDashboards_CreateScheduledReport_Examples"></a>

### To create a scheduled report
<a name="API_bcmDashboards_CreateScheduledReport_Example_1"></a>

The following example creates a scheduled report that runs every Monday at 8:00 AM Pacific Time.

```
{
    "scheduledReport": {
        "name": "weekly-cost-report",
        "dashboardArn": "arn:aws:bcm-dashboards::123456789012:dashboard/cost-dashboard-1",
        "scheduledReportExecutionRoleArn": "arn:aws:iam::123456789012:role/BCMDashboardsScheduledReportRole",
        "scheduleConfig": {
            "scheduleExpression": "cron(0 8 ? * MON *)",
            "scheduleExpressionTimeZone": "America/Los_Angeles",
            "schedulePeriod": {
                "startTime": "2026-04-01T00:00:00Z"
            },
            "state": "ENABLED"
        }
    }
}
```

## See Also
<a name="API_bcmDashboards_CreateScheduledReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-dashboards-2025-08-18/CreateScheduledReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-dashboards-2025-08-18/CreateScheduledReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/CreateScheduledReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-dashboards-2025-08-18/CreateScheduledReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/CreateScheduledReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-dashboards-2025-08-18/CreateScheduledReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-dashboards-2025-08-18/CreateScheduledReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-dashboards-2025-08-18/CreateScheduledReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-dashboards-2025-08-18/CreateScheduledReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/CreateScheduledReport)
