---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListAccessPolicies.html
---

# ListAccessPolicies
<a name="API_ListAccessPolicies"></a>

Returns information about a list of OpenSearch Serverless access policies.

## Request Syntax
<a name="API_ListAccessPolicies_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resource": [ "{{string}}" ],
   "type": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAccessPolicies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListAccessPolicies_RequestSyntax) **   <a name="opensearchserverless-ListAccessPolicies-request-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results. The default is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListAccessPolicies_RequestSyntax) **   <a name="opensearchserverless-ListAccessPolicies-request-nextToken"></a>
If your initial `ListAccessPolicies` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListAccessPolicies` operations, which returns results in the next page.
Type: String
Required: No

 ** [resource](#API_ListAccessPolicies_RequestSyntax) **   <a name="opensearchserverless-ListAccessPolicies-request-resource"></a>
Resource filters (can be collections or indexes) that policies can apply to.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Required: No

 ** [type](#API_ListAccessPolicies_RequestSyntax) **   <a name="opensearchserverless-ListAccessPolicies-request-type"></a>
The type of access policy.
Type: String
Valid Values: `data`
Required: Yes

## Response Syntax
<a name="API_ListAccessPolicies_ResponseSyntax"></a>

```
{
   "accessPolicySummaries": [
      {
         "createdDate": number,
         "description": "string",
         "lastModifiedDate": number,
         "name": "string",
         "policyVersion": "string",
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAccessPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessPolicySummaries](#API_ListAccessPolicies_ResponseSyntax) **   <a name="opensearchserverless-ListAccessPolicies-response-accessPolicySummaries"></a>
Details about the requested access policies.
Type: Array of [AccessPolicySummary](API_AccessPolicySummary.md) objects

 ** [nextToken](#API_ListAccessPolicies_ResponseSyntax) **   <a name="opensearchserverless-ListAccessPolicies-response-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListAccessPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_ListAccessPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/ListAccessPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/ListAccessPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/ListAccessPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/ListAccessPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/ListAccessPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/ListAccessPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/ListAccessPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/ListAccessPolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/ListAccessPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/ListAccessPolicies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
