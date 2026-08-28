---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_UpdateDashboard.html
---

# UpdateDashboard
<a name="API_bcmDashboards_UpdateDashboard"></a>

Updates an existing dashboard's properties, including its name, description, and widget configurations.

## Request Syntax
<a name="API_bcmDashboards_UpdateDashboard_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "widgets": [
      {
         "configs": [
            {
               "displayConfig": { ... },
               "queryParameters": { ... }
            }
         ],
         "description": "{{string}}",
         "height": {{number}},
         "horizontalOffset": {{number}},
         "id": "{{string}}",
         "title": "{{string}}",
         "width": {{number}}
      }
   ]
}
```

## Request Parameters
<a name="API_bcmDashboards_UpdateDashboard_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_bcmDashboards_UpdateDashboard_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateDashboard-request-arn"></a>
The ARN of the dashboard to update.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:dashboard/(\*|[-a-z0-9]+)`
Required: Yes

 ** [description](#API_bcmDashboards_UpdateDashboard_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateDashboard-request-description"></a>
The new description for the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!.* {2})[ a-zA-Z0-9.,!?;:@#$%&\-_/\\]*`
Required: No

 ** [name](#API_bcmDashboards_UpdateDashboard_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateDashboard-request-name"></a>
The new name for the dashboard.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `(?!.* {2})[a-zA-Z][a-zA-Z0-9 _-]{0,48}[a-zA-Z0-9_-]`
Required: Yes

 ** [widgets](#API_bcmDashboards_UpdateDashboard_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateDashboard-request-widgets"></a>
The updated array of widget configurations for the dashboard. Replaces all existing widgets.
Type: Array of [Widget](API_bcmDashboards_Widget.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## Response Syntax
<a name="API_bcmDashboards_UpdateDashboard_ResponseSyntax"></a>

```
{
   "arn": "string"
}
```

## Response Elements
<a name="API_bcmDashboards_UpdateDashboard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_bcmDashboards_UpdateDashboard_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_UpdateDashboard-response-arn"></a>
The ARN of the updated dashboard.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:dashboard/(\*|[-a-z0-9]+)`

## Errors
<a name="API_bcmDashboards_UpdateDashboard_Errors"></a>

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
<a name="API_bcmDashboards_UpdateDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-dashboards-2025-08-18/UpdateDashboard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-dashboards-2025-08-18/UpdateDashboard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/UpdateDashboard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-dashboards-2025-08-18/UpdateDashboard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/UpdateDashboard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-dashboards-2025-08-18/UpdateDashboard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-dashboards-2025-08-18/UpdateDashboard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-dashboards-2025-08-18/UpdateDashboard)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-dashboards-2025-08-18/UpdateDashboard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/UpdateDashboard)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
