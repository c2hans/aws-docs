---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ListChannels.html
---

# ListChannels
<a name="API_ListChannels"></a>

Retrieves information about the channels that are associated with the current AWS account.

## Request Syntax
<a name="API_ListChannels_RequestSyntax"></a>

```
GET /channels?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListChannels_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListChannels_RequestSyntax) **   <a name="mediatailor-ListChannels-request-uri-MaxResults"></a>
The maximum number of channels that you want MediaTailor to return in response to the current request. If there are more than `MaxResults` channels, use the value of `NextToken` in the response to get the next page of results.
The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than `MaxResults` items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the `NextToken` value from each response until the response no longer includes a `NextToken` value.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListChannels_RequestSyntax) **   <a name="mediatailor-ListChannels-request-uri-NextToken"></a>
Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
For the first `ListChannels` request, omit this value. For subsequent requests, get the value of `NextToken` from the previous response and specify that value for `NextToken` in the request. Continue making requests until the response no longer includes a `NextToken` value, which indicates that all results have been retrieved.

## Request Body
<a name="API_ListChannels_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListChannels_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Arn": "string",
         "Audiences": [ "string" ],
         "ChannelName": "string",
         "ChannelState": "string",
         "CreationTime": number,
         "FillerSlate": {
            "SourceLocationName": "string",
            "VodSourceName": "string"
         },
         "LastModifiedTime": number,
         "LogConfiguration": {
            "LogTypes": [ "string" ]
         },
         "Outputs": [
            {
               "DashPlaylistSettings": {
                  "ManifestWindowSeconds": number,
                  "MinBufferTimeSeconds": number,
                  "MinUpdatePeriodSeconds": number,
                  "SuggestedPresentationDelaySeconds": number
               },
               "DualStackPlaybackUrl": "string",
               "HlsPlaylistSettings": {
                  "AdMarkupType": [ "string" ],
                  "ManifestWindowSeconds": number
               },
               "ManifestName": "string",
               "PlaybackUrl": "string",
               "SourceGroup": "string"
            }
         ],
         "PlaybackMode": "string",
         "tags": {
            "string" : "string"
         },
         "Tier": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListChannels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListChannels_ResponseSyntax) **   <a name="mediatailor-ListChannels-response-Items"></a>
A list of channels that are associated with this account.
Type: Array of [Channel](API_Channel.md) objects

 ** [NextToken](#API_ListChannels_ResponseSyntax) **   <a name="mediatailor-ListChannels-response-NextToken"></a>
Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
Type: String

## Errors
<a name="API_ListChannels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListChannels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/ListChannels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/ListChannels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/ListChannels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/ListChannels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/ListChannels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/ListChannels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/ListChannels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/ListChannels)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/ListChannels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/ListChannels)
