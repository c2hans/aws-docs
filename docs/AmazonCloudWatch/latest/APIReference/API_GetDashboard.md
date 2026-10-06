---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetDashboard.html
---

# GetDashboard
<a name="API_GetDashboard"></a>

Displays the details of the dashboard that you specify.

To copy an existing dashboard, use `GetDashboard`, and then use the data returned within `DashboardBody` as the template for the new dashboard when you call `PutDashboard` to create the copy.

You might have recently enabled an [opt-in Region (Region that is disabled by default)](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#optinregion) for your account. In that Region, `GetDashboard` can return an access denied error for up to 24 hours after you enable the Region. This delay occurs while dashboard data propagates. The error does not indicate a problem with your permissions. Because dashboards are global, you can call `GetDashboard` in any other enabled Region, or retry after propagation completes.

## Request Syntax
<a name="API_GetDashboard_RequestSyntax"></a>

```
{
   "DashboardName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDashboard_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DashboardName](#API_GetDashboard_RequestSyntax) **   <a name="ACW-GetDashboard-request-DashboardName"></a>
The name of the dashboard to be described.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetDashboard_ResponseSyntax"></a>

```
{
   "DashboardArn": "string",
   "DashboardBody": "string",
   "DashboardName": "string"
}
```

## Response Elements
<a name="API_GetDashboard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DashboardArn](#API_GetDashboard_ResponseSyntax) **   <a name="ACW-GetDashboard-response-DashboardArn"></a>
The Amazon Resource Name (ARN) of the dashboard.
Type: String

 ** [DashboardBody](#API_GetDashboard_ResponseSyntax) **   <a name="ACW-GetDashboard-response-DashboardBody"></a>
The detailed information about the dashboard, including what widgets are included and their location on the dashboard. For more information about the `DashboardBody` syntax, see [Dashboard Body Structure and Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Dashboard-Body-Structure.html).
Type: String

 ** [DashboardName](#API_GetDashboard_ResponseSyntax) **   <a name="ACW-GetDashboard-response-DashboardName"></a>
The name of the dashboard.
Type: String

## Errors
<a name="API_GetDashboard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
Request processing has failed due to some unknown error, exception, or failure.
 ** Message **

HTTP Status Code: 500

 ** InvalidParameterValue **
The value of an input parameter is bad or out-of-range.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFound **
The specified dashboard does not exist.
HTTP Status Code: 404

## See Also
<a name="API_GetDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/GetDashboard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetDashboard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetDashboard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/GetDashboard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetDashboard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/GetDashboard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/GetDashboard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/GetDashboard)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetDashboard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetDashboard)
