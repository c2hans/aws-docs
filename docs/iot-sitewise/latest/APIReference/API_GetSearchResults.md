---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetSearchResults.html
---

# GetSearchResults
<a name="API_GetSearchResults"></a>

Retrieves the ranked results of a search, ordered by descending relevance score. Results are available only after the search has reached the `SUCCEEDED` status. Calling this on a search that exists but has not yet completed returns `InvalidRequestException`, while calling it on a search that does not exist returns `ResourceNotFoundException`. The response is paginated: when `nextToken` is present, pass it on a subsequent call to retrieve the next page.

## Request Syntax
<a name="API_GetSearchResults_RequestSyntax"></a>

```
GET /workspaces/{{workspaceName}}/searches/{{searchId}}/results?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSearchResults_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_GetSearchResults_RequestSyntax) **   <a name="iotsitewise-GetSearchResults-request-uri-maxResults"></a>
The maximum number of results to return in a single page. Valid range is 1 to 10,000; if omitted, a service-defined default is used.
Valid Range: Minimum value of 1. Maximum value of 10000.

 ** [nextToken](#API_GetSearchResults_RequestSyntax) **   <a name="iotsitewise-GetSearchResults-request-uri-nextToken"></a>
The pagination token returned by a previous GetSearchResults call. Provide it to retrieve the next page of results; omit it to retrieve the first page.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

 ** [searchId](#API_GetSearchResults_RequestSyntax) **   <a name="iotsitewise-GetSearchResults-request-uri-searchId"></a>
The identifier of the search whose results are retrieved.
Length Constraints: Minimum length of 23. Maximum length of 36.
Pattern: `[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*`
Required: Yes

 ** [workspaceName](#API_GetSearchResults_RequestSyntax) **   <a name="iotsitewise-GetSearchResults-request-uri-workspaceName"></a>
The name of the workspace the search belongs to.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_GetSearchResults_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSearchResults_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "searchResults": [
      {
         "datasetId": "string",
         "endTimestamp": {
            "offsetInNanos": number,
            "timeInSeconds": number
         },
         "score": number,
         "searchId": "string",
         "startTimestamp": {
            "offsetInNanos": number,
            "timeInSeconds": number
         },
         "timeSeriesId": "string",
         "topTimestamp": {
            "offsetInNanos": number,
            "timeInSeconds": number
         },
         "workspaceName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetSearchResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetSearchResults_ResponseSyntax) **   <a name="iotsitewise-GetSearchResults-response-nextToken"></a>
The pagination token to use in a subsequent GetSearchResults call to retrieve the next page. Absent when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

 ** [searchResults](#API_GetSearchResults_ResponseSyntax) **   <a name="iotsitewise-GetSearchResults-response-searchResults"></a>
A page of search results, ordered by descending relevance score.
Type: Array of [SearchResult](API_SearchResult.md) objects

## Errors
<a name="API_GetSearchResults_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_GetSearchResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/GetSearchResults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/GetSearchResults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/GetSearchResults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/GetSearchResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/GetSearchResults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/GetSearchResults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/GetSearchResults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/GetSearchResults)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/GetSearchResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/GetSearchResults)
