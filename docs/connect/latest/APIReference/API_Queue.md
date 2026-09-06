---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Queue.html
---

# Queue
<a name="API_Queue"></a>

Contains information about a queue.

## Contents
<a name="API_Queue_Contents"></a>

 ** Description **   <a name="connect-Type-Queue-Description"></a>
The description of the queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** HoursOfOperationId **   <a name="connect-Type-Queue-HoursOfOperationId"></a>
The identifier for the hours of operation.
Type: String
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-Queue-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-Queue-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** MaxContacts **   <a name="connect-Type-Queue-MaxContacts"></a>
The maximum number of contacts that can be in the queue before it is considered full.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Name **   <a name="connect-Type-Queue-Name"></a>
The name of the queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

 ** OutboundCallerConfig **   <a name="connect-Type-Queue-OutboundCallerConfig"></a>
The outbound caller ID name, number, and outbound whisper flow.
Type: [OutboundCallerConfig](API_OutboundCallerConfig.md) object
Required: No

 ** OutboundEmailConfig **   <a name="connect-Type-Queue-OutboundEmailConfig"></a>
The outbound email address ID for a specified queue.
Type: [OutboundEmailConfig](API_OutboundEmailConfig.md) object
Required: No

 ** QueueArn **   <a name="connect-Type-Queue-QueueArn"></a>
The Amazon Resource Name (ARN) for the queue.
Type: String
Required: No

 ** QueueId **   <a name="connect-Type-Queue-QueueId"></a>
The identifier for the queue.
Type: String
Required: No

 ** Status **   <a name="connect-Type-Queue-Status"></a>
The status of the queue.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** Tags **   <a name="connect-Type-Queue-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_Queue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Queue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Queue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Queue)
