---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListQueues.html
---

# ListQueues
<a name="API_ListQueues"></a>

Returns a summary of each queue in the AWS account and Region used by the request. Use `StreamFilter` to list only the queues on a particular data stream.

If the response contains a `NextToken`, more queues are available. Call `ListQueues` again with that value to retrieve the next page.

## Request Syntax
<a name="API_ListQueues_RequestSyntax"></a>

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
<a name="API_ListQueues_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListQueues_RequestSyntax) **   <a name="Streams-ListQueues-request-MaxResults"></a>
The maximum number of queue summaries to return in one response. The response might contain fewer summaries than this value, and might contain a `NextToken` even when it contains fewer.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** [NextToken](#API_ListQueues_RequestSyntax) **   <a name="Streams-ListQueues-request-NextToken"></a>
The `NextToken` returned by a previous `ListQueues` request. Use it to retrieve the next page of queue summaries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Required: No

 ** [StreamFilter](#API_ListQueues_RequestSyntax) **   <a name="Streams-ListQueues-request-StreamFilter"></a>
Lists only the queues created on the specified data stream.
Type: Array of [QueueStreamFilter](API_QueueStreamFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10000 items.
Required: No

## Response Syntax
<a name="API_ListQueues_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "QueueSummaries": [
      {
         "QueueARN": "string",
         "QueueCreationTimestamp": number,
         "QueueName": "string",
         "QueueStatus": "string",
         "Streams": [
            {
               "StreamARN": "string",
               "StreamCreationTimestamp": number
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_ListQueues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListQueues_ResponseSyntax) **   <a name="Streams-ListQueues-response-NextToken"></a>
The token to pass to the next `ListQueues` request to retrieve the next page of queue summaries. This member is absent when no more queues are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.

 ** [QueueSummaries](#API_ListQueues_ResponseSyntax) **   <a name="Streams-ListQueues-response-QueueSummaries"></a>
A summary of each queue that matched the request.
Type: Array of [QueueSummary](API_QueueSummary.md) objects

## Errors
<a name="API_ListQueues_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Specifies that you do not have the permissions required to perform this operation.
HTTP Status Code: 400

 ** ExpiredNextTokenException **
The pagination token passed to the operation is expired.
HTTP Status Code: 400

 ** InternalFailureException **
The processing of the request failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

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
The request failed validation. For example, a parameter value is not valid, a combination of parameters is not supported, or the operation is not supported for the stream's capacity mode. The error message describes the specific reason.
HTTP Status Code: 400

## See Also
<a name="API_ListQueues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/ListQueues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/ListQueues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/ListQueues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/ListQueues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/ListQueues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/ListQueues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/ListQueues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/ListQueues)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListQueues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/ListQueues)
