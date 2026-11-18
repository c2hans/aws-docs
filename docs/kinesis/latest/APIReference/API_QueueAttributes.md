---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_QueueAttributes.html
---

# QueueAttributes
<a name="API_QueueAttributes"></a>

The configuration attributes for a queue.

## Contents
<a name="API_QueueAttributes_Contents"></a>

 ** DeadLetterConfiguration **   <a name="Streams-Type-QueueAttributes-DeadLetterConfiguration"></a>
The dead-letter handling configuration for the queue. If you omit this attribute, dead-letter handling is enabled with a `MaxReceiveCount` of 6. If you specify it with a `TargetType` of `BUILT_IN`, you must also specify `MaxReceiveCount`.
Type: [DeadLetterConfiguration](API_DeadLetterConfiguration.md) object
Required: No

 ** VisibilityTimeoutSeconds **   <a name="Streams-Type-QueueAttributes-VisibilityTimeoutSeconds"></a>
The duration, in seconds, that a record is in flight and not visible to any consumer instance after it is received. A record that is not acknowledged before this duration elapses becomes visible in the queue again and can be received by any consumer instance. If you omit this attribute when you create a queue, the queue uses 30 seconds.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 43200.
Required: No

## See Also
<a name="API_QueueAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/QueueAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/QueueAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/QueueAttributes)
