---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListBridges.html
---

# ListBridges
<a name="API_ListBridges"></a>

 Displays a list of bridges that are associated with this account and an optionally specified Amazon Resource Name (ARN). This request returns a paginated result.

## Request Syntax
<a name="API_ListBridges_RequestSyntax"></a>

```
GET /v1/bridges?filterArn={{filterArn}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBridges_RequestParameters"></a>

The request uses the following URI parameters.

 ** [filterArn](#API_ListBridges_RequestSyntax) **   <a name="mediaconnect-ListBridges-request-uri-filterArn"></a>
 Filter the list results to display only the bridges associated with the selected ARN.

 ** [maxResults](#API_ListBridges_RequestSyntax) **   <a name="mediaconnect-ListBridges-request-uri-maxResults"></a>
 The maximum number of results to return per API request.
For example, you submit a `ListBridges` request with `MaxResults` set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a `NextToken` value that you can use to fetch the next batch of results.)
The service might return fewer results than the `MaxResults` value. If `MaxResults` is not included in the request, the service defaults to pagination with a maximum of 10 results per page.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListBridges_RequestSyntax) **   <a name="mediaconnect-ListBridges-request-uri-nextToken"></a>
 The token that identifies the batch of results that you want to see.
For example, you submit a `ListBridges` request with `MaxResults` set at 5. The service returns the first batch of results (up to 5) and a `NextToken` value. To see the next batch of results, you can submit the `ListBridges` request a second time and specify the `NextToken` value.

## Request Body
<a name="API_ListBridges_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBridges_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "bridges": [
      {
         "bridgeArn": "string",
         "bridgeState": "string",
         "bridgeType": "string",
         "name": "string",
         "placementArn": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBridges_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [bridges](#API_ListBridges_ResponseSyntax) **   <a name="mediaconnect-ListBridges-response-bridges"></a>
 A list of bridge summaries.
Type: Array of [ListedBridge](API_ListedBridge.md) objects

 ** [nextToken](#API_ListBridges_ResponseSyntax) **   <a name="mediaconnect-ListBridges-response-nextToken"></a>
 The token that identifies the batch of results that you want to see.
For example, you submit a `ListBridges` request with `MaxResults` set at 5. The service returns the first batch of results (up to 5) and a `NextToken` value. To see the next batch of results, you can submit the `ListBridges` request a second time and specify the `NextToken` value.
Type: String

## Errors
<a name="API_ListBridges_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_ListBridges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/ListBridges)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/ListBridges)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ListBridges)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/ListBridges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ListBridges)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/ListBridges)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/ListBridges)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/ListBridges)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/ListBridges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ListBridges)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
