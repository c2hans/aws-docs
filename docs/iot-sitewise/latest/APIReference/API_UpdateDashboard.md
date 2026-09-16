---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateDashboard.html
---

# UpdateDashboard
<a name="API_UpdateDashboard"></a>

**Important**
The AWS IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025 . If you would like to use the AWS IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS IoT SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

Updates an AWS IoT SiteWise Monitor dashboard.

## Request Syntax
<a name="API_UpdateDashboard_RequestSyntax"></a>

```
PUT /dashboards/{{dashboardId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "dashboardDefinition": "{{string}}",
   "dashboardDescription": "{{string}}",
   "dashboardName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDashboard_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dashboardId](#API_UpdateDashboard_RequestSyntax) **   <a name="iotsitewise-UpdateDashboard-request-uri-dashboardId"></a>
The ID of the dashboard to update.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateDashboard_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateDashboard_RequestSyntax) **   <a name="iotsitewise-UpdateDashboard-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [dashboardDefinition](#API_UpdateDashboard_RequestSyntax) **   <a name="iotsitewise-UpdateDashboard-request-dashboardDefinition"></a>
The new dashboard definition, as specified in a JSON literal.
+  AWS IoT SiteWise Monitor (Classic) see [Create dashboards (AWS CLI)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html)
+  AWS IoT SiteWise Monitor (AI-aware) see [Create dashboards (AWS CLI)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-ai-dashboard-cli.html)
in the * AWS IoT SiteWise User Guide*
Type: String
Length Constraints: Minimum length of 0. Maximum length of 204800.
Pattern: `.+`
Required: Yes

 ** [dashboardDescription](#API_UpdateDashboard_RequestSyntax) **   <a name="iotsitewise-UpdateDashboard-request-dashboardDescription"></a>
A new description for the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [dashboardName](#API_UpdateDashboard_RequestSyntax) **   <a name="iotsitewise-UpdateDashboard-request-dashboardName"></a>
A new friendly name for the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

## Response Syntax
<a name="API_UpdateDashboard_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateDashboard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDashboard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_UpdateDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/UpdateDashboard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/UpdateDashboard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/UpdateDashboard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/UpdateDashboard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/UpdateDashboard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/UpdateDashboard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/UpdateDashboard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/UpdateDashboard)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/UpdateDashboard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/UpdateDashboard)
