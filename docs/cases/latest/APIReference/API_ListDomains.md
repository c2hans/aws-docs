---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_ListDomains.html
---

# ListDomains
<a name="API_connect-cases_ListDomains"></a>

Lists all cases domains in the AWS account. Each list item is a condensed summary object of the domain.

## Request Syntax
<a name="API_connect-cases_ListDomains_RequestSyntax"></a>

```
POST /domains-list?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-cases_ListDomains_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_connect-cases_ListDomains_RequestSyntax) **   <a name="connect-connect-cases_ListDomains-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [nextToken](#API_connect-cases_ListDomains_RequestSyntax) **   <a name="connect-connect-cases_ListDomains-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 9000.

## Request Body
<a name="API_connect-cases_ListDomains_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-cases_ListDomains_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "domains": [
      {
         "domainArn": "string",
         "domainId": "string",
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_connect-cases_ListDomains_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domains](#API_connect-cases_ListDomains_ResponseSyntax) **   <a name="connect-connect-cases_ListDomains-response-domains"></a>
The Cases domain.
Type: Array of [DomainSummary](API_connect-cases_DomainSummary.md) objects

 ** [nextToken](#API_connect-cases_ListDomains_ResponseSyntax) **   <a name="connect-connect-cases_ListDomains-response-nextToken"></a>
The token for the next set of results. This is null if there are no more results to return.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 9000.

## Errors
<a name="API_connect-cases_ListDomains_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
We couldn't process your request because of an issue with the server. Try again later.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## Examples
<a name="API_connect-cases_ListDomains_Examples"></a>

### Request and Response example
<a name="API_connect-cases_ListDomains_Example_1"></a>

This example illustrates one usage of ListDomains.

```
{ }
```

```
{
"domains": [
  {
    "domainArn": "arn:aws:cases:us-west-2:[account_id]:domain/[domain_id]",
    "domainId": "[domain_id]",
    "name": "[domain_name]"
  }
]
"nextToken": [nextToken]
}
```

## See Also
<a name="API_connect-cases_ListDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/ListDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/ListDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/ListDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/ListDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/ListDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/ListDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/ListDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/ListDomains)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/ListDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/ListDomains)
