---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ListDictionaries.html
---

# ListDictionaries
<a name="API_ListDictionaries"></a>

Lists the dictionaries in your account.

## Request Syntax
<a name="API_ListDictionaries_RequestSyntax"></a>

```
GET /v1/dictionaries?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDictionaries_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListDictionaries_RequestSyntax) **   <a name="elementalinference-ListDictionaries-request-uri-maxResults"></a>
The maximum number of results to return per API request. Valid range: 1 to 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListDictionaries_RequestSyntax) **   <a name="elementalinference-ListDictionaries-request-uri-nextToken"></a>
The token that identifies the next batch of results to return.

## Request Body
<a name="API_ListDictionaries_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDictionaries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dictionaries": [
      {
         "arn": "string",
         "id": "string",
         "language": "string",
         "name": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDictionaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dictionaries](#API_ListDictionaries_ResponseSyntax) **   <a name="elementalinference-ListDictionaries-response-dictionaries"></a>
A list of DictionarySummary objects.
Type: Array of [DictionarySummary](API_DictionarySummary.md) objects

 ** [nextToken](#API_ListDictionaries_ResponseSyntax) **   <a name="elementalinference-ListDictionaries-response-nextToken"></a>
The token to use to retrieve the next batch of results.
Type: String

## Errors
<a name="API_ListDictionaries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** TooManyRequestException **
The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying.
HTTP Status Code: 400

## See Also
<a name="API_ListDictionaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/ListDictionaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/ListDictionaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/ListDictionaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/ListDictionaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/ListDictionaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/ListDictionaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/ListDictionaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/ListDictionaries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/ListDictionaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/ListDictionaries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Inference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-inference` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
