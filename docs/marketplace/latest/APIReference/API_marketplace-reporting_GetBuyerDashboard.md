---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-reporting_GetBuyerDashboard.html
---

# GetBuyerDashboard
<a name="API_marketplace-reporting_GetBuyerDashboard"></a>

Generates an embedding URL for an Amazon QuickSight dashboard for an anonymous user.

**Note**
This API is available only to AWS Organization management accounts or delegated administrators registered for the procurement insights (`procurement-insights.marketplace.amazonaws.com`) feature.

The following rules apply to a generated URL:
+ It contains a temporary bearer token, valid for 5 minutes after it is generated. Once redeemed within that period, it cannot be re-used again.
+ It has a session lifetime of one hour. The 5-minute validity period runs separately from the session lifetime.

## Request Syntax
<a name="API_marketplace-reporting_GetBuyerDashboard_RequestSyntax"></a>

```
POST /getBuyerDashboard HTTP/1.1
Content-type: application/json

{
   "dashboardIdentifier": "{{string}}",
   "embeddingDomains": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_marketplace-reporting_GetBuyerDashboard_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_marketplace-reporting_GetBuyerDashboard_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dashboardIdentifier](#API_marketplace-reporting_GetBuyerDashboard_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-reporting_GetBuyerDashboard-request-dashboardIdentifier"></a>
The ARN of the requested dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Pattern: `arn:aws:aws-marketplace::[0-9]{12}:AWSMarketplace/ReportingData/(Agreement_V1/Dashboard/AgreementSummary_V1|BillingEvent_V1/Dashboard/CostAnalysis_V1)`
Required: Yes

 ** [embeddingDomains](#API_marketplace-reporting_GetBuyerDashboard_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-reporting_GetBuyerDashboard-request-embeddingDomains"></a>
Fully qualified domains that you add to the allow list for access to the generated URL that is then embedded. You can list up to two domains or subdomains in each API call. To include all subdomains under a specific domain, use `*`. For example, `https://*.amazon.com` includes all subdomains under `https://aws.amazon.com`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `(https://[a-zA-Z\.\*0-9\-_]+[\.]{1}[a-zA-Z]{1,}[a-zA-Z0-9&?/-_=]*[a-zA-Z\*0-9/]+|http[s]*://localhost(:[0-9]{1,5})?)`
Required: Yes

## Response Syntax
<a name="API_marketplace-reporting_GetBuyerDashboard_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dashboardIdentifier": "string",
   "embeddingDomains": [ "string" ],
   "embedUrl": "string"
}
```

## Response Elements
<a name="API_marketplace-reporting_GetBuyerDashboard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dashboardIdentifier](#API_marketplace-reporting_GetBuyerDashboard_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-reporting_GetBuyerDashboard-response-dashboardIdentifier"></a>
The ARN of the returned dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Pattern: `arn:aws:aws-marketplace::[0-9]{12}:AWSMarketplace/ReportingData/(Agreement_V1/Dashboard/AgreementSummary_V1|BillingEvent_V1/Dashboard/CostAnalysis_V1)`

 ** [embeddingDomains](#API_marketplace-reporting_GetBuyerDashboard_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-reporting_GetBuyerDashboard-response-embeddingDomains"></a>
The fully qualified domains specified in the request. The domains enable access to the generated URL that is then embedded. You can list up to two domains or subdomains in each API call. To include all subdomains under a specific domain, use `*`. For example, `https://*.amazon.com` includes all subdomains under `https://aws.amazon.com`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `(https://[a-zA-Z\.\*0-9\-_]+[\.]{1}[a-zA-Z]{1,}[a-zA-Z0-9&?/-_=]*[a-zA-Z\*0-9/]+|http[s]*://localhost(:[0-9]{1,5})?)`

 ** [embedUrl](#API_marketplace-reporting_GetBuyerDashboard_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-reporting_GetBuyerDashboard-response-embedUrl"></a>
The dashboard's embedding URL.
Type: String

## Errors
<a name="API_marketplace-reporting_GetBuyerDashboard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The request is malformed, or it contains an error such as an invalid parameter. Ensure the request has all required parameters.
HTTP Status Code: 400

 ** InternalServerException **
The operation failed due to a server error.
HTTP Status Code: 500

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

## See Also
<a name="API_marketplace-reporting_GetBuyerDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-reporting-2018-05-10/GetBuyerDashboard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-reporting-2018-05-10/GetBuyerDashboard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-reporting-2018-05-10/GetBuyerDashboard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-reporting-2018-05-10/GetBuyerDashboard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-reporting-2018-05-10/GetBuyerDashboard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-reporting-2018-05-10/GetBuyerDashboard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-reporting-2018-05-10/GetBuyerDashboard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-reporting-2018-05-10/GetBuyerDashboard)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-reporting-2018-05-10/GetBuyerDashboard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-reporting-2018-05-10/GetBuyerDashboard)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
