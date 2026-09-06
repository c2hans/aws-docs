---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateStreamWarmThroughput.html
---

# UpdateStreamWarmThroughput
<a name="API_UpdateStreamWarmThroughput"></a>

Updates the warm throughput configuration for the specified Amazon Kinesis Data Streams on-demand data stream. Updates the warm throughput configuration for the specified on-demand data stream. Use this operation to scale your stream to a specified throughput level before anticipated traffic spikes, or to release excess capacity after traffic has decreased.

**Note**
When invoking this API, you must use either the `StreamARN` or the `StreamName` parameter, or both. It is recommended that you use the `StreamARN` input parameter when you invoke this API.

Updating the warm throughput is an asynchronous operation. Upon receiving the request, Kinesis Data Streams returns immediately and sets the status of the stream to `UPDATING`. After the update is complete, Kinesis Data Streams sets the status of the stream back to `ACTIVE`. Depending on the size of the stream, the scaling action could take a few minutes to complete. You can continue to read and write data to your stream while its status is `UPDATING`.

This operation is only supported for data streams with the on-demand capacity mode in accounts that have `MinimumThroughputBillingCommitment` enabled. Provisioned capacity mode streams do not support warm throughput configuration.

To release excess capacity, call the API again and set the warm throughput to the same or a lower value.

This operation has the following default limits. By default, you cannot do the following:
+ Scale to more than 10 GiBps for an on-demand stream.
+ This API has a call limit of 5 transactions per second (TPS) for each AWS account. TPS over 5 will initiate the `LimitExceededException`.

For the default limits for an AWS account, see [Streams Limits](https://docs.aws.amazon.com/kinesis/latest/dev/service-sizes-and-limits.html) in the *Amazon Kinesis Data Streams Developer Guide*. To request an increase in the call rate limit, the shard limit for this API, or your overall shard limit, use the [limits form](https://console.aws.amazon.com/support/v1#/case/create?issueType=service-limit-increase&limitType=service-code-kinesis).

## Request Syntax
<a name="API_UpdateStreamWarmThroughput_RequestSyntax"></a>

```
{
   "StreamARN": "{{string}}",
   "StreamId": "{{string}}",
   "StreamName": "{{string}}",
   "WarmThroughputMiBps": {{number}}
}
```

## Request Parameters
<a name="API_UpdateStreamWarmThroughput_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [StreamARN](#API_UpdateStreamWarmThroughput_RequestSyntax) **   <a name="Streams-UpdateStreamWarmThroughput-request-StreamARN"></a>
The ARN of the stream to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
Required: No

 ** [StreamId](#API_UpdateStreamWarmThroughput_RequestSyntax) **   <a name="Streams-UpdateStreamWarmThroughput-request-StreamId"></a>
Not Implemented. Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `[a-z0-9]{20}-[a-z0-9]{3}`
Required: No

 ** [StreamName](#API_UpdateStreamWarmThroughput_RequestSyntax) **   <a name="Streams-UpdateStreamWarmThroughput-request-StreamName"></a>
The name of the stream to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [WarmThroughputMiBps](#API_UpdateStreamWarmThroughput_RequestSyntax) **   <a name="Streams-UpdateStreamWarmThroughput-request-WarmThroughputMiBps"></a>
The target warm throughput in MB/s that the stream should be scaled to handle. This represents the throughput capacity that will be immediately available for write operations.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

## Response Syntax
<a name="API_UpdateStreamWarmThroughput_ResponseSyntax"></a>

```
{
   "StreamARN": "string",
   "StreamName": "string",
   "WarmThroughput": {
      "CurrentMiBps": number,
      "TargetMiBps": number
   }
}
```

## Response Elements
<a name="API_UpdateStreamWarmThroughput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StreamARN](#API_UpdateStreamWarmThroughput_ResponseSyntax) **   <a name="Streams-UpdateStreamWarmThroughput-response-StreamARN"></a>
The ARN of the stream that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`

 ** [StreamName](#API_UpdateStreamWarmThroughput_ResponseSyntax) **   <a name="Streams-UpdateStreamWarmThroughput-response-StreamName"></a>
The name of the stream that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [WarmThroughput](#API_UpdateStreamWarmThroughput_ResponseSyntax) **   <a name="Streams-UpdateStreamWarmThroughput-response-WarmThroughput"></a>
Specifies the updated warm throughput configuration for your data stream.
Type: [WarmThroughputObject](API_WarmThroughputObject.md) object

## Errors
<a name="API_UpdateStreamWarmThroughput_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Specifies that you do not have the permissions required to perform this operation.
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

 ** ValidationException **
Specifies that you tried to invoke this API for a data stream with the on-demand capacity mode. This API is only supported for data streams with the provisioned capacity mode.
HTTP Status Code: 400

## See Also
<a name="API_UpdateStreamWarmThroughput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-2013-12-02/UpdateStreamWarmThroughput)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-2013-12-02/UpdateStreamWarmThroughput)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/UpdateStreamWarmThroughput)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-2013-12-02/UpdateStreamWarmThroughput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/UpdateStreamWarmThroughput)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-2013-12-02/UpdateStreamWarmThroughput)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-2013-12-02/UpdateStreamWarmThroughput)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-2013-12-02/UpdateStreamWarmThroughput)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/UpdateStreamWarmThroughput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/UpdateStreamWarmThroughput)
