---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateDashboard.html
---

# CreateDashboard
<a name="API_CreateDashboard"></a>

**Important**
The AWS IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025 . If you would like to use the AWS IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS IoT SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

Creates a dashboard in an AWS IoT SiteWise Monitor project.

## Request Syntax
<a name="API_CreateDashboard_RequestSyntax"></a>

```
POST /dashboards HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "dashboardDefinition": "{{string}}",
   "dashboardDescription": "{{string}}",
   "dashboardName": "{{string}}",
   "projectId": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDashboard_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDashboard_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateDashboard_RequestSyntax) **   <a name="iotsitewise-CreateDashboard-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [dashboardDefinition](#API_CreateDashboard_RequestSyntax) **   <a name="iotsitewise-CreateDashboard-request-dashboardDefinition"></a>
The dashboard definition specified in a JSON literal.
+  AWS IoT SiteWise Monitor (Classic) see [Create dashboards (AWS CLI)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html)
+  AWS IoT SiteWise Monitor (AI-aware) see [Create dashboards (AWS CLI)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-ai-dashboard-cli.html)
in the * AWS IoT SiteWise User Guide*
Type: String
Length Constraints: Minimum length of 0. Maximum length of 204800.
Pattern: `.+`
Required: Yes

 ** [dashboardDescription](#API_CreateDashboard_RequestSyntax) **   <a name="iotsitewise-CreateDashboard-request-dashboardDescription"></a>
A description for the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [dashboardName](#API_CreateDashboard_RequestSyntax) **   <a name="iotsitewise-CreateDashboard-request-dashboardName"></a>
A friendly name for the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** [projectId](#API_CreateDashboard_RequestSyntax) **   <a name="iotsitewise-CreateDashboard-request-projectId"></a>
The ID of the project in which to create the dashboard.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** [tags](#API_CreateDashboard_RequestSyntax) **   <a name="iotsitewise-CreateDashboard-request-tags"></a>
A list of key-value pairs that contain metadata for the dashboard. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the * AWS IoT SiteWise User Guide*.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateDashboard_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "dashboardArn": "string",
   "dashboardId": "string"
}
```

## Response Elements
<a name="API_CreateDashboard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [dashboardArn](#API_CreateDashboard_ResponseSyntax) **   <a name="iotsitewise-CreateDashboard-response-dashboardArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the dashboard, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:dashboard/${DashboardId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [dashboardId](#API_CreateDashboard_ResponseSyntax) **   <a name="iotsitewise-CreateDashboard-response-dashboardId"></a>
The ID of the dashboard.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

## Errors
<a name="API_CreateDashboard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** LimitExceededException **
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 410

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_CreateDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CreateDashboard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CreateDashboard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CreateDashboard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CreateDashboard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CreateDashboard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CreateDashboard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CreateDashboard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CreateDashboard)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CreateDashboard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CreateDashboard)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
