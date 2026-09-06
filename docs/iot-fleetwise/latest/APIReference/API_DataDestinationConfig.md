---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DataDestinationConfig.html
---

# DataDestinationConfig
<a name="API_DataDestinationConfig"></a>

The destination where the campaign sends data. You can send data to an MQTT topic, or store it in Amazon S3 or Amazon Timestream.

## Contents
<a name="API_DataDestinationConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** mqttTopicConfig **   <a name="iotfleetwise-Type-DataDestinationConfig-mqttTopicConfig"></a>
The MQTT topic to which the AWS IoT FleetWise campaign routes data.
Type: [MqttTopicConfig](API_MqttTopicConfig.md) object
Required: No

 ** s3Config **   <a name="iotfleetwise-Type-DataDestinationConfig-s3Config"></a>
The Amazon S3 bucket where the AWS IoT FleetWise campaign sends data.
Type: [S3Config](API_S3Config.md) object
Required: No

 ** timestreamConfig **   <a name="iotfleetwise-Type-DataDestinationConfig-timestreamConfig"></a>
The Amazon Timestream table where the campaign sends data.
Type: [TimestreamConfig](API_TimestreamConfig.md) object
Required: No

## See Also
<a name="API_DataDestinationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/DataDestinationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/DataDestinationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/DataDestinationConfig)
