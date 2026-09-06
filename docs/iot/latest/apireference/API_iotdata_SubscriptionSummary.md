---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_SubscriptionSummary.html
---

# SubscriptionSummary
<a name="API_iotdata_SubscriptionSummary"></a>

Contains information about a subscription for an MQTT client, including the topic filter and Quality of Service (QoS) level.

## Contents
<a name="API_iotdata_SubscriptionSummary_Contents"></a>

 ** qos **   <a name="iot-Type-iotdata_SubscriptionSummary-qos"></a>
The Quality of Service (QoS) level for the subscription. Valid values are 0 (at most once) and 1 (at least once).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

 ** topicFilter **   <a name="iot-Type-iotdata_SubscriptionSummary-topicFilter"></a>
The topic filter pattern that the client is subscribed to. May include MQTT wildcards such as \+ (single-level) and \# (multi-level).
Type: String
Required: Yes

## See Also
<a name="API_iotdata_SubscriptionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-data-2015-05-28/SubscriptionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-data-2015-05-28/SubscriptionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-data-2015-05-28/SubscriptionSummary)
