---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_KafkaActionHeader.html
---

# KafkaActionHeader
<a name="API_KafkaActionHeader"></a>

Specifies a Kafka header using key-value pairs when you create a Rule’s Kafka Action. You can use these headers to route data from IoT clients to downstream Kafka clusters without modifying your message payload.

For more information about Rule's Kafka action, see [Apache Kafka](https://docs.aws.amazon.com/iot/latest/developerguide/apache-kafka-rule-action.html).

## Contents
<a name="API_KafkaActionHeader_Contents"></a>

 ** key **   <a name="iot-Type-KafkaActionHeader-key"></a>
The key of the Kafka header.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: Yes

 ** value **   <a name="iot-Type-KafkaActionHeader-value"></a>
The value of the Kafka header.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: Yes

## See Also
<a name="API_KafkaActionHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/KafkaActionHeader)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/KafkaActionHeader)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/KafkaActionHeader)
