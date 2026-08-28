---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-app-integrations_ListApplications.html
---

# ListApplications
<a name="API_connect-app-integrations_ListApplications"></a>

Lists applications in the account.

## Request Syntax
<a name="API_connect-app-integrations_ListApplications_RequestSyntax"></a>

```
GET /applications?applicationType={{ApplicationType}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-app-integrations_ListApplications_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationType](#API_connect-app-integrations_ListApplications_RequestSyntax) **   <a name="connect-connect-app-integrations_ListApplications-request-uri-ApplicationType"></a>
The type of application.
Valid Values: `STANDARD | SERVICE | MCP_SERVER`

 ** [MaxResults](#API_connect-app-integrations_ListApplications_RequestSyntax) **   <a name="connect-connect-app-integrations_ListApplications-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_connect-app-integrations_ListApplications_RequestSyntax) **   <a name="connect-connect-app-integrations_ListApplications-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.*`

## Request Body
<a name="API_connect-app-integrations_ListApplications_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-app-integrations_ListApplications_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Applications": [
      {
         "ApplicationType": "string",
         "Arn": "string",
         "CreatedTime": number,
         "Id": "string",
         "IsService": boolean,
         "LastModifiedTime": number,
         "Name": "string",
         "Namespace": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_connect-app-integrations_ListApplications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Applications](#API_connect-app-integrations_ListApplications_ResponseSyntax) **   <a name="connect-connect-app-integrations_ListApplications-response-Applications"></a>
The Applications associated with this account.
Type: Array of [ApplicationSummary](API_connect-app-integrations_ApplicationSummary.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

 ** [NextToken](#API_connect-app-integrations_ListApplications_ResponseSyntax) **   <a name="connect-connect-app-integrations_ListApplications-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.*`

## Errors
<a name="API_connect-app-integrations_ListApplications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServiceError **
Request processing failed due to an error or failure with the service.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
HTTP Status Code: 400

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_connect-app-integrations_ListApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/ListApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/ListApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/ListApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/ListApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/ListApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/ListApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/ListApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/ListApplications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/ListApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/ListApplications)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
