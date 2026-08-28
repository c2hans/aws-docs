---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeDashboard.html
---

# DescribeDashboard
<a name="API_DescribeDashboard"></a>

Retrieves information about a dashboard.

## Request Syntax
<a name="API_DescribeDashboard_RequestSyntax"></a>

```
GET /dashboards/{{dashboardId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDashboard_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dashboardId](#API_DescribeDashboard_RequestSyntax) **   <a name="iotsitewise-DescribeDashboard-request-uri-dashboardId"></a>
The ID of the dashboard.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

## Request Body
<a name="API_DescribeDashboard_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDashboard_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dashboardArn": "string",
   "dashboardCreationDate": number,
   "dashboardDefinition": "string",
   "dashboardDescription": "string",
   "dashboardId": "string",
   "dashboardLastUpdateDate": number,
   "dashboardName": "string",
   "projectId": "string"
}
```

## Response Elements
<a name="API_DescribeDashboard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dashboardArn](#API_DescribeDashboard_ResponseSyntax) **   <a name="iotsitewise-DescribeDashboard-response-dashboardArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the dashboard, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:dashboard/${DashboardId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [dashboardCreationDate](#API_DescribeDashboard_ResponseSyntax) **   <a name="iotsitewise-DescribeDashboard-response-dashboardCreationDate"></a>
The date the dashboard was created, in Unix epoch time.
Type: Timestamp

 ** [dashboardDefinition](#API_DescribeDashboard_ResponseSyntax) **   <a name="iotsitewise-DescribeDashboard-response-dashboardDefinition"></a>
The dashboard's definition JSON literal. For detailed information, see [Creating dashboards (CLI)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 204800.
Pattern: `.+`

 ** [dashboardDescription](#API_DescribeDashboard_ResponseSyntax) **   <a name="iotsitewise-DescribeDashboard-response-dashboardDescription"></a>
The dashboard's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [dashboardId](#API_DescribeDashboard_ResponseSyntax) **   <a name="iotsitewise-DescribeDashboard-response-dashboardId"></a>
The ID of the dashboard.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [dashboardLastUpdateDate](#API_DescribeDashboard_ResponseSyntax) **   <a name="iotsitewise-DescribeDashboard-response-dashboardLastUpdateDate"></a>
The date the dashboard was last updated, in Unix epoch time.
Type: Timestamp

 ** [dashboardName](#API_DescribeDashboard_ResponseSyntax) **   <a name="iotsitewise-DescribeDashboard-response-dashboardName"></a>
The name of the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [projectId](#API_DescribeDashboard_ResponseSyntax) **   <a name="iotsitewise-DescribeDashboard-response-projectId"></a>
The ID of the project that the dashboard is in.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

## Errors
<a name="API_DescribeDashboard_Errors"></a>

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
<a name="API_DescribeDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeDashboard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeDashboard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeDashboard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeDashboard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeDashboard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeDashboard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeDashboard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeDashboard)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeDashboard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeDashboard)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
