---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ExecuteScheduledReport.html
---

# ExecuteScheduledReport
<a name="API_bcmDashboards_ExecuteScheduledReport"></a>

Triggers an immediate execution of a scheduled report, outside of its regular schedule. The scheduled report must be in `ENABLED` state. Calling this operation on a `DISABLED` scheduled report returns a `ValidationException`.

**Note**
If a `clientToken` is provided, the service uses it for idempotency. Requests with the same client token will not trigger a new execution within the same minute.

## Request Syntax
<a name="API_bcmDashboards_ExecuteScheduledReport_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "clientToken": "{{string}}",
   "dryRun": {{boolean}}
}
```

## Request Parameters
<a name="API_bcmDashboards_ExecuteScheduledReport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_bcmDashboards_ExecuteScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_ExecuteScheduledReport-request-arn"></a>
The ARN of the scheduled report to execute.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:scheduled-report/(\*|[-a-z0-9]+)`
Required: Yes

 ** [clientToken](#API_bcmDashboards_ExecuteScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_ExecuteScheduledReport-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\u0021-\u007E]+`
Required: No

 ** [dryRun](#API_bcmDashboards_ExecuteScheduledReport_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_ExecuteScheduledReport-request-dryRun"></a>
When set to `true`, validates the scheduled report configuration without triggering an actual execution.
Type: Boolean
Required: No

## Response Syntax
<a name="API_bcmDashboards_ExecuteScheduledReport_ResponseSyntax"></a>

```
{
   "executionTriggered": boolean,
   "healthStatus": {
      "lastRefreshedAt": number,
      "statusCode": "string",
      "statusReasons": [ "string" ]
   }
}
```

## Response Elements
<a name="API_bcmDashboards_ExecuteScheduledReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executionTriggered](#API_bcmDashboards_ExecuteScheduledReport_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_ExecuteScheduledReport-response-executionTriggered"></a>
Indicates whether the execution was successfully triggered.
Type: Boolean

 ** [healthStatus](#API_bcmDashboards_ExecuteScheduledReport_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_ExecuteScheduledReport-response-healthStatus"></a>
The health status of the scheduled report after the execution request.
Type: [HealthStatus](API_bcmDashboards_HealthStatus.md) object

## Errors
<a name="API_bcmDashboards_ExecuteScheduledReport_Errors"></a>

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

## See Also
<a name="API_bcmDashboards_ExecuteScheduledReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-dashboards-2025-08-18/ExecuteScheduledReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-dashboards-2025-08-18/ExecuteScheduledReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/ExecuteScheduledReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-dashboards-2025-08-18/ExecuteScheduledReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/ExecuteScheduledReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-dashboards-2025-08-18/ExecuteScheduledReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-dashboards-2025-08-18/ExecuteScheduledReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-dashboards-2025-08-18/ExecuteScheduledReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-dashboards-2025-08-18/ExecuteScheduledReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/ExecuteScheduledReport)
