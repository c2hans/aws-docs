---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListFunctions.html
---

# ListFunctions
<a name="API_ListFunctions"></a>

Retrieves all functions associated with your AWS account in the current Region. For more information about functions, see [Working with functions](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the *MediaTailor User Guide*.

## Request Syntax
<a name="API_ListFunctions_RequestSyntax"></a>

```
GET /functions?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFunctions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListFunctions_RequestSyntax) **   <a name="mediatailor-ListFunctions-request-uri-MaxResults"></a>
The maximum number of functions that you want MediaTailor to return in response to the current request. If there are more than `MaxResults` functions, use the value of `NextToken` in the response to get the next page of results.
The default value is 100. MediaTailor uses token-based pagination, which means that a response might contain fewer than `MaxResults` items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the `NextToken` value from each response until the response no longer includes a `NextToken` value.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListFunctions_RequestSyntax) **   <a name="mediatailor-ListFunctions-request-uri-NextToken"></a>
Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
For the first `ListFunctions` request, omit this value. For subsequent requests, get the value of `NextToken` from the previous response and specify that value for `NextToken` in the request. Continue making requests until the response no longer includes a `NextToken` value, which indicates that all results have been retrieved.

## Request Body
<a name="API_ListFunctions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFunctions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Arn": "string",
         "ConcurrentExecutorConfiguration": {
            "FunctionList": [
               {
                  "Alias": "string",
                  "FunctionId": "string",
                  "RunCondition": "string"
               }
            ],
            "MaxConcurrency": number,
            "Output": {
               "string" : "string"
            },
            "Runtime": "string",
            "TimeoutMilliseconds": number
         },
         "CustomOutputConfiguration": {
            "Output": {
               "string" : "string"
            },
            "Runtime": "string"
         },
         "Description": "string",
         "FunctionId": "string",
         "FunctionType": "string",
         "HttpRequestConfiguration": {
            "Body": "string",
            "Headers": {
               "string" : "string"
            },
            "MethodType": "string",
            "Output": {
               "string" : "string"
            },
            "RequestTimeoutMilliseconds": number,
            "Runtime": "string",
            "Url": "string"
         },
         "SequentialExecutorConfiguration": {
            "FunctionList": [
               {
                  "Alias": "string",
                  "FunctionId": "string",
                  "RunCondition": "string"
               }
            ],
            "Output": {
               "string" : "string"
            },
            "Runtime": "string",
            "TimeoutMilliseconds": number
         },
         "tags": {
            "string" : "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListFunctions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListFunctions_ResponseSyntax) **   <a name="mediatailor-ListFunctions-response-Items"></a>
A list of functions associated with your account in the current Region.
Type: Array of [Function](API_Function.md) objects

 ** [NextToken](#API_ListFunctions_ResponseSyntax) **   <a name="mediatailor-ListFunctions-response-NextToken"></a>
Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
For the first `ListFunctions` request, omit this value. For subsequent requests, get the value of `NextToken` from the previous response and specify that value for `NextToken` in the request. Continue making requests until the response no longer includes a `NextToken` value, which indicates that all results have been retrieved.
Type: String

## Errors
<a name="API_ListFunctions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListFunctions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/ListFunctions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/ListFunctions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/ListFunctions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/ListFunctions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/ListFunctions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/ListFunctions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/ListFunctions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/ListFunctions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/ListFunctions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/ListFunctions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
