---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_MqttTopicConfig.html
---

# MqttTopicConfig
<a name="API_MqttTopicConfig"></a>

The MQTT topic to which the AWS IoT FleetWise campaign routes data. For more information, see [Device communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html) in the * AWS IoT Core Developer Guide*.

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Contents
<a name="API_MqttTopicConfig_Contents"></a>

 ** executionRoleArn **   <a name="iotfleetwise-Type-MqttTopicConfig-executionRoleArn"></a>
The ARN of the role that grants AWS IoT FleetWise permission to access and act on messages sent to the MQTT topic.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)`
Required: Yes

 ** mqttTopicArn **   <a name="iotfleetwise-Type-MqttTopicConfig-mqttTopicArn"></a>
The ARN of the MQTT topic.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

## See Also
<a name="API_MqttTopicConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/MqttTopicConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/MqttTopicConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/MqttTopicConfig)
