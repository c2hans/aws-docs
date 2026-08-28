---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ListScheduledReports.html
---

# ListScheduledReports
<a name="API_bcmDashboards_ListScheduledReports"></a>

Returns a list of scheduled reports in your account.

## Request Syntax
<a name="API_bcmDashboards_ListScheduledReports_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_bcmDashboards_ListScheduledReports_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_bcmDashboards_ListScheduledReports_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_ListScheduledReports-request-maxResults"></a>
The maximum number of results to return in a single call. Valid range is 1 to 100. The default value is 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_bcmDashboards_ListScheduledReports_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_ListScheduledReports-request-nextToken"></a>
The token for the next page of results. Use the value returned in the previous response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_bcmDashboards_ListScheduledReports_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "scheduledReports": [
      {
         "arn": "string",
         "dashboardArn": "string",
         "healthStatus": {
            "lastRefreshedAt": number,
            "statusCode": "string",
            "statusReasons": [ "string" ]
         },
         "name": "string",
         "scheduleExpression": "string",
         "scheduleExpressionTimeZone": "string",
         "state": "string",
         "widgetIds": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_bcmDashboards_ListScheduledReports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_bcmDashboards_ListScheduledReports_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_ListScheduledReports-response-nextToken"></a>
The token to use to retrieve the next page of results. Not returned if there are no more results to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [scheduledReports](#API_bcmDashboards_ListScheduledReports_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_ListScheduledReports-response-scheduledReports"></a>
An array of scheduled report summaries, containing basic information about each scheduled report.
Type: Array of [ScheduledReportSummary](API_bcmDashboards_ScheduledReportSummary.md) objects

## Errors
<a name="API_bcmDashboards_ListScheduledReports_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action. Verify your IAM permissions and any resource policies.
HTTP Status Code: 400

 ** InternalServerException **
An internal error occurred while processing the request. Retry your request. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling. Reduce the frequency of requests and use exponential backoff.
HTTP Status Code: 400

 ** ValidationException **
The input parameters do not satisfy the requirements. Check the error message for specific validation details.
HTTP Status Code: 400

## See Also
<a name="API_bcmDashboards_ListScheduledReports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-dashboards-2025-08-18/ListScheduledReports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-dashboards-2025-08-18/ListScheduledReports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/ListScheduledReports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-dashboards-2025-08-18/ListScheduledReports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/ListScheduledReports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-dashboards-2025-08-18/ListScheduledReports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-dashboards-2025-08-18/ListScheduledReports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-dashboards-2025-08-18/ListScheduledReports)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-dashboards-2025-08-18/ListScheduledReports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/ListScheduledReports)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
