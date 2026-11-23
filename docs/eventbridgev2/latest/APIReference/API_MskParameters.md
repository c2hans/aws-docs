---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_MskParameters.html
---

# MskParameters

MSK (Apache Kafka) invocation parameters for subscribers targeting an Amazon MSK cluster.

## Contents
<a name="API_MskParameters_Contents"></a>

 ** Connectivity **   <a name="eventbridgev2-Type-MskParameters-Connectivity"></a>
How the service connects to the cluster. A cluster can have public access and multi-VPC private connectivity turned on at the same time, so the subscriber names the one to use. That path must be turned on, with IAM access control, on the cluster.
Type: String
Valid Values: `PUBLIC | PRIVATE`
Required: Yes

 ** TopicName **   <a name="eventbridgev2-Type-MskParameters-TopicName"></a>
Name of the Kafka topic events are produced to. Accepts a literal or a JSONata expression resolved once per delivered event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: Yes

 ** Acks **   <a name="eventbridgev2-Type-MskParameters-Acks"></a>
Producer acknowledgement mode. Defaults to ALL.
Type: String
Valid Values: `ALL | LEADER`
Required: No

 ** ClientId **   <a name="eventbridgev2-Type-MskParameters-ClientId"></a>
Producer client.id passed to the Kafka broker. Identifies the producer in broker-side logs, metrics, and quota enforcement. A literal, not a JSONata expression: it is a connection-level setting resolved once when the producer is created, not per event. If you do not set it, EventBridge uses the subscriber ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Compression **   <a name="eventbridgev2-Type-MskParameters-Compression"></a>
Producer compression codec applied to the record batch. Defaults to NONE.
Type: String
Valid Values: `NONE | GZIP | SNAPPY | LZ4 | ZSTD`
Required: No

 ** Headers **   <a name="eventbridgev2-Type-MskParameters-Headers"></a>
Kafka record headers attached to each produced record.
Type: Array of [MskHeader](API_MskHeader.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** PartitionKey **   <a name="eventbridgev2-Type-MskParameters-PartitionKey"></a>
Kafka record key. Accepts a literal or a JSONata expression (for example, "{% $events.data.customerId %}") resolved once per delivered event; the resolved value selects the destination partition. If you omit it, the producer selects the partition; on an ordered (FIFO) subscriber, EventBridge instead uses the event group ID as the record key to preserve ordering.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

## See Also
<a name="API_MskParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/MskParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/MskParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/MskParameters)
