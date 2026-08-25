---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_GetDashboard.html
---

# GetDashboard
<a name="API_bcmDashboards_GetDashboard"></a>

Retrieves the configuration and metadata of a specified dashboard, including its widgets and layout settings.

## Request Syntax
<a name="API_bcmDashboards_GetDashboard_RequestSyntax"></a>

```
{
   "arn": "{{string}}"
}
```

## Request Parameters
<a name="API_bcmDashboards_GetDashboard_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_bcmDashboards_GetDashboard_RequestSyntax) **   <a name="awscostmanagement-bcmDashboards_GetDashboard-request-arn"></a>
The ARN of the dashboard to retrieve. This is required to uniquely identify the dashboard.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:dashboard/(\*|[-a-z0-9]+)`
Required: Yes

## Response Syntax
<a name="API_bcmDashboards_GetDashboard_ResponseSyntax"></a>

```
{
   "arn": "string",
   "createdAt": number,
   "description": "string",
   "name": "string",
   "type": "string",
   "updatedAt": number,
   "widgets": [
      {
         "configs": [
            {
               "displayConfig": { ... },
               "queryParameters": { ... }
            }
         ],
         "description": "string",
         "height": number,
         "horizontalOffset": number,
         "id": "string",
         "title": "string",
         "width": number
      }
   ]
}
```

## Response Elements
<a name="API_bcmDashboards_GetDashboard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_bcmDashboards_GetDashboard_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_GetDashboard-response-arn"></a>
The ARN of the retrieved dashboard.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:bcm-dashboards::[0-9]{12}:dashboard/(\*|[-a-z0-9]+)`

 ** [createdAt](#API_bcmDashboards_GetDashboard_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_GetDashboard-response-createdAt"></a>
The timestamp when the dashboard was created.
Type: Timestamp

 ** [description](#API_bcmDashboards_GetDashboard_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_GetDashboard-response-description"></a>
The description of the retrieved dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(?!.* {2})[ a-zA-Z0-9.,!?;:@#$%&\-_/\\]*`

 ** [name](#API_bcmDashboards_GetDashboard_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_GetDashboard-response-name"></a>
The name of the retrieved dashboard.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `(?!.* {2})[a-zA-Z][a-zA-Z0-9 _-]{0,48}[a-zA-Z0-9_-]`

 ** [type](#API_bcmDashboards_GetDashboard_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_GetDashboard-response-type"></a>
The dashboard type. The following values are valid:
+  `CUSTOM` – A dashboard that you create and manage.
+  `AWS_MANAGED` – A predefined, read-only dashboard that AWS authors and maintains. You cannot modify, delete, share, tag, or schedule reports for an `AWS_MANAGED` dashboard.
Type: String
Valid Values: `CUSTOM | AWS_MANAGED`

 ** [updatedAt](#API_bcmDashboards_GetDashboard_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_GetDashboard-response-updatedAt"></a>
The timestamp when the dashboard was last modified.
Type: Timestamp

 ** [widgets](#API_bcmDashboards_GetDashboard_ResponseSyntax) **   <a name="awscostmanagement-bcmDashboards_GetDashboard-response-widgets"></a>
An array of widget configurations that make up the dashboard.
Type: Array of [Widget](API_bcmDashboards_Widget.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

## Errors
<a name="API_bcmDashboards_GetDashboard_Errors"></a>

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
<a name="API_bcmDashboards_GetDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-dashboards-2025-08-18/GetDashboard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-dashboards-2025-08-18/GetDashboard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/GetDashboard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-dashboards-2025-08-18/GetDashboard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/GetDashboard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-dashboards-2025-08-18/GetDashboard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-dashboards-2025-08-18/GetDashboard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-dashboards-2025-08-18/GetDashboard)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-dashboards-2025-08-18/GetDashboard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/GetDashboard)
