---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_Message.html
---

# Message
<a name="API_Message"></a>

An Amazon SQS message.

## Contents
<a name="API_Message_Contents"></a>

 ** Attributes **   <a name="SQS-Type-Message-Attributes"></a>
A map of the attributes requested in ` ReceiveMessage ` to their respective values. Supported attributes:
+  `ApproximateReceiveCount`
+  `ApproximateFirstReceiveTimestamp`
+  `MessageDeduplicationId`
+  `MessageGroupId`
+  `SenderId`
+  `SentTimestamp`
+  `SequenceNumber`
 `ApproximateFirstReceiveTimestamp` and `SentTimestamp` are each returned as an integer representing the [epoch time](http://en.wikipedia.org/wiki/Unix_time) in milliseconds.
Type: String to string map
Valid Keys: `All | SenderId | SentTimestamp | ApproximateReceiveCount | ApproximateFirstReceiveTimestamp | SequenceNumber | MessageDeduplicationId | MessageGroupId | AWSTraceHeader | DeadLetterQueueSourceArn`
Required: No

 ** Body **   <a name="SQS-Type-Message-Body"></a>
The message's contents (not URL-encoded).
Type: String
Required: No

 ** MD5OfBody **   <a name="SQS-Type-Message-MD5OfBody"></a>
An MD5 digest of the non-URL-encoded message body string.
Type: String
Required: No

 ** MD5OfMessageAttributes **   <a name="SQS-Type-Message-MD5OfMessageAttributes"></a>
An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see [RFC1321](https://www.ietf.org/rfc/rfc1321.txt).
Type: String
Required: No

 ** MessageAttributes **   <a name="SQS-Type-Message-MessageAttributes"></a>
Each message attribute consists of a `Name`, `Type`, and `Value`. For more information, see [Amazon SQS message attributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html#sqs-message-attributes) in the *Amazon SQS Developer Guide*.
Type: String to [MessageAttributeValue](API_MessageAttributeValue.md) object map
Required: No

 ** MessageId **   <a name="SQS-Type-Message-MessageId"></a>
A unique identifier for the message. A `MessageId`is considered unique across all AWS accounts for an extended period of time.
Type: String
Required: No

 ** ReceiptHandle **   <a name="SQS-Type-Message-ReceiptHandle"></a>
An identifier associated with the act of receiving the message. A new receipt handle is returned every time you receive a message. When deleting a message, you provide the last received receipt handle to delete the message.
Type: String
Required: No

## See Also
<a name="API_Message_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sqs-2012-11-05/Message)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sqs-2012-11-05/Message)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sqs-2012-11-05/Message)
