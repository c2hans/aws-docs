---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamConsumer.html
---

# DescribeStreamConsumer
<a name="API_DescribeStreamConsumer"></a>

To get the description of a registered consumer, provide the ARN of the consumer. Alternatively, you can provide the ARN of the data stream and the name you gave the consumer when you registered it. You may also provide all three parameters, as long as they don't conflict with each other. If you don't know the name or ARN of the consumer that you want to describe, you can use the [ListStreamConsumers](API_ListStreamConsumers.md) operation to get a list of the descriptions of all the consumers that are currently registered with a given data stream.

This operation has a limit of 20 transactions per second per stream.

**Note**
When making a cross-account call with `DescribeStreamConsumer`, make sure to provide the ARN of the consumer.

## Request Syntax
<a name="API_DescribeStreamConsumer_RequestSyntax"></a>

```
{
   "ConsumerARN": "{{string}}",
   "ConsumerName": "{{string}}",
   "StreamARN": "{{string}}",
   "StreamId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeStreamConsumer_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ConsumerARN](#API_DescribeStreamConsumer_RequestSyntax) **   <a name="Streams-DescribeStreamConsumer-request-ConsumerARN"></a>
The ARN returned by Kinesis Data Streams when you registered the consumer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(arn):aws.*:kinesis:.*:\d{12}:.*stream\/[a-zA-Z0-9_.-]+\/consumer\/[a-zA-Z0-9_.-]+:[0-9]+`
Required: No

 ** [ConsumerName](#API_DescribeStreamConsumer_RequestSyntax) **   <a name="Streams-DescribeStreamConsumer-request-ConsumerName"></a>
The name that you gave to the consumer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [StreamARN](#API_DescribeStreamConsumer_RequestSyntax) **   <a name="Streams-DescribeStreamConsumer-request-StreamARN"></a>
The ARN of the Kinesis data stream that the consumer is registered with. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: No

 ** [StreamId](#API_DescribeStreamConsumer_RequestSyntax) **   <a name="Streams-DescribeStreamConsumer-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

## Response Syntax
<a name="API_DescribeStreamConsumer_ResponseSyntax"></a>

```
{
   "ConsumerDescription": {
      "ConsumerARN": "string",
      "ConsumerCreationTimestamp": number,
      "ConsumerName": "string",
      "ConsumerStatus": "string",
      "StreamARN": "string"
   }
}
```

## Response Elements
<a name="API_DescribeStreamConsumer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConsumerDescription](#API_DescribeStreamConsumer_ResponseSyntax) **   <a name="Streams-DescribeStreamConsumer-response-ConsumerDescription"></a>
An object that represents the details of the consumer.
Type: [ConsumerDescription](API_ConsumerDescription.md) object

## Errors
<a name="API_DescribeStreamConsumer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNotFoundException **
The requested resource could not be found. The stream might not be specified correctly.
 ** message **
A message that provides information about the error.
HTTP Status Code: 400

## See Also
<a name="API_DescribeStreamConsumer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/DescribeStreamConsumer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/DescribeStreamConsumer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/DescribeStreamConsumer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/DescribeStreamConsumer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/DescribeStreamConsumer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/DescribeStreamConsumer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/DescribeStreamConsumer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/DescribeStreamConsumer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DescribeStreamConsumer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/DescribeStreamConsumer)
