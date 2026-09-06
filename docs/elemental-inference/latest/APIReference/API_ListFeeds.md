---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ListFeeds.html
---

# ListFeeds
<a name="API_ListFeeds"></a>

Displays a list of feeds that belong to this AWS account.

## Request Syntax
<a name="API_ListFeeds_RequestSyntax"></a>

```
GET /v1/feeds?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFeeds_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListFeeds_RequestSyntax) **   <a name="elementalinference-ListFeeds-request-uri-maxResults"></a>
The maximum number of results to return per API request.
For example, you submit a list request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.)
The service might return fewer results than the MaxResults value. If MaxResults is not included in the request, the service defaults to pagination with a maximum of 10 results per page.
Valid Range: Minimum value of 1. Maximum value of 1000.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListFeeds_RequestSyntax) **   <a name="elementalinference-ListFeeds-request-uri-nextToken"></a>
The token that identifies the batch of results that you want to see.
For example, you submit a ListFeeds request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListFeeds request a second time and specify the NextToken value.

## Request Body
<a name="API_ListFeeds_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFeeds_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "feeds": [
      {
         "arn": "string",
         "association": {
            "associatedResourceName": "string"
         },
         "id": "string",
         "name": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListFeeds_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [feeds](#API_ListFeeds_ResponseSyntax) **   <a name="elementalinference-ListFeeds-response-feeds"></a>
A list of FeedSummary objects.
Type: Array of [FeedSummary](API_FeedSummary.md) objects

 ** [nextToken](#API_ListFeeds_ResponseSyntax) **   <a name="elementalinference-ListFeeds-response-nextToken"></a>
The token that identifies the batch of results that you want to see. For example, you submit a list request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the list request a second time and specify the NextToken value.
Type: String

## Errors
<a name="API_ListFeeds_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
An internal server error occurred. This is a temporary condition and the request can be retried. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource specified in the action doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestException **
The request was denied due to request throttling. Too many requests have been made within a given time period. Reduce the frequency of requests and use exponential backoff when retrying.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check the error message for details about which parameter or field is invalid and correct the request before retrying.
HTTP Status Code: 400

## See Also
<a name="API_ListFeeds_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elementalinference-2018-11-14/ListFeeds)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elementalinference-2018-11-14/ListFeeds)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/ListFeeds)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elementalinference-2018-11-14/ListFeeds)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/ListFeeds)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elementalinference-2018-11-14/ListFeeds)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elementalinference-2018-11-14/ListFeeds)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elementalinference-2018-11-14/ListFeeds)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elementalinference-2018-11-14/ListFeeds)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/ListFeeds)
