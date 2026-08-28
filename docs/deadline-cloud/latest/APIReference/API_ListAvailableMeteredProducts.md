---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListAvailableMeteredProducts.html
---

# ListAvailableMeteredProducts
<a name="API_ListAvailableMeteredProducts"></a>

A list of the available metered products.

## Request Syntax
<a name="API_ListAvailableMeteredProducts_RequestSyntax"></a>

```
GET /2023-10-12/metered-products?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAvailableMeteredProducts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAvailableMeteredProducts_RequestSyntax) **   <a name="deadlinecloud-ListAvailableMeteredProducts-request-uri-maxResults"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAvailableMeteredProducts_RequestSyntax) **   <a name="deadlinecloud-ListAvailableMeteredProducts-request-uri-nextToken"></a>
The token for the next set of results, or `null` to start from the beginning.
Length Constraints: Minimum length of 0. Maximum length of 4096.

## Request Body
<a name="API_ListAvailableMeteredProducts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAvailableMeteredProducts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "meteredProducts": [
      {
         "family": "string",
         "port": number,
         "productId": "string",
         "vendor": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAvailableMeteredProducts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [meteredProducts](#API_ListAvailableMeteredProducts_ResponseSyntax) **   <a name="deadlinecloud-ListAvailableMeteredProducts-response-meteredProducts"></a>
The metered products.
Type: Array of [MeteredProductSummary](API_MeteredProductSummary.md) objects

 ** [nextToken](#API_ListAvailableMeteredProducts_ResponseSyntax) **   <a name="deadlinecloud-ListAvailableMeteredProducts-response-nextToken"></a>
If Deadline Cloud returns `nextToken`, then there are more results available. The value of `nextToken` is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then `nextToken` is set to `null`. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 `ValidationException` error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

## Errors
<a name="API_ListAvailableMeteredProducts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerErrorException **
Deadline Cloud can't process your request right now. Try again later.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
Your request exceeded a request rate quota.
 ** context **
Information about the resources in use when the exception was thrown.
 ** quotaCode **
Identifies the quota that is being throttled.
 ** retryAfterSeconds **
The number of seconds a client should wait before retrying the request.
 ** serviceCode **
Identifies the service that is being throttled.
HTTP Status Code: 429

## See Also
<a name="API_ListAvailableMeteredProducts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/deadline-2023-10-12/ListAvailableMeteredProducts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/deadline-2023-10-12/ListAvailableMeteredProducts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ListAvailableMeteredProducts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/deadline-2023-10-12/ListAvailableMeteredProducts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ListAvailableMeteredProducts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/deadline-2023-10-12/ListAvailableMeteredProducts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/deadline-2023-10-12/ListAvailableMeteredProducts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/deadline-2023-10-12/ListAvailableMeteredProducts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/deadline-2023-10-12/ListAvailableMeteredProducts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ListAvailableMeteredProducts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
