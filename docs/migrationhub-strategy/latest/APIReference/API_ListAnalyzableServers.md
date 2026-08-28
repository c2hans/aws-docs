---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListAnalyzableServers.html
---

# ListAnalyzableServers
<a name="API_ListAnalyzableServers"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Retrieves a list of servers. The servers are fetched from VMWare vCenter using Migration Hub Strategy Recommendations application data collector.

## Request Syntax
<a name="API_ListAnalyzableServers_RequestSyntax"></a>

```
POST /list-analyzable-servers HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sort": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListAnalyzableServers_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListAnalyzableServers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListAnalyzableServers_RequestSyntax) **   <a name="migrationhubstrategy-ListAnalyzableServers-request-maxResults"></a>
The maximum number of items to include in the response. The maximum value is 100.
Type: Integer
Required: No

 ** [nextToken](#API_ListAnalyzableServers_RequestSyntax) **   <a name="migrationhubstrategy-ListAnalyzableServers-request-nextToken"></a>
The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set `maxResults` to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** [sort](#API_ListAnalyzableServers_RequestSyntax) **   <a name="migrationhubstrategy-ListAnalyzableServers-request-sort"></a>
Specifies whether to sort by ascending (`ASC`) or descending (`DESC`) order.
Type: String
Valid Values: `ASC | DESC`
Required: No

## Response Syntax
<a name="API_ListAnalyzableServers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "analyzableServers": [
      {
         "hostname": "string",
         "ipAddress": "string",
         "source": "string",
         "vmId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAnalyzableServers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analyzableServers](#API_ListAnalyzableServers_ResponseSyntax) **   <a name="migrationhubstrategy-ListAnalyzableServers-response-analyzableServers"></a>
The list of analyzable servers with a summary of information about each server.
Type: Array of [AnalyzableServerSummary](API_AnalyzableServerSummary.md) objects

 ** [nextToken](#API_ListAnalyzableServers_ResponseSyntax) **   <a name="migrationhubstrategy-ListAnalyzableServers-response-nextToken"></a>
The token you use to retrieve the next set of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*\S.*`

## Errors
<a name="API_ListAnalyzableServers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.
HTTP Status Code: 403

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
 The request body isn't valid.
HTTP Status Code: 400

## See Also
<a name="API_ListAnalyzableServers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/ListAnalyzableServers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/ListAnalyzableServers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/ListAnalyzableServers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/ListAnalyzableServers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/ListAnalyzableServers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/ListAnalyzableServers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/ListAnalyzableServers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/ListAnalyzableServers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/ListAnalyzableServers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/ListAnalyzableServers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
