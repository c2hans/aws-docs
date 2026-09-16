---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreamConsumers.html
---

# ListStreamConsumers
<a name="API_ListStreamConsumers"></a>

Lists the consumers registered to receive data from a stream using enhanced fan-out, and provides information about each consumer.

This operation has a limit of 5 transactions per second per stream.

## Request Syntax
<a name="API_ListStreamConsumers_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StreamARN": "{{string}}",
   "StreamCreationTimestamp": {{number}},
   "StreamId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListStreamConsumers_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListStreamConsumers_RequestSyntax) **   <a name="Streams-ListStreamConsumers-request-MaxResults"></a>
The maximum number of consumers that you want a single call of `ListStreamConsumers` to return. The default value is 100. If you specify a value greater than 100, at most 100 results are returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** [NextToken](#API_ListStreamConsumers_RequestSyntax) **   <a name="Streams-ListStreamConsumers-request-NextToken"></a>
When the number of consumers that are registered with the data stream is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of consumers that are registered with the data stream, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListStreamConsumers` to list the next set of registered consumers.
Don't specify `StreamName` or `StreamCreationTimestamp` if you specify `NextToken` because the latter unambiguously identifies the stream.
You can optionally specify a value for the `MaxResults` parameter when you specify `NextToken`. If you specify a `MaxResults` value that is less than the number of consumers that the operation returns if you don't specify `MaxResults`, the response will contain a new `NextToken` value. You can use the new `NextToken` value in a subsequent call to the `ListStreamConsumers` operation to list the next set of consumers.
Tokens expire after 300 seconds. When you obtain a value for `NextToken` in the response to a call to `ListStreamConsumers`, you have 300 seconds to use that value. If you specify an expired token in a call to `ListStreamConsumers`, you get `ExpiredNextTokenException`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Required: No

 ** [StreamARN](#API_ListStreamConsumers_RequestSyntax) **   <a name="Streams-ListStreamConsumers-request-StreamARN"></a>
The ARN of the Kinesis data stream for which you want to list the registered consumers. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: Yes

 ** [StreamCreationTimestamp](#API_ListStreamConsumers_RequestSyntax) **   <a name="Streams-ListStreamConsumers-request-StreamCreationTimestamp"></a>
Specify this input parameter to distinguish data streams that have the same name. For example, if you create a data stream and then delete it, and you later create another data stream with the same name, you can use this input parameter to specify which of the two streams you want to list the consumers for.
You can't specify this parameter if you specify the NextToken parameter.
Type: Timestamp
Required: No

 ** [StreamId](#API_ListStreamConsumers_RequestSyntax) **   <a name="Streams-ListStreamConsumers-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

## Response Syntax
<a name="API_ListStreamConsumers_ResponseSyntax"></a>

```
{
   "Consumers": [
      {
         "ConsumerARN": "string",
         "ConsumerCreationTimestamp": number,
         "ConsumerName": "string",
         "ConsumerStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListStreamConsumers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Consumers](#API_ListStreamConsumers_ResponseSyntax) **   <a name="Streams-ListStreamConsumers-response-Consumers"></a>
An array of JSON objects. Each object represents one registered consumer.
Type: Array of [Consumer](API_Consumer.md) objects

 ** [NextToken](#API_ListStreamConsumers_ResponseSyntax) **   <a name="Streams-ListStreamConsumers-response-NextToken"></a>
When the number of consumers that are registered with the data stream is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of registered consumers, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListStreamConsumers` to list the next set of registered consumers. For more information about the use of this pagination token when calling the `ListStreamConsumers` operation, see [ListStreamConsumers:NextToken](#Streams-ListStreamConsumers-request-NextToken).
Tokens expire after 300 seconds. When you obtain a value for `NextToken` in the response to a call to `ListStreamConsumers`, you have 300 seconds to use that value. If you specify an expired token in a call to `ListStreamConsumers`, you get `ExpiredNextTokenException`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.

## Errors
<a name="API_ListStreamConsumers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceInUseException **
The resource is not available for this operation. For successful operation, the resource must be in the `ACTIVE` state.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found. The stream might not be specified correctly.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## See Also
<a name="API_ListStreamConsumers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/ListStreamConsumers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/ListStreamConsumers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/ListStreamConsumers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/ListStreamConsumers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/ListStreamConsumers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/ListStreamConsumers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/ListStreamConsumers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/ListStreamConsumers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListStreamConsumers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/ListStreamConsumers)
