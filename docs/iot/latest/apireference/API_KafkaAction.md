---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_KafkaAction.html
---

# KafkaAction
<a name="API_KafkaAction"></a>

Send messages to an Amazon Managed Streaming for Apache Kafka (Amazon MSK) or self-managed Apache Kafka cluster.

## Contents
<a name="API_KafkaAction_Contents"></a>

 ** clientProperties **   <a name="iot-Type-KafkaAction-clientProperties"></a>
Properties of the Apache Kafka producer client.
Type: String to string map
Required: Yes

 ** destinationArn **   <a name="iot-Type-KafkaAction-destinationArn"></a>
The ARN of Kafka action's VPC `TopicRuleDestination`.
Type: String
Required: Yes

 ** topic **   <a name="iot-Type-KafkaAction-topic"></a>
The Kafka topic for messages to be sent to the Kafka broker.
Type: String
Required: Yes

 ** headers **   <a name="iot-Type-KafkaAction-headers"></a>
The list of Kafka headers that you specify.
Type: Array of [KafkaActionHeader](API_KafkaActionHeader.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** key **   <a name="iot-Type-KafkaAction-key"></a>
The Kafka message key.
Type: String
Required: No

 ** partition **   <a name="iot-Type-KafkaAction-partition"></a>
The Kafka message partition.
Type: String
Required: No

## See Also
<a name="API_KafkaAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/KafkaAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/KafkaAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/KafkaAction)
