---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetUpgradeHistory.html
---

# GetUpgradeHistory
<a name="API_GetUpgradeHistory"></a>

Retrieves the complete history of the last 10 upgrades performed on an Amazon OpenSearch Service domain.

## Request Syntax
<a name="API_GetUpgradeHistory_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/upgradeDomain/{{DomainName}}/history?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetUpgradeHistory_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_GetUpgradeHistory_RequestSyntax) **   <a name="opensearchservice-GetUpgradeHistory-request-uri-DomainName"></a>
The name of an existing domain.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [MaxResults](#API_GetUpgradeHistory_RequestSyntax) **   <a name="opensearchservice-GetUpgradeHistory-request-uri-MaxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results.
Valid Range: Maximum value of 100.

 ** [NextToken](#API_GetUpgradeHistory_RequestSyntax) **   <a name="opensearchservice-GetUpgradeHistory-request-uri-NextToken"></a>
If your initial `GetUpgradeHistory` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `GetUpgradeHistory` operations, which returns results in the next page.

## Request Body
<a name="API_GetUpgradeHistory_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetUpgradeHistory_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "UpgradeHistories": [
      {
         "StartTimestamp": number,
         "StepsList": [
            {
               "Issues": [ "string" ],
               "ProgressPercent": number,
               "UpgradeStep": "string",
               "UpgradeStepStatus": "string"
            }
         ],
         "UpgradeName": "string",
         "UpgradeStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetUpgradeHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetUpgradeHistory_ResponseSyntax) **   <a name="opensearchservice-GetUpgradeHistory-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

 ** [UpgradeHistories](#API_GetUpgradeHistory_ResponseSyntax) **   <a name="opensearchservice-GetUpgradeHistory-response-UpgradeHistories"></a>
A list of objects corresponding to each upgrade or upgrade eligibility check performed on a domain.
Type: Array of [UpgradeHistory](API_UpgradeHistory.md) objects

## Errors
<a name="API_GetUpgradeHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_GetUpgradeHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/GetUpgradeHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/GetUpgradeHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/GetUpgradeHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/GetUpgradeHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/GetUpgradeHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/GetUpgradeHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/GetUpgradeHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/GetUpgradeHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/GetUpgradeHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/GetUpgradeHistory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
