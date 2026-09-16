---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_CreateDashboard.html
---

# CreateDashboard
<a name="API_bcmDashboards_CreateDashboard"></a>

Creates a new dashboard that can contain multiple widgets displaying cost and usage data. You can add custom widgets or use predefined widgets, arranging them in your preferred layout.

## Request Syntax
<a name="API_bcmDashboards_CreateDashboard_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "name": "{{string}}",
   "resourceTags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
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
<a name="API_bcmDashboards_CreateDashboard_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_bcmDashboards_CreateDashboard_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_CreateDashboard-request-description"></a>
A description of the dashboard's purpose or contents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!.* {2})[ a-zA-Z0-9.,!?;:@#$%&\-_/\\]*`
Required: No

 ** [name](#API_bcmDashboards_CreateDashboard_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_CreateDashboard-request-name"></a>
The name of the dashboard. The name must be unique within your account.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `(?!.* {2})[a-zA-Z][a-zA-Z0-9 _-]{0,48}[a-zA-Z0-9_-]`
Required: Yes

 ** [resourceTags](#API_bcmDashboards_CreateDashboard_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_CreateDashboard-request-resourceTags"></a>
The tags to apply to the dashboard resource for organization and management.
Type: Array of [ResourceTag](API_bcmDashboards_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [widgets](#API_bcmDashboards_CreateDashboard_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_CreateDashboard-request-widgets"></a>
An array of widget configurations that define the visualizations to be displayed in the dashboard. Each dashboard can contain up to 20 widgets.
Type: Array of [Widget](API_bcmDashboards_Widget.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: Yes

## Response Syntax
<a name="API_bcmDashboards_CreateDashboard_ResponseSyntax"></a>

```
{
   "arn": "string"
}
```

## Response Elements
<a name="API_bcmDashboards_CreateDashboard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_bcmDashboards_CreateDashboard_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_CreateDashboard-response-arn"></a>
The ARN of the newly created dashboard.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:dashboard/(\*|[-a-z0-9]+)`

## Errors
<a name="API_bcmDashboards_CreateDashboard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action. Verify your IAM permissions and any resource policies.
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

## See Also
<a name="API_bcmDashboards_CreateDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-dashboards-2025-08-18/CreateDashboard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-dashboards-2025-08-18/CreateDashboard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/CreateDashboard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-dashboards-2025-08-18/CreateDashboard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/CreateDashboard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-dashboards-2025-08-18/CreateDashboard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-dashboards-2025-08-18/CreateDashboard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-dashboards-2025-08-18/CreateDashboard)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bcm-dashboards-2025-08-18/CreateDashboard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/CreateDashboard)
