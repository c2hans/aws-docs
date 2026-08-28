---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_GetScheduledReport.html
---

# GetScheduledReport
<a name="API_bcmDashboards_GetScheduledReport"></a>

Retrieves the configuration and metadata of a specified scheduled report.

## Request Syntax
<a name="API_bcmDashboards_GetScheduledReport_RequestSyntax"></a>

```
{
   "arn": "{{string}}"
}
```

## Request Parameters
<a name="API_bcmDashboards_GetScheduledReport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_bcmDashboards_GetScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_GetScheduledReport-request-arn"></a>
The ARN of the scheduled report to retrieve.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:scheduled-report/(\*|[-a-z0-9]+)`
Required: Yes

## Response Syntax
<a name="API_bcmDashboards_GetScheduledReport_ResponseSyntax"></a>

```
{
   "scheduledReport": {
      "arn": "string",
      "createdAt": number,
      "dashboardArn": "string",
      "description": "string",
      "healthStatus": {
         "lastRefreshedAt": number,
         "statusCode": "string",
         "statusReasons": [ "string" ]
      },
      "lastExecutionAt": number,
      "name": "string",
      "scheduleConfig": {
         "scheduleExpression": "string",
         "scheduleExpressionTimeZone": "string",
         "schedulePeriod": {
            "endTime": number,
            "startTime": number
         },
         "state": "string"
      },
      "scheduledReportExecutionRoleArn": "string",
      "updatedAt": number,
      "widgetDateRangeOverride": {
         "endTime": {
            "type": "string",
            "value": "string"
         },
         "startTime": {
            "type": "string",
            "value": "string"
         }
      },
      "widgetIds": [ "string" ]
   }
}
```

## Response Elements
<a name="API_bcmDashboards_GetScheduledReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [scheduledReport](#API_bcmDashboards_GetScheduledReport_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_GetScheduledReport-response-scheduledReport"></a>
The scheduled report configuration and metadata.
Type: [ScheduledReport](API_bcmDashboards_ScheduledReport.md) object

## Errors
<a name="API_bcmDashboards_GetScheduledReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action. Verify your IAM permissions and any resource policies.
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

## See Also
<a name="API_bcmDashboards_GetScheduledReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-dashboards-2025-08-18/GetScheduledReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-dashboards-2025-08-18/GetScheduledReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/GetScheduledReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-dashboards-2025-08-18/GetScheduledReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/GetScheduledReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-dashboards-2025-08-18/GetScheduledReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-dashboards-2025-08-18/GetScheduledReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-dashboards-2025-08-18/GetScheduledReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-dashboards-2025-08-18/GetScheduledReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/GetScheduledReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
