---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_ListAppBundles.html
---

# ListAppBundles
<a name="API_ListAppBundles"></a>

Returns a list of app bundles.

## Request Syntax
<a name="API_ListAppBundles_RequestSyntax"></a>

```
GET /appbundles?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAppBundles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAppBundles_RequestSyntax) **   <a name="appfabric-ListAppBundles-request-uri-maxResults"></a>
The maximum number of results that are returned per call. You can use `nextToken` to obtain further pages of results.
This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAppBundles_RequestSyntax) **   <a name="appfabric-ListAppBundles-request-uri-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken error*.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_ListAppBundles_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAppBundles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appBundleSummaryList": [
      {
         "arn": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAppBundles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appBundleSummaryList](#API_ListAppBundles_ResponseSyntax) **   <a name="appfabric-ListAppBundles-response-appBundleSummaryList"></a>
Contains a list of app bundle summaries.
Type: Array of [AppBundleSummary](API_AppBundleSummary.md) objects

 ** [nextToken](#API_ListAppBundles_ResponseSyntax) **   <a name="appfabric-ListAppBundles-response-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken error*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListAppBundles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure with an internal server.
 ** retryAfterSeconds **
The period of time after which you should retry your request.
HTTP Status Code: 500

 ** ThrottlingException **
The request rate exceeds the limit.
 ** quotaCode **
The code for the quota exceeded.
 ** retryAfterSeconds **
The period of time after which you should retry your request.
 ** serviceCode **
The code of the service.
HTTP Status Code: 429

 ** ValidationException **
The request has invalid or missing parameters.
 ** fieldList **
The field list.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListAppBundles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appfabric-2023-05-19/ListAppBundles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appfabric-2023-05-19/ListAppBundles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/ListAppBundles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appfabric-2023-05-19/ListAppBundles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/ListAppBundles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appfabric-2023-05-19/ListAppBundles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appfabric-2023-05-19/ListAppBundles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appfabric-2023-05-19/ListAppBundles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appfabric-2023-05-19/ListAppBundles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/ListAppBundles)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
