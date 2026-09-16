---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListOfferings.html
---

# ListOfferings
<a name="API_ListOfferings"></a>

 Displays a list of all offerings that are available to this account in the current AWS Region. If you have an active reservation (which means you've purchased an offering that has already started and hasn't expired yet), your account isn't eligible for other offerings.

## Request Syntax
<a name="API_ListOfferings_RequestSyntax"></a>

```
GET /v1/offerings?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListOfferings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListOfferings_RequestSyntax) **   <a name="mediaconnect-ListOfferings-request-uri-maxResults"></a>
 The maximum number of results to return per API request.
For example, you submit a `ListOfferings` request with `MaxResults` set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a `NextToken` value that you can use to fetch the next batch of results.)
The service might return fewer results than the `MaxResults` value. If `MaxResults` is not included in the request, the service defaults to pagination with a maximum of 10 results per page.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListOfferings_RequestSyntax) **   <a name="mediaconnect-ListOfferings-request-uri-nextToken"></a>
 The token that identifies the batch of results that you want to see.
For example, you submit a `ListOfferings` request with `MaxResults` set at 5. The service returns the first batch of results (up to 5) and a `NextToken` value. To see the next batch of results, you can submit the `ListOfferings` request a second time and specify the `NextToken` value.

## Request Body
<a name="API_ListOfferings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListOfferings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "offerings": [
      {
         "currencyCode": "string",
         "duration": number,
         "durationUnits": "string",
         "offeringArn": "string",
         "offeringDescription": "string",
         "pricePerUnit": "string",
         "priceUnits": "string",
         "resourceSpecification": {
            "reservedBitrate": number,
            "resourceType": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListOfferings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListOfferings_ResponseSyntax) **   <a name="mediaconnect-ListOfferings-response-nextToken"></a>
 The token that identifies the batch of results that you want to see.
For example, you submit a `ListOfferings` request with `MaxResults` set at 5. The service returns the first batch of results (up to 5) and a `NextToken` value. To see the next batch of results, you can submit the `ListOfferings` request a second time and specify the `NextToken` value.
Type: String

 ** [offerings](#API_ListOfferings_ResponseSyntax) **   <a name="mediaconnect-ListOfferings-response-offerings"></a>
 A list of offerings that are available to this account in the current AWS Region.
Type: Array of [Offering](API_Offering.md) objects

## Errors
<a name="API_ListOfferings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

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
<a name="API_ListOfferings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/ListOfferings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/ListOfferings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ListOfferings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/ListOfferings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ListOfferings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/ListOfferings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/ListOfferings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/ListOfferings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/ListOfferings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ListOfferings)
