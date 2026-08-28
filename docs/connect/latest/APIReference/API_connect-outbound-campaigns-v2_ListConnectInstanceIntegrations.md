---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_ListConnectInstanceIntegrations.html
---

# ListConnectInstanceIntegrations
<a name="API_connect-outbound-campaigns-v2_ListConnectInstanceIntegrations"></a>

Lists integrations with the Connect Customer instance.

## Request Syntax
<a name="API_connect-outbound-campaigns-v2_ListConnectInstanceIntegrations_RequestSyntax"></a>

```
GET /v2/connect-instance/{{connectInstanceId}}/integrations?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns-v2_ListConnectInstanceIntegrations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [connectInstanceId](#API_connect-outbound-campaigns-v2_ListConnectInstanceIntegrations_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_ListConnectInstanceIntegrations-request-uri-connectInstanceId"></a>
The identifier of the Connect Customer instance. You can find the `instanceId` in the ARN of the instance.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: Yes

 ** [maxResults](#API_connect-outbound-campaigns-v2_ListConnectInstanceIntegrations_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_ListConnectInstanceIntegrations-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_connect-outbound-campaigns-v2_ListConnectInstanceIntegrations_RequestSyntax) **   <a name="connect-connect-outbound-campaigns-v2_ListConnectInstanceIntegrations-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_connect-outbound-campaigns-v2_ListConnectInstanceIntegrations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-outbound-campaigns-v2_ListConnectInstanceIntegrations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "integrationSummaryList": [
      { ... }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_connect-outbound-campaigns-v2_ListConnectInstanceIntegrations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [integrationSummaryList](#API_connect-outbound-campaigns-v2_ListConnectInstanceIntegrations_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns-v2_ListConnectInstanceIntegrations-response-integrationSummaryList"></a>
Summary information about the integrations.
Type: Array of [IntegrationSummary](API_connect-outbound-campaigns-v2_IntegrationSummary.md) objects

 ** [nextToken](#API_connect-outbound-campaigns-v2_ListConnectInstanceIntegrations_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns-v2_ListConnectInstanceIntegrations-response-nextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Errors
<a name="API_connect-outbound-campaigns-v2_ListConnectInstanceIntegrations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the outbound campaigns.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_connect-outbound-campaigns-v2_ListConnectInstanceIntegrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaignsv2-2024-04-23/ListConnectInstanceIntegrations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaignsv2-2024-04-23/ListConnectInstanceIntegrations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/ListConnectInstanceIntegrations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaignsv2-2024-04-23/ListConnectInstanceIntegrations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/ListConnectInstanceIntegrations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaignsv2-2024-04-23/ListConnectInstanceIntegrations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaignsv2-2024-04-23/ListConnectInstanceIntegrations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaignsv2-2024-04-23/ListConnectInstanceIntegrations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcampaignsv2-2024-04-23/ListConnectInstanceIntegrations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/ListConnectInstanceIntegrations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
