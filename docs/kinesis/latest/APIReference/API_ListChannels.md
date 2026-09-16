---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListChannels.html
---

# ListChannels
<a name="API_ListChannels"></a>

Lists the channels in your account. You can filter the results by source stream. The results are paginated. Use the `NextToken` value returned in the response to retrieve additional results.

Use this operation to find channels before deleting a stream, or to audit the channels configured in an AWS Region.

This operation has a call limit of 5 transactions per second (TPS) for each AWS account. Exceeding 5 TPS results in a `LimitExceededException`.

## Request Syntax
<a name="API_ListChannels_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StreamFilter": [
      {
         "StreamARN": "{{string}}",
         "StreamCreationTimestamp": {{number}}
      }
   ]
}
```

## Request Parameters
<a name="API_ListChannels_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListChannels_RequestSyntax) **   <a name="Streams-ListChannels-request-MaxResults"></a>
The maximum number of channels to return in a single call. The default value is 100. If you specify a value greater than 100, at most 100 results are returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** [NextToken](#API_ListChannels_RequestSyntax) **   <a name="Streams-ListChannels-request-NextToken"></a>
The pagination token returned by a previous call. Specify this token to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Required: No

 ** [StreamFilter](#API_ListChannels_RequestSyntax) **   <a name="Streams-ListChannels-request-StreamFilter"></a>
Filters the results to channels associated with the specified streams.
Type: Array of [StreamFilter](API_StreamFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10000 items.
Required: No

## Response Syntax
<a name="API_ListChannels_ResponseSyntax"></a>

```
{
   "ChannelSummaries": [
      {
         "ChannelARN": "string",
         "ChannelCreationTimestamp": number,
         "ChannelDestinationType": "string",
         "ChannelId": "string",
         "ChannelName": "string",
         "ChannelStatus": "string",
         "ChannelStatusReason": "string",
         "Streams": [
            {
               "StreamARN": "string",
               "StreamCreationTimestamp": number
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListChannels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChannelSummaries](#API_ListChannels_ResponseSyntax) **   <a name="Streams-ListChannels-response-ChannelSummaries"></a>
A list of channel summaries.
Type: Array of [ChannelSummary](API_ChannelSummary.md) objects

 ** [NextToken](#API_ListChannels_ResponseSyntax) **   <a name="Streams-ListChannels-response-NextToken"></a>
The pagination token to use in a subsequent call to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.

## Errors
<a name="API_ListChannels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Specifies that you do not have the permissions required to perform this operation.
HTTP Status Code: 400

 ** ExpiredNextTokenException **
The pagination token passed to the operation is expired.
HTTP Status Code: 400

 ** InvalidArgumentException **
A specified parameter exceeds its restrictions, is not supported, or can't be used. For more information, see the returned message.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** LimitExceededException **
The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ValidationException **
Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode.
HTTP Status Code: 400

## See Also
<a name="API_ListChannels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/ListChannels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/ListChannels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/ListChannels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/ListChannels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/ListChannels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/ListChannels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/ListChannels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/ListChannels)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListChannels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/ListChannels)
