---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListSourceLocations.html
---

# ListSourceLocations
<a name="API_ListSourceLocations"></a>

Lists the source locations for a channel. A source location defines the host server URL, and contains a list of sources.

## Request Syntax
<a name="API_ListSourceLocations_RequestSyntax"></a>

```
GET /sourceLocations?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSourceLocations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListSourceLocations_RequestSyntax) **   <a name="mediatailor-ListSourceLocations-request-uri-MaxResults"></a>
 The maximum number of source locations that you want MediaTailor to return in response to the current request. If there are more than `MaxResults` source locations, use the value of `NextToken` in the response to get the next page of results.
The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than `MaxResults` items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the `NextToken` value from each response until the response no longer includes a `NextToken` value.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListSourceLocations_RequestSyntax) **   <a name="mediatailor-ListSourceLocations-request-uri-NextToken"></a>
Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
For the first `ListSourceLocations` request, omit this value. For subsequent requests, get the value of `NextToken` from the previous response and specify that value for `NextToken` in the request. Continue making requests until the response no longer includes a `NextToken` value, which indicates that all results have been retrieved.

## Request Body
<a name="API_ListSourceLocations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSourceLocations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "AccessConfiguration": {
            "AccessType": "string",
            "SecretsManagerAccessTokenConfiguration": {
               "HeaderName": "string",
               "SecretArn": "string",
               "SecretStringKey": "string"
            }
         },
         "Arn": "string",
         "CreationTime": number,
         "DefaultSegmentDeliveryConfiguration": {
            "BaseUrl": "string"
         },
         "HttpConfiguration": {
            "BaseUrl": "string"
         },
         "LastModifiedTime": number,
         "SegmentDeliveryConfigurations": [
            {
               "BaseUrl": "string",
               "Name": "string"
            }
         ],
         "SourceLocationName": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListSourceLocations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListSourceLocations_ResponseSyntax) **   <a name="mediatailor-ListSourceLocations-response-Items"></a>
A list of source locations.
Type: Array of [SourceLocation](API_SourceLocation.md) objects

 ** [NextToken](#API_ListSourceLocations_ResponseSyntax) **   <a name="mediatailor-ListSourceLocations-response-NextToken"></a>
Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
Type: String

## Errors
<a name="API_ListSourceLocations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListSourceLocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/ListSourceLocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/ListSourceLocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/ListSourceLocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/ListSourceLocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/ListSourceLocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/ListSourceLocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/ListSourceLocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/ListSourceLocations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/ListSourceLocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/ListSourceLocations)
