---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SubscribeToShardEventStream.html
---

# SubscribeToShardEventStream
<a name="API_SubscribeToShardEventStream"></a>

This is a tagged union for all of the types of events an enhanced fan-out consumer can receive over HTTP/2 after a call to [SubscribeToShard](API_SubscribeToShard.md).

## Contents
<a name="API_SubscribeToShardEventStream_Contents"></a>

 ** SubscribeToShardEvent **   <a name="Streams-Type-SubscribeToShardEventStream-SubscribeToShardEvent"></a>
After you call [SubscribeToShard](API_SubscribeToShard.md), Kinesis Data Streams sends events of this type to your consumer. For an example of how to handle these events, see [Enhanced Fan-Out Using the Kinesis Data Streams API](/streams/latest/dev/building-enhanced-consumers-api.html).
Type: [SubscribeToShardEvent](API_SubscribeToShardEvent.md) object
Required: Yes

 ** InternalFailureException **   <a name="Streams-Type-SubscribeToShardEventStream-InternalFailureException"></a>
The processing of the request failed because of an unknown error, exception, or failure.
Type: Exception
HTTP Status Code:
Required: No

 ** KMSAccessDeniedException **   <a name="Streams-Type-SubscribeToShardEventStream-KMSAccessDeniedException"></a>
The ciphertext references a key that doesn't exist or that you don't have access to.
Type: Exception
HTTP Status Code:
Required: No

 ** KMSDisabledException **   <a name="Streams-Type-SubscribeToShardEventStream-KMSDisabledException"></a>
The request was rejected because the specified customer master key (CMK) isn't enabled.
Type: Exception
HTTP Status Code:
Required: No

 ** KMSInvalidStateException **   <a name="Streams-Type-SubscribeToShardEventStream-KMSInvalidStateException"></a>
The request was rejected because the state of the specified resource isn't valid for this request. For more information, see [How Key State Affects Use of a Customer Master Key](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.
Type: Exception
HTTP Status Code:
Required: No

 ** KMSNotFoundException **   <a name="Streams-Type-SubscribeToShardEventStream-KMSNotFoundException"></a>
The request was rejected because the specified entity or resource can't be found.
Type: Exception
HTTP Status Code:
Required: No

 ** KMSOptInRequired **   <a name="Streams-Type-SubscribeToShardEventStream-KMSOptInRequired"></a>
The AWS access key ID needs a subscription for the service.
Type: Exception
HTTP Status Code:
Required: No

 ** KMSThrottlingException **   <a name="Streams-Type-SubscribeToShardEventStream-KMSThrottlingException"></a>
The request was denied due to request throttling. For more information about throttling, see [Limits](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#requests-per-second) in the * AWS Key Management Service Developer Guide*.
Type: Exception
HTTP Status Code:
Required: No

 ** ResourceInUseException **   <a name="Streams-Type-SubscribeToShardEventStream-ResourceInUseException"></a>
The resource is not available for this operation. For successful operation, the resource must be in the `ACTIVE` state.
Type: Exception
HTTP Status Code:
Required: No

 ** ResourceNotFoundException **   <a name="Streams-Type-SubscribeToShardEventStream-ResourceNotFoundException"></a>
The requested resource could not be found. The stream might not be specified correctly.
Type: Exception
HTTP Status Code:
Required: No

## See Also
<a name="API_SubscribeToShardEventStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/SubscribeToShardEventStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/SubscribeToShardEventStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/SubscribeToShardEventStream)
