---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatchResultEntry.html
---

# SendMessageBatchResultEntry
<a name="API_SendMessageBatchResultEntry"></a>

Encloses a `MessageId` for a successfully-enqueued message in a ` SendMessageBatch.`

## Contents
<a name="API_SendMessageBatchResultEntry_Contents"></a>

 ** Id **   <a name="SQS-Type-SendMessageBatchResultEntry-Id"></a>
An identifier for the message in this batch.
Type: String
Required: Yes

 ** MD5OfMessageBody **   <a name="SQS-Type-SendMessageBatchResultEntry-MD5OfMessageBody"></a>
An MD5 digest of the non-URL-encoded message body string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt).
Type: String
Required: Yes

 ** MessageId **   <a name="SQS-Type-SendMessageBatchResultEntry-MessageId"></a>
An identifier for the message.
Type: String
Required: Yes

 ** MD5OfMessageAttributes **   <a name="SQS-Type-SendMessageBatchResultEntry-MD5OfMessageAttributes"></a>
An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt).
Type: String
Required: No

 ** MD5OfMessageSystemAttributes **   <a name="SQS-Type-SendMessageBatchResultEntry-MD5OfMessageSystemAttributes"></a>
An MD5 digest of the non-URL-encoded message system attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt).
Type: String
Required: No

 ** SequenceNumber **   <a name="SQS-Type-SendMessageBatchResultEntry-SequenceNumber"></a>
This parameter applies only to FIFO (first-in-first-out) queues.
The large, non-consecutive number that Amazon SQS assigns to each message.
The length of `SequenceNumber` is 128 bits. As `SequenceNumber` continues to increase for a particular `MessageGroupId`.
Type: String
Required: No

## See Also
<a name="API_SendMessageBatchResultEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/SendMessageBatchResultEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/SendMessageBatchResultEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/SendMessageBatchResultEntry)
